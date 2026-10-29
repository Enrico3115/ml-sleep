# Sleep Debt & Screen Time Regression

Predicting next-day fatigue based on late-night phone habits.

## Dataset
- **Target Variable:** `next_day_fatigue_score` (Regression)
- **Source:** [Kaggle Dataset](https://www.kaggle.com/datasets/samartalwar/sleep-debt-and-screen-time-late-night-phone-habits)

## Project Structure
```text
├── data/                  # Raw dataset (ignored by git)
├── notebooks/
│   └── 01_eda_and_modeling.ipynb
├── src/
│   └── download_data.py   # Script to authenticate and fetch Kaggle data
├── .env                   # Kaggle API token (create manually, ignored by git)
├── .gitignore
├── README.md
└── requirements.txt       # Requires: pandas, scikit-learn, kaggle, python-dotenv, ipykernel
```

## Setup
1. Clone the repository.
2. Create and activate a virtual environment:
   ```powershell
   python -m venv .venv
   .venv\Scripts\activate
   ```
3. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
4. Set up Kaggle authentication by creating a `.env` file in the project root:
   ```text
   KAGGLE_API_TOKEN=your_kaggle_token_here
   ```
5. Download the dataset and start modeling by running `notebooks/01_eda_and_modeling.ipynb`, which automatically calls `src/download_data.py`.