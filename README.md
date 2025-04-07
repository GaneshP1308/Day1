# Netflix Data Cleaning Project

This project focuses on cleaning a raw dataset from Netflix using Python and Pandas. The dataset includes information about Netflix shows such as title, director, cast, country, release year, etc.

## 📁 Files Included
- `data_cleaning.py` – Python script that performs data cleaning.
- `netflix_cleaned.csv` – Cleaned version of the dataset.

## 🧹 Data Cleaning Steps Performed
1. **Handled missing values** – Replaced nulls with appropriate defaults.
2. **Removed duplicate records** – Ensured no repeated data.
3. **Standardized text values** – Made values consistent (e.g., country names).
4. **Converted date formats** – Standardized to dd-mm-yyyy format.
5. **Renamed column headers** – Lowercase, removed spaces.
6. **Checked and fixed data types** – Ensured correct types like int and datetime.

## 🛠️ Tools Used
- Python 3.12
- Pandas

## 📌 How to Run
```bash
python data_cleaning.py
