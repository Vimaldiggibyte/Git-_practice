# Sales Data Cleaner

A simple Python project that cleans raw sales data using Pandas and demonstrates practical Git workflows.

## Features

* Remove rows with missing customer or amount values
* Remove duplicate order IDs
* Remove negative amount values
* Normalize dates to YYYY-MM-DD format
* Generate basic dataset summary information

  * Row count
  * Column count
  * Dataset description

## Project Structure

```text
sales-data-cleaner/
├── data/
│   ├── raw_sales.csv
│   └── clean_sales.csv
├── src/
│   ├── clean.py
│   └── summary.py
├── .gitignore
└── README.md
```

## Run

```bash
python src/clean.py
```

## Technologies Used

* Python
* Pandas
* NumPy
* Git
* GitHub

## Git Concepts Practiced

### Repository Management

* Git initialization
* Staging and committing changes
* Writing meaningful commit messages
* Viewing commit history with `git log`

### Branching and Merging

* Creating feature branches
* Switching between branches
* Fast-forward merge
* Merge commits
* Branch cleanup using `git branch -d`

### Remote Repository Operations

* GitHub repository creation
* SSH key configuration
* Pushing branches to GitHub
* Tracking remote branches

### Commit Management

* Modifying commits using `git commit --amend`
* Renaming commit messages
* Adding forgotten files to previous commits

### Rebase

* Standard rebase
* Interactive rebase
* Reordering commits
* Squashing commits
* Rewording commit messages
* Dropping unwanted commits

### Debugging and Recovery

* Using `git reflog` to recover commits
* Using `git bisect` to identify bug-introducing commits

### Inspection Commands

* `git diff`
* `git log --oneline`
* `git log --graph --decorate --all`
* `git status`

## Learning Outcomes

Through this project, I gained hands-on experience with:

* Version control fundamentals
* Branching strategies
* Merge and rebase workflows
* Commit history management
* GitHub collaboration basics
* Recovery and debugging tools in Git
