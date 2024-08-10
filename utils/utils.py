from typing import Tuple, List, Any


def parse_input(user_input: str) -> Tuple[str, List[str]]:
    cmd, *args = user_input.split()
    return cmd.strip().lower(), args


def list_to_numerated_rows(lst: List[Any]) -> str:
    """
    Converts a list to numerated rows.
    Args:
        lst (List[Any]): A list of elements to be converted to numerated rows.
    Returns:
        str: A string with each element of the list on a new line, prefixed with its index.
    Example:
        >>> list_to_numerated_rows(["first", "second", "third"])
        1. first
        2. second
        3. third
    """
    return "\n".join(f"{i + 1}. {record}" for i, record in enumerate(lst))
