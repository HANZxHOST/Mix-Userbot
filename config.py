from os import getenv

from dotenv import load_dotenv

load_dotenv()

api_id = int(getenv("32937413"))
api_hash = getenv("49471bf6497846c6feacdf2272eb19b4")
session = getenv("BQH2lcUArnHNYIwnOAXNdKLzNjQOKB3WXtcyO1OvQ5YWBRoYAzJT2tBdOr395tc8Y9QMATpfMKuMWpozcjaapnu5G2jg8egfHVqOih-kmeEnLzdRa0cKlxIi2wjlIe5yYpyaI8_tSFbQVdyr1epTEpoqEVp2jgSHvHma9s_3aoTv_UJSTJdg66EEyMx_jDrP9-fZJaaxu0OoB3Fp_ybYW7j3TQObuoDJtRR-ugDH7p2A7a3HrY0-L7KSlMUP7RySYO7qNCeGUBZtmTF8yKnjYcG9KLjKaTC8Z219IkJ_3Oqq0GV9HD1cUguxxzJUcSjAUVJW70xPBHft3rGUYT7hDhBvpguJQgAAAAHFh6CDAA")
bot_token = getenv("8340436784:AAEgOOWvzV9fDVGX5pFeWktRWwDgUzLwxe8")
db_name = getenv("hanzuserbot")
mongo_uri = getenv("mongodb+srv://hanzUserbot:<db_password>@cluster0.ekhrzhw.mongodb.net/?appName=Cluster0")
def_bahasa = getenv("def_bahasa", "toxic")
log_pic = getenv("log_pic", "https://telegra.ph//file/43cec0ae0ded594b55247.jpg")
heroku_api = getenv("heroku_api")
heroku_app_name = getenv("heroku_app_name")
upstream_repo = getenv(
    "upstream_repo",
    "https://github.com/naya1503/Mix-Userbot",
)
upstream_branch = getenv("upstream_branch", "final")
git_token = getenv("git_token", None)
log_channel = getenv("-5020453370")
genius_api = getenv(
    "genius_api",
    "zhtfIphjnawHBcLFkIi-zE7tp8B9kJqY3xGnz_BlzQM9nhJJrD7csS1upSxUE0OMmiP3c7lgabJcRaB0hwViow",
)
# scheme = getenv("scheme", None)
# hostname = getenv("hostname", None)
# port = int(getenv("port", None))
# username = getenv("username", None)
# password = getenv("password", None)
