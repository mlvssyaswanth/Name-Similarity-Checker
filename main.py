"""
Main entry point for the name similarity checker.
Loads the dataset, takes user input, computes similarity, and prints results.
"""

from data_loader import load_names
from similarity import rank_names

TOP_N_DEFAULT = 10


def main():
    names = load_names()
    if not names:
        print("Error: No names in dataset. Cannot run.")
        return

    print("Name Similarity Checker")
    print("Enter a person name to find the most similar names in the dataset.")
    print()

    while True:
        try:
            query = input("Enter a name (or press Enter to quit): ").strip()
        except EOFError:
            break
        except KeyboardInterrupt:
            print()
            print("Goodbye.")
            return
        if not query:
            print("Goodbye.")
            break

        ranked = rank_names(query, names)
        best_name, best_score = ranked[0] if ranked else (None, 0.0)

        print()
        print(f"Best match: {best_name!r} (score: {best_score:.4f})")
        print(f"Top {TOP_N_DEFAULT} similar names:")
        for name, score in rank_names(query, names, top_n=TOP_N_DEFAULT):
            print(f"  {score:.4f}  {name!r}")
        print()


if __name__ == "__main__":
    main()
