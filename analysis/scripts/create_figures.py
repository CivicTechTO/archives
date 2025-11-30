#!/usr/bin/env python3
"""
Create interactive Plotly visualizations for CivicTech Toronto archive analysis.
"""

import json
from pathlib import Path
import plotly.graph_objects as go
import plotly.express as px
from collections import defaultdict

DATA_DIR = Path(__file__).parent.parent / "data"
FIGURES_DIR = Path(__file__).parent.parent / "figures"

# Default color scheme (can be extended dynamically)
DEFAULT_COLORS = {
    'Academic': '#1f77b4',      # blue
    'Public': '#2ca02c',        # green
    'Industry': '#ff7f0e',      # orange
    'Nonprofit': '#d62728',     # red
    'Park': '#8c564b',          # brown
    'Hospitality': '#e377c2',   # pink
    'Online': '#9467bd'         # purple
}

# Fallback colors for any new categories not in default list
FALLBACK_COLORS = [
    '#17becf', '#bcbd22', '#7f7f7f', '#e377c2', '#8c564b',
    '#9467bd', '#c5b0d5', '#c49c94', '#f7b6d2', '#c7c7c7'
]


def get_color_for_category(category, color_map):
    """Get color for a category, assigning fallback color if not predefined."""
    if category in color_map:
        return color_map[category]

    # Assign a fallback color
    used_fallbacks = sum(1 for c in color_map.values() if c in FALLBACK_COLORS)
    return FALLBACK_COLORS[used_fallbacks % len(FALLBACK_COLORS)]


def generate_colors_for_categories(categories):
    """Generate color mapping for all categories dynamically."""
    color_map = DEFAULT_COLORS.copy()

    for category in categories:
        if category not in color_map:
            color_map[category] = get_color_for_category(category, color_map)

    return color_map


def load_data():
    """Load all processed data."""
    with open(DATA_DIR / "topic_analysis.json", 'r') as f:
        topic_data = json.load(f)

    with open(DATA_DIR / "venue_categories.json", 'r') as f:
        venue_data = json.load(f)

    return topic_data, venue_data


def create_topic_over_time(topic_data):
    """Figure 1: Topic Distribution Over Years (line chart for top topics)."""
    print("Creating Figure 1: Topic Distribution Over Years...")

    by_year = topic_data['by_year']
    total_counts = topic_data['total_counts']

    # Get top 10 topics by total count
    top_topics = list(total_counts.keys())[:10]

    # Build time series for each topic
    years = sorted(by_year.keys())

    fig = go.Figure()

    for topic in top_topics:
        counts = [by_year[str(year)].get(topic, 0) for year in years]

        fig.add_trace(go.Scatter(
            x=years,
            y=counts,
            mode='lines+markers',
            name=topic.replace('-', ' ').title(),
            hovertemplate='<b>%{fullData.name}</b><br>' +
                         'Year: %{x}<br>' +
                         'Events: %{y}<br>' +
                         '<extra></extra>'
        ))

    fig.update_layout(
        title='Topic Distribution Over Years (Top 10 Topics)',
        xaxis_title='Year',
        yaxis_title='Number of Events',
        hovermode='x unified',
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01
        ),
        height=600
    )

    output_file = FIGURES_DIR / "topic_over_time.html"
    fig.write_html(output_file)
    print(f"  ✓ Saved to {output_file}")

    return fig


def create_topic_distribution(topic_data):
    """Figure 2: Topic Count Distribution (horizontal bar chart)."""
    print("Creating Figure 2: Topic Count Distribution...")

    total_counts = topic_data['total_counts']

    # Take top 20 topics for readability
    topics = list(total_counts.keys())[:20]
    counts = [total_counts[topic] for topic in topics]

    # Format topic names
    topic_labels = [topic.replace('-', ' ').title() for topic in topics]

    fig = go.Figure(go.Bar(
        x=counts,
        y=topic_labels,
        orientation='h',
        marker_color='#1f77b4',
        hovertemplate='<b>%{y}</b><br>' +
                     'Events: %{x}<br>' +
                     '<extra></extra>'
    ))

    fig.update_layout(
        title='Topic Count Distribution (Top 20 Topics)',
        xaxis_title='Number of Events',
        yaxis_title='',
        height=700,
        yaxis={'autorange': 'reversed'}
    )

    output_file = FIGURES_DIR / "topic_distribution.html"
    fig.write_html(output_file)
    print(f"  ✓ Saved to {output_file}")

    return fig


def create_venue_categories(venue_data, COLORS):
    """Figure 3: Venue Categories (pie chart)."""
    print("Creating Figure 3: Venue Categories Distribution...")

    category_summary = venue_data['category_summary']
    event_counts = category_summary['event_counts']

    # Filter out categories with 0 events
    categories = [cat for cat, count in event_counts.items() if count > 0]
    counts = [event_counts[cat] for cat in categories]
    colors = [COLORS[cat] for cat in categories]

    fig = go.Figure(go.Pie(
        labels=categories,
        values=counts,
        marker=dict(colors=colors),
        hovertemplate='<b>%{label}</b><br>' +
                     'Events: %{value}<br>' +
                     'Percentage: %{percent}<br>' +
                     '<extra></extra>'
    ))

    fig.update_layout(
        title='Event Distribution by Venue Category',
        height=500
    )

    output_file = FIGURES_DIR / "venue_categories.html"
    fig.write_html(output_file)
    print(f"  ✓ Saved to {output_file}")

    return fig


def create_venue_prevalence(venue_data, COLORS):
    """Figure 4: Venue Prevalence (horizontal bar chart with category colors)."""
    print("Creating Figure 4: Venue Prevalence...")

    venues = venue_data['venues_by_category']

    # Take top 15 venues
    top_venues = venues[:15]

    names = [v['name'] for v in top_venues]
    counts = [v['count'] for v in top_venues]
    categories = [v['category'] for v in top_venues]
    colors_list = [COLORS[cat] for cat in categories]

    fig = go.Figure(go.Bar(
        x=counts,
        y=names,
        orientation='h',
        marker=dict(
            color=colors_list,
            line=dict(color='white', width=1)
        ),
        hovertemplate='<b>%{y}</b><br>' +
                     'Events: %{x}<br>' +
                     'Category: %{customdata}<br>' +
                     '<extra></extra>',
        customdata=categories
    ))

    fig.update_layout(
        title='Top 15 Venues by Event Count',
        xaxis_title='Number of Events',
        yaxis_title='',
        height=600,
        yaxis={'autorange': 'reversed'},
        showlegend=False
    )

    # Add category legend manually
    for category, color in COLORS.items():
        if category in categories:
            fig.add_trace(go.Scatter(
                x=[None],
                y=[None],
                mode='markers',
                marker=dict(size=10, color=color),
                name=category,
                showlegend=True
            ))

    output_file = FIGURES_DIR / "venue_prevalence.html"
    fig.write_html(output_file)
    print(f"  ✓ Saved to {output_file}")

    return fig


def create_venue_distribution(venue_data, COLORS):
    """Figure 5: Venue Count Distribution (bar chart showing all venues)."""
    print("Creating Figure 5: Venue Count Distribution...")

    venues = venue_data['venues_by_category']

    names = [v['name'] for v in venues]
    counts = [v['count'] for v in venues]
    categories = [v['category'] for v in venues]
    colors_list = [COLORS[cat] for cat in categories]

    fig = go.Figure(go.Bar(
        x=list(range(len(names))),
        y=counts,
        marker=dict(
            color=colors_list,
            line=dict(color='white', width=0.5)
        ),
        hovertemplate='<b>%{customdata[0]}</b><br>' +
                     'Events: %{y}<br>' +
                     'Category: %{customdata[1]}<br>' +
                     '<extra></extra>',
        customdata=[[name, cat] for name, cat in zip(names, categories)]
    ))

    fig.update_layout(
        title='All Venues: Event Count Distribution',
        xaxis_title='Venue (sorted by event count)',
        yaxis_title='Number of Events',
        height=500,
        showlegend=True
    )

    # Add category legend
    for category, color in COLORS.items():
        if category in categories:
            fig.add_trace(go.Scatter(
                x=[None],
                y=[None],
                mode='markers',
                marker=dict(size=10, color=color),
                name=category,
                showlegend=True
            ))

    output_file = FIGURES_DIR / "venue_distribution.html"
    fig.write_html(output_file)
    print(f"  ✓ Saved to {output_file}")

    return fig


def create_dashboard():
    """Create an HTML dashboard with all figures."""
    print("Creating dashboard...")

    html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CivicTech Toronto Archive Analysis</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        h1 {
            color: #333;
            text-align: center;
            margin-bottom: 10px;
        }
        .subtitle {
            text-align: center;
            color: #666;
            margin-bottom: 40px;
        }
        .figure-container {
            background: white;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 30px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .figure-container h2 {
            margin-top: 0;
            color: #444;
        }
        iframe {
            width: 100%;
            border: none;
            border-radius: 4px;
        }
        .description {
            color: #666;
            margin-bottom: 15px;
            line-height: 1.6;
        }
    </style>
</head>
<body>
    <h1>CivicTech Toronto Archive Analysis</h1>
    <p class="subtitle">Interactive visualizations of 10 years of civic technology community events (2015-2025)</p>

    <div class="figure-container">
        <h2>Topic Distribution Over Years</h2>
        <p class="description">
            Evolution of top 10 civic tech topics discussed at hacknights from 2015 to 2025.
            Hover over lines to see details. Click legend items to show/hide topics.
        </p>
        <iframe src="topic_over_time.html" height="650"></iframe>
    </div>

    <div class="figure-container">
        <h2>Topic Count Distribution</h2>
        <p class="description">
            Total number of hacknight events covering each topic (top 20 shown).
            Shows the breadth of civic tech issues addressed by the community.
        </p>
        <iframe src="topic_distribution.html" height="750"></iframe>
    </div>

    <div class="figure-container">
        <h2>Event Distribution by Venue Category</h2>
        <p class="description">
            Distribution of events across venue types: Academic (universities), Public (government),
            Industry (corporate), and Nonprofit (community organizations).
        </p>
        <iframe src="venue_categories.html" height="550"></iframe>
    </div>

    <div class="figure-container">
        <h2>Top 15 Venues by Event Count</h2>
        <p class="description">
            Most frequently used venues for hacknight events, color-coded by category.
            Shows the key partners and spaces that supported the community.
        </p>
        <iframe src="venue_prevalence.html" height="650"></iframe>
    </div>

    <div class="figure-container">
        <h2>All Venues: Event Count Distribution</h2>
        <p class="description">
            Complete distribution of all 63 venues used over 10 years, sorted by event count.
            Demonstrates the wide range of community support and partnerships.
        </p>
        <iframe src="venue_distribution.html" height="550"></iframe>
    </div>

    <footer style="text-align: center; color: #999; margin-top: 50px; padding-bottom: 20px;">
        <p>Generated from CivicTech Toronto Archive | 521 Hacknights | 2015-2025</p>
    </footer>
</body>
</html>
"""

    output_file = FIGURES_DIR / "index.html"
    with open(output_file, 'w') as f:
        f.write(html_template)

    print(f"  ✓ Dashboard saved to {output_file}")


def main():
    """Generate all figures."""
    print("=" * 60)
    print("CivicTech Toronto Archive - Figure Generation")
    print("=" * 60)

    # Create figures directory
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)

    # Load data
    print("\nLoading data...")
    topic_data, venue_data = load_data()

    # Discover categories and generate colors dynamically
    all_categories = venue_data.get('all_categories', [])
    print(f"Discovered {len(all_categories)} venue categories: {', '.join(all_categories)}")

    COLORS = generate_colors_for_categories(all_categories)
    print("Generated color scheme for all categories")

    # Create all figures
    print("\nGenerating figures...")
    create_topic_over_time(topic_data)
    create_topic_distribution(topic_data)
    create_venue_categories(venue_data, COLORS)
    create_venue_prevalence(venue_data, COLORS)
    create_venue_distribution(venue_data, COLORS)

    # Create dashboard
    create_dashboard()

    print("\n" + "=" * 60)
    print("✓ All figures generated successfully!")
    print("=" * 60)
    print(f"\nOpen the dashboard: {FIGURES_DIR / 'index.html'}")
    print("\nIndividual figures:")
    print("  - topic_over_time.html")
    print("  - topic_distribution.html")
    print("  - venue_categories.html")
    print("  - venue_prevalence.html")
    print("  - venue_distribution.html")


if __name__ == "__main__":
    main()
