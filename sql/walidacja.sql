CREATE OR REPLACE FUNCTION mozna_usunac_hodowce(id_hodowca integer)
RETURNS boolean
LANGUAGE plpgsql AS
$func$
BEGIN
    RETURN NOT ( EXISTS (SELECT * FROM Hodowla WHERE id_wlasciciel=id_hodowca)
	OR EXISTS (SELECT * FROM Pies WHERE id_wlasciciel=id_hodowca));
END
$func$;
 
CREATE OR REPLACE FUNCTION mozna_usunac_rase(id_del_rasa integer)
RETURNS boolean
LANGUAGE plpgsql AS
$func$
 BEGIN
    RETURN NOT EXISTS (SELECT * FROM Pies WHERE Pies.id_rasa=id_del_rasa);
 END
$func$;
 
CREATE OR REPLACE FUNCTION mozna_usunac_psa(id_del_pies integer)
RETURNS boolean
LANGUAGE plpgsql AS
$func$
 BEGIN
    RETURN NOT ( EXISTS (SELECT * FROM Miot WHERE id_ojciec=id_del_pies)
	OR EXISTS (SELECT * FROM Miot WHERE id_matka=id_del_pies));
END
$func$;
 
 

CREATE OR REPLACE FUNCTION mozna_usunac_region(id_del_region integer)
RETURNS boolean
LANGUAGE plpgsql AS
$func$
BEGIN
    RETURN NOT ( EXISTS (SELECT * FROM Hodowla WHERE id_region=id_del_region)
	OR EXISTS (SELECT * FROM Egzamin WHERE id_region=id_del_region));	 
END
$func$;
 
CREATE OR REPLACE FUNCTION mozna_usunac_hodowle(id_del_hodowla integer)
RETURNS boolean
LANGUAGE plpgsql AS
$func$
BEGIN
	RETURN NOT EXISTS (SELECT * FROM Miot WHERE id_hodowla=id_del_hodowla);	 
END
$func$;
  
CREATE OR REPLACE FUNCTION waliduj_dodanie_psa()
RETURNS TRIGGER
LANGUAGE plpgsql AS
$$
BEGIN
	IF EXISTS(SELECT * FROM Pies WHERE id_wlasciciel=NEW.id_wlasciciel AND imie=NEW.imie) THEN
		RAISE EXCEPTION 'Właściciel posiada już psa o tym imieniu.';
	ELSIF NOT EXISTS(SELECT * FROM Hodowca WHERE id=NEW.id_wlasciciel) THEN
		RAISE EXCEPTION 'W bazie nie ma hodowcy o id=%', NEW.id_wlasciciel; 
	ELSIF NOT EXISTS(SELECT * FROM Miot WHERE id=NEW.id_miot) THEN
		RAISE EXCEPTION 'W bazie nie ma miotu o id=%', NEW.id_miot; 
	ELSIF NOT EXISTS(SELECT * FROM Rasa WHERE id=NEW.id_rasa) THEN
		RAISE EXCEPTION 'W bazie nie ma rasy o id=%', NEW.id_rasa; 
	ELSE
		RETURN NEW; 
	END IF;
END;
$$;
  
CREATE TRIGGER dodanie_nowego_psa
BEFORE INSERT OR UPDATE ON Pies
FOR EACH ROW EXECUTE PROCEDURE waliduj_dodanie_psa();


CREATE OR REPLACE FUNCTION waliduj_dodanie_osoby()
RETURNS TRIGGER
LANGUAGE plpgsql AS
$$
BEGIN
IF NEW.numer_telefonu ~ '\+(9[976]\d|8[987530]\d|6[987]\d|5[90]\d|42\d|3[875]\d|2[98654321]\d|9[8543210]|8[6421]|6[6543210]|5[87654321]|4[987654310]|3[9643210]|2[70]|7|1)\d{1,14}$'  THEN
	RETURN NEW; 
END IF;
	RAISE EXCEPTION '% nie jest prawidłowym numerem telefonu', NEW.numer_telefonu; 
END;
$$;
 
CREATE TRIGGER dodanie_nowego_pracownika
BEFORE INSERT OR UPDATE ON Pracownik
FOR EACH ROW EXECUTE PROCEDURE waliduj_dodanie_osoby();
  
CREATE TRIGGER dodanie_nowego_hodowcy
BEFORE INSERT OR UPDATE ON Hodowca
FOR EACH ROW EXECUTE PROCEDURE waliduj_dodanie_osoby();
  
CREATE OR REPLACE FUNCTION waliduj_dodanie_hodowlii()
RETURNS TRIGGER
LANGUAGE plpgsql AS
$$
BEGIN
	IF NOT EXISTS(SELECT * FROM Hodowca where id=NEW.id_wlasciciel) THEN
		RAISE EXCEPTION 'W bazie nie ma hodowcy o id=%', NEW.id_wlasciciel; 
	ELSIF NOT EXISTS(SELECT * FROM Region where id=NEW.id_region) THEN
		RAISE EXCEPTION 'W bazie nie ma regionu o id=%', NEW.id_region; 
	ELSE
		RETURN NEW; 
	END IF;
END;
$$;
  
CREATE TRIGGER dodanie_nowej_hodowlii
BEFORE INSERT OR UPDATE ON Hodowla
FOR EACH ROW EXECUTE PROCEDURE waliduj_dodanie_hodowlii();


  
CREATE OR REPLACE FUNCTION waliduj_dodanie_miotu()
RETURNS TRIGGER
LANGUAGE plpgsql AS
$$
BEGIN
	IF NOT EXISTS(SELECT * FROM Pies WHERE id=NEW.id_ojciec AND plec='M') THEN
		RAISE EXCEPTION 'W bazie nie ma psa o id=%', NEW.id_ojciec; 
	ELSIF NOT EXISTS(SELECT * FROM Pies WHERE id=NEW.id_matka AND plec='K') THEN
		RAISE EXCEPTION 'W bazie nie ma suki o id=%', NEW.id_matka; 
	ELSIF LENGTH(NEW.alias) != 1 THEN
		RAISE EXCEPTION 'Alias powinien być jedną literą';
	ELSE
		RETURN NEW; 
	END IF;
END;
$$;
  
CREATE TRIGGER dodanie_nowego_miotu
BEFORE INSERT OR UPDATE ON Miot
FOR EACH ROW EXECUTE PROCEDURE waliduj_dodanie_miotu();