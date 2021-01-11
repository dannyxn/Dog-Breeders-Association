INSERT INTO Region (id, nazwa)
VALUES
(1, 'Zachodniopomorskie'),
(2, 'Pomorskie'),
(3, 'Warmińsko-Mazurskie'),
(4, 'Lubuskie'),
(5, 'Wielkopolskie'),
(6, 'Kujawsko-Pomorskie'),
(7, 'Mazowieckie'),
(8, 'Podlaskie'),
(9, 'Dolnośląskie'),
(10, 'Łódzkie'),
(11, 'Świętokrzyskie'),
(12, 'Lubelskie'),
(13, 'Opolskie'),
(14, 'Śląskie'),
(15, 'Małopolskie'),
(16, 'Podkarpackie');

INSERT INTO Hodowca
(id, imie, nazwisko, email, haslo, numer_telefonu)
VALUES
(1, 'Albert', 'Abacki', 'abacki@gmail.com', 'password', '123456789'),
(2, 'Bartek', 'Babacki', 'babacki@gmail.com', 'password', '123456789'),
(3, 'Cezar', 'Cabacki', 'cabacki@gmail.com', 'password', '123456789'),
(4, 'Daniel', 'Dabacki', 'dadacki@gmail.com', 'password', '123456789'),
(5, 'Dawid', 'Chara', 'dchara@gmail.com', 'password', '123456789');


INSERT INTO Hodowla
(id, id_wlasciciel, id_region, nazwa)
VALUES
(1, 1, 1, 'Leśna polana'),
(2, 2, 2, 'Wilcze stado'),
(3, 3, 3, 'Miód malina'),
(4, 4, 4, 'Big kennel'),
(5, 5, 15, 'Wiśniowa dolina');

INSERT INTO Rasa
(id, nazwa, typ, proba_pracy)
VALUES
(1, 'Owczarek niemiecki', 'Owczarek', true),
(2, 'Owczarek belgijski', 'Owczarek', true),
(3, 'Owczarek holenderski', 'Owczarek', true),
(4, 'Owczarek szkocki', 'Owczarek', true),
(5, 'Owczarek australijski', 'Owczarek', true);

INSERT INTO Pracownik
(id, imie, nazwisko, email, haslo, numer_telefonu)
VALUES
(1, 'Adrian', 'Wąski', 'waski@gmail.com', 'password', '123456789'),
(2, 'Bartosz', 'Szeroki', 'szeroki@gmail.com', 'password', '123456789');

INSERT INTO Pies
(id, id_wlasciciel, id_miot, id_rasa, imie)
VALUES
(1, 5, null , 5, 'Ares'),
(2, 5, null, 5, 'Akira'),
(3, 2, null, 2, 'Borys'),
(4, 2, null, 2, 'Benia'),
(5, 3, null, 3, 'Cel'),
(6, 3, null, 3, 'Ciri'),
(7, 4, null, 4, 'Denis'),
(8, 4, null, 4, 'Dina'),
(9, 5, null, 1, 'Ares'),
(10, 5, null, 1, 'Aria');

INSERT INTO Miot
(id, id_ojciec, id_matka, alias)
VALUES
(1, 9, 10, 'A');

INSERT INTO Egzamin
(id, nazwa, opis, id_region, id_egzaminator, data_zaliczenia)
VALUES
(1, 'Obrona junior', 'Podstawowe szkolenie obronne dla psów do 12 miesiąca',
15, 1, '06-01-2021');

