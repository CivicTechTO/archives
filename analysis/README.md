# CivicTech Toronto Archive Analysis

Interactive visualizations and analytics for the CivicTech Toronto archive. Analyzes 10 years (2015-2025) of civic technology community events, including 521 hacknights, 103 topics, and 63 venues.

## Quick Start

### 1. Setup Virtual Environment

```bash
cd analysis
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Extract Data

```bash
python scripts/extract_data.py
```

This extracts data from the archive's markdown files and creates:
- `data/hacknights.json` - All hacknight events with metadata
- `data/venues.json` - All venue information
- `data/topic_analysis.json` - Topic counts by year and overall
- `data/venue_analysis.json` - Venue usage statistics

### 3. Categorize Venues

```bash
python scripts/categorize_venues.py
```

**Dynamic Categorization:** The script automatically discovers all venue categories from the markdown files - no predefined list needed!

Creates: `data/venue_categories.json`

The script:
1. Scans all venue files and discovers categories (e.g., Academic, Public, Industry, Nonprofit, Park, Hospitality, Online)
2. For venues used in events, applies their markdown `category` property
3. For venues without categories, falls back to keyword-based auto-categorization

**Adding new categories:** Just add `category: venue-category/YourNewCategory` to any venue file and it will automatically be discovered and visualized with a unique color!

**To manually correct categories:**

#### Option 1: Review and edit individual venues

1. Review auto-categorizations:
   ```bash
   python scripts/review_categories.py
   ```

2. Edit venue markdown files in `../_venues/` and add a category:
   ```yaml
   ---
   title: Venue Name
   category: venue-category/Academic  # Academic, Public, Industry, Nonprofit, or Online
   organization:
     - "[[Organization Name]]"
   ---
   ```

3. Re-run categorization to see updates:
   ```bash
   python scripts/categorize_venues.py
   ```

#### Option 2: Bulk apply auto-categorizations

If the auto-categorizations look good, you can bulk-apply them:

```bash
# Preview what would be added
python scripts/add_categories_to_venues.py --dry-run

# Apply to all auto-categorized venues
python scripts/add_categories_to_venues.py

# Or apply only to specific category
python scripts/add_categories_to_venues.py --category Academic
```

This adds `category` fields to venue markdown files, making the categorizations permanent.

### 4. Generate Interactive Figures

```bash
python scripts/create_figures.py
```

Creates all Plotly visualizations and the dashboard.

### 5. View Results

**Interactive Dashboard:**
Open `figures/index.html` in your browser for the interactive dashboard.

**Presentation:**
Open `presentation.html` in your browser for the full Reveal.js presentation.
- Use arrow keys or space to navigate
- Press 'S' for speaker notes
- Press 'F' for fullscreen
- Press 'ESC' for overview mode

## Presentation

**Title:** 10 Years of Civic Tech Toronto from the Archive

A Reveal.js presentation featuring:
- Overview of the archive and its technology
- Timeline of 10 years of community growth
- Interactive data visualizations embedded in slides
- Key insights and reflections
- Speaker notes for presentation delivery

The presentation automatically embeds all generated figures and provides narrative context around the data.

## Generated Figures

All figures are interactive - hover for details, click legends to show/hide data.

1. **Topic Distribution Over Years** (`topic_over_time.html`)
   - Line chart showing evolution of top 10 topics from 2015-2025
   - Reveals trending topics and sustained interests

2. **Topic Count Distribution** (`topic_distribution.html`)
   - Horizontal bar chart of top 20 topics by event count
   - Shows breadth of civic tech coverage

3. **Event Distribution by Venue Category** (`venue_categories.html`)
   - Pie chart of events across venue types
   - Academic: 107 events
   - Public: 61 events
   - Industry: 207 events
   - Nonprofit: 15 events

4. **Top 15 Venues by Event Count** (`venue_prevalence.html`)
   - Bar chart of most-used venues, color-coded by category
   - Highlights key community partners

5. **All Venues: Event Count Distribution** (`venue_distribution.html`)
   - Complete distribution of all 63 venues
   - Shows diversity of community support

## Data Summary

- **521 Hacknights** (July 2015 - November 2025)
- **103 Unique Topics** (democracy, open data, AI, transportation, housing, etc.)
- **63 Venues** across 5 categories
- **565 People** (speakers, organizers, community members)
- **119 Organizations** (partner organizations)

## Scripts

- `extract_data.py` - Parse markdown frontmatter from archive
- `categorize_venues.py` - Classify venues by type (reads `category` from markdown, falls back to auto-categorization)
- `review_categories.py` - Review current categorizations and identify venues needing correction
- `add_categories_to_venues.py` - Bulk add `category` fields to venue markdown files
- `create_figures.py` - Generate all Plotly visualizations

## Future Migration

This analysis toolkit is designed to be separated into its own repository. When migrating:

### Option 1: Git Submodule

```bash
# In new analysis repo
git submodule add https://github.com/civictechto/archives.git archive
```

Update script paths to reference `archive/_hacknights/`, etc.

### Option 2: External Reference

Clone both repos side-by-side and update `REPO_ROOT` paths in scripts:

```python
REPO_ROOT = Path(__file__).parent.parent.parent / "archives"
```

## Requirements

- Python 3.8+
- plotly >= 5.18.0
- pandas >= 2.1.0
- pyyaml >= 6.0
- python-frontmatter >= 1.0.0

## License

Analysis scripts are provided for research and presentation purposes. Original archive data is licensed under CC BY-NC-SA 4.0.
