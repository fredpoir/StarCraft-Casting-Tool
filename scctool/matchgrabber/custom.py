"""Grab match data from websites."""
import logging

import requests

import scctool.settings.translation

# create logger
module_logger = logging.getLogger(__name__)
_ = scctool.settings.translation.gettext


class MatchGrabber(object):
    """Parent definition,i.e., for custom matchs."""

    _provider = "Custom"

    def __init__(self, matchData, controller, ident=False):
        """Init match grabber."""
        self._id = 0
        self.setID(ident)
        self._controller = controller
        self._matchData = matchData
        self._urlprefix = ""
        self._apiprefix = ""
        self._rawData = None

    def setID(self, ident=False):
        """Set ID."""
        if ident:
            self._id = int(ident)

    def getID(self):
        """Get ID as int."""
        return int(self._id)

    def _getAPI(self, ident=False):
        if id:
            self.setID(ident)
        return self._apiprefix + str(self.getID())

    def getURL(self, ident=False):
        """Get URL."""
        if ident:
            self.setID(ident)
        return self._urlprefix + str(self.getID())

    def getProvider(self):
        """Get name of the provider."""
        return self._provider

    def grabData(self, metaChange=False, logoManager=None):
        """Grab match data."""
        raise ValueError(
            "Error: Cannot grab data from this provider.")

    def _getJson(self):
        data = requests.get(url=self._getAPI()).json()
        return data

    def _aliasPlayer(self, player):
        return self._controller.aliasManager.translatePlayer(player)

    def _aliasTeam(self, player):
        return self._controller.aliasManager.translateTeam(player)

    def downloadLogos(self, logoManager):
        """Download logos."""
        raise UserWarning(
            "Error: Cannot download logos from this provider.")

    def downloadBanner(self):
        """Download Banner."""
        raise UserWarning(
            "Error: Cannot download a match banner from this provider.")
