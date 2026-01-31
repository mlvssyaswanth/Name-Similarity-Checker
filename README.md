# Name Similarity Checker

## Objective

Build a name-matching system that finds the most similar names from a dataset when a user inputs a name.

## Key Steps

### Data Preparation

- Similar names (e.g. Geetha, Geeta, Gita, Gitu, Mohammed, Muhammad, Catherine, Katherine, etc.) are stored in a list.
- The dataset has at least 30 names and is kept in `data/names_dataset.py` as `PERSON_NAMES`.
- `data_loader.py` loads this list via `load_names()` for use by the matching logic.

### Similarity Matching

- When a user enters a name, it is compared against all names in the dataset.
- Similarity is computed using Python's built-in `difflib` (sequence matching). No external APIs, Vector DB, or cloud services are used—everything runs locally.
- Scores are normalized in the range 0–1 and ordering is deterministic.

## Expected Output

- **Best Match:** The closest matching name with a similarity score.
- **List of Matches:** A ranked list of other similar names with scores (e.g. top 10).

Example:

```
Name Similarity Checker
Enter a person name to find the most similar names in the dataset.

Enter a name (or press Enter to quit): Geeta

Best match: 'Geeta' (score: 1.0000)
Top 10 similar names:
  1.0000  'Geeta'
  0.9091  'Geetha'
  0.6667  'Gita'
  0.5000  'Margret'
  ...

Enter a name (or press Enter to quit): [Enter]
Goodbye.
```

## Project Structure

```
name-similarity-checker/
|-- data/
|   |-- __init__.py
|   +-- names_dataset.py   # List of 30+ person names (Geetha, Gita, Gitu, etc.)
|-- data_loader.py         # Loads the name list
|-- similarity.py          # Similarity computation and ranking
|-- main.py                # Entry point: input, match, print best + list
+-- README.md
```

## Setup and Run

- **Python:** 3.8 or newer (Windows or Linux).
- **Dependencies:** None; only the standard library is used.

### Run the program

From the project root:

**Windows:**
```powershell
python main.py
```

**Linux / macOS:**
```bash
python3 main.py
```

Type a name when prompted; press Enter with no input to quit.
