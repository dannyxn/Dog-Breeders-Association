insert into Region (id, nazwa)
values
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

insert into Hodowca
(id, imie, nazwisko, email, numer_telefonu)
values
(1, 'Albert', 'Abacki', 'abacki@gmail.com', '123456789'),
(2, 'Bartek', 'Babacki', 'babacki@gmail.com', '123456789'),
(3, 'Cezar', 'Cabacki', 'cabacki@gmail.com',  '123456789'),
(4, 'Daniel', 'Dabacki', 'dadacki@gmail.com', '123456789'),
(5, 'Dawid', 'Chara', 'dchara@gmail.com', '123456789');


insert into Hodowla
(id, id_wlasciciel, id_region, nazwa)
values
(1, 1, 1, 'Leśna polana'),
(2, 2, 2, 'Wilcze stado'),
(3, 3, 3, 'Miód malina'),
(4, 4, 4, 'Big kennel'),
(5, 5, 15, 'Wiśniowa dolina');

insert into Rasa
(id, nazwa, typ, proba_pracy)
values
(1, 'Owczarek niemiecki', 'Owczarek', true),
(2, 'Owczarek belgijski', 'Owczarek', true),
(3, 'Owczarek holenderski', 'Owczarek', true),
(4, 'Owczarek szkocki', 'Owczarek', true),
(5, 'Owczarek australijski', 'Owczarek', true);

insert into Pracownik
(id, imie, nazwisko, email, haslo, numer_telefonu)
values
(1, 'Adrian', 'Wąski', 'waski@gmail.com', 'password', '123456789'),
(2, 'Bartosz', 'Szeroki', 'szeroki@gmail.com', 'password', '123456789');

insert into Pies
(id, id_wlasciciel, id_miot, id_rasa, imie, data_urodzenia, plec)
values
(1, 5, null , 5, 'Ares', '01-01-2016', 'M'),
(2, 5, null, 5, 'Akira', '01-01-2016', 'K'),
(3, 2, null, 2, 'Borys', '01-01-2016', 'M'),
(4, 2, null, 2, 'Benia', '01-01-2016', 'K'),
(5, 3, null, 3, 'Cel', '01-01-2016', 'M'),
(6, 3, null, 3, 'Ciri', '01-01-2016', 'K'),
(7, 4, null, 4, 'Denis', '01-01-2016', 'M'),
(8, 4, null, 4, 'Dina', '01-01-2016', 'K'),
(9, 5, null, 1, 'Ares', '01-01-2016', 'M'),
(10, 5, null, 1, 'Aria', '01-01-2016', 'K');

insert into Miot
(id, id_ojciec, id_matka, id_hodowla, alias)
values
(1, 9, 10, 5, 'A');

insert into Egzamin
(id, nazwa, opis, id_region, id_egzaminator, data_zaliczenia)
values
(1, 'Obrona junior', 'Podstawowe szkolenie obronne dla psów do 12 miesiąca',
15, 1, '06-01-2021');


insert into Pies_egzamin(id_pies, id_egzamin)
values
(1, 1),
(2, 1),
(3, 1),
(4, 1),
(5, 1),
(6, 1),
(7, 1);
