EMBED_CONFIG = {
    "title": "GHOST HERE",    # Maine Embed Title here 
    "description": "DADDY GHOST",   # Main Embed Description here 
    "color": 000000,   # Change embed color if you want (red)
    "fields": [
        {"name": "test", "value": "test", "inline": False},    # Embed Field → Juste Modify → Just edit the empty places
        {"name": "test", "value": "test", "inline": False},
        {"name": "test","value": "test", "inline": False},    # Exemple → "name": "Title 1", "value": "Hello, here is my message", "inline": False
    ],
    "image": "",   # Embed Icon url here → https://image.jpg
    "footer": "",  # Embed Footer here 
}

SERVER_CONFIG = {
    "new_name": "TRASHED BY GHOST",  # New Server Name here 
    "new_icon": "https://images-ext-1.discordapp.net/external/W0YRxLPLoVwkIOZTSLsalqrmW895TI77ao9nHW4wfx4/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1217116527308963901/a_a69a3d18d6dea267b5de7bfa7d007f17.gif",   # New Server Icon url here → https://image.jpg 
    "new_description": "TRASHED BY NEXTRA",  # New Server Description here 
}

WEBHOOK_CONFIG = {
    "default_name": "GHOST",  # Webhook Name here 
}


AUTO_RAID_CONFIG = {
    'num_channels': 50,  # Number of channels
    'channel_type': 'text',  # text/voice
    'channel_name': 'nuked by Ghost',  # Channel name
    'num_messages': 100,  # Number of message to spam
    'message_content': '@everyone https://discord.gg/HKDRZzDufR' # Spam Message
}

NO_BAN_KICK_ID = {
    1029093967389806753,       # Put Whitelist ID
    1027444990139453484,       # No Ban & No Kick
    222222222222,
}

BOT_PRESENCE = {
    "type": "streaming",  # "watching", "listening", or "watching"
    "text": "wake up"  # Your text presence
}
