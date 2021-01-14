ALL_KENNELS = "SELECT * FROM Hodowla ORDER BY id"

ADD_KENNEL = "INSERT INTO Hodowla(id, id_wlasciciel, id_region, nazwa) VALUES ({0}, {1}, {2}, '{3}')"
DELETE_KENNEL = "DELETE FROM Hodowla WHERE id = {0}"
UPDATE_KENNEL = "UPDATE Hodowla SET id_wlasiciel = {1}, id_region = {2}, nazwa = '{3}'  WHERE id = {0}"

GET_LATEST_ID = "SELECT * FROM Hodowla_ostatni_indeks"