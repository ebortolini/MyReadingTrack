# MyReadingTrack

A simple project to analyze your reading habits using CSV files and [GitHub Copilot SDK](https://github.com/github/copilot-sdk/tree/main).

## Requirements
- Python 3.8+
- [Copilot CLI](https://github.com/github/copilot-cli?locale=en-US)
- uv tool -> Good introduction [here](https://realpython.com/python-uv/#getting-to-know-uv-for-python)

## Sync
```
uv sync
```

## Usage
1. Place your yearly reading CSV files in the `CSVs` folder (e.g., `2023.csv`, `2024.csv`).
2. Run the main script:

```
uv run main.py
```

3. When prompted, type your question about your reading habits, or type `exit` to quit.

## Notes
- If you get encoding errors, try saving your CSVs as UTF-8 or update the code to use `encoding='latin-1'`.
- The first time you run, the CSV data is loaded and sent to the Copilot session. Each question is then answered using that context.
