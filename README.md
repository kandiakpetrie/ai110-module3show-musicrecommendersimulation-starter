# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.



---

## How The System Works

Explain your design in plain language.

1) My recommender scores each song by looking at how closely 
it matches your music taste based on the most common genre you listened
to as well how similar the songs are to your most listened songs and 
assigns a number between 0 and 1 and then it ranks the songs based on 
how far off they are from your target demographic for songs, with the closest
songs towards the top of the recommender. Features the Songs could use
would be genre, mood, energy, tempo, etc. Features the UserProfile could use is favorite moods and genre as well as target energy. 

Genre exact match → +4.0
Energy 0.76 is inside (0.7–0.9) → +4.0
Mood match → +2.0
Total = 10.0 → score = 1.00 (a perfect match)

Some prompts to answer:
- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:


=======================================================
                  TOP RECOMMENDATIONS                  
=======================================================

1. Sunrise City
   Score: 1.00
   Reasons:
     • genre 'pop' is one of your favorites (+4 pts)
     • energy 0.82 is right in your target range (0.70-0.90) (+4.0 pts)
     • mood 'happy' matches your favorite mood (+2 pts)

2. Rooftop Lights
   Score: 1.00
   Reasons:
     • genre 'indie pop' is one of your favorites (+4 pts)
     • energy 0.76 is right in your target range (0.70-0.90) (+4.0 pts)
     • mood 'happy' matches your favorite mood (+2 pts)

3. Morning Stretch
   Score: 1.00
   Reasons:
     • genre 'pop' is one of your favorites (+4 pts)
     • energy 0.80 is right in your target range (0.70-0.90) (+4.0 pts)
     • mood 'happy' matches your favorite mood (+2 pts)

4. Festival Anthem
   Score: 0.80
   Reasons:
     • genre 'indie pop' is one of your favorites (+4 pts)
     • energy 0.88 is right in your target range (0.70-0.90) (+4.0 pts)
     • mood 'intense' differs from your favorite 'happy' (+0 pts)

5. Gym Hero
   Score: 0.79
   Reasons:
     • genre 'pop' is one of your favorites (+4 pts)
     • energy 0.93 is close to your target range (0.70-0.90) (+3.9 pts)
     • mood 'intense' differs from your favorite 'happy' (+0 pts)


```
def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Scores every song, then ranks and returns the top k (Stage 3 of the recipe).

    Returns a list of (song_dict, score, explanation).
    """
    favorites = {g.strip().lower() for g in (user_prefs.get("favorite_genres") or [])}

    scored = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)          # delegate scoring
        genre_match = int((song.get("genre") or "").strip().lower() in favorites)
        explanation = "\n".join(f"  • {r}" for r in reasons) if reasons else "  • general match"
        scored.append((song, score, explanation, genre_match))

    # RANKING: score DESC, then genre match DESC, then id ASC (stable & deterministic).
    scored.sort(key=lambda x: (-x[1], -x[3], x[0].get("id", 0)))

    return [(song, score, explanation) for song, score, explanation, _ in scored[:k]]

def main() -> None:
    songs = load_songs("ai110-module3show-musicrecommendersimulation-starter/data/songs.csv") 

    # Starter example profile
    user_prefs = {
        "favorite_genres": ["pop", "indie pop"],
        "favorite_mood": "happy",
        "target_energy": (0.7, 0.9),
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    width = 55
    print()
    print("=" * width)
    print("TOP RECOMMENDATIONS".center(width))
    print("=" * width)

    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print()
        print(f"{rank}. {song['title']}")
        print(f"   Score: {score:.2f}")
        print("   Reasons:")
        for reason in explanation.splitlines():
            print(f"     {reason.strip()}")

    print()


if __name__ == "__main__":
    main()

```
# e.g.:
# User profile: genre= (songs that include pop in their description), mood=happy, energy= (between 0.75 and 1.00)
# Recommendations:
#   1. Sunrise City, Neon Echo,  pop,  happy,  0.82,   118,    0.84,   0.79,   0.18
#   2. Morning Stretch,	Max Pulse,	pop,	happy,	0.80,	120,	0.83,	0.85,	0.12
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



