# Monitoring Website

## Description

A web scraping monitoring tool that automatically tracks changes on a target website and sends Discord notifications when updates are detected. This project uses Playwright for web scraping and difflib for intelligent content comparison, ensuring that only genuine new content is reported (not just reordered lines).

**Key Features:**
- Automated website monitoring
- Change detection using LCS (Longest Common Subsequence) algorithm
- Discord webhook integration for instant notifications
- Thai language support
- Configurable monitoring intervals

## How to Clone

```bash
git clone https://github.com/yourusername/Monitoring-Website.git
cd Monitoring-Website
```

## How to Run

### Prerequisites
- Python 3.8 or higher
- Discord webhook URL

### Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Create a `.env` file** in the project root with your Discord webhook:
   ```
   DISCORD_WEBHOOK=your_discord_webhook_url_here
   ```

3. **Run the monitoring script:**
   ```bash
   python scrap-action.py
   ```

## Project Structure

```
Monitoring-Website/
├── scrap-action.py        # Main monitoring script (scrapes website and detects changes)
├── alert.py               # Discord alert system (sends notifications via webhook)
├── requirements.txt       # Project dependencies
├── last_file.txt          # Stores last scraped content for comparison
├── README.md              # Project documentation
├── .gitignore             # Git ignore rules
└── __pycache__/          # Python cache directory
```

### File Details

- **scrap-action.py**: Main entry point that monitors the target website, compares current content with previous content, detects changes, and triggers alerts
- **alert.py**: Handles sending formatted messages to Discord webhook with timestamp and notification details
- **requirements.txt**: Lists all required Python packages (Playwright, requests, python-dotenv)