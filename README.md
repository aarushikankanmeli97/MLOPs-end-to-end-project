# 🎬 Movie Review Analysis — MLOps Pipeline

## 📌 Overview

This project demonstrates an **end-to-end MLOps pipeline** built around a **movie review analysis use case**, with a strong focus on **production-grade machine learning practices**.

The pipeline covers the full ML lifecycle:

* Data ingestion
* Data validation & preprocessing
* Feature engineering
* Model training & evaluation
* Model registration
* Experiment tracking
* Pipeline orchestration (DVC)
* CI/CD integration

It leverages modern tooling such as:

* **MLflow (via Dagshub)** for experiment tracking
* **DVC** for pipeline and data versioning
* **AWS S3** for remote storage
* **Docker-ready structure & modular Python codebase**
* **GitHub Actions** for CI

---

## ⚡ TL;DR

* Built a **complete MLOps pipeline** for movie review analysis
* Uses **DVC + MLflow (Dagshub)** for reproducibility and tracking
* Integrated **AWS S3** as remote storage
* Automated workflows with **CI setup (GitHub Actions)**

---

## 🏗️ Project Setup & Workflow

### 🔹 Project Initialization

1. Create repo and clone locally
2. Create virtual environment:

   ```bash
   conda create -n atlas python=3.10
   conda activate atlas
   ```
3. Install cookiecutter:

   ```bash
   pip install cookiecutter
   ```
4. Generate project template:

   ```bash
   cookiecutter -c v1 https://github.com/drivendata/cookiecutter-data-science
   ```
5. Rename:

   ```
   src.models → src.model
   ```
6. Commit and push:

   ```bash
   git add .
   git commit -m "Initial project structure"
   git push
   ```

---

### 🔹 MLflow Setup (Dagshub)

7. Go to Dagshub dashboard
8. Create and connect repository
9. Copy experiment tracking URL and code snippet
10. Install dependencies:

```bash
pip install dagshub mlflow
```

11. Run experiment notebooks
12. Commit and push changes

---

### 🔹 DVC Pipeline Setup

13. Initialize DVC:

```bash
dvc init
```

14. Create local storage:

```
local_s3/
```

15. Add local remote:

```bash
dvc remote add -d mylocal local_s3
```

16. Add core pipeline modules inside `src/`:

* logger
* data_ingestion.py
* data_preprocessing.py
* feature_engineering.py
* model_building.py
* model_evaluation.py
* register_model.py

17. Add configuration files:

* `dvc.yaml` (till model evaluation.metrics)
* `params.yaml`

18. Run pipeline:

```bash
dvc repro
```

19. Check pipeline status:

```bash
dvc status
```

20. Commit and push

---

### 🔹 AWS S3 Integration

21. Create IAM user and S3 bucket
22. Install dependencies:

```bash
pip install "dvc[s3]" awscli
```

23. (Optional) Manage remotes:

```bash
dvc remote list
dvc remote remove <name>
```

24. Configure AWS:

```bash
aws configure
```

25. Add S3 as remote:

```bash
dvc remote add -d myremote s3://<bucket-name>
```

---

### 🔹 Application Layer

26. Create directory:

```
flask_app/
```

27. Install Flask and run app:

```bash
pip install flask
dvc push
```

---

### 🔹 Dependency Management

28. Export dependencies:

```bash
pip freeze > requirements.txt
```

---

### 🔹 CI/CD Setup

29. Add workflow file:

```
.github/workflows/ci.yaml
```

30. Generate Dagshub token:

* Go to repo → Settings → Tokens
* Generate new token

```
capstone_test: 54b1d67648a9b1267ef906fsdfsd8b292f779f0
```

31. Add token to GitHub Secrets & Variables and update CI file

---

### 🔹 Testing Setup

32. Add directories:

```
tests/
scripts/
```

* Contains test-related scripts for CI

---

