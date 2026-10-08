# Handle Missing Values — Veda Technology

## Objective
Learn basic data preprocessing for machine learning by identifying and treating missing values using Pandas.

## Tools
- Python
- Pandas
- Jupyter Notebook

## Method Used
- Numerical columns (`Age`, `Fare`): median imputation.
- Categorical column (`Embarked`): mode imputation.

Median is preferred for numerical data because it is less sensitive to extreme values than the mean. Mode is appropriate for a categorical column.

## Files
- `titanic_missing_values.csv` — original dataset containing missing values.
- `titanic_cleaned.csv` — cleaned dataset.
- `missing_value_analysis.csv` — before/after missing-value summary.
- `handle_missing_values.py` — Python implementation.
- `handle_missing_values.ipynb` — Jupyter Notebook.
- `project_report.pdf` — project report.

## Run
```bash
pip install pandas jupyter
python handle_missing_values.py
```
