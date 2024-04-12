-- drop tables if needed
DROP TABLE games;
DROP TABLE players;
DROP TABLE games_details;
DROP TABLE teams;
DROP TABLE ranking;


-- view tables
SELECT * FROM games;
SELECT * FROM players;
SELECT * FROM games_details;
SELECT * FROM teams;
SELECT * FROM ranking;

-- games.csv import
CREATE TABLE games (
	GAME_DATE_EST VARCHAR,
	GAME_ID INT,
	GAME_STATUS_TEXT VARCHAR,
	HOME_TEAM_ID INT,
	VISITOR_TEAM_ID INT,
	SEASON INT,
	TEAM_ID_home INT,
	PTS_home FLOAT,
	FG_PCT_home FLOAT,
	FT_PCT_home FLOAT,
	FG3_PCT_home FLOAT,
	AST_home FLOAT,
	REB_home FLOAT,
	TEAM_ID_away INT,
	PTS_away FLOAT,
	FG_PCT_away FLOAT,
	FT_PCT_away FLOAT,
	FG3_PCT_away FLOAT,
	AST_away FLOAT,
	REB_away FLOAT,
	HOME_TEAM_WINS INT
);

SELECT * FROM games;

-- players.csv import
CREATE TABLE players (
    PLAYER_NAME VARCHAR,
	PLAYER_ID INT,
    TEAM_ID INT,
	SEASON INT);

SELECT * FROM players;

-- games_details.csv import
CREATE TABLE games_details (
	"GAME_ID" INTEGER,
	"TEAM_ID" INTEGER,
	"TEAM_ABBREVIATION" VARCHAR,
	"TEAM_CITY" VARCHAR,
	"PLAYER_ID" INTEGER,
	"PLAYER_NAME" VARCHAR,
	"NICKNAME" VARCHAR,
	"START_POSITION" VARCHAR,
	"COMMENT" VARCHAR,
	"MIN" VARCHAR,
	"FGM" FLOAT,
	"FGA" FLOAT,
	"FG_PCT" FLOAT,
	"FG3M" FLOAT,
	"FG3A" FLOAT,
	"FG3_PCT" FLOAT,
	"FTM" FLOAT,
	"FTA" FLOAT,
	"FT_PCT" FLOAT,
	"OREB" FLOAT,
	"DREB" FLOAT,
	"REB" FLOAT,
	"AST" FLOAT,
	"STL" FLOAT,
	"BLK" FLOAT,
	"TO" FLOAT,
	"PF" FLOAT,
	"PTS" FLOAT,
	"PLUS_MINUS" FLOAT
);

SELECT * FROM games_details;

-- teams.csv import
CREATE TABLE teams (
league_id FLOAT,
team_id FLOAT,
min_year VARCHAR,
max_year VARCHAR,
abbreviation VARCHAR,
nickname VARCHAR,
year_founded VARCHAR,
city VARCHAR,
arena VARCHAR,
arena_capacity FLOAT,
owner VARCHAR,
general_manager VARCHAR,
head_coach VARCHAR,
d_league_affiliation VARCHAR
);

SELECT * FROM teams;

-- ranking.csv import
CREATE TABLE ranking (
	"TEAM_ID" INTEGER,
	"LEAGUE_ID" INTEGER,
	"SEASON_ID" INTEGER,
	"STANDINGSDATE" VARCHAR,
	"CONFERENCE" VARCHAR,
	"TEAM" VARCHAR,
	"G" INTEGER,
	"W" INTEGER,
	"L" INTEGER,
	"W_PCT" FLOAT,
	"HOME_RECORD" VARCHAR,
	"ROAD_RECORD" VARCHAR,
	"RETURNTOPLAY" VARCHAR
);

SELECT * FROM ranking;