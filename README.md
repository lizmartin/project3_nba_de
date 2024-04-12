# project3_nba_de
UO Data Visualization Bootcamp | Project 3: NBA Stats Data Engineering

Team Members:
* Brent Lang
* Julia Olson
* Jerrica Raemer
* Liz Martin-Strong

Data Source: <https://www.kaggle.com/datasets/nathanlauga/nba-games>

Final Presentation: <https://docs.google.com/presentation/d/1jitIVNhLtQB_3x7I_MvaMxaWbhT4AMgsIfI0hynPA68/edit?usp=sharing>

Proposal:

We want to build a super-team based on which players performed the best in 2022 to predict the best players for 2023. We’ll analyze the stats of particular players to give specific predictions of their performance for 2023.

Data is uniform and that lends it well to a structured format. We are leaning towards using SQL / SQL Alchemy and exploring using BokehInitial build in SQL leveraging PGAdmin
Do initial cleaning and downsizing to make the size into a manageable size and then start working with it in SQL Alchemy or a python library.

We pulled a data set for NBA stats from Kaggle at: https://www.kaggle.com/datasets/nathanlauga/nba-games. We were interested in the trending interest in sports analysis and sports betting. Based on this, we would explore the Data Engineering track of the project challenge.

Some of the questions we will explore include:
•	Do teams tend to win more home games than away?
•	To illustrate maximized performance, we will build a fantasy team with the best players in their position.
o	12 players - Players must play in 75% or more of games in the season.
o	We will look at the following metrics:
	2pt FG
	3pt FG
	Assists
	Rebounds
	Defensive
	Offensive
	Blocks
	+/- (would first need to determine what exactly this metrics defines)
•	Players who have the highest 2 pt shots
•	Someone who has a high number of rebounds
If we have time, we’ll build a fantasy team for east coast and west coast players. It would be interesting to simulate a game between east and west coast players. This is an ambitious ask that we will do only if we have time. 




