#!/usr/bin/env python3
"""
Categorize venues dynamically based on 'category' property in markdown frontmatter.

All categories are discovered from the venue files themselves - no predefined list needed.
If a venue doesn't have a category, it can be auto-categorized with fallback rules.
"""

import json
from pathlib import Path
import frontmatter
from collections import defaultdict

REPO_ROOT = Path(__file__).parent.parent.parent
VENUES_DIR = REPO_ROOT / "_venues"
DATA_DIR = Path(__file__).parent.parent / "data"

# Fallback categorization rules (only used if venue has no category)
FALLBACK_RULES = {
    'Academic': {
        'keywords': ['university', 'college', 'u of t', 'ryerson', 'york university',
                    'myhal', 'sandford fleming', 'bahen', 'utsu', 'tmu'],
        'organizations': ['University of Toronto', 'Ryerson University', 'York University',
                         'Toronto Metropolitan University']
    },
    'Public': {
        'keywords': ['city hall', 'metro hall', 'ontario digital service', 'civic',
                    'municipal', 'government', 'public library', 'library'],
        'organizations': ['City of Toronto', 'Ontario Digital Service', 'Toronto Public Library']
    },
    'Nonprofit': {
        'keywords': ['foundation', 'centre for social innovation', 'csi', 'atkinson',
                    'community', 'hacklab'],
        'organizations': ['Centre for Social Innovation', 'Atkinson Foundation', 'Hacklab.TO']
    },
    'Park': {
        'keywords': ['park', 'common'],
        'organizations': []
    },
    'Hospitality': {
        'keywords': ['restaurant', 'bar', 'social house'],
        'organizations': []
    },
    'Online': {
        'keywords': ['online', 'virtual', 'zoom', 'remote'],
        'organizations': []
    }
}


def categorize_venue_fallback(venue_name, organizations):
    """
    Fallback categorization based on keywords and organizations.
    Only used if venue doesn't have a category in its markdown.
    """
    venue_lower = venue_name.lower()

    for category, rules in FALLBACK_RULES.items():
        # Check keywords in venue name
        if any(keyword in venue_lower for keyword in rules['keywords']):
            return category

        # Check organizations
        if organizations:
            for org in organizations:
                if any(rule_org.lower() in org.lower() for rule_org in rules['organizations']):
                    return category

    # Default to Industry if can't determine
    return 'Industry'


def load_all_venue_categories():
    """
    Load ALL venue categories from markdown files.
    Returns map of venue_name -> category.
    """
    venue_category_map = {}

    for md_file in VENUES_DIR.glob("*.md"):
        try:
            post = frontmatter.load(md_file)
            venue_name = post.get('title', md_file.stem)

            # Check if category is specified in frontmatter
            if 'category' in post:
                category = post['category']
                # Strip namespace if present (venue-category/Academic -> Academic)
                if category.startswith('venue-category/'):
                    category = category.replace('venue-category/', '')
                venue_category_map[venue_name] = category
        except Exception as e:
            print(f"Warning: Could not read {md_file}: {e}")

    return venue_category_map


def discover_categories(all_venue_categories):
    """
    Discover all unique categories that exist in the venue files.
    Returns sorted list of category names.
    """
    categories = set(all_venue_categories.values())
    return sorted(categories)


def main():
    """Categorize all venues dynamically based on markdown categories."""
    print("Categorizing venues...")

    # Load ALL venue categories from markdown frontmatter
    print("Loading categories from venue markdown files...")
    all_venue_categories = load_all_venue_categories()
    print(f"  Found {len(all_venue_categories)} venues with categories")

    # Discover what categories exist
    discovered_categories = discover_categories(all_venue_categories)
    print(f"  Discovered categories: {', '.join(discovered_categories)}")

    # Load venue analysis (venues that were actually used in events)
    with open(DATA_DIR / "venue_analysis.json", 'r') as f:
        venue_data = json.load(f)

    # Initialize dynamic category counters
    category_counts = defaultdict(int)
    category_event_counts = defaultdict(int)
    categorized_venues = []
    auto_categorized = []

    for venue in venue_data['venue_counts']:
        venue_name = venue['name']

        # Use markdown category if available, otherwise auto-categorize
        if venue_name in all_venue_categories:
            category = all_venue_categories[venue_name]
            source = 'markdown'
        else:
            category = categorize_venue_fallback(venue_name, venue.get('organization', []))
            source = 'auto'
            auto_categorized.append(venue_name)

        categorized_venue = {
            **venue,
            'category': category,
            'category_source': source
        }
        categorized_venues.append(categorized_venue)

        # Count venues and events per category (dynamic)
        category_counts[category] += 1
        category_event_counts[category] += venue['count']

    # Create summary with all discovered categories
    summary = {
        'venues_by_category': categorized_venues,
        'category_summary': {
            'venue_counts': dict(category_counts),
            'event_counts': dict(category_event_counts)
        },
        'total_venues': venue_data['total_venues'],
        'all_categories': discovered_categories
    }

    # Save categorized data
    output_file = DATA_DIR / "venue_categories.json"
    with open(output_file, 'w') as f:
        json.dump(summary, f, indent=2)

    print(f"\n✓ Categorized {len(categorized_venues)} venues")
    print(f"  - {len(all_venue_categories)} from markdown")
    print(f"  - {len(auto_categorized)} auto-categorized")

    print("\nCategory Distribution (events only):")
    for category in sorted(category_counts.keys()):
        count = category_counts[category]
        event_count = category_event_counts[category]
        print(f"  {category}: {count} venues, {event_count} events")

    if auto_categorized:
        print("\nAuto-categorized venues (consider adding 'category' to markdown):")
        for venue_name in auto_categorized[:10]:
            print(f"  - {venue_name}")
        if len(auto_categorized) > 10:
            print(f"  ... and {len(auto_categorized) - 10} more")

    print(f"\nData saved to: {output_file}")


if __name__ == "__main__":
    main()
