from typing import List


def chunks(lst: List, n: int):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def getTitle(text: str):
    return f"<h1 style='text-align: center;'>{text}</h1>"
