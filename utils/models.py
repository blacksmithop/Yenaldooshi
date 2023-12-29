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


class EmojiCollection(BaseModel):
    id: str
    emojiIds: List[str]
    promoImageUrl: str
    promoImagePrimaryColor: str
    iconUrl: str
    bonusLoadingScreenId: str
    bonusMinItemCount: int
    emojis: List[Emoji] = []


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


def _getEmojiCollectionObjects(emojis: List[Dict[str, Union[str, Dict]]]):
    emojCollectioniList = []
    for emoji in emojis:
        try:
            entry = EmojiCollection(**emoji)
            emojCollectioniList.append(entry)
        except Exception as e:
            print(e)
            print(emoji)
    return emojCollectioniList


def _mapEmojiCollections(emojis, collections):
    for item in collections:
        emojiIds = item.emojiIds
        emojis = [emoji for emoji in emojis if emoji.id in emojiIds]
        item.emojis = emojis
    return collections


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


class AvatarItemSets(BaseModel):
    id: str
    promoImageUrl: str
    avatarItemIds: List[str]
    promoImagePrimaryColor: str = None
    ids: List[AvatarItems] = []


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


def _getAvatarItemSetObjects(items: List[Dict[str, Union[str, Dict]]]):
    itemSetList = []
    for item in items:
        try:
            entry = AvatarItemSets(**item)
            itemSetList.append(entry)
        except Exception as e:
            print(e)
            print(item)
    return itemSetList


def _mapItemItemSets(sets, items):
    for setItem in sets:
        avatarIds = setItem.avatarItemIds
        ids = [item.imageUrl for item in items if item.id in avatarIds]
        setItem.ids = ids
    return sets


class ProfileIcons(BaseModel):
    id: str
    name: str
    rarity: str


def getIconName(name: str):
    parts = name.split(":")
    icon = parts[1]
    return icon


def _getProfileIconObjects(profile_icons: List[Dict[str, Union[str, Dict]]]):
    profileIconList = []
    for icon in profile_icons:
        try:
            entry = ProfileIcons(**icon)
            entry.name = getIconName(entry.name)

            profileIconList.append(entry)
        except Exception as e:
            print(e)
            print(icon)
    return profileIconList

def getUrl(text: str):
    return text.split("'")[1]

class Backgrounds(BaseModel):
    id: str
    rarity: str
    imageNight: Image
    imageNightWide: Image
    imageNightSmall: Image
    imageDay: Image
    imageDayWide: Image
    imageDaySmall: Image


def _getBackgroundObjects(backgrounds: List[Dict[str, Union[str, Dict]]]):
    backgroundList = []
    for icon in backgrounds:
        try:
            entry = Backgrounds(**icon)
            backgroundList.append(entry)
        except Exception as e:
            print(e)
            print(icon)
    return backgroundList


class AdvancedRoleCardOffers(BaseModel):
    id: str
    advancedRoleId: str
    avatarItemSetId: str
    abilityExchangeVoucherCount: int
    talismanCount: int
    loyaltyTokenCount: int
    promoImageUrl: str

def _getRoleCardOfferObjects(offers: List[Dict[str, Union[str, Dict]]]):
    roleCardOfferList = []
    for icon in offers:
        try:
            entry = AdvancedRoleCardOffers(**icon)
            roleCardOfferList.append(entry)
        except Exception as e:
            print(e)
            print(icon)
    return roleCardOfferList