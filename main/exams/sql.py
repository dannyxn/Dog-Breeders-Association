ALL_EXAMS = "SELECT * FROM Egzamin ORDER BY id"

ADD_EXAM = "INSERT INTO Egzamin (id, nazwa, opis, id_region, id_egzaminator, data_zaliczenia)" \
              " VALUES ({0}, '{1}', '{2}', {3}, {4}, '{5}')"

DELETE_EXAM = "DELETE FROM Egzamin WHERE id = {0}"

UPDATE_EXAM = "UPDATE Hodowca SET nazwa = '{1}', opis = '{2}'," \
              " id_region = {3}, id_egzaminator = {4}, data_zaliczenia = '{5}' WHERE id = {0}"
