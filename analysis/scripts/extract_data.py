#!/usr/bin/env python3
"""
Extract data from CivicTech Toronto archive markdown files.
Parses YAML frontmatter and creates structured JSON files for analysis.
"""

import os
import json
from pathlib import Path
import frontmatter
from datetime import datetime
from collections import defaultdict

# Paths relative to project root
REPO_ROOT = Path(__file__).parent.parent.parent
HACKNIGHTS_DIR = REPO_ROOT / "_hacknights"
VENUES_DIR = REPO_ROOT / "_venues"
DATA_DIR = REPO_ROOT / "analysis" / "data"


def extract_hacknights():
    """Extract all hacknight data including dates, topics, and venues."""
    hacknights = []

    for md_file in sorted(HACKNIGHTS_DIR.glob("*.md")):
        try:
            post = frontmatter.load(md_file)

            # Extract basic info
            hacknight_data = {
                'number': post.get('number'),
                'date': str(post.get('date')) if post.get('date') else None,
                'title': post.get('title', ''),
                'topic': post.get('topic', ''),
                'venue': post.get('venue', ''),
                'via': post.get('via', ''),
                'booker': post.get('booker', ''),
                'speakers': post.get('speakers', []),
                'tags': post.get('tags', [])
            }

            # Extract only topic tags (remove type/hacknight)
            topic_tags = [
                tag.replace('topic/', '')
                for tag in hacknight_data['tags']
                if tag.startswith('topic/')
            ]
            hacknight_data['topic_tags'] = topic_tags

            # Parse year from date
            if hacknight_data['date']:
                try:
                    date_obj = datetime.fromisoformat(hacknight_data['date'])
                    hacknight_data['year'] = date_obj.year
                except:
                    hacknight_data['year'] = None
            else:
                hacknight_data['year'] = None

            # Clean venue name (remove [[ ]] wikilink syntax)
            if hacknight_data['venue']:
                hacknight_data['venue'] = hacknight_data['venue'].replace('[[', '').replace(']]', '')

            hacknights.append(hacknight_data)

        except Exception as e:
            print(f"Error processing {md_file}: {e}")
            continue

    return hacknights


def extract_venues():
    """Extract all venue data."""
    venues = []

    for md_file in VENUES_DIR.glob("*.md"):
        try:
            post = frontmatter.load(md_file)

            venue_data = {
                'name': post.get('title', md_file.stem),
                'organization': post.get('organization', []),
                'address': post.get('address', ''),
                'tags': post.get('tags', [])
            }

            # Clean organization names (remove wikilink syntax)
            if venue_data['organization']:
                venue_data['organization'] = [
                    org.replace('[[', '').replace(']]', '')
                    for org in venue_data['organization']
                ]

            venues.append(venue_data)

        except Exception as e:
            print(f"Error processing {md_file}: {e}")
            continue

    return venues


def analyze_topics(hacknights):
    """Analyze topic distribution across years."""
    topics_by_year = defaultdict(lambda: defaultdict(int))
    topic_counts = defaultdict(int)

    for hacknight in hacknights:
        year = hacknight.get('year')
        if not year:
            continue

        for topic in hacknight.get('topic_tags', []):
            topics_by_year[year][topic] += 1
            topic_counts[topic] += 1

    # Convert to sorted structure
    topic_distribution = {
        'by_year': {
            year: dict(topics)
            for year, topics in sorted(topics_by_year.items())
        },
        'total_counts': dict(sorted(topic_counts.items(), key=lambda x: x[1], reverse=True))
    }

    return topic_distribution


def analyze_venues(hacknights, venues):
    """Analyze venue usage and create categorization."""
    venue_counts = defaultdict(int)

    # Count venue usage from hacknights
    for hacknight in hacknights:
        venue = hacknight.get('venue')
        if venue:
            venue_counts[venue] += 1

    # Create venue lookup with metadata
    venue_metadata = {
        venue['name']: venue
        for venue in venues
    }

    # Combine counts with metadata
    venue_analysis = []
    for venue_name, count in venue_counts.items():
        metadata = venue_metadata.get(venue_name, {})
        venue_analysis.append({
            'name': venue_name,
            'count': count,
            'organization': metadata.get('organization', []),
            'address': metadata.get('address', '')
        })

    # Sort by count
    venue_analysis.sort(key=lambda x: x['count'], reverse=True)

    return {
        'venue_counts': venue_analysis,
        'total_venues': len(venue_counts)
    }


def analyze_speakers(hacknights):
    """Analyze speaker appearances across hacknights."""
    speaker_counts = defaultdict(int)

    # Count speaker appearances
    for hacknight in hacknights:
        speakers = hacknight.get('speakers', [])
        if speakers is None:
            continue
        for speaker in speakers:
            # Clean speaker name (remove wikilink syntax)
            clean_speaker = speaker.replace('[[', '').replace(']]', '')
            if clean_speaker:  # Skip empty names
                speaker_counts[clean_speaker] += 1

    # Sort by count
    speaker_leaderboard = [
        {'name': name, 'appearances': count}
        for name, count in sorted(speaker_counts.items(), key=lambda x: x[1], reverse=True)
    ]

    return {
        'speaker_leaderboard': speaker_leaderboard,
        'total_speakers': len(speaker_counts)
    }


def main():
    """Main extraction process."""
    print("Extracting CivicTech Toronto archive data...")

    # Create data directory
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    # Extract hacknights
    print(f"Extracting hacknights from {HACKNIGHTS_DIR}...")
    hacknights = extract_hacknights()
    print(f"  Found {len(hacknights)} hacknights")

    # Extract venues
    print(f"Extracting venues from {VENUES_DIR}...")
    venues = extract_venues()
    print(f"  Found {len(venues)} venues")

    # Analyze topics
    print("Analyzing topics...")
    topic_analysis = analyze_topics(hacknights)
    print(f"  Found {len(topic_analysis['total_counts'])} unique topics")

    # Analyze venues
    print("Analyzing venue usage...")
    venue_analysis = analyze_venues(hacknights, venues)
    print(f"  Found {venue_analysis['total_venues']} unique venues used")

    # Analyze speakers
    print("Analyzing speakers...")
    speaker_analysis = analyze_speakers(hacknights)
    print(f"  Found {speaker_analysis['total_speakers']} unique speakers")

    # Save data
    print(f"Saving data to {DATA_DIR}...")

    with open(DATA_DIR / "hacknights.json", 'w') as f:
        json.dump(hacknights, f, indent=2)

    with open(DATA_DIR / "venues.json", 'w') as f:
        json.dump(venues, f, indent=2)

    with open(DATA_DIR / "topic_analysis.json", 'w') as f:
        json.dump(topic_analysis, f, indent=2)

    with open(DATA_DIR / "venue_analysis.json", 'w') as f:
        json.dump(venue_analysis, f, indent=2)

    with open(DATA_DIR / "speaker_analysis.json", 'w') as f:
        json.dump(speaker_analysis, f, indent=2)

    print("✓ Data extraction complete!")
    print(f"\nSummary:")
    print(f"  - {len(hacknights)} hacknights")
    print(f"  - {len(venues)} venues")
    print(f"  - {len(topic_analysis['total_counts'])} topics")
    print(f"  - {venue_analysis['total_venues']} venues used")
    print(f"  - {speaker_analysis['total_speakers']} speakers")
    print(f"\nData saved to: {DATA_DIR}")


if __name__ == "__main__":
    main()
