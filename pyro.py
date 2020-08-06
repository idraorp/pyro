from pyrogram import Client

api_id = 1417324
api_hash = "a1ad27ec651079a80f66e6fee406e437"

with Client("my_account", api_id, api_hash) as app:
    app.send_message("me", "bruhfurhf **brubruh**!")