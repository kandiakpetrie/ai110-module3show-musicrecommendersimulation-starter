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
        "favorite_moods": ["happy", "upbeat"],
        "target_energy": (0.7, 0.9),
    }

    hip_hop_listener = {
        "favorite_genres": ["hip hop", "rap"],
        "favorite_moods": ["energetic", "confident", "moody"],
        "target_energy": (0.75, 1.0),
    }

    rock_listener = {
        "favorite_genres": ["rock", "metal", "punk"],
        "favorite_moods": ["intense"],
        "target_energy": (0.6, 0.8),
    }

    ballad_listener = {
        "favorite_genres": ["ballad", "lofi"],
        "favorite_moods": ["happy", "chill"],
        "target_energy": (0.3, 0.5),
    }

    international_listener = {
        "favorite_genres": ["reggae", "latin", "afrobeat", "world"],
        "favorite_moods": ["happy", "upbeat", "energetic", "intense"],
        "target_energy": (0.6, 0.9),
    }



    

    recommendations1 = recommend_songs(user_prefs, songs, k=5)
    recommendations2 = recommend_songs(hip_hop_listener, songs, k=5)
    recommendations3 = recommend_songs(rock_listener, songs, k=5)
    recommendations4 = recommend_songs(ballad_listener, songs, k=5)
    recommendations5 = recommend_songs(international_listener, songs, k=5)

    width = 55
    print()
    print("=" * width)
    print("TOP RECOMMENDATIONS FOR POP/INDIE POP LISTENER".center(width))
    print("=" * width)

    for rank, (song, score, explanation) in enumerate(recommendations1, start=1):
        print()
        print(f"{rank}. {song['title']}")
        print(f"   Score: {score:.2f}")
        print("   Reasons:")
        for reason in explanation.splitlines():
            print(f"     {reason.strip()}")

    print()

    print("=" * width)
    print("TOP RECOMMENDATIONS FOR HIP HOP LISTENER".center(width))
    print("=" * width)


    for rank, (song, score, explanation) in enumerate(recommendations2, start=1):
        print()
        print(f"{rank}. {song['title']}")
        print(f"   Score: {score:.2f}")
        print("   Reasons:")
        for reason in explanation.splitlines():
            print(f"     {reason.strip()}")

    print()

    print("=" * width)
    print("TOP RECOMMENDATIONS FOR ROCK LISTENER".center(width))
    print("=" * width)

    for rank, (song, score, explanation) in enumerate(recommendations3, start=1):
        print()
        print(f"{rank}. {song['title']}")
        print(f"   Score: {score:.2f}")
        print("   Reasons:")
        for reason in explanation.splitlines():
            print(f"     {reason.strip()}")

    print()

    print("=" * width)
    print("TOP RECOMMENDATIONS FOR BALLAD LISTENER".center(width))
    print("=" * width)

    for rank, (song, score, explanation) in enumerate(recommendations4, start=1):
        print()
        print(f"{rank}. {song['title']}")
        print(f"   Score: {score:.2f}")
        print("   Reasons:")
        for reason in explanation.splitlines():
            print(f"     {reason.strip()}")

    print()

    print("=" * width)
    print("TOP RECOMMENDATIONS FOR INTERNATIONAL LISTENER".center(width))
    print("=" * width)

    for rank, (song, score, explanation) in enumerate(recommendations5, start=1):
        print()
        print(f"{rank}. {song['title']}")
        print(f"   Score: {score:.2f}")
        print("   Reasons:")
        for reason in explanation.splitlines():
            print(f"     {reason.strip()}")

    print()


if __name__ == "__main__":
    main()
