import os
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(os.getenv("POSTGRES_URL"))

files = {
    "skill_taxonomy": "Technology_Skills.txt",
    "skills": "Skills.txt",
    "tools_used": "Tools_Used.txt"
}

for table, filename in files.items():
    path = os.path.join("data", "raw", "onet", filename)
    df = pd.read_csv(path, sep="\t")
    df.to_sql(table, engine, if_exists="replace", index=False)
    print(f"Loaded {len(df)} rows into {table}")
    