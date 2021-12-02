# Ohjelmistotekniikka

## Tehtävät

### Viikko 1

[gitlog.txt](https://github.com/nikitaessine/otharjoitustyo/blob/master/laskarit/viikko1/gitlog.txt)

[komentorivi.txt](https://github.com/nikitaessine/otharjoitustyo/blob/master/laskarit/viikko1/komentorivi.txt)

### Projekti:Laskin

[vaatimusmäärittely](https://github.com/nikitaessine/otharjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Suorita vaadittavat alustustoimenpiteet komennolla:

```bash
poetry run invoke build
```

3. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon.



# Työaikakirjanpito

| päivä | aika | mitä tein  |
| :----:|:-----| :-----|
| 10.11. | 2    | projektin aloitus |
| 15.11. | 1    | alustava README |
|       | 2    | testien kirjoitus |
|       | 3    | poetryn asennusongelmien ratkaisu |
|       | 1    | määrittelydokumentti |
| 16.11.| 4    | perustoiminnallisuus |
| 20.11.| 1    | käyttöliittynmän suunnittelu |
| 30.11 | 1    | käyttöohje |
|       | 2    | testaus |
| 2.12  | 2    | formatointi ja pylint opettelu |
| yht   | 30   | | 