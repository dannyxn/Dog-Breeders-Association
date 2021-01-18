ALL_REGIONS = "SELECT * FROM Region ORDER BY id"

ADD_REGION = "INSERT INTO Region(id, nazwa) VALUES ({0}, '{1}')"
DELETE_REGION = "DELETE FROM REGION WHERE id = {0}"
UPDATE_REGION = "UPDATE Region SET nazwa = '{}' WHERE id = {}"

GET_LATEST_ID = "SELECT * FROM Region_ostatni_indeks"

SEARCH_REGIONS = "SELECT * FROM Region WHERE"

POSSIBLE_TO_DELETE_REGION = "SELECT mozna_usunac_region({})"