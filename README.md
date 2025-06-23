
# 🛠️ Active Developer Badge Bot

A simple Discord bot that helps you qualify for the [Active Developer Badge](https://discord.com/developers/active-developer) by providing a slash command (`/activedeveloperbadge`) that fulfills Discord’s interaction requirement.

---

## 📦 Requirements

- Python 3.8 or higher
- A Discord Bot Token
- A Discord server where you have permission to add bots

---

## 🔧 Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/iCritical/active-developer-badge-bot.git
   cd active-developer-badge-bot
   ```

2. **Install the required dependencies**
   ```bash
   pip install -U discord.py
   ```

3. **Set up your bot in the Discord Developer Portal**
   - Go to [https://discord.com/developers/applications](https://discord.com/developers/applications)
   - Create a new application
   - Go to **Bot** tab → Click **Add Bot**
   - Copy the **Token** and replace `YOUR-BOT-TOKEN-HERE` in the script

4. **Invite the bot to your server**
   Use this OAuth2 URL (replace `YOUR_CLIENT_ID` with your app's Client ID):

   ```
   https://discord.com/oauth2/authorize?client_id=YOUR_CLIENT_ID&scope=bot%20applications.commands&permissions=274877975552
   ```

5. **Run the bot**
   ```bash
   python bot.py
   ```

---

## ✅ How It Works

- The bot registers a slash command `/activedeveloperbadge`.
- When you run this command in any server the bot is in, it logs your interaction.
- Discord detects this and enables you to claim your badge within ~24 hours.

---

## 🪪 Claiming the Active Developer Badge

1. Run the command `/activedeveloperbadge` in your server.
2. Visit [https://discord.com/developers/active-developer](https://discord.com/developers/active-developer).
3. Select your bot, your community server, and a dev-news channel.
4. Click **Claim**.
5. You’re done! 🎉

---

## 🧠 Note

- This command must be used at least **once every 30 days** to remain eligible.
- The bot only needs to be run once and doesn’t require hosting 24/7 unless you want to automate the process.

---

## 📄 License

MIT – do what you want, but leave a star if you found it helpful! 🌟
