import os


class Config:

    BOT_TOKEN = os.environ.get("BOT_TOKEN","7619364034:AAHsuBrDWONcUzCPv8iMBehfh7GeojenSWk")

    SESSION_NAME = os.environ.get("SESSION_NAME", ":memory:")

    API_ID = int(os.environ.get("API_ID","2944318"))

    API_HASH = os.environ.get("API_HASH","9e93d41112872cc3bd58f4e29fd82c0a")

    CLIENT_ID = os.environ.get("CLIENT_ID","69689902615-3b0c0tgg7me2pulu9vftvnsf9o9mpf6i.apps.googleusercontent.com")

    CLIENT_SECRET = os.environ.get("CLIENT_SECRET","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")

    BOT_OWNER = int(os.environ.get("BOT_OWNER","7651377821"))

    AUTH_USERS_TEXT = os.environ.get("AUTH_USERS", "")

    AUTH_USERS = [BOT_OWNER] + (
        [int(user.strip()) for user in AUTH_USERS_TEXT.split(",")]
        if AUTH_USERS_TEXT
        else []
    )

    VIDEO_DESCRIPTION = (
        os.environ.get("VIDEO_DESCRIPTION", "").replace("<", "").replace(">", "")
    )

    VIDEO_CATEGORY = (
        int(os.environ.get("VIDEO_CATEGORY")) if os.environ.get("VIDEO_CATEGORY") else 0
    )

    VIDEO_TITLE_PREFIX = os.environ.get("VIDEO_TITLE_PREFIX", "")

    VIDEO_TITLE_SUFFIX = os.environ.get("VIDEO_TITLE_SUFFIX", "")

    DEBUG = bool(os.environ.get("DEBUG"))

    UPLOAD_MODE = os.environ.get("UPLOAD_MODE") or False
    if UPLOAD_MODE:
        if UPLOAD_MODE.lower() in ["private", "public", "unlisted"]:
            UPLOAD_MODE = UPLOAD_MODE.lower()
        else:
            UPLOAD_MODE = False

    CRED_FILE = "auth_token.txt"
