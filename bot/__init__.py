import logging
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class ENV_VARS(object):
    API_ID = int(os.environ.get("API_ID", "25000803"))
    API_HASH = os.environ.get("API_HASH", "e2132a1280d0e6cd29a6e6fef064e112")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8546230285:AAEQTaODc5gmtgsG1tiPDmZaGzY6G0XOa18")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "sorensnapchatdownloaderbot")
    #AUTH_USER = int(os.environ.get("AUTH_USER", 5071059420))


Config = ENV_VARS

handler = Config.BOT_USERNAME


class CMD(object):
    START = ["start", f"start@{handler}"]
