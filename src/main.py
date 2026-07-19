"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


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
