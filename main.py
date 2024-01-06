import requests
import datetime

def update_discord_status():
    # Calculate time 24 hours from now
    future_time = datetime.datetime.utcnow() + datetime.timedelta(hours=24)
    formatted_time = future_time.strftime('%Y-%m-%dT%H:%M:%S.%fZ')

    # Data to be sent
    data = {
        "invites_disabled_until": None,
        "dms_disabled_until": formatted_time
    }

    # Discord API endpoint
    url = 'https://discord.com/api/v9/guilds/1067165013397213286/incident-actions'

    # Your bot token
    token = 'MTE0Nzg5Mjg4NTczNjQwNzEzMA.GwFPcF.mrdXYd7Z8Q8MivhvUOHUrnvR2_ViKvwdq9O1DE'

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

