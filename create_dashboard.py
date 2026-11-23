
import os
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Create dashboard folder
os.makedirs("dashboard", exist_ok=True)

# Load analysis reports
funnel = pd.read_csv("reports/marketing_funnel_analysis.csv")
origin = pd.read_csv("reports/lead_origin_analysis.csv")
monthly = pd.read_csv("reports/monthly_lead_conversion.csv")
segments = pd.read_csv("reports/business_segment_analysis.csv")
lead_types = pd.read_csv("reports/lead_type_analysis.csv")
conversion_time = pd.read_csv("reports/conversion_time_analysis.csv")

# Calculate KPIs
total_leads = len(funnel)
closed_deals = int(funnel["converted"].sum())
not_converted = total_leads - closed_deals
conversion_rate = closed_deals / total_leads * 100

# Create charts
figures = []

# 1. Marketing Funnel
fig = go.Figure(go.Funnel(
    y=["Qualified Leads", "Closed Deals"],
    x=[total_leads, closed_deals],
    textinfo="value+percent initial"
))
fig.update_layout(title="Marketing Conversion Funnel")
figures.append(fig)

# 2. Leads by Origin
fig = px.bar(
    origin.sort_values("total_leads", ascending=False),
    x="origin", y="total_leads",
    title="Qualified Leads by Origin",
    text_auto=True
)
figures.append(fig)

# 3. Conversion Rate by Origin
fig = px.bar(
    origin.sort_values("conversion_rate", ascending=False),
    x="origin", y="conversion_rate",
    title="Conversion Rate by Lead Origin",
    text_auto=".2f"
)
figures.append(fig)

# 4. Monthly Trend
fig = px.line(
    monthly,
    x="month",
    y=["total_leads", "closed_deals"],
    markers=True,
    title="Monthly Leads vs Closed Deals"
)
figures.append(fig)

# 5. Business Segment
fig = px.bar(
    segments,
    x="business_segment",
    y="closed_deals",
    title="Closed Deals by Business Segment",
    text_auto=True
)
figures.append(fig)

# 6. Lead Type
fig = px.pie(
    lead_types,
    names="lead_type",
    values="closed_deals",
    title="Closed Deals by Lead Type"
)
figures.append(fig)

# 7. Conversion Time
fig = px.histogram(
    conversion_time,
    x="conversion_days",
    nbins=30,
    title="Conversion Time Distribution",
    labels={"conversion_days": "Days to Close Deal"}
)
figures.append(fig)

# 8. Revenue Distribution
funnel["declared_monthly_revenue"] = pd.to_numeric(
    funnel["declared_monthly_revenue"], errors="coerce"
)

revenue_data = funnel[funnel["converted"] == 1].dropna(
    subset=["declared_monthly_revenue"]
)

fig = px.histogram(
    revenue_data,
    x="declared_monthly_revenue",
    nbins=30,
    title="Declared Monthly Revenue Distribution"
)
figures.append(fig)

# Build HTML dashboard
html = f"""
<html>
<head>
<title>Marketing Funnel Dashboard</title>
<style>
body {{
    font-family: Arial, sans-serif;
    background: #f1f5f9;
    margin: 0;
    padding: 25px;
}}
.header {{
    background: #172554;
    color: white;
    padding: 25px;
    border-radius: 10px;
    text-align: center;
}}
.kpis {{
    display: flex;
    gap: 15px;
    margin: 25px 0;
    flex-wrap: wrap;
}}
.kpi {{
    background: white;
    padding: 20px;
    border-radius: 10px;
    flex: 1;
    min-width: 160px;
    text-align: center;
}}
.kpi h2 {{
    color: #2563eb;
}}
.chart {{
    background: white;
    padding: 15px;
    margin: 20px 0;
    border-radius: 10px;
}}
</style>
</head>
<body>

<div class="header">
<h1>Marketing Funnel & Conversion Dashboard</h1>
<p>Olist Marketing Qualified Leads Analysis</p>
</div>

<div class="kpis">
<div class="kpi">
<h2>{total_leads:,}</h2>
<p>Total Qualified Leads</p>
</div>
<div class="kpi">
<h2>{closed_deals:,}</h2>
<p>Closed Deals</p>
</div>
<div class="kpi">
<h2>{conversion_rate:.2f}%</h2>
<p>Conversion Rate</p>
</div>
<div class="kpi">
<h2>{not_converted:,}</h2>
<p>Not Converted</p>
</div>
</div>
"""

for i, fig in enumerate(figures):
    html += '<div class="chart">'
    html += fig.to_html(
        full_html=False,
        include_plotlyjs="cdn" if i == 0 else False
    )
    html += '</div>'

html += """
</body>
</html>
"""

output_path = "dashboard/Marketing_Funnel_Dashboard.html"

with open(output_path, "w", encoding="utf-8") as file:
    file.write(html)

print("Dashboard generated successfully!")
print("Saved at:", os.path.abspath(output_path))
print("Total Leads:", total_leads)
print("Closed Deals:", closed_deals)
print("Conversion Rate:", round(conversion_rate, 2), "%")
