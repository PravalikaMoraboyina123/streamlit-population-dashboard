# Streamlit Population Dashboard

A basic data visualization dashboard built using Streamlit, Pandas, and Plotly. This project uses a public population dataset to display interactive charts and comparisons between countries.

## Project Overview

This dashboard provides:
- Population growth trends over time
- Country-wise population comparison
- Population distribution visualization
- Interactive country selection using sidebar filters

The application is built using public data and deployed using Streamlit Community Cloud.

## Technologies Used

- Python
- Streamlit
- Pandas
- Plotly

## Dataset

Public Dataset Source:

https://raw.githubusercontent.com/datasets/population/master/data/population.csv

The dataset contains:
- Country names
- Year-wise population values
- Historical population statistics

## Features

- Interactive line chart for population growth
- Bar chart for latest population comparison
- Pie chart for population share distribution
- Sidebar country selection filter
- Responsive dashboard layout

## Project Structure

```text
streamlit-population-dashboard/
│
├── app.py
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/PravalikaMoraboyina123/streamlit-population-dashboard.git
```

Move into the project directory:

```bash
cd streamlit-population-dashboard
```

Create virtual environment:

```bash
python3 -m venv venv
```

Activate virtual environment:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
streamlit run app.py
```

## Deployment

The project is deployed using Streamlit Community Cloud.

## Future Improvements

- Add more public datasets
- Add advanced analytics
- Add downloadable reports
- Improve dashboard UI
- Add real-time data integration

## Author

Pravalika Moraboyina
