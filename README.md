# project3_nba_de
UO Data Visualization Bootcamp | Project 3: NBA Stats Data Engineering

Team Members:
* Brent Lang
* Julia Olson
* Jerrica Raemer
* Liz Martin-Strong

Data Source: <https://www.kaggle.com/datasets/nathanlauga/nba-games>

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



Project Instructions:

Data Engineering Track
For this track, your group will follow data engineering processes. Here are the specific requirements:

Data must be stored in a SQL or NoSQL database (PostgreSQL, MongoDB, SQLite, etc) and the database must include at least two tables (SQL) or collections (NoSQL).

The database must contain at least 100 records.

Your project must use ETL workflows to ingest data into the database (i.e. the data should not be exactly the same as the original source; it should have been transformed in some way).

Your project must include a method for reading data from the database and displaying it for future use, such as:

Pandas DataFrame

Flask API with JSON output

Your project must use one additional library not covered in class related to data engineering. Consider libraries for data streaming, cloud, data pipelines, or data validation.

Your GitHub repo must include a README.md with an outline of the project including:

An overview of the project and its purpose

Instructions on how to use and interact with the project

Documentation of the database used and why (e.g. benefits of SQL or NoSQL for this project)

ETL workflow with diagrams or ERD

At least one paragraph summarizing efforts for ethical considerations made in the project

References for the data source(s)

References for any code used that is not your own

OPTIONAL: add user-driven interaction, either before or after the ETL process. e.g.:

BEFORE: provide a menu of options for the user to narrow the range of data being extracted from a data source (e.g. API or CSV file, where fields are known in advance).

AFTER: Once the data is stored in the database, add user capability to extract filtered data from the database prior to loading it in a Pandas DataFrame or a JSON output from a Flask API.

For this project, you can focus your efforts within a specific industry, as detailed in the following examples.

