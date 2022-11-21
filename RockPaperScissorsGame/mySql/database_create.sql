use db;

CREATE TABLE games(
	GameID int not null AUTO_INCREMENT,
	RoundOneResult varchar(100) NOT NULL,
	RoundTwoResult varchar(100) NOT NULL,
	RoundThreeResult varchar(100) NOT NULL,
	RoundFourResult varchar(100) NOT NULL,
	RoundFiveResult varchar(100) NOT NULL,
	OverallResult BOOLEAN NOT NULL,
	PRIMARY KEY (GameID)
);

