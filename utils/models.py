from pydantic import BaseModel
from typing import Dict, List, Union


class Image(BaseModel):
    url: str
    width: int
    height: int


class Role(BaseModel):
    id: str
    team: str
    aura: str
    name: str
    description: str
    image: Image


def _getRoleObjects(roles: List[Dict[str, Union[str, Dict]]]):
    roleList = []
    for role in roles:
        try:
            entry = Role(**role)
            roleList.append(entry)
        except Exception as e:
            print(e)
            print(role)
    return roleList


class Emoji(BaseModel):
    id: str
    name: str
    rarity: str
    urlPreview: str
    urlAnimation: str
    event: str = None


def _getEmojiObjects(emojis: List[Dict[str, Union[str, Dict]]]):
    emojiList = []
    for emoji in emojis:
        try:
            entry = Emoji(**emoji)
            emojiList.append(entry)
        except Exception as e:
            print(e)
            print(emoji)
    return emojiList
