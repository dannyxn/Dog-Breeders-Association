ALL_LITTERS = "SELECT * FROM Miot ORDER BY id"

ADD_LITTER = "INSERT INTO Miot (id, id_ojciec, id_matka, alias) VALUES ({0}, {1}, {2}, '{3}')"
DELETE_LITTER = "DELETE FROM Miot WHERE id = {0}"
UPDATE_LITTER = "UPDATE Hodowca SET id_ojciec = {1}, id_matka = {2}, alias = '{3}' WHERE id = {0}"

GET_LATEST_ID = "SELECT * FROM Miot_ostatni_indeks"

SEARCH_LITTERS = "SELECT * FROM Miot WHERE"