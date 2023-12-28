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
    icons: List[str] = None


class RoleIcon(BaseModel):
    id: str
    rarity: str
    image: Image
    roleId: str


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


def _getRoleIconObjects(icons: List[Dict[str, Union[str, Dict]]]):
    roleIconList = []
    for icon in icons:
        try:
            entry = RoleIcon(**icon)
            roleIconList.append(entry)
        except Exception as e:
            print(e)
            print(icon)
    return roleIconList


def _mapRoleRoleIcons(roles, icons):
    for role in roles:
        id = role.id
        iconList = [icon.image.url for icon in icons if icon.roleId == id]
        role.icons = iconList
    return roles


class LoadingScreen(BaseModel):
    id: str
    rarity: str
    image: Image
    imageWide: Image
    imagePrimaryColor: str

def _getScreenObjects(screens: List[Dict[str, Union[str, Dict]]]):
    screenList = []
    for screen in screens:
        try:
            entry = LoadingScreen(**screen)
            screenList.append(entry)
        except Exception as e:
            print(e)
            print(screen)
    return screenList

class AvatarItems(BaseModel):
    id: str
    imageUrl: str
    type: str
    rarity: str
    costInGold: int = 0

def _getAvatarObjects(items: List[Dict[str, Union[str, Dict]]]):
    itemList = []
    for item in items:
        try:
            entry = AvatarItems(**item)
            itemList.append(entry)
        except Exception as e:
            print(e)
            print(item)
    return itemList