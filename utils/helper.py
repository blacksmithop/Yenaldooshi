from typing import List, Tuple
from utils.models import AvatarItems


def chunks(lst: List, n: int):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def getTitle(text: str):
    return f"<h1 style='text-align: center;'>{text}</h1>"

def groupItemCategories(items: Tuple[AvatarItems]):
    groups = {}
    for item in items:
        if item.type not in groups:
            groups[item.type] = [item]
        else:
            groups[item.type].append(item)

    return groups