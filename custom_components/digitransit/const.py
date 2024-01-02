"""Constants for Digitransit."""
from datetime import timedelta

from logging import Logger, getLogger

LOGGER: Logger = getLogger(__package__)

NAME = "Digitransit"
DOMAIN = "digitransit"
VERSION = "0.0.0"
ATTRIBUTION = "Data from Digitransit"

INTERVAL = timedelta(seconds = 60)
