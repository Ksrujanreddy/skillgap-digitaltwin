## Target Roles (v1 scope)
1. Software Engineer
2. Data Scientist
3. Cybersecurity Analyst

Rationale: high job-posting volume, well-documented skill taxonomies in O*NET/ESCO,
and clear certification pathways — good for prototyping before expanding scope.
## Learner Persona & Available Inputs
- Academic record: GPA/percentage, relevant coursework list
- Self-reported skills: skill name + self-rated level (1-5)
- Resume text (optional, free text)
- Certifications: list of completed certification names
- Project history: project titles + short descriptions
- Target role: one of the 3 roles above (student-selected)
## Module Specifications

### 1. SGSI (Skill Gap Severity Index)
Input: student's skill vector + target role's required skill weights (from job postings)
Process: weighted shortfall calculation
Output: a single score 0-1 per student, plus a per-skill breakdown

### 2. Forecasting Engine
Input: 12-24 months of historical monthly skill-mention counts per skill
Process: LSTM time-series prediction
Output: predicted demand for each skill, 6-12 months ahead

### 3. Employability Prediction
Input: academic score + SGSI + forecast-alignment + certifications + projects
Process: XGBoost/NN classification or regression
Output: employability score (0-100) or employable/at-risk label

### 4. Explainability (SHAP)
Input: trained employability model + a specific student's feature vector
Process: SHAP value computation (global + local)
Output: ranked feature importances + one-sentence human explanation

### 5. Roadmap Generator
Input: SGSI per-skill breakdown + forecasted demand + course catalog + time budget
Process: weighted ranking + greedy/knapsack selection
Output: ranked list of courses/certifications/projects