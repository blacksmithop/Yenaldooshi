from utils.models import (
    _getRoleObjects,
    _getEmojiObjects,
    _getRoleIconObjects,
    _mapRoleRoleIcons,
    _getScreenObjects,
    _getAvatarObjects,
    _getProfileIconObjects,
    _getEmojiCollectionObjects,
    _mapEmojiCollections,
    _getAvatarItemSetObjects,
    _mapItemItemSets,
    _getBackgroundObjects,
    _getRoleCardOfferObjects,
)
from dotenv import load_dotenv
from os import getenv
import requests
import requests_cache
from functools import lru_cache


requests_cache.install_cache("api_requests")

load_dotenv()


class Wolvesville:
    def __init__(self, api_key=None):
        if api_key == None:
            API_KEY = getenv("API_KEY")
        else:
            API_KEY = api_key
        self.headers = {"Authorization": f"Bot {API_KEY}"}
        self.url = "https://api.wolvesville.com"

    @lru_cache(maxsize=None)
    def getRoles(self):
        data = requests.get(f"{self.url}/roles", headers=self.headers).json()
        roles = data["roles"]
        resp = _getRoleObjects(roles=roles)
        return resp

    @lru_cache(maxsize=None)
    def getRoleIcons(self):
        data = requests.get(f"{self.url}/items/roleIcons", headers=self.headers).json()
        resp = _getRoleIconObjects(icons=data)
        return resp

    @lru_cache(maxsize=None)
    def getRoleRoleIcons(self):
        roles = self.getRoles()
        icons = self.getRoleIcons()
        mapping = _mapRoleRoleIcons(roles=roles, icons=icons)
        return mapping

    @lru_cache(maxsize=None)
    def getEmojis(self):
        emojis = requests.get(f"{self.url}/items/emojis", headers=self.headers).json()
        resp = _getEmojiObjects(emojis=emojis)
        return resp

    @lru_cache(maxsize=None)
    def getEmojiCollections(self):
        emojis = requests.get(
            f"{self.url}/items/emojiCollections", headers=self.headers
        ).json()
        resp = _getEmojiCollectionObjects(emojis=emojis)
        return resp

    @lru_cache(maxsize=None)
    def getEmojiAsCollections(self):
        emojis = self.getEmojis()
        collections = self.getEmojiCollections()
        mapping = _mapEmojiCollections(emojis=emojis, collections=collections)
        return mapping

    @lru_cache(maxsize=None)
    def getScreens(self):
        screens = requests.get(
            f"{self.url}/items/loadingScreens", headers=self.headers
        ).json()
        resp = _getScreenObjects(screens=screens)
        return resp

    @lru_cache(maxsize=None)
    def getBackgrounds(self):
        backgrounds = requests.get(
            f"{self.url}/items/backgrounds", headers=self.headers
        ).json()
        resp = _getBackgroundObjects(backgrounds=backgrounds)
        return resp

    @lru_cache(maxsize=None)
    def getItems(self):
        items = requests.get(
            f"{self.url}/items/avatarItems", headers=self.headers
        ).json()
        resp = _getAvatarObjects(items=items)
        return resp

    @lru_cache(maxsize=None)
    def getItemSets(self):
        itemSets = requests.get(
            f"{self.url}/items/avatarItemSets", headers=self.headers
        ).json()
        resp = _getAvatarItemSetObjects(items=itemSets)
        return resp

    @lru_cache(maxsize=None)
    def getItemAsSets(self):
        items = self.getItems()
        sets = self.getItemSets()
        mapping = _mapItemItemSets(sets=sets, items=items)
        return mapping

    @lru_cache(maxsize=None)
    def getProfileIcons(self):
        icons = requests.get(
            f"{self.url}/items/profileIcons", headers=self.headers
        ).json()
        resp = _getProfileIconObjects(profile_icons=icons)
        return resp

    @lru_cache(maxsize=None)
    def getRoleCardOffers(self):
        icons = requests.get(
            f"{self.url}/items/advancedRoleCardOffers", headers=self.headers
        ).json()
        resp = _getRoleCardOfferObjects(offers=icons)
        return resp
