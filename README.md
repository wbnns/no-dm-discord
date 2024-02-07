# No-DM Discord Bot

## Introduction

This Python package is designed for interacting with the Discord API to enable or disable direct messaging (DM) on a Discord server. It utilizes environment variables for secure and flexible configuration.

## Installation

To install and use this package, follow these steps:

1. Clone the repository:
   ```bash
   git clone [your-repository-url]
   ```
2. Navigate to the cloned directory:
   ```bash
   cd no-dm-discord
   ```
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Before running the script, you need to set up the following environment variables in a `.env` file:

- `DISCORD_BOT_TOKEN`: Your Discord bot token.
- `DISCORD_GUILD_ID`: The Guild ID of your Discord server.

Example `.env` file:

```
DISCORD_BOT_TOKEN=your_bot_token
DISCORD_GUILD_ID=your_guild_id
```

## Usage

Run the script using Python:

```python
python main.py
```

## Getting a Bot Token

To obtain a bot token:

1. Visit the [Discord Developer Portal](https://discord.com/developers/applications).
2. Create a new application and add a bot to it.
3. Copy the bot token provided.

## Setting Up the Bot

Ensure your bot has administrative permissions on the Discord server for it to function correctly.

## Getting the Guild ID

To find your Discord server's Guild ID:

1. Enable Developer Mode in Discord (Settings -> Advanced -> Developer Mode).
2. Right-click your server name and click 'Copy ID'.

## Contributing

Contributions to this package are welcome. Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature.
3. Commit your changes.
4. Push to the branch.
5. Open a pull request.

## Code Sample

Below is a simple example of how to use this package within your Python project to disable DMs for your Discord server:

```python
from no_dm_discord import update_discord_status

# Ensure your .env file has the DISCORD_BOT_TOKEN and DISCORD_GUILD_ID set
update_discord_status()

print("DMs have been successfully disabled.")
```

This example assumes you have set up your environment variables correctly and have the `no_dm_discord` package installed in your environment.

Remember, the actual function call and package import might need to be adjusted based on your package structure and function definitions.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
