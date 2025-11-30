#!/usr/bin/env python3
"""
Review current venue categorizations and generate a report.
Helps identify venues that need manual category correction.
"""

import json
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data"


def main():
    """Generate categorization review report."""
    with open(DATA_DIR / "venue_categories.json", 'r') as f:
        data = json.load(f)

    venues = data['venues_by_category']

    # Group by category and source
    by_category = {}
    for venue in venues:
        cat = venue['category']
        if cat not in by_category:
            by_category[cat] = {'markdown': [], 'auto': []}

        source = venue.get('category_source', 'auto')
        by_category[cat][source].append({
            'name': venue['name'],
            'count': venue['count'],
            'organization': venue.get('organization', [])
        })

    print("=" * 70)
    print("VENUE CATEGORIZATION REVIEW")
    print("=" * 70)

    for category in ['Academic', 'Public', 'Industry', 'Nonprofit', 'Online']:
        if category not in by_category:
            continue

        cat_data = by_category[category]
        total = len(cat_data['markdown']) + len(cat_data['auto'])

        print(f"\n{category.upper()} ({total} venues)")
        print("-" * 70)

        if cat_data['markdown']:
            print(f"\n✓ Manually categorized ({len(cat_data['markdown'])}):")
            for v in sorted(cat_data['markdown'], key=lambda x: x['count'], reverse=True):
                orgs = ', '.join(v['organization']) if v['organization'] else 'N/A'
                print(f"  • {v['name']} ({v['count']} events) - {orgs}")

        if cat_data['auto']:
            print(f"\n⚠ Auto-categorized ({len(cat_data['auto'])}) - REVIEW THESE:")
            for v in sorted(cat_data['auto'], key=lambda x: x['count'], reverse=True):
                orgs = ', '.join(v['organization']) if v['organization'] else 'N/A'
                print(f"  • {v['name']} ({v['count']} events) - {orgs}")

    print("\n" + "=" * 70)
    print("To fix a categorization, add 'category' to the venue's markdown file:")
    print("---")
    print("title: Venue Name")
    print("category: Academic  # or Public, Industry, Nonprofit, Online")
    print("organization:")
    print("  - \"[[Organization Name]]\"")
    print("---")
    print("=" * 70)


if __name__ == "__main__":
    main()
