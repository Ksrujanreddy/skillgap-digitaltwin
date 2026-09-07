import pandas as pd
import numpy as np
import uuid

np.random.seed(42)
N = 1000
roles = ["Software Engineer", "Data Scientist", "Cybersecurity"]

# a small skill pool per role — expand later using your taxonomy
role_skills = {
    "Software Engineer": ["Python", "Java", "SQL", "Git", "REST APIs", "Data Structures"],
    "Data Scientist": ["Python", "SQL", "Machine Learning", "Statistics", "Pandas", "TensorFlow"],
    "Cybersecurity": ["Network Security", "Linux", "Python", "Cryptography", "SIEM Tools"]
}

rows = []
for _ in range(N):
    role = np.random.choice(roles)
    gpa = round(np.clip(np.random.normal(7.5, 1.0), 4, 10), 2)
    skill_pool = role_skills[role]
    n_known = np.random.randint(1, len(skill_pool)+1)
    known_skills = np.random.choice(skill_pool, size=n_known, replace=False)
    skill_levels = {s: np.random.randint(1, 6) for s in known_skills}
    n_certs = np.random.poisson(1)
    n_projects = np.random.poisson(2)

    rows.append({
        "student_id": str(uuid.uuid4()),
        "target_role": role,
        "academic_score": gpa,
        "skills": skill_levels,
        "certifications_count": n_certs,
        "projects_count": n_projects
    })

df = pd.DataFrame(rows)
df.to_json("data/interim/synthetic_students.json", orient="records", indent=2)
print(f"Generated {len(df)} synthetic students")