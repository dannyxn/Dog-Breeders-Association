ALL_DOGS = "SELECT * FROM Pies ORDER BY id"

ADD_DOG = "INSERT INTO Pies(id, id_wlasciciel, id_miot, id_rasa, imie) VALUES (100, {0}, {1}, {2}, '{3}')"
DELETE_DOG = "DELETE FROM Pies WHERE id = {0}"
UPDATE_DOG = "UPDATE Rasa SET id_wlasciciel = {1}, id_miot = {2}, id_rasa = {3}  imie = '{4}'" \
             "WHERE id = {0}"

GET_LATEST_ID = "SELECT * FROM Pies_ostatni_indeks"

SEARCH_DOGS = "SELECT * FROM Pies WHERE"