import pandas as pd
import re
from collections import Counter
import os

SKILLS = [
    "Python", "SQL", "Java", "C++", "C#", "JavaScript", "HTML", "CSS",
    "TensorFlow", "PyTorch", "Keras", "Pandas", "NumPy", "Scikit-learn",
    "Docker", "Kubernetes", "Linux", "Git", "Airflow", "Tableau", "Power BI",
    "Spark", "Hadoop", "PostgreSQL", "MongoDB", "MySQL", "FastAPI", "Flask"
]

def clean_text(text):
    if pd.isna(text):
        return ""
    text = re.sub(r"<.*?>", " ", text)
    text = re.sub(r"[^a-zA-Z0-9+.#]", " ", text)
    return text.lower()

def extract_skills(requirements_series):
    all_skills = []
    for req in requirements_series:
        cleaned = clean_text(req)
        for skill in SKILLS:
            if skill.lower() in cleaned:
                all_skills.append(skill)
    return Counter(all_skills)

if __name__ == "__main__":
    df = pd.read_csv("data/jobs.csv")
    skill_counts = extract_skills(df["requirement"])
    top_skills = skill_counts.most_common(20)
    df_skills = pd.DataFrame(top_skills, columns=["skill", "count"])
    os.makedirs("data", exist_ok=True)
    df_skills.to_csv("data/top_skills.csv", index=False)
