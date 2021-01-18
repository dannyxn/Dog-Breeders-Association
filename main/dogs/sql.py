ALL_DOGS = "SELECT * FROM Pies ORDER BY id"

ADD_DOG = "INSERT INTO Pies(id, id_wlasciciel, id_miot, id_rasa, imie, data_urodzenia, plec) VALUES ({0}, {1}, {2}, {3}, '{4}', '{5}', '{6}')"
DELETE_DOG = "DELETE FROM Pies WHERE id = {0}"
UPDATE_DOG = "UPDATE Rasa SET id_wlasciciel = {1}, id_miot = {2}, id_rasa = {3}  imie = '{4}', data_urodzenia = '{5}', plec='{6}'" \
             "WHERE id = {0}"

GET_LATEST_ID = "SELECT * FROM Pies_ostatni_indeks"

SEARCH_DOGS = "SELECT * FROM Pies WHERE"
DOGS_ALL_EXAMS =  "SELECT Egzamin.id, Egzamin.nazwa, Egzamin.data_zaliczenia, CONCAT(Pracownik.imie, ' ', Pracownik.nazwisko),"\
                  " Region.nazwa" \
                  " FROM Egzamin JOIN Pies_egzamin ON Egzamin.id = Pies_egzamin.id_egzamin" \
                  " JOIN Pracownik ON Egzamin.id_egzaminator = Pracownik.id" \
                  " JOIN Region ON Egzamin.id_region = Region.id" \
                  " where Pies_egzamin.id_pies = {}"

ADD_PASSED_EXAM = "INSERT INTO Pies_egzamin (id_pies, id_egzamin) values" \
                  " ( {0}, {1} )" \
                  " ON CONFLICT (id_pies, id_egzamin)" \
                  " DO NOTHING"

POSSIBLE_TO_DELETE_DOG = "SELECT mozna_usunac_psa({})"