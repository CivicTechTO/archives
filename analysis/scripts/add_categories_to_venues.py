#!/usr/bin/env python3
"""
Helper script to add category metadata to venue markdown files.

This script helps you quickly add 'category' fields to venue markdown files
based on the current auto-categorization results.

Usage:
    python scripts/add_categories_to_venues.py --dry-run  # Preview changes
    python scripts/add_categories_to_venues.py            # Apply changes
"""

import json
import argparse
from pathlib import Path
import frontmatter

REPO_ROOT = Path(__file__).parent.parent.parent
VENUES_DIR = REPO_ROOT / "_venues"
DATA_DIR = Path(__file__).parent.parent / "data"


def find_venue_file(venue_name):
    """Find the markdown file for a venue by name."""
    # Try exact match first
    for md_file in VENUES_DIR.glob("*.md"):
        post = frontmatter.load(md_file)
        if post.get('title') == venue_name:
            return md_file

    # Fallback: try filename match
    safe_name = venue_name.replace('/', '-').replace('_venues/', '')
    potential_file = VENUES_DIR / f"{safe_name}.md"
    if potential_file.exists():
        return potential_file

    return None


def add_category_to_venue(venue_file, category, dry_run=True):
    """Add category field to venue markdown file with namespace."""
    post = frontmatter.load(venue_file)

    # Check if already has category
    if 'category' in post.metadata:
        return False, f"Already has category: {post['category']}"

    # Add category with namespace
    namespaced_category = f"venue-category/{category}"
    post['category'] = namespaced_category

    if dry_run:
        return True, "Would add category"
    else:
        # Write back to file
        with open(venue_file, 'w') as f:
            f.write(frontmatter.dumps(post))
        return True, "Category added"


def main():
    parser = argparse.ArgumentParser(
        description="Add category metadata to venue markdown files"
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help="Preview changes without modifying files"
    )
    parser.add_argument(
        '--category',
        type=str,
        help="Only process venues in this category (Academic, Public, Industry, Nonprofit, Online)"
    )
    parser.add_argument(
        '--auto-only',
        action='store_true',
        help="Only process auto-categorized venues (skip manually categorized)"
    )

    args = parser.parse_args()

    # Load categorization data
    with open(DATA_DIR / "venue_categories.json", 'r') as f:
        data = json.load(f)

    venues = data['venues_by_category']

    # Filter venues
    venues_to_process = []
    for venue in venues:
        # Skip if filtering by category
        if args.category and venue['category'] != args.category:
            continue

        # Skip if only processing auto-categorized
        if args.auto_only and venue.get('category_source') != 'auto':
            continue

        venues_to_process.append(venue)

    if not venues_to_process:
        print("No venues to process")
        return

    print("=" * 70)
    if args.dry_run:
        print("DRY RUN - No files will be modified")
    else:
        print("ADDING CATEGORIES TO VENUE FILES")
    print("=" * 70)

    stats = {
        'updated': 0,
        'already_categorized': 0,
        'not_found': 0
    }

    for venue in venues_to_process:
        venue_name = venue['name']
        category = venue['category']

        # Find venue file
        venue_file = find_venue_file(venue_name)

        if not venue_file:
            print(f"✗ {venue_name} - FILE NOT FOUND")
            stats['not_found'] += 1
            continue

        # Add category
        updated, message = add_category_to_venue(venue_file, category, args.dry_run)

        if updated:
            symbol = "→" if args.dry_run else "✓"
            print(f"{symbol} {venue_name} → {category}")
            stats['updated'] += 1
        else:
            print(f"  {venue_name} - {message}")
            stats['already_categorized'] += 1

    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Would update: {stats['updated']}" if args.dry_run else f"Updated: {stats['updated']}")
    print(f"Already categorized: {stats['already_categorized']}")
    print(f"Not found: {stats['not_found']}")

    if args.dry_run and stats['updated'] > 0:
        print("\nRe-run without --dry-run to apply changes")


if __name__ == "__main__":
    main()
