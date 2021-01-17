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
 END IF;

 RETURN NEW;

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
 IF NEW.email::email THEN
	 RETURN NEW;
 ELSE
 	 RAISE EXCEPTION '% to nieprawidłowy adres e-mail.',  NEW.email;
 END IF;


 END;
 $$;

  CREATE TRIGGER dodanie_nowego_hodowcy
  BEFORE INSERT OR UPDATE ON Hodowca
  FOR EACH ROW EXECUTE PROCEDURE waliduj_dodanie_osoby();


  CREATE TRIGGER dodanie_nowego_pracownika
  BEFORE INSERT OR UPDATE ON Pracownik
  FOR EACH ROW EXECUTE PROCEDURE waliduj_dodanie_osoby();