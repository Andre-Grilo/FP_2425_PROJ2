# FP2425P2 – ORBITO-n Game Project

**A Python implementation of the ORBITO-n board game using Abstract Data Types (TADs), following the official 2024/25 FP Project 2 specification.**

This repository contains my solution for **Fundamentos da Programação – Projeto 2 (2024/25)**.  
The entire implementation is contained in a single file, as required: `projectoFP2.py`.

---

## 📘 Game Description

Orbito-n is an abstract two-player board game.  
It is a special case of an **m,n,k game** with:

- `m = n = k = 4`
- The board is formed by **2 to 5 orbits**
- Players alternate turns
- A turn consists of:
  1. **Placing** a stone on any free position  
  2. **Rotating** all stones **one position anticlockwise** around their orbit

The game ends when:

- The board has no free positions, **or**
- A player obtains **k = 2×n consecutive stones** horizontally, vertically or diagonally.

If both players complete a line simultaneously, the game ends in a **draw**.

---

## 🧩 Board, Positions and Stones

### Positions
- Identified as `(column, row)` e.g. `'b3'`
- Adjacent positions include horizontal, vertical, and diagonal neighbors
- Order of reading:  
  → from **inner orbit** to **outer orbit**  
  → left to right  
  → top to bottom

### Stones
- `'X'` → black (player 1)  
- `'O'` → white (player -1)  
- `' '` → neutral stone (empty position)

---

## 🤖 Automatic Strategy

### **Easy Mode**
- Choose a free position which, *after rotation*, ends adjacent to one of the player's stones  
- If none exists, choose the first free position in reading order

### **Normal Mode**
- Determine the largest `L ≤ k` such that:
  - the player can form a line of `L` after rotation  
  - or the opponent could do so after two rotations
- Prefer moves that allow forming L
- Otherwise, block positions where the opponent could form L
