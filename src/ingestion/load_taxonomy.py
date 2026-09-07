import pandas as pd
from sqlalchemy import create_engine
import os

engine = create_engine(os.getenv("POSTGRES_URL"))

skills = pd.read_csv("data/raw/onet/Technology_Skills.txt", sep="\t")
skills = skills.rename(columns={
    "Example": "skill_name",
    "Commodity Code": "skill_id"
})[["skill_id", "skill_name"]].drop_duplicates()

skills.to_sql("skill_taxonomy", engine, if_exists="replace", index=False)
print(f"Loaded {len(skills)} skills into skill_taxonomy")