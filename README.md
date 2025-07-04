# CLI Pokédex

A simple Python command-line Pokédex tool that fetches and displays data about any Pokémon using the [PokeAPI](https://pokeapi.co/). It includes stats, evolution details, type advantages/weaknesses, and categorized moves.

---

## 📦 Modules & Packages Used

### Python Standard Library:

* `sys`: For flush printing characters one-by-one.
* `time`: For creating typing effects in terminal output.

### External Packages:

* `requests`: For making HTTP requests to the PokeAPI.
* `python-box` (`Box`): To access deeply nested JSON data using dot notation for cleaner code.

> Install dependencies using:

```bash
pip install requests python-box
```

---

## 📁 Project Structure

```
project/
├── main.py           # Main CLI file with interactive interface
├── functions.py      # Contains all utility functions
└── README.md         # Documentation
```

---

## ⚙️ Functions Overview (`functions.py`)

* **`get_pokemon_data(name)`**: Fetches and returns data about a given Pokémon.
* **`pokemon_moves(data)`**: Returns all move names associated with the Pokémon.
* **`filtering_moves(data)`**: Filters moves into physical (has power) and status (no power).
* **`get_evolution_data(data)`**: Fetches the evolution chain and color of the Pokémon.
* **`extract_evolution_chain(chain_node)`**: Recursively builds a readable evolution path.
* **`strong_annd_weaktypes(data)`**: Returns which types the Pokémon is strong and weak against.
* **`color_and_description(data)`**: Gets color and flavor text description from species data.

---

## 🚀 How to Run

```bash
python main.py
```

Then follow the on-screen prompts to enter a Pokémon name and explore its data.

---

## 📌 Features

* Fetches **basic info** (type, height, weight)
* Lists **base stats**
* Shows **evolution chain** with triggers
* Categorizes **moves** into physical and non-damaging
* Shows **type effectiveness** (strong/weak against)
* Includes a **typing animation** for better CLI UX

---

## 📝 Notes

* Internet connection is required as the data comes from PokeAPI.
* Some descriptions might include special formatting from the original games.
* Make sure names are entered correctly (e.g., `pikachu`, not `Pikachu`).

---

Happy Exploring! 🎉
