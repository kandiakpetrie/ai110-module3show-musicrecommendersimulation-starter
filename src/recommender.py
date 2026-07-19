import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genres: List[str]           # one or more genres the user likes, e.g. ["pop", "indie pop"]
    favorite_mood: str
    target_energy: Tuple[float, float]   # acceptable energy range as (min, max), e.g. (0.6, 0.9)
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        """Store the catalog of songs this recommender will draw from.

        Args:
            songs: The pool of Song objects available to recommend.
        """
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return the top k songs for a user, ranked by taste match.

        Args:
            user: The user's taste preferences.
            k: The maximum number of songs to return.

        Returns:
            A list of up to k recommended Song objects.
        """
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Explain why a given song was recommended to a user.

        Args:
            user: The user's taste preferences.
            song: The song to explain.

        Returns:
            A human-readable explanation of the match.
        """
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    numeric_fields = {
        "id": int,
        "energy": float,
        "tempo_bpm": float,
        "valence": float,
        "danceability": float,
        "acousticness": float,
    }

    songs: List[Dict] = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            song: Dict = {}
            for key, value in row.items():
                if key is None:
                    continue
                key = key.strip()
                value = value.strip() if value is not None else ""
                if key in numeric_fields:
                    song[key] = numeric_fields[key](value)
                else:
                    song[key] = value
            songs.append(song)

    return songs

# Point values for each scoring signal (max total = 10.0).
GENRE_MATCH_POINTS = 4.0     # song's genre is one of the user's favorites
GENRE_RELATED_POINTS = 2.0   # genre shares a word with a favorite (pop <-> indie pop)
ENERGY_MAX_POINTS = 4.0      # scaled by how close energy is to the target
MOOD_MATCH_POINTS = 2.0      # song's mood equals the user's favorite mood
MAX_POINTS = 10.0


def _energy_range(user_prefs: Dict) -> Tuple[float, float]:
    """Return the user's target energy as a (min, max) range.

    Accepts either a range tuple/list or a single float (treated as a point range).
    """
    target = user_prefs.get("target_energy", user_prefs.get("energy"))
    if target is None:
        return (0.0, 1.0)                     # no preference -> everything is "inside"
    if isinstance(target, (tuple, list)):
        lo, hi = float(target[0]), float(target[1])
        return (min(lo, hi), max(lo, hi))
    value = float(target)
    return (value, value)


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences (Stage 2 of the recipe).

    Adds up genre, energy-closeness, and mood points, then normalizes to 0-1.
    Returns (score, reasons).
    """
    points = 0.0
    reasons: List[str] = []

    favorite_genres = user_prefs.get("favorite_genres") or []
    favorite_mood = user_prefs.get("favorite_mood") or user_prefs.get("mood")
    song_genre = (song.get("genre") or "").strip().lower()
    song_mood = (song.get("mood") or "").strip().lower()
    favorites = [g.strip().lower() for g in favorite_genres]

    # Rule 1 - Genre (up to 4 pts): exact match, else partial credit for a shared word.
    if song_genre and song_genre in favorites:
        points += GENRE_MATCH_POINTS
        reasons.append(
            f"genre '{song_genre}' is one of your favorites (+{GENRE_MATCH_POINTS:.0f} pts)"
        )
    else:
        song_words = set(song_genre.split())
        favorite_words = {w for g in favorites for w in g.split()}
        shared = song_words & favorite_words
        if shared:
            points += GENRE_RELATED_POINTS
            reasons.append(
                f"genre '{song_genre}' is related to your favorites "
                f"(shares '{' '.join(sorted(shared))}', +{GENRE_RELATED_POINTS:.0f} pts)"
            )
        elif song_genre:
            reasons.append(f"genre '{song_genre}' doesn't match your favorites (+0 pts)")

    # Rule 2 - Energy similarity (up to 4 pts): points scale by closeness to the target range.
    lo, hi = _energy_range(user_prefs)
    energy = float(song.get("energy", 0.0))
    if lo <= energy <= hi:
        distance = 0.0
    elif energy < lo:
        distance = lo - energy
    else:
        distance = energy - hi
    energy_points = ENERGY_MAX_POINTS * max(0.0, 1.0 - distance)
    points += energy_points
    if distance == 0.0:
        reasons.append(
            f"energy {energy:.2f} is right in your target range "
            f"({lo:.2f}-{hi:.2f}) (+{energy_points:.1f} pts)"
        )
    elif energy_points > 0:
        reasons.append(
            f"energy {energy:.2f} is close to your target range "
            f"({lo:.2f}-{hi:.2f}) (+{energy_points:.1f} pts)"
        )
    else:
        reasons.append(
            f"energy {energy:.2f} is far from your target range "
            f"({lo:.2f}-{hi:.2f}) (+0 pts)"
        )

    # Rule 3 - Mood (up to 2 pts): exact match only.
    if favorite_mood and song_mood == str(favorite_mood).strip().lower():
        points += MOOD_MATCH_POINTS
        reasons.append(
            f"mood '{song_mood}' matches your favorite mood (+{MOOD_MATCH_POINTS:.0f} pts)"
        )
    elif favorite_mood and song_mood:
        reasons.append(
            f"mood '{song_mood}' differs from your favorite '{str(favorite_mood).strip().lower()}' (+0 pts)"
        )

    score = points / MAX_POINTS      # always between 0 and 1
    return (score, reasons)


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
