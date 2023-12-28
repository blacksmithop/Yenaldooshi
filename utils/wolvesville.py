from utils.models import (
    _getRoleObjects,
    _getEmojiObjects,
    _getRoleIconObjects,
    _mapRoleRoleIcons,
    _getScreenObjects,
    _getAvatarObjects
)
from dotenv import load_dotenv
from os import getenv
import requests

load_dotenv()


class Wolvesville:
    def __init__(self, api_key=None):
        if api_key == None:
            API_KEY = getenv("API_KEY")
        else:
            API_KEY = api_key
        self.headers = {"Authorization": f"Bot {API_KEY}"}
        self.url = "https://api.wolvesville.com"

    def getRoles(self):
        data = requests.get(f"{self.url}/roles", headers=self.headers).json()
        roles = data["roles"]
        resp = _getRoleObjects(roles=roles)
        return resp

    def getRoleIcons(self):
        data = requests.get(f"{self.url}/items/roleIcons", headers=self.headers).json()
        resp = _getRoleIconObjects(icons=data)
        return resp

    def getRoleRoleIcons(self):
        roles = self.getRoles()
        icons = self.getRoleIcons()
        mapping = _mapRoleRoleIcons(roles=roles, icons=icons)
        return mapping

    def getEmojis(self):
        emojis = requests.get(f"{self.url}/items/emojis", headers=self.headers).json()
        resp = _getEmojiObjects(emojis=emojis)
        return resp

    def getScreens(self):
            screens = requests.get(f"{self.url}/items/loadingScreens", headers=self.headers).json()
            resp = _getScreenObjects(screens=screens)
            return resp

    def getItems(self):
        screens = requests.get(f"{self.url}/items/avatarItems", headers=self.headers).json()
        resp = _getAvatarObjects(items=screens)
        return resp