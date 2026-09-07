import pandas as pd
from pymongo import MongoClient
import os

client = MongoClient(os.getenv("MONGO_URL"))
db = client.skillgap_db

df = pd.read_csv("data/raw/job_postings/postings.csv")
target_roles = ["Software Engineer", "Data Scientist", "Cybersecurity"]
mask = df["title"].str.contains("|".join(target_roles), case=False, na=False)
filtered = df[mask]

records = filtered.to_dict("records")
db.job_postings.insert_many(records)
print(f"Inserted {len(records)} job postings")