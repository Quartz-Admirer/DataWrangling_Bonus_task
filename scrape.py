import requests
import pandas as pd
import time
import os

def fetch_vacancies_by_keyword(keyword, pages=10, per_page=50):
    base_url = "https://api.hh.ru/vacancies"
    vacancies = []
    headers = {"User-Agent": "Mozilla/5.0"}

    for page in range(pages):
        params = {"text": keyword, "page": page, "per_page": per_page}
        response = requests.get(base_url, headers=headers, params=params)

        if response.status_code != 200:
            print(f"[{keyword}] Page {page}: Failed with status {response.status_code}")
            break

        items = response.json().get("items", [])
        if not items:
            print(f"[{keyword}] Page {page}: No more items.")
            break

        for vacancy in items:
            vacancies.append({
                "id": vacancy["id"],
                "name": vacancy["name"],
                "keyword": keyword,
                "area": vacancy["area"]["name"],
                "experience": vacancy.get("experience", {}).get("name"),
                "employment": vacancy.get("employment", {}).get("name"),
                "schedule": vacancy.get("schedule", {}).get("name"),
                "url": vacancy.get("alternate_url"),
                "requirement": vacancy.get("snippet", {}).get("requirement"),
                "responsibility": vacancy.get("snippet", {}).get("responsibility"),
            })

        print(f"[{keyword}] Page {page}: Retrieved {len(items)} items.")
        time.sleep(0.5)

    print(f"[{keyword}] Total vacancies collected: {len(vacancies)}")
    return vacancies

if __name__ == "__main__":
    keywords = ["Data Scientist", "ML Engineer", "Python Developer"]
    all_vacancies = []

    for kw in keywords:
        vacancies = fetch_vacancies_by_keyword(kw, pages=10)
        all_vacancies.extend(vacancies)

    df = pd.DataFrame(all_vacancies).drop_duplicates(subset="id")
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/jobs.csv", index=False)
    print(f"Total unique vacancies saved: {len(df)} → data/jobs.csv")
