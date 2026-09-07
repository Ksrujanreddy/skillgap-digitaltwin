## skill_taxonomy (Postgres)
| Field | Type | Description |
|---|---|---|
| skill_id | string | O*NET commodity code |
| skill_name | string | Human-readable skill name |

## job_postings (MongoDB)
| Field | Type | Description |
|---|---|---|
| title | string | Job title |
| description | string | Full posting text |
| date_posted | date | Used for time-series demand |
| company | string | Employer name |

## synthetic_students (interim JSON, will move to Postgres in Phase 4)
| Field | Type | Description |
|---|---|---|
| student_id | UUID | Anonymized identifier |
| target_role | string | One of the 3 scoped roles |
| academic_score | float | Synthetic GPA (4-10 scale) |
| skills | dict | skill_name -> self-rated level (1-5) |
| certifications_count | int | Number of certifications |
| projects_count | int | Number of projects |