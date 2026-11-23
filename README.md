# Marketing Funnel & Conversion Performance Analysis

## Project Overview
This project analyzes the Olist Marketing Funnel dataset to understand lead generation, lead sources, business segments, and lead-to-deal conversion performance.

The objective is to identify marketing channel performance and understand how qualified leads convert into closed deals.

## Dataset
Source: [Olist Marketing Funnel Dataset – Kaggle](https://www.kaggle.com/datasets/olistbr/marketing-funnel-olist)

The project uses two datasets:
- Marketing Qualified Leads: 8,000 records
- Closed Deals: 842 records

The datasets are connected using the `mql_id` column.

## Key Performance Indicators

| Metric | Result |
|---|---:|
| Total Qualified Leads | 8,000 |
| Closed Deals | 842 |
| Not Converted Leads | 7,158 |
| Overall Conversion Rate | 10.53% |

## Analysis Performed
- Data understanding and quality assessment
- Data cleaning and missing-value handling
- Marketing funnel analysis
- Lead origin and channel performance analysis
- Monthly lead and closed-deal trends
- Business segment analysis
- Lead type analysis
- Conversion time analysis
- Declared monthly revenue analysis

## Dashboard
An interactive HTML dashboard was developed using Plotly.

Dashboard includes:
- Marketing conversion funnel
- Lead origin performance
- Conversion rate by origin
- Monthly lead vs closed-deal trends
- Business segment performance
- Lead type distribution
- Conversion time distribution
- Revenue distribution

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Jupyter Notebook

## Project Structure

```text
FUTURE_DS_03/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_data_cleaning.ipynb
│   └── 03_exploratory_data_analysis.ipynb
│
├── reports/
│   ├── business_segment_analysis.csv
│   ├── conversion_time_analysis.csv
│   ├── lead_origin_analysis.csv
│   ├── lead_type_analysis.csv
│   ├── marketing_channel_performance.csv
│   ├── marketing_funnel_analysis.csv
│   ├── monthly_lead_conversion.csv
│   └── revenue_summary.csv
│
├── dashboard/
│   └── Marketing_Funnel_Dashboard.html
│
├── create_dashboard.py
└── README.md
```

## How to Run

1. Clone the repository.
2. Install the required libraries:

```bash
pip install pandas numpy matplotlib seaborn plotly jupyter
```

3. Download the Olist Marketing Funnel dataset from Kaggle.
4. Place both original CSV files inside `data/raw/`.
5. Run the notebooks in sequence.
6. Generate the dashboard:

```bash
python create_dashboard.py
```

7. Open `dashboard/Marketing_Funnel_Dashboard.html` in a browser.

## Key Finding
Out of 8,000 marketing qualified leads, 842 resulted in closed deals, giving an overall lead-to-deal conversion rate of approximately 10.53%.

## Note
The analysis measures conversion from marketing qualified leads to closed deals. It does not represent a complete website visitor-to-customer funnel because website traffic data is not included.

Raw datasets are excluded from this repository. Download them from the original Kaggle source.
