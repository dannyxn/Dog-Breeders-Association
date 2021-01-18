ALL_BREEDERS = "SELECT * FROM Hodowca ORDER BY id"


ADD_BREEDER = "INSERT INTO Hodowca (id, imie, nazwisko, email, numer_telefonu)" \
              " VALUES ({0}, '{1}', '{2}', '{3}', '{4}')"
DELETE_BREEDER = "DELETE FROM Hodowca WHERE id = {0}"
UPDATE_BREEDER = "UPDATE Hodowca SET imie = '{1}', nazwisko = '{2}', email = '{3}', numer_telefonu = '{4}'" \
                 "  WHERE id = {0}"
GET_LATEST_ID = "SELECT * FROM Hodowca_ostatni_indeks"

SEARCH_BREEDER = "SELECT * FROM Hodowca WHERE"
BREEDER_KENNELS_COUNT = "SELECT COUNT FROM ilosc_hodowlii_wlasciciela WHERE id_wlasciciel = {}"
BREEDER_DOGS_COUNT = "SELECT COUNT FROM ilosc_psow_wlasciciela WHERE id_wlasciciel = {}"
BREEDER_BREEDS_COUNT = "SELECT COUNT(DISTINCT id_rasa) FROM Pies WHERE id_wlasciciel = {}"
BREEDER_REGIONS_COUNT = "SELECT COUNT(DISTINCT id_region) FROM Hodowla WHERE id_wlasciciel = {}"
POSSIBLE_TO_DELETE_BREEDER = "SELECT mozna_usunac_hodowce({})"