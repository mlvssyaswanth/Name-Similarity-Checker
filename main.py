# name similarity checker - find closest names from our list when user types something

from data_loader import load_names
from similarity import rank_names

HOW_MANY_TO_SHOW = 10


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
        print(f"Top {HOW_MANY_TO_SHOW} similar names:")
        for name, score in rank_names(query, names, top_n=HOW_MANY_TO_SHOW):
            print(f"  {score:.4f}  {name!r}")
        print()


if __name__ == "__main__":
    main()
