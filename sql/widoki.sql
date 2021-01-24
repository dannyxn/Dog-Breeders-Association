CREATE VIEW Hodowca_ostatni_indeks AS SELECT MAX(id) FROM Hodowca;
CREATE VIEW Hodowla_ostatni_indeks AS SELECT MAX(id) FROM Hodowla;
CREATE VIEW Miot_ostatni_indeks AS SELECT MAX(id) FROM Miot;
CREATE VIEW Pies_ostatni_indeks AS SELECT MAX(id) FROM Pies;
CREATE VIEW Region_ostatni_indeks AS SELECT MAX(id) FROM Region;
CREATE VIEW Rasa_ostatni_indeks AS SELECT MAX(id) FROM Rasa;
CREATE VIEW Pracownik_ostatni_indeks AS SELECT MAX(id) FROM Pracownik;
CREATE VIEW Egzamin_ostatni_indeks AS SELECT MAX(id) FROM Egzamin;

CREATE VIEW ilosc_hodowlii_wlasciciela AS
	SELECT COUNT(*), id_wlasciciel FROM hodowla GROUP BY id_wlasciciel;

CREATE VIEW ilosc_psow_wlasciciela AS SELECT COUNT(*),
	id_wlasciciel FROM Pies GROUP BY id_wlasciciel;