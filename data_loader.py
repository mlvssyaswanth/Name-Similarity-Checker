# loads the list of names we match against

from data.names_dataset import PERSON_NAMES


def load_names():
    """Just return the names list. Kept separate so we can swap dataset later if needed."""
    return list(PERSON_NAMES)
