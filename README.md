# Naive Bayes classifier Flight Review
 

# Naive Bayes Classifier – Flight Reviews

This project implements a simple **Naive Bayes classifier** to predict whether a flight is recommended based on its text review. It uses a small dataset of flight reviews and a from-scratch implementation built on top of `pandas`. :contentReference[oaicite:0]{index=0}

---

## Project structure

- `main.py` – loads the dataset, trains the Naive Bayes classifier, evaluates it and prints basic metrics.
- `Reviews.csv` – dataset containing flight reviews and their associated label (recommended / not recommended). :contentReference[oaicite:1]{index=1}
- `.gitattributes` – Git configuration file.

> If you change the structure or column names of `Reviews.csv`, make sure to update `main.py` accordingly.

---

## Requirements

- Python 3.x
- `pip` (Python package manager)
- Python libraries:
  - `pandas`

Install dependencies:

```bash
pip install pandas
