from pyrogram import Client
from Config import Config


plugins = dict(
    root="plugins",
    include=[
        "start",
        "help",
        "forceSubscribe"
    ]
)

app = Client(
     'eagle_eye',
      bot_token = Config.2029835371:AAHzwWfuqwA4rf-wbaBMC4CfZuveKRfegFQ,
      api_id = Config.8522555,
      api_hash = Config.9e0b9e90b854c23fe89ee57b0a75ff32,
      plugins = plugins
)

app.run()
