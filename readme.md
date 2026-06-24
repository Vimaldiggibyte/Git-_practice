# Sales Data Cleaner

A simple Python script that cleans raw sales data.

## Features

* Remove rows with missing customer or amount values
* Remove duplicate order IDs
* Remove negative amount values
* Normalize dates to YYYY-MM-DD format

## Project Structure

```text
sales-data-cleaner/
├── data/
│   ├── raw_sales.csv
│   └── clean_sales.csv
├── src/
│   └── clean.py
├── .gitignore
└── README.md
```

## Run

```bash
python src/clean.py
```

## Git Practice

This project was used to practice:

* Commits and version control
* Branching (`feature/fix-date-format`)
* Fast-forward merging
* Branch cleanup (`git branch -d`)
* Pushing code to GitHub
