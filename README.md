# Markov Basketball Game Simulation

This project simulates basketball game shot chart for players like **Stephen Curry**, **LeBron James**, and **Kevin Durant** using a **Markov chain model**.  
It generates a game sequence, calculates predicted points, and overlays shot frequencies on a half-court image.

---

## Running the Code
- clone the repository
- install dependencies (matlablib.pyplot)
- run the main script
- enter a player name from given options (currently limited to **Curry**, **Lebron**, **Durant**)

---

## Why This Was Meaningful to Me

As a college basketball player and someone who has been watching NBA basketball his whole life I always find the statistics associated with the game incredibly interesting.
When we were asked to come up with a creative way to use **Markov Chains** I immediately thought of a way to predict the next shot taken by a player in a game. Shot charts 
are one of the most commonly used displays to show a player's game, so I decided to use **Markov Chains** paired with career statistics from some of my favorite players 
(including number of shots taken per game and shooting percentages from different places on the court) to determine their likelihood to take each shot after a previous shot,
as well as their likelihood of making that shot. Through these methods I was able to construct a shot chart and predict the number of points they would score in a game.

---

## How I was Challenged

This project challenged me in terms of building familiarity with different libraries, particularly matplot. While I have a good amount of experience writing my own code
in Python I have not spent a lot of time working with different libraries and exploring their capabilities, so I enjoyed that challenge. I also challenged myself to 
incorporate what I have learned in previous classes, such as pulling in statistics to make my work as accurate as possible. This was particularly important to me because 
I believe a crucial part of a liberal arts education is being able to see connections between subjects and classes and use those connections to your advantage. If I were 
to work on this project further I would likely want to incorporate more randomness into shooting percentages, particularly game to game as players sometimes have games they
play better in than others. The games they play better in they are also likely to shoot more shots, so rather than having players take their average number of shots every 
time I would like to have the number of shots they take revolve around a standard deviation. In future projects I am excited to explore more Python libraries and learn more
about the capabilities of these libraries.

---

## Creativity?



---

## Sources

[Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/images.html#sphx-glr-tutorials-images-py)
[Basketball Reference](https://www.basketball-reference.com/players/j/jamesle01/shooting/2025)

