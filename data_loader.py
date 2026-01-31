"""
Data loading for the name similarity checker.
Provides a single entry point to load the predefined person names dataset.
"""

from data.names_dataset import PERSON_NAMES


def load_names():
    """
    Load the predefined list of person names from the dataset.

    Returns
    -------
    list of str
        All person names in the dataset. Order is stable and deterministic.
    """
    return list(PERSON_NAMES)
