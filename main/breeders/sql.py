ALL_BREEDERS = "SELECT * FROM Hodowca ORDER BY id"


ADD_BREEDER = "INSERT INTO Hodowca (id, imie, nazwisko, email, numer_telefonu)" \
              " VALUES ({0}, '{1}', '{2}', '{3}', '{4}')"
DELETE_BREEDER = "DELETE FROM Hodowca WHERE id = {0}"
UPDATE_BREEDER = "UPDATE Hodowca SET imie = '{1}', nazwisko = '{2}', email = '{3}', numer_telefonu = '{4}'" \
                 "  WHERE id = {0}"
GET_LATEST_ID = "SELECT * FROM Hodowca_ostatni_indeks"