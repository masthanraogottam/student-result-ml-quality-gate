# Student Result ML: Practicals 3 and 4

This repository contains the student-result prediction project with two separate GitHub Actions workflows.

## Practical 3 — Model Quality Gate

Files: `train_model.py`, `quality_gate.py`, `test_ml_pipeline.py`, and `.github/workflows/practical-3-quality-gate.yml`.

The pipeline trains a reproducible Logistic Regression model, produces `metrics.json`, checks that accuracy is at least **0.85**, and runs automated tests. If accuracy is below the threshold, the quality gate exits with a non-zero status and the workflow fails.

## Practical 4 — Save Model Artifacts

File: `.github/workflows/practical-4-artifacts.yml`.

This workflow repeats training, quality-gate validation, and unit tests, then uploads these generated files as a GitHub Actions artifact named `student-result-ml-artifacts`:
- `student_result_model.pkl`
- `metrics.json`
- `student_results.csv`

Artifact retention is set to 7 days. The artifact upload runs only after training, quality gate, and tests succeed.

## Run locally

```bash
python -m pip install -r requirements.txt
python train_model.py
python quality_gate.py
python -m unittest discover -v
```

The dataset is synthetic and is intended for educational practice only, not real student assessment. Labels are 1 = PASS and 0 = FAIL, using a weighted score of attendance (25%), internal marks (35%), assignments (20%), and previous score (20%); a score of 60 or more is labelled PASS.
