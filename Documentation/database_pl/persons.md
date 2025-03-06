# Ludzie (person)

W bazie danych osoby są podzielone na trzy kategorie: Główne postacie (celebritypeople), Drugoplanowe postacie (insignificantpeople) i Role filmowe (programmemeroles).

Osoby te pojawiły się w filmach itp. i są dostępne do produkcji w różnych zawodach.
Liczne cechy są już zdefiniowane w bazie danych dla głównych postaci.
Z drugiej strony, nieprofesjonaliści dostępni w supermarkecie są wybierani spośród postaci drugoplanowych, a ich cechy są składane.

Role filmowe (podobne do Jamesa Bonda) to postacie przedstawiane w filmach.

Które z poniższych właściwości i elementów podrzędnych są obsługiwane w każdym przypadku, są wymienione w sekcjach dotyczących głównych postaci, postaci drugorzędnych i ról filmowych.



W przeciwieństwie do tytułów filmów itp., wartości specyficzne dla języka (np. inna pisownia nazwy w innym języku) nie są bezpośrednio obsługiwane przez główną definicję.
Lokalizacja nazw osobowych lub ról filmowych jest możliwa w [oddzielnych plikach](lang.md).

## Właściwości_osoby

| Nazwa | Typ | Opis |
| ---- | --- |------------- |
| guid | Obowiązkowe | [GUID](main.md#guid), insb. für Referenzierung bei Filmen etc. |
| first_name | Obowiązkowe* | Imię |
| last_name | Obowiązkowe* | Nazwisko |
| nick_name | opcjonalny | Pseudonim|
| title | opcjonalny | Tytuł |
| gender | opcjonalny | [Płeć](main.md#Geschlecht) |
| job | opcjonalny | (obecnie) wykonywane [Zawody](main.md#Job) |
| country | opcjonalny | [Kraj pochodzenia](main.md#Länder) |
| first_name_original | informacyjny | jeśli istnieje prawdziwy wzór do naśladowania - oryginalne imię |
| last_name_original | informacyjny |  jeśli istnieje prawdziwy wzór do naśladowania - oryginalne nazwisko |
| nick_name_original | informacyjny |  jeśli istnieje prawdziwy wzór do naśladowania - oryginalny pseudonim |
| title_original | informacyjny |  jeśli istnieje prawdziwy wzór do naśladowania - oryginalny tytuł |
| fictional | opcjonalny | [Standardowa właściwość](main.md#fictional) |
| levelup | opcjonalny | Wartość prawdy - czy dana osoba może zostać "główną osobą" (wartość domyślna 1) |
| castable | opcjonalny | Wartość prawdy - czy dana osoba może ogólnie uczestniczyć w produkcji? |
| face_code | opcjonalny | Zdefiniowany wygląd awatara |
| generator | opcjonalny | Instrukcje dotyczące automatycznego generowania atrybutów (nazwisko, imię, kraj pochodzenia) |
| tmdb_id | Metadaten opcjonalny |  [Standardowa właściwość](main.md#tmdb_id) |
| imdb_id | Metadaten opcjonalny | [Standardowa właściwość](main.md#imdb_id) |
| creator | Metadaten opcjonalny | [Standardowa właściwość](main.md#creator) |
| created_by | Metadaten opcjonalny | [Standardowa właściwość](main.md#created_by) |
| comment |  informacyjny  |[Standardowa właściwość](main.md#comment) |

Domyślną wartością dla "castable" (do wersji 0.8.2 "bookable") jest "1".
Zasadniczo jednak tylko postacie fikcyjne mogą być wykorzystywane w produkcjach wewnętrznych.
Program rozróżnia "castable" (w zasadzie) i "bookable" (obecnie).

`generator` jest rzadko używany, wartość zawiera oddzielony przecinkami skrót kraju i płeć do określenia nazwy.
Przykład `generator="de,2"` dla Niemki.
Zobacz także opis generatora osób w [zmienne](variables.md).

## Rodzaje osób

Dla lepszej czytelności, [główne osoby](persons.md#main_persons) czasami zawiera także `first_name`, `last_name`, `nick_name`, `title` i ich oryginalne wersje jako elementy potomne.

### Szczegóły (details)

Większość pól można również określić bezpośrednio jako atrybut osoby.
W węźle `details` są one dostępne głównie w [Główne osoby](persons.md#Main persons) dla lepszej czytelności.

| Nazwa | Typ | Opis |
| ---- | --- |------------- |
| job | opcjonalny | (obecnie) wykonywane [zawody](main.md#Job) |
| gender | opcjonalny | [Płeć](main.md#Geschlecht) |
| birthday | opcjonalny | Urodziny |
| deathday | opcjonalny | Rok śmierci |
| fictional | informacyjny | [Standardowa właściwość](main.md#fictional) |
| country | opcjonalny |[Kraj pochodzenia](main.md#Kraje) |
| face_code | opcjonalny | Zdefiniowany wygląd awatara |

Przykład `<details job="2" gender="1" birthday="1970-08-23" deathday="1993-10-31" country="US" />` - Amerykański aktor, który żył od 23 sierpnia 1970 roku do 31 października 1993 roku.

Od wersji 0.8.2 obsługiwane są również lata względne (ujemne), np. dla roku urodzenia.
Jest to interesujące dla postaci fikcyjnych, które powinny być w tym samym wieku niezależnie od roku rozpoczęcia gry.
`birthday="-31-03-02"` oznaczałoby więc 31 lat przed rokiem początkowym.

### dane (data)

Dane te określają w szczególności wartości przydatności do spotkania.
O ile nie określono inaczej, możliwe wartości wynoszą od 0 do 100 (procent).

| Nazwa | Typ | Opis |
| ---- | --- |------------- |
| topgenre | opcjonalny | [Gatunek główny](main.md#Gatunek_główny) |
| price_mod | opcjonalny | Współczynnik ceny (liczba z miejscami dziesiętnymi wokół 1) |
| affinity | opcjonalny | Affinity |
| charisma | opcjonalny | Charisma |
| humor | opcjonalny | Humor |
| power | opcjonalny | Moc |
| appearance | opcjonalny | Wygląd |
| fame | opcjonalny | Celebryta |
| scandalizing | opcjonalny | Tendencja do wywoływania skandali |
| popularity | opcjonalny | Popularność |
| popularity_target | opcjonalny | Długoterminowa popularność|

Przykład `<data popularity="20" affinity="50" fame="20" scandalizing="0" price_mod="0.7" power="0" humor="9" charisma="11" appearance="21" topgenre="0" />`

Długoterminowa popularność nie jest jeszcze wykorzystywana w bazie danych.

## Główne postacie

Główne osoby są osadzone w tagu `celebritypeople` jako lista elementów podrzędnych `person`.
Wszystkie powyższe właściwości i elementy podrzędne są obsługiwane.
Należy zauważyć, że tylko fikcyjne główne postacie są dostępne w swoich profesjach do obsadzenia w produkcjach bezpośrednio na początku gry.

```XML
<celebritypeople>
	<person guid="TheRob-TowerTV-VeraZottova" tmdb_id="0" imdb_id="0" creator="8751" created_by="TheRob">
		<first_name>Vera</first_name>
		<last_name>Zottorova</last_name>
		<nick_name></nick_name>
		<details gender="2" fictional="1" birthday="" deathday="" country="" />
		<data popularity="5" affinity="60" fame="60" scandalizing="20" price_mod="1" power="60" humor="24" charisma="78" appearance="88" topgenre="0" />
	</person>
	<person ...
	</person>
	...
</celebritypeople>
```

## Postacie_drugoplanowe

Osoby drugorzędne są osadzone jako lista elementów podrzędnych `person` w tagu `insignificantpeople`.
Definiowane są tylko najważniejsze właściwości; w szczególności, nie ma dalszych węzłów podrzędnych poniżej `person`.
Fikcyjne postacie drugoplanowe są dostępne jako laicy w produkcjach, ale mogą zostać awansowane na główne postacie w trakcie gry.

```XML
<insignificantpeople>
	<person guid="Per_custom_Freddy_21" first_name="Sophie" last_name="McAgne" nick_name="" gender="2" country="SCO" fictional="1" />
	<person guid="ronny-people-generated-01" generator="de,2" last_name="Mueller" />
	...
</insignificantpeople>
```

Pierwszą osobą jest zmyślona Szkotka, a drugą niemiecka pani Mueller, której imię jest wybierane losowo.

## Role_filmowe

Role filmowe to osoby przedstawiane w programach.
Są one osadzone w tagu `programmeroles` jako lista elementów potomnych `programmerole`.

```XML
<programmeroles>
	<programmerole guid="script-roles-ron-001" first_name="Miranda" last_name="Jones" title="Dr." gender="2" />
	<programmerole guid="script-roles-ron-002" first_name="Jonathan" last_name="Spykes" gender="1" />
	...
</programmeroles>
```

Należy zdefiniować następujące pola

| Nazwa | Typ | Opis |
| ---- | --- |------------- |
| guid | Obowiązkowe | [GUID](main.md#guid), zwłaszcza do odwoływania się do szkiców scenariuszy itp. |
| first_name | Obowiązkowe* | Imię |
| last_name | Obowiązkowe* | Nazwisko |
| nick_name | opcjonalny | Pseudonim |
| title | opcjonalny | Tytuł (Dr itp) |
| gender | opcjonalny | [Płeć](main.md#Płeć) |
| country | opcjonalny | [Kraj pochodzenia](main.md#Kraje) |
| fictional | opcjonalny | [Standardowa właściwość](main.md#fictional) |

## DO ZROBIENIA i pytania

### Ogólne

* dane - czy te wartości są traktowane jako podstawa, a następnie rolowane?
* dane podczas wczytywania również wartości min/max (brak obsługi gramatyki)