# 🪙 Treasure Catcher

A 2D arcade-style game developed in Python using the **Pygame** library. The player controls a basket to collect falling treasures, activate power-ups, and avoid hazardous obstacles.

---

## 🎮 Game Features

- **Difficulty Levels**: Start screen allowing players to select between Easy, Medium, and Hard.
- **Power-ups & Items**:
  - **Gold Coins & Gems**: Standard (+10) and Super Bonus (+50) score boosters.
  - **Zig-zag Coins**: Moving target coins (+30).
  - **Coin Magnet**: Cyan power-up that pulls coins toward the basket.
  - **Shield**: Purple power-up protecting the player from bomb hits.
  - **Slow-Mo Clock**: Ice-blue power-up that slows down falling items.
  - **Extra Lives**: Green hearts to replenish lost health.
- **Game Events**: Random Fast Fall, Bomb Storms, and Fever Mode (Coin Rain).
- **Obstacles**: Standard bombs and Smoke Bombs (screen blinding effect).
- **Restart**: Press `R` after Game Over to restart instantly.

---

## 🛠️ Project Structure

```text
treasure_catcher/
├── game_config.py   # Screen settings, colors, and game constants
├── player.py        # Player movement, basket size, and power-up activation
├── item.py          # Logic for falling items, movement, and types
└── main.py          # Main game loop, UI rendering, and collision handling
🚀 How to Run
Clone the repository:

Bash
git clone [https://github.com/abdullah250222/treasure_catcher.git](https://github.com/abdullah250222/treasure_catcher.git)
cd treasure_catcher
Install Pygame:

Bash
pip install pygame
Run the game:

Bash
python main.py
