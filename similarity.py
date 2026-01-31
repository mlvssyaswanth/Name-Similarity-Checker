# compare user input to each name and score how similar they are (0 to 1)

from typing import List, Optional, Tuple

import difflib


def compute_similarity(name_a: str, name_b: str) -> float:
    """Score between 0 and 1. Same name (ignoring case) = 1.0."""
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
    """Sort all names by how close they are to query. Pass top_n to limit results."""
    query_str = str(query).strip() if query is not None else ""
    if names is None:
        names = []
    scored = [(name, compute_similarity(query_str, name)) for name in names]
    # higher score first, then alphabetical for ties
    scored.sort(key=lambda x: (-x[1], x[0]))
    if top_n is not None:
        return scored[:top_n]
    return scored
