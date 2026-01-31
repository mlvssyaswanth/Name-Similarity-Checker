"""
Similarity logic for matching user input against the name dataset.
Uses Python's difflib for deterministic, normalized string similarity (0-1).
No external services or cloud APIs; runs fully locally.
"""

from typing import List, Optional, Tuple

import difflib


def compute_similarity(name_a: str, name_b: str) -> float:
    """
    Compute a normalized similarity score between two names in the range [0, 1].
    Uses sequence matching; comparison is case-insensitive for stability.

    Parameters
    ----------
    name_a : str
        First name (e.g., user input).
    name_b : str
        Second name (e.g., dataset name).

    Returns
    -------
    float
        Similarity score in [0, 1]. 1.0 means identical (after normalization).
    """
    a = (str(name_a).strip().lower()) if name_a is not None else ""
    b = (str(name_b).strip().lower()) if name_b is not None else ""
    if not a and not b:
        return 1.0
    if not a or not b:
        return 0.0
    return difflib.SequenceMatcher(None, a, b).ratio()


def rank_names(
    query: str, names: List[str], top_n: Optional[int] = None
) -> List[Tuple[str, float]]:
    """
    Rank all names by similarity to the query. Results are deterministic and stable.

    Parameters
    ----------
    query : str
        The user-entered name to match against.
    names : list of str
        List of candidate names (e.g., from the dataset).
    top_n : int or None, optional
        If set, return only the top N results. If None, return all names ranked.

    Returns
    -------
    list of tuple (str, float)
        Pairs of (name, score) sorted by score descending. Scores are in [0, 1].
    """
    query_str = str(query).strip() if query is not None else ""
    if names is None:
        names = []
    scored = [(name, compute_similarity(query_str, name)) for name in names]
    scored.sort(key=lambda x: (-x[1], x[0]))
    if top_n is not None:
        return scored[:top_n]
    return scored
