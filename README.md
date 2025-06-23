🛠️ Active Developer Badge Bot

A lightweight, open-source Discord bot designed to help developers easily claim the Discord Active Developer Badge. This bot provides a simple slash command (/activedeveloperbadge) that fulfills Discord’s interaction requirement for the badge.

📦 Requirements

- Python 3.8 or higher
- A valid Discord Bot Token
- A Discord server where you have permission to add bots

🔧 Installation & Setup

Clone this repository

```bash
git clone https://github.com/iCritical/discord-active-developer-badge-bot.git
cd active-developer-badge-bot
```

Install dependencies

```bash
pip install -U discord.py
```

Configure your Discord Bot

- Go to the Discord Developer Portal
- Create a new application and add a bot
- Copy the Bot Token and replace `YOUR-BOT-TOKEN-HERE` in the script

Invite the bot to your server

Use this OAuth2 URL (replace `YOUR_CLIENT_ID` with your app's Client ID):

```bash
https://discord.com/oauth2/authorize?client_id=YOUR_CLIENT_ID&scope=bot%20applications.commands&permissions=274877975552
```

Run the bot

```bash
python bot.py
```

✅ How It Works

- Registers a slash command `/activedeveloperbadge` in your Discord server
- When executed, it logs your interaction with Discord’s API
- Discord recognizes the interaction, enabling you to claim the Active Developer Badge within ~24 hours

✅ How to Claim Your Active Developer Badge

- Use the `/activedeveloperbadge` command in any server with the bot
- Go to Discord’s Active Developer Badge page
- Select your bot, your community server, and a developer news channel
- Click Claim
- Celebrate your new badge! 🎉

🧠 Important Notes

- Use the command at least once every 30 days to maintain eligibility
- The bot only needs to run when you want to claim or renew the badge — 24/7 hosting is optional

⭐ Why Use This Bot?

- Simplifies the process of earning the Active Developer Badge
- Open source and easy to customize
- Lightweight with minimal dependencies

📄 License

MIT License — Feel free to use, modify, and distribute. If this bot helped you, a star is appreciated! 🌟
