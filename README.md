# emometer-pilot

Pilot notebooks for Emometer. They track emotions over a story in two ways: with sparse autoencoder (SAE) features from [Neuronpedia](https://www.neuronpedia.org), and with the [NRC EmoLex](https://saifmohammad.com/WebPages/NRC-Emotion-Lexicon.htm) word lexicon as a baseline.

## Notebooks

| Notebook | What it does |
| --- | --- |
| `1a_sae_hand_picked_features.ipynb` | Pilot 1: demonstrates how a single SAE works, with one hand-picked feature per emotion over *The Yellow Wallpaper*. |
| `1b_emolex_baseline.ipynb` | Pilot 1 baseline: scores the same story with EmoLex instead of an SAE. |
| `1c_compare_sae_vs_emolex.ipynb` | Pilot 1 comparison: puts the arcs from 1a and 1b on one graph. Run 1a and 1b first. |
| `2_sae_feature_groups.ipynb` | Pilot 2: expands to 5 SAE features for one emotion on one text. |
| `3_four_emotions_four_stories.ipynb` | Pilot 3: uses 5 SAE features for each of four emotions, over four different texts. |

The notebooks use paths relative to the repo root, which is where Jupyter and VS Code run them from.

## Layout

```
data/
  lexicons/          NRC EmoLex v0.92, and the labMT happiness word list (not used by the notebooks yet)
  stories/           the story texts, from Project Gutenberg
outputs/
  arcs/              emotion arcs saved by 1a and 1b, read by 1c
  figures/           figures saved by the notebooks, in pilot1/, pilot2/ and pilot3/
scripts/
  format_json.py     pretty-prints a JSON file in place
```

Neuronpedia responses are cached in `.activation_cache/`, `.search_cache/` and `.layer_cache/`. These folders aren't committed.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Then create a `.env` file in the repo root with your Neuronpedia API key:

```
NEURONPEDIA_API_KEY=your-key-here
```

`.env` is listed in `.gitignore`, so the key stays on your machine.
