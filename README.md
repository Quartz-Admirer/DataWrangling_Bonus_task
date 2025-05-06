# DataWrangling_Bonus_task

This project collects job postings from [hh.ru](https://hh.ru) for roles related to **Data Science**, **Machine Learning Engineering**, and **Python Development**, and provides a dashboard visualizing key requirements.

---

## 📁 Project Structure

```
.
├── scrape.py        # Scrapes job data from hh.ru API
├── analyze.py       # Analyzes most frequent skills in job descriptions
├── dashboard.py     # Streamlit dashboard for data visualization
├── data/            # Contains jobs.csv and top_skills.csv
├── requirements.txt # List of required Python packages
└── README.md
```

---

## ⚙️ Installation

1. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 How to Run

1. **Scrape job data**

   ```bash
   python scrape.py
   ```

   Downloads job postings and saves them to `data/jobs.csv`

2. **Analyze job requirements**

   ```bash
   python analyze.py
   ```

   Extracts most frequent skills and saves to `data/top_skills.csv`

3. **Launch the dashboard**

   ```bash
   streamlit run dashboard.py
   ```

   Opens a web-based dashboard with charts

---

## 📊 Dashboard Features

* **Top 10 In-Demand Skills** — Based on mentions in job requirements
* **Experience Level Distribution** — Pie chart of required experience levels
* **Top 10 Locations** — Regions with the most job postings

---

## 📆 Requirements

* Python 3.8+
* Packages listed in `requirements.txt`:

  * `pandas`
  * `requests`
  * `streamlit`
  * `matplotlib`
  * `seaborn`

---

