import json
import random
from pathlib import Path

# Paths
DATA_FILE = Path("data/quotes.json")
README_FILE = Path("README.md")

def get_random_quote():
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        quotes = json.load(file)
    return random.choice(quotes)

def update_readme(quote):
    with open(README_FILE, "r", encoding="utf-8") as file:
        lines = file.readlines()

    # Look for a placeholder in the README
    start_marker = "<!-- START QUOTE -->"
    end_marker = "<!-- END QUOTE -->"
    start_index = lines.index(f"{start_marker}\n") + 1
    end_index = lines.index(f"{end_marker}\n")

    # Replace the quote section
    lines[start_index:end_index] = [
        "```\n",
        f"{quote['text']}\n",
        f"— {quote['autor']}\n",
        "```\n",
    ]

    with open(README_FILE, "w", encoding="utf-8") as file:
        file.writelines(lines)

def main():
    quote = get_random_quote()
    update_readme(quote)

if __name__ == "__main__":
    main()