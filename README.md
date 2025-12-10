# 🃏 Blackjack Game (Python)

A command-line Blackjack game written in Python.
The player competes against the computer, drawing cards without repeating values, and trying to reach a score as close as possible to **21** without going over.

## 📌 Features

* No repeated cards (deck now works like a real one)
* Random card dealing using Python’s `random` module
* Player and computer hands tracked across turns
* Option to draw additional cards or pass
* Automatic score calculation
* Simple win/lose/draw conditions
* Replay option after each game

## 🚀 How to Run

1. Make sure you have **Python 3** installed.
2. Save the script as `blackjack.py`.
3. Run the game from your terminal:

```bash
python3 blackjack.py
```

4. Follow the instructions on screen:

```
Do you want play blackjack? [Y/n]:
```

## 🎮 Game Rules (Simplified)

* The deck is a fixed list of values:

  * Numbers **2–10** keep their natural value
  * Face cards count as **10**
  * Ace is fixed as **11** in this version
* **No card will be repeated**, because every drawn card is removed from the deck
* Both player and computer start with **two cards**
* You may choose to:

  * **(Y)** draw another card
  * **(N)** end your turn
* The computer also draws alongside the player
* The winner is defined by:

  * Highest score without going over **21**
  * Equal scores → draw
  * Automatic Blackjack detection

## 📂 Code Structure

* `cards`: deck of remaining cards
* `start()`: main game loop
* Global lists store each hand for player and computer
* Deck shrinks as cards are drawn, preventing duplicates

## ⚠️ Known Limitations

* Ace always counts as **11** (not dynamic)
* Computer logic is very simple
* No betting or chips system yet

## 📝 Example Output

```
Your cards: [7, 10], current score: 17
Computer's first card: 8
Type 'y' to get another card, type 'n' to pass [Y/n]:
```

# 📜 License — GNU GPL V3.0
