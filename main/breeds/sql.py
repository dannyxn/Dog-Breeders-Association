ALL_BREEDS = "SELECT * FROM Rasa ORDER BY id"


ADD_BREED = "INSERT INTO Rasa(id, nazwa, typ, proba_pracy) VALUES ({0}, '{1}', '{2}', {3})"
DELETE_BREED = "DELETE FROM Rasa WHERE id = {0}"
UPDATE_BREED = "UPDATE Rasa SET nazwa = '{1}', typ = '{2}', proba_pracy = {3}  WHERE id = {0}"

