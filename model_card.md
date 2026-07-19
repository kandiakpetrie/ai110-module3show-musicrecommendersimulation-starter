# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

Model Name: Resonance 

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

1) Basically this thing takes what you're into — your genres, your moods, the energy level you want and hands you back the 5 songs from the catalog that fit you best. It assumes you actually know your own taste and can put it into words, which isn't always true for real people. This is a classroom build for learning how recommenders work, not something I'd ship to real users yet.

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

1) Every song earns points on three things: does its genre match what you like, is its energy close to what you asked for, and does its mood match your vibe then I add those up into one score out of 10. Genre is worth the most, energy is right behind it, and mood is the tiebreaker on top. I sort every song by that score and give you the top 5, so the songs that hit all three of your buttons rise to the front.

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.


---

## 4. Data  

Describe the dataset the model uses.  

1) There are 38 songs in the catalog spread across about 20 genres (pop, lofi, rock, hip hop, latin, reggae, world, classical, and a bunch more) and 7 moods like happy, chill, intense, and moody. I didn't add or remove anything it's the starter dataset as-is. The gaps show up fast though: there's no ballad or afrobeat even though my test profiles asked for them, and genres like world and classical only get 1 song each, so whole slices of taste are barely there.

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

1) It nails it when you have a clear, well-stocked taste — the rock listener got back 5 solid rock/metal/punk tracks and the ballad listener got 5 chill lofi songs, exactly what you'd expect. Energy is the star: asking for high-energy vs. low-energy cleanly splits the catalog into hype songs vs. mellow ones every time. When a genre has plenty of songs in the pool, the top picks feel obvious and right, which matched my gut.

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

1) My recommender's biggest weakness is a genre filter bubble: genre drives 40% of the score and is used again as a ranking tiebreaker, so the user's existing tastes get rewarded twice while new genres rarely break through. The "related genre" credit is purely lexical (string-token overlap), which unfairly bridges multi-word genres like pop→indie pop while leaving single-word genres like jazz or soul isolated. The final id-ascending tiebreaker leaks catalog order into results, systematically favoring the front-loaded mainstream/electronic songs over the later-listed latin, world, classical, and punk tracks, a bias compounded by a skewed catalog where lofi has 5 songs but world/classical/punk have only 1 each. Finally, the system has no diversity controls (nothing prevents 5 results from the same artist or genre) and ignores half its own signals, valence, danceability, acousticness, and even the defined likes_acoustic preference are never used, leaving no lever to break users out of a narrow, homogeneous bubble.

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

## Sample Recommendation Output
```
=======================================================
     TOP RECOMMENDATIONS FOR POP/INDIE POP LISTENER    
=======================================================

1. Sunrise City
   Score: 1.00
   Reasons:
     • genre 'pop' is one of your favorites (+4 pts)
     • energy 0.82 is right in your target range (0.70-0.90) (+4.0 pts)
     • mood 'happy' is one of your favorite moods (+2 pts)

2. Rooftop Lights
   Score: 1.00
   Reasons:
     • genre 'indie pop' is one of your favorites (+4 pts)
     • energy 0.76 is right in your target range (0.70-0.90) (+4.0 pts)
     • mood 'happy' is one of your favorite moods (+2 pts)

3. Morning Stretch
   Score: 1.00
   Reasons:
     • genre 'pop' is one of your favorites (+4 pts)
     • energy 0.80 is right in your target range (0.70-0.90) (+4.0 pts)
     • mood 'happy' is one of your favorite moods (+2 pts)

4. Festival Anthem
   Score: 0.80
   Reasons:
     • genre 'indie pop' is one of your favorites (+4 pts)
     • energy 0.88 is right in your target range (0.70-0.90) (+4.0 pts)
     • mood 'intense' isn't one of your favorites (happy, upbeat) (+0 pts)

5. Gym Hero
   Score: 0.79
   Reasons:
     • genre 'pop' is one of your favorites (+4 pts)
     • energy 0.93 is close to your target range (0.70-0.90) (+3.9 pts)
     • mood 'intense' isn't one of your favorites (happy, upbeat) (+0 pts)

=======================================================
        TOP RECOMMENDATIONS FOR HIP HOP LISTENER       
=======================================================

1. Concrete Kings
   Score: 1.00
   Reasons:
     • genre 'hip hop' is one of your favorites (+4 pts)
     • energy 0.78 is right in your target range (0.75-1.00) (+4.0 pts)
     • mood 'confident' is one of your favorite moods (+2 pts)

2. Late Night Cypher
   Score: 0.96
   Reasons:
     • genre 'hip hop' is one of your favorites (+4 pts)
     • energy 0.64 is close to your target range (0.75-1.00) (+3.6 pts)
     • mood 'moody' is one of your favorite moods (+2 pts)

3. Bars on Fire
   Score: 0.80
   Reasons:
     • genre 'rap' is one of your favorites (+4 pts)
     • energy 0.86 is right in your target range (0.75-1.00) (+4.0 pts)
     • mood 'intense' isn't one of your favorites (energetic, confident, moody) (+0 pts)

4. Night Drive Loop
   Score: 0.60
   Reasons:
     • genre 'synthwave' doesn't match your favorites (+0 pts)
     • energy 0.75 is right in your target range (0.75-1.00) (+4.0 pts)
     • mood 'moody' is one of your favorite moods (+2 pts)

5. Electric Sunset
   Score: 0.59
   Reasons:
     • genre 'synthwave' doesn't match your favorites (+0 pts)
     • energy 0.72 is close to your target range (0.75-1.00) (+3.9 pts)
     • mood 'moody' is one of your favorite moods (+2 pts)

=======================================================
         TOP RECOMMENDATIONS FOR ROCK LISTENER         
=======================================================

1. Storm Runner
   Score: 0.96
   Reasons:
     • genre 'rock' is one of your favorites (+4 pts)
     • energy 0.91 is close to your target range (0.60-0.80) (+3.6 pts)
     • mood 'intense' is one of your favorite moods (+2 pts)

2. Riff Storm
   Score: 0.95
   Reasons:
     • genre 'punk' is one of your favorites (+4 pts)
     • energy 0.92 is close to your target range (0.60-0.80) (+3.5 pts)
     • mood 'intense' is one of your favorite moods (+2 pts)

3. Neon Overdrive
   Score: 0.94
   Reasons:
     • genre 'rock' is one of your favorites (+4 pts)
     • energy 0.95 is close to your target range (0.60-0.80) (+3.4 pts)
     • mood 'intense' is one of your favorite moods (+2 pts)

4. Breaking Chains
   Score: 0.94
   Reasons:
     • genre 'metal' is one of your favorites (+4 pts)
     • energy 0.96 is close to your target range (0.60-0.80) (+3.4 pts)
     • mood 'intense' is one of your favorite moods (+2 pts)

5. Iron Veins
   Score: 0.93
   Reasons:
     • genre 'metal' is one of your favorites (+4 pts)
     • energy 0.97 is close to your target range (0.60-0.80) (+3.3 pts)
     • mood 'intense' is one of your favorite moods (+2 pts)

=======================================================
        TOP RECOMMENDATIONS FOR BALLAD LISTENER        
=======================================================

1. Midnight Coding
   Score: 1.00
   Reasons:
     • genre 'lofi' is one of your favorites (+4 pts)
     • energy 0.42 is right in your target range (0.30-0.50) (+4.0 pts)
     • mood 'chill' is one of your favorite moods (+2 pts)

2. Library Rain
   Score: 1.00
   Reasons:
     • genre 'lofi' is one of your favorites (+4 pts)
     • energy 0.35 is right in your target range (0.30-0.50) (+4.0 pts)
     • mood 'chill' is one of your favorite moods (+2 pts)

3. Paper Boats
   Score: 1.00
   Reasons:
     • genre 'lofi' is one of your favorites (+4 pts)
     • energy 0.38 is right in your target range (0.30-0.50) (+4.0 pts)
     • mood 'chill' is one of your favorite moods (+2 pts)

4. Focus Flow
   Score: 0.80
   Reasons:
     • genre 'lofi' is one of your favorites (+4 pts)
     • energy 0.40 is right in your target range (0.30-0.50) (+4.0 pts)
     • mood 'focused' isn't one of your favorites (happy, chill) (+0 pts)

5. Study Session
   Score: 0.80
   Reasons:
     • genre 'lofi' is one of your favorites (+4 pts)
     • energy 0.41 is right in your target range (0.30-0.50) (+4.0 pts)
     • mood 'focused' isn't one of your favorites (happy, chill) (+0 pts)

=======================================================
     TOP RECOMMENDATIONS FOR INTERNATIONAL LISTENER    
=======================================================

1. Compas del Sur
   Score: 1.00
   Reasons:
     • genre 'latin' is one of your favorites (+4 pts)
     • energy 0.83 is right in your target range (0.60-0.90) (+4.0 pts)
     • mood 'happy' is one of your favorite moods (+2 pts)

2. Noche de Baile
   Score: 1.00
   Reasons:
     • genre 'latin' is one of your favorites (+4 pts)
     • energy 0.87 is right in your target range (0.60-0.90) (+4.0 pts)
     • mood 'intense' is one of your favorite moods (+2 pts)

3. Island Time
   Score: 0.78
   Reasons:
     • genre 'reggae' is one of your favorites (+4 pts)
     • energy 0.55 is close to your target range (0.60-0.90) (+3.8 pts)
     • mood 'relaxed' isn't one of your favorites (happy, upbeat, energetic, intense) (+0 pts)

4. Dub Horizon
   Score: 0.76
   Reasons:
     • genre 'reggae' is one of your favorites (+4 pts)
     • energy 0.50 is close to your target range (0.60-0.90) (+3.6 pts)
     • mood 'chill' isn't one of your favorites (happy, upbeat, energetic, intense) (+0 pts)

5. Raga Sunrise
   Score: 0.74
   Reasons:
     • genre 'world' is one of your favorites (+4 pts)
     • energy 0.44 is close to your target range (0.60-0.90) (+3.4 pts)
     • mood 'chill' isn't one of your favorites (happy, upbeat, energetic, intense) (+0 pts)
```

### Profile-to-Profile Comparisons

Each pair below compares what changed between the two profiles' top-5 lists and why that change makes sense given their preferences.

- **Pop/Indie vs. Hip Hop** — Both ask for high-energy, upbeat-ish songs, but Pop stays 100% in-genre (every pick is pop/indie pop), while Hip Hop's #4–5 leak to *off-genre* synthwave (Night Drive Loop, Electric Sunset) that score 0 genre points and survive on mood+energy alone. This makes sense: the catalog has only ~3 hip hop/rap songs in that energy band, so once they run out, non-genre songs float up.

- **Pop/Indie vs. Rock** — Pop's top 3 hit a perfect 1.00 because pop songs sit *inside* its 0.70–0.90 energy range, whereas Rock caps at 0.96 — its picks (0.91–0.97 energy) are all above the requested 0.60–0.80 band and only earn "close" partial energy credit. Genre + intense-mood carry them anyway, showing energy is a soft signal, not a filter.

- **Pop/Indie vs. Ballad** — Near-mirror images on energy: Pop targets 0.70–0.90 (bright, upbeat) and returns pop, while Ballad targets 0.30–0.50 (mellow) and returns all lofi. Both perfect-score their top 3, confirming the model cleanly separates high- vs. low-energy taste.

- **Pop/Indie vs. International** — Both want happy, danceable songs and both hit 1.00 on their in-genre happy tracks (Sunrise City vs. Compas del Sur). The difference is coverage: Pop's genres are well-stocked, but International requested `afrobeat`, which returns nothing — a catalog gap, not a scoring gap.

- **Hip Hop vs. Rock** — Both are aggressive/energetic profiles, but Rock's list is *cleaner* — all 5 picks are in-genre (rock/metal/punk) and all match the "intense" mood — because that cluster is dense in the catalog. Hip Hop's tail muddies with synthwave. Same intent, different result purity, driven by how many matching songs exist.

- **Hip Hop vs. Ballad** — Opposite on both axes: Hip Hop wants 0.75–1.00 energy with confident/moody moods; Ballad wants 0.30–0.50 with happy/chill. Ballad's picks are pristine lofi, while Hip Hop's high-energy demand plus a thin genre pool forces off-genre songs into the list. Validates that energy + mood together pull the lists far apart.

- **Hip Hop vs. International** — Both are broad, multi-genre, energetic profiles, but International keeps all 5 picks in-genre (latin/reggae/world are covered) while Hip Hop leaks. Interesting because both listed a genre the catalog can't fully serve — International's `afrobeat` and Hip Hop's narrow high-energy `rap` pool.

- **Rock vs. Ballad** — The sharpest contrast in the whole test: Rock = maxed-out energy (0.91–0.97), intense mood; Ballad = lowest energy (0.35–0.42), chill mood. Both stay fully in-genre, so this pair is the clearest proof that the energy preference alone can steer the recommender to opposite ends of the catalog.

- **Rock vs. International** — Both include the "intense" mood, but Rock is one tight sonic cluster (rock/metal/punk, all ~0.9 energy) while International spans 0.44–0.87 across latin, reggae, and world. Rock's picks all match on mood; International's lower-ranked reggae/world songs lose mood points (relaxed/chill), so its scores taper from 1.00 down to 0.74. Diversity comes at the cost of consistency.

- **Ballad vs. International** — Opposite energy and mood again: Ballad is calm, low-energy lofi; International is lively latin/reggae. Ballad's top 3 all score 1.00, while International peaks at 1.00 then drops as its reggae/world picks miss the happy/upbeat/energetic/intense moods — showing International's mood list is too narrow for the mellower songs it still surfaces on genre.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

1) Next I'd actually use the song features I'm ignoring danceability, valence, acousticness and hook up the likes_acoustic preference that's just sitting there unused. I'd also add diversity rules so you don't get 5 songs by the same artist or all one genre, plus give related genres/moods real connections instead of just matching on shared words. Longer term I'd want to fill the catalog gaps (afrobeat, ballad, more world/classical) so underrepresented tastes actually have songs to pull from.

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

1) The biggest thing I learned is that a recommender is only as good as the data behind it, my scoring could be perfect and it'd still fail if the catalog has no afrobeat or ballad songs to give you. What surprised me most was how easily the filter bubble sneaks in: weighting genre so heavily meant the model basically just handed people more of what they already picked. Now when a real app like Spotify keeps feeding me the same vibe, I get why the math is quietly rewarding my past taste instead of pushing me somewhere new.

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
