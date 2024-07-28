
# Loteria Game

Welcome to my Loteria game built in Python! This project demonstrates the capabilities of ChatGPT to write code and create graphics. Loteria has always been an interesting game for me, and I always looked forward to playing it in Spanish class.

## Overview

This Loteria game is built using Flask for the backend and Socket.IO for real-time interactions. The goal of the project is to create a fully functional Loteria game with 54 custom cards, each generated using ChatGPT's image-building capability. All of the code was written with the help of ChatGPT, simply by explaining what we were trying to accomplish and debugging along the way.

## Features

- **Multiplayer Support**: Up to 10 players can join a game and play together.
- **Real-time Gameplay**: Uses Socket.IO for real-time communication between the server and clients.
- **Custom Card Generation**: Placeholder images for the 54 Loteria cards are generated using Python's Pillow library.
- **Dynamic Game Management**: Start and join games dynamically, with game state management.

## Getting Started

### Prerequisites

- Python 3.10 or higher
- Virtualenv (recommended)
- Flask
- Flask-SocketIO
- Pillow (Python Imaging Library)

### Installation

1. **Clone the repository**:
   \`\`\`bash
   git clone https://github.com/yourusername/loteria-game.git
   cd loteria-game
   \`\`\`

2. **Create and activate a virtual environment**:
   \`\`\`bash
   python3 -m venv .venv
   source .venv/bin/activate
   \`\`\`

3. **Install the dependencies**:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

4. **Generate placeholder images**:
   \`\`\`bash
   python3 frontend/images/cards/generate_cards.py
   \`\`\`

5. **Run the application**:
   \`\`\`bash
   python3 backend/app.py
   \`\`\`

### Running the Game

1. Open your browser and go to \`http://localhost:5000\`.
2. Start a new game and join using different browser windows or tabs.
3. Play the game by calling cards and marking them on your card.

## Contribution

Anyone is welcome to fork or contribute to this project. If you have any ideas or improvements, feel free to create a pull request or reach out to me.

## Future Work

The goal is to make 54 custom cards using ChatGPT's image-building capability. This project will continue to evolve as new features are added and improvements are made.

## Acknowledgments

- Thanks to ChatGPT for assisting in writing the code and creating the graphics.
- Special mention to my Spanish class memories that inspired this project.

---

Enjoy the game and happy playing!

