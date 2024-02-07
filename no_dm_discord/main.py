import requests
import datetime
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def update_discord_status():
    # Calculate time 24 hours from now
    future_time = datetime.datetime.utcnow() + datetime.timedelta(hours=24)
    formatted_time = future_time.strftime('%Y-%m-%dT%H:%M:%S.%fZ')

    # Data to be sent
    data = {
        "invites_disabled_until": None,
        "dms_disabled_until": formatted_time
    }

    # Access the bot token and guild ID from environment variables
    token = os.getenv('DISCORD_BOT_TOKEN')
    guild_id = os.getenv('DISCORD_GUILD_ID')

    # Discord API endpoint, now dynamically using the guild ID
    url = f'https://discord.com/api/v9/guilds/{guild_id}/incident-actions'

    # Headers
    headers = {
        'Authorization': f'Bot {token}',
        'Content-Type': 'application/json'
    }

    # Make the PUT request
    response = requests.put(url, json=data, headers=headers)

    # Check the response
    if response.status_code in [200, 204]:
        print("Status updated successfully.")
    else:
        print(f"Failed to update status. Response Code: {response.status_code}, Response Body: {response.text}")

# Call the function
update_discord_status()
