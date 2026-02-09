# Blackjack — Terminal Game

Simple terminal-based Blackjack (21) game implemented in Python.

## Description

This is a lightweight command-line Blackjack game. Players can play rounds against a dealer, place bets, and track high scores.

## Features

- Play Blackjack from the terminal
- Simple betting and score tracking persisted in `high_score.txt`
- Rules implemented in `game_rules.py` and game flow in `main.py`

## Requirements

- Python 3.8 or newer

## Files

- `main.py` — game entry point
- `Class.py` — game classes and data structures
- `game_rules.py` — Blackjack rules and helper logic
- `high_score.txt` — persisted high score data

## Installation

Clone the repository and run the game with Python:

```bash
git clone <repo-url>
cd BlackJack-Terminal_Game
python3 main.py
```

Replace `python3` with your Python executable if needed.

## Usage

Run the game with:

```bash
python3 main.py
```

Follow on-screen prompts to place bets, hit, stand, and view scores. High scores are saved to `high_score.txt` in the project folder.

## Game Rules (Quick)

- Goal: get a hand value as close to 21 as possible without going over.
- Face cards (J, Q, K) are worth 10. Aces are 1 or 11.
- Dealer acts according to rules in `game_rules.py`.

## Contributing

Feel free to open issues or pull requests to improve gameplay, add features (e.g., multiple players, AI strategies), or improve tests and packaging.
