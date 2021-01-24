SET SEARCH_PATH TO public;

CREATE EXTENSION IF NOT EXISTS citext;
CREATE DOMAIN email_domena AS citext
   CHECK ( value ~ '^[a-zA-Z0-9.!#$%&''*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$' );


CREATE TABLE Hodowca
(
id int NOT NULL,
imie varchar(64) NOT NULL,
nazwisko varchar(64) NOT NULL,
email email_domena NOT NULL,
numer_telefonu varchar(64),
UNIQUE(email, numer_telefonu)

);

CREATE TABLE Hodowla
(
id int NOT NULL,
id_wlasciciel int NOT NULL,
id_region int NOT NULL,
nazwa varchar(64) NOT NULL
);

CREATE TABLE Region
(
id int NOT NULL,
nazwa varchar(64) NOT NULL
);

CREATE TABLE Pies
(
id int NOT NULL,
id_wlasciciel int NOT NULL,
id_miot int,
id_rasa int NOT NULL,
imie varchar(64) NOT NULL,
data_urodzenia date NOT NULL,
plec varchar(1) NOT NULL
);

CREATE TABLE Egzamin
(
id int NOT NULL,
nazwa varchar(64) NOT NULL,
opis varchar(255) NOT NULL,
id_region int NOT NULL,
id_egzaminator int NOT NULL,
data_zaliczenia date NOT NULL
);

CREATE TABLE Pies_egzamin
(
id_pies int NOT NULL,
id_egzamin int NOT NULL,
UNIQUE(id_pies, id_egzamin)
);

CREATE TABLE Rasa
(
id int NOT NULL,
nazwa varchar(64) NOT NULL,
typ varchar(64) NOT NULL,
proba_pracy boolean NOT NULL
);

CREATE TABLE Miot
(
id int NOT NULL,
id_ojciec int NOT NULL,
id_matka int NOT NULL,
id_hodowla int NOT NULL,
alias varchar(1)
);

CREATE TABLE Pracownik
(
id int NOT NULL,
imie varchar(64) NOT NULL,
nazwisko varchar(64) NOT NULL,
email email_domena NOT NULL,
haslo varchar(64) NOT NULL,
numer_telefonu varchar(64),
unique(email, numer_telefonu)
);

ALTER TABLE Hodowca ADD PRIMARY KEY (id);
ALTER TABLE Hodowla ADD PRIMARY KEY (id);
ALTER TABLE Region ADD PRIMARY KEY (id);
ALTER TABLE Egzamin ADD PRIMARY KEY (id);
ALTER TABLE Pies ADD PRIMARY KEY (id);
ALTER TABLE Rasa ADD PRIMARY KEY (id);
ALTER TABLE Miot ADD PRIMARY KEY (id);
ALTER TABLE Pracownik ADD PRIMARY KEY (id);

ALTER TABLE Hodowla ADD FOREIGN KEY (id_wlasciciel) REFERENCES Hodowca (id);
ALTER TABLE Hodowla ADD FOREIGN KEY (id_region) REFERENCES Region (id);
ALTER TABLE Pies ADD FOREIGN KEY (id_wlasciciel) REFERENCES Hodowca (id);
ALTER TABLE Pies ADD FOREIGN KEY (id_miot) REFERENCES Miot (id);
ALTER TABLE Pies ADD FOREIGN KEY (id_rasa) REFERENCES Rasa (id);
ALTER TABLE Egzamin ADD FOREIGN KEY (id_egzaminator) REFERENCES Pracownik (id);
ALTER TABLE Egzamin ADD FOREIGN KEY (id_region) REFERENCES Region (id);
ALTER TABLE Pies_egzamin ADD FOREIGN KEY (id_pies) REFERENCES Pies (id) ON DELETE CASCADE;
ALTER TABLE Pies_egzamin ADD FOREIGN KEY (id_egzamin) REFERENCES Egzamin (id) ON DELETE CASCADE;
ALTER TABLE Miot ADD FOREIGN KEY (id_ojciec) REFERENCES Pies (id);
ALTER TABLE Miot ADD FOREIGN KEY (id_matka) REFERENCES Pies (id);
ALTER TABLE Miot ADD FOREIGN KEY (id_hodowla) REFERENCES Hodowla (id);
	


