# Programme (programmes)

Wpisy programów są osadzone jako lista elementów podrzędnych `programme` w tagu `allprogrammes`.

```XML
<allprogrammes>
	<programme guid="54084557-4497-48d5-8e3a-6a6c987ebb26" product="1" licence_type="1" tmdb_id="0" imdb_id="tt0114746" creator="">
		<title_fake>
			<de>11 Donkeys</de>
			<en>11 Donkeys</en>
			<pl>11 Donkeys</pl>
		</title_fake>
		<title>
			<de>12 Monkeys</de>
			<en>Twelve Monkeys</en>
			<pl>Dwanaście małp</pl>
		</title>
		<description>
			<de>${.self:"cast":1:"fullname"} als potentieller Weltretter, der in die Vergangenheit geschickt wird, um die Apokalypse aufzuhalten.</de>
			<en>${.self:"cast":1:"fullname"} as a potential world savior sent back in time to stop the apocalypse.</en>
			<pl>${.self:"cast":1:"fullname"} jako potencjalny zbawca świata wysłany w przeszłość, by powstrzymać apokalipsę.</pl>
		</description>
		<staff>
			<member index="0" function="1">85341df9-bd8f-4fd0-9f80-c9ab44ca0829</member>
			<member index="1" function="2">2b6af8c4-7775-44da-820e-1ce9c55d8cd9</member>
			<member index="2" function="2">1312b7b5-3215-40fd-92c8-fb0a16a2aebe</member>
			<member index="3" function="2">6773978f-3667-4c03-813b-0fbc01b8135c</member>
			<member index="4" function="2">cf2e581a-2189-4635-9358-68d9c83aad01</member>
		</staff>
		<groups target_groups="18" pro_pressure_groups="0" contra_pressure_groups="0" />
		<targetgroupattractivity employees="1.5" unemployed="2" />
		<data country="USA" year="1995" distribution="1" maingenre="16" subgenre="17,14" flags="0" blocks="3" price_mod="0.67" />
		<ratings critics="79" speed="79" outcome="64" />
	</programme>
</allprogrammes>
```

Kraj: USA (`country`) Gatunek: Science-Fiction(`maingenre`) Rodzaj: Film (`product`) Tytuł: 11 Donkeys (`title`) Rok: 1995 (`year`) Dystrybucja: W kinach (`distribution`) Ilość bloków: trwa 3 godziny (`blocks`) Tempo: ale niezbyt szybkie tempo (`speed`).
Ocena krytyków (`critics`) i wynik handlowy (`outcome`) był przeciętny.
Nie określono konkretnej grupy docelowej (`target_groups`).
Reżyser (`member index 0`) i 3 głównych aktorów (`member index 1-3`).
Pojedyncza licencja (`licence_type`) jest dostępny w rozsądnej cenie (`price_mod`).

## Właściwości programów

|    Nazwa     |   Typ               |                          Opis                             |
|    -----     |   ----------------  |  -----------------------------------------------------    |
| guid         | Obowiązkowe         | [GUID](main.md#guid)                                      |
| product      | Obowiązkowe         | [Typ programu](main.md#Programmtyp) 						 |
| licence_type | Obowiązkowe         | [Typ licencji](main.md#Lizenztyp)                         |
| fictional    | Opcjonalne          | [Standardowa właściwość](main.md#fictional)               |
| tmdb_id      | Opcjonalne          | [Standardowa właściwość](main.md#tmdb_id)                 |
| imdb_id      | Opcjonalne          | [Standardowa właściwość](main.md#imdb_id)                 |
| creator      | Metadane opcjonalne | [Standardowa właściwość](main.md#creator)                 |
| created_by   | Metadane opcjonalne | [Standardowa właściwość](main.md#created_by)              |
| comment 	   | Informatycyjne      | [Standardowa właściwość](main.md#comment)                 |

## Elementy programu dotyczące "dzieci" - child

Standardowe elementy tytułu [title](main.md#title) i opis [description](main.md#description) należy zdefiniować w całości.
Analogicznie do tytułu, oryginalny tytuł może być wprowadzony w `title_original`.
Zmienne znane z wiadomości lub skryptów nie występują obecnie w programach, ale specjalny przypadek [Zmienne rzutowania](_pl#Zmienne rzutowania) aby przenieść nazwy bezpośrednio z obsady do tytułu i opisu.

Wymagane są również następujące dane (`data`) oraz ocena treści programu (`ratings`).

### Współtwórcy (staff)

Lista współpracowników (`member`) może być zdefiniowana w głównym węźle `staff`.
Zwykle będzie to odniesienie do osób zdefiniowanych w bazie danych.
Właściwość `index` określa pozycję (0,1,2,...), aby móc odwoływać się do wpisów w zmiennych, `function` definiuje [zawód](_pl#Job).
Jeśli skład ma być generowany całkowicie losowo, można go również zdefiniować za pomocą `generator`.
Atrybut `role_guid` może być użyty do powiązania zawodu ze zdefiniowaną rolą.

* `<member index="1" function="2">person-0815</member>` - osoba z identyfikatorem GUID `person-0815` jest aktorem w obsadzie
* `<member index="2" function="64" generator="es,0"></member>` - Hiszpański gość, mężczyzna lub kobieta
* `<member index="1" function="2" role_guid="role_hercules">person-4711</member>` - [role](persons.md#filmreels) Herkules został obsadzony w filmie z aktorem o identyfikatorze GUID `person-4711`.

### Grupy docelowe i lobbystyczne

|       Nazwa            |      Typ            |                      Opis                                 |
| ---------------------- | -----------------   | --------------------------------------------------------- |
| target_groups          | obowiązkowe         | zdecydowanie używane [Grupa docelowa](_pl#Zielgruppe) |
| pro_pressure_groups    | opcjonalnie         | adresowany [Grupa lobbystów](_pl#Lobbygruppe)         |
| contra_pressure_groups | opcjonalne          | wygaszone [Grupa lobbystów](_pl#Lobbygruppe)          |

Przykład:`<groups target_groups="128" pro_pressure_groups="8" contra_pressure_groups="4" />` - Grupa docelowa: kobiety, pacyfiści - zadowoleni, lobby zbrojeniowe  - zirytowane.

### Atrakcyjność dla grupy docelowej (targetgroupattractivity)

Zobacz [Standardowy element podrzędny](main.md#targetgroupattractivity).

### Wycena (ratings)

Jest to kluczowy punkt do zdefiniowania jakości programu - wartości tempo (`speed`), opinii krytyków (`critics`) i sukcesu komercyjnego (`outcome`).
Możliwe wartości to od 0 do 100.

Przykład: `<ratings critics="45" speed="30" outcome="40" />`

### Dane (data)

|           Nazwa           |    Typ      | Opis                                                                       |
| ------------------------- | ----------  |--------------------------------------------------------------------------- |
| country                   | skrót       | wyprodukowano w [country](main.md#Kraje)                                   |
| year                      | opcjonalnie | rok produkcji                                                              |
| distribution              | opcjonalnie | kanał dystrybucji patrz poniżej                                            |
| maingenre                 | obowiązkowe | [maingenre](main.md#Gatunek) gatunek programu                              |
| subgenre                  | opcjonalnie | [subgenre](main.md#Gatunek) podgatunek programu                            |
| flags                     | opcjonalnie | [flags](main.md#Flagi)                                                     |
| licence_flags             | opcjonalnie | [Programmflags](main.md#licence_flags)                                     |
| blocks                    | opcjonalnie | Długość w godzinach (wartość domyślna i minimalna 1, maksymalna 12)        |
| price_mod                 | opcjonalnie | Czynnik do obliczenia ceny                                                 |
| broadcast_time_slot_start | opcjonalnie | Najwcześniejszy początek pierwszego bloku                                  |
| broadcast_time_slot_end   | opcjonalnie | Ostatni koniec ostatniego bloku                                            |
| broadcast_limit           | opcjonalnie | Liczba możliwych transmisji                                                |
| broadcast_flags           | opcjonalnie | [Flagi transmisji](main.md#Flagi_transmisji)                               |
| licence_broadcast_limit   | opcjonalnie | Liczba możliwych transmisji (tylko dla tej licencji)                       |
| licence_broadcast_flags   | opcjonalnie | [Flagi transmisji](main.md#Flagi_licencyjne) (tylko dla tej licencji)      |
| available                 | opcjonalnie | Wartość prawdy - czy licencja jest początkowo dostępna                     |


`country` i `maingenre` są obowiązkowe dla "głównych programów", dla sekwencji serii używane są wartości elementu nadrzędnego.
Rok" powinien być określony.
Jednakże, jeśli chcesz określić lata względne lub bardziej precyzyjne daty na początku gry, możesz pominąć `year` i użyć węzła `releaseTime`.
Flagi nadawcze są interesujące w połączeniu z programami na żywo i ograniczeniami dotyczącymi czasu lub częstotliwości nadawania.

Od wersji 0.8.2, zarówno `maingenre` jak i `subgenre` są uwzględniane w obliczeniach popularności/oglądalności.

Od wersji 0.8.2, licencja może być początkowo dezaktywowana przy użyciu `available="0"`.
Następnie jest aktywowana przez efekt (`modifyProgrammeAvailability` patrz [Effects](main#effects)), np. przez pojawienie się wiadomości lub emisję innego programu.
Przypadkiem użycia tej flagi byłaby na przykład definicja wielu sezonów serialu, przy czym kolejne sezony powinny być dostępne dopiero po wykorzystaniu poprzedniego sezonu.


### Publikacja (releaseTime)

Wydanie programu można również określić z dokładnością do dnia.

Przykład: `<releaseTime year="1986" day="4" hour="12" />` - Publikacja w 4. dniu gry w 1986 roku o godzinie 12 w południe.

Kontrola jest jednak jeszcze bardziej szczegółowa.
Obsługiwane są następujące właściwości.

| Nazwa | Znaczenie |
| -----| --------- |
| year | rok bezwzględny |
| year_relative | Lata względem początku gry (-2, +4) |
| year_relative_min | minimalny rok bezwzględny |
| year_relative_max | Maksymalny rok bezwzględny |
| day | Dzień roku |
| day_random_min | minimalny losowy dzień |
| day_random_max | Maksymalny losowy dzień |
| day_random_slope |  |
| hour | Godzina |
| hour_random_min | minimalna losowa godzina |
| hour_random_max | Maksymalna losowa godzina |
| hour_random_slope |  |

Lata względne mogą być dodatnie (od roku początkowego) i ujemne (przed rokiem początkowym). Przykład `<releaseTime year_relative="-4" year_relative_min="1983" year_relative_max="1995" />` - cztery lata przed rozpoczęciem gry, ale w latach 1983-1995.

W przypadku programów na żywo, które nie są oznaczone jako "zawsze na żywo", czas zwolnienia jest również czasem, w którym program może być nadawany na żywo.
Później jest to tylko nagranie.

### Effekte (effects)

Ab Version 0.8.2 werden auch für Programme Effekte unterstützt.
Die Syntax ist analog zu den Effekten in den Nachrichten ([Effekte](_pl#effects)).
Für Programmeffekte werden die folgenden Trigger unterstützt (`happen` wie bei den Nachrichten ist insb. nicht dabei).

* `broadcast` - efekt występuje na początku *każdej* emisji
* `broadcastDone` - efekt występuje na końcu *każdej* emisji
* `broadcastFirstTime` - efekt pojawia się natychmiast po rozpoczęciu pierwszej emisji (niezależnie od gracza).
* `broadcastFirstTimeDone` - efekt pojawia się na końcu pierwszej transmisji (niezależnie od gracza).

```
	<effects> 
		<effect trigger="broadcastFirstTime" type="modifyProgrammeAvailability" guid="ronny-programme-livereportage-raketenstart1" />
	</effects>
```

### Modifier

Składnia patrz także [modifiers](main#modifiers).
Możliwe korekty to

| Nazwa | Znaczenie |
| -----| --------- |
| price | Cena (odpowiada `price_mod`) |
| topicality::age | Wpływ wieku na maksymalną aktualność (0,8 niższy, 1,2 silniejszy) |
| topicality::refresh | Odzyskiwanie świeżości po transmisji (0,8 wolniej, 1,2 szybciej) |
| topicality::trailerRefresh | Przywracanie świeżości traillera programu po emisji (0,8 wolniej, 1,2 szybciej) |
| topicality::wearoff | Utrata aktualności transmisji (0,8 mniej, 1,2 więcej) |
| topicality::trailerWearoff | Utrata aktualności w przypadku emisji jako zwiastun (0,9 mniej, 1,2 więcej) |
| topicality::firstBroadcastDone | Wpływ pierwszej transmisji na maksymalną aktualność (domyślnie 0 brak, 0.1 niski, 1.0 wysoki) |
| topicality::notLive | Wpływ „już nie na żywo” na maksymalną aktualność (0,8 mniej, 1,2 więcej) |
| topicality::timesBroadcasted | Wpływ liczby transmisji na maksymalną rzeczywistość (0,8 mniej, 1,2 więcej) |
| callin::perViewerRevenue | Przychody z programów typu call-in (0,8 mniej, 1,2 więcej) |
| betty::pointsabsolute | punkty betty przyznawane bezpośrednio graczowi (100 = 1%, -50 = -0,5%) |
| betty::rawquality | Jakość programu dla automatycznego obliczania punktów betty (0.0-1.0) |
| betty::pointsmod | Współczynnik do automatycznego obliczania punktów bety (0,8 mniej, 1,2 więcej) |

Przykład: `<modifier name="topicality::age" value="1.6" />` - program starzeje się znacznie szybciej niż zwykle.

`topicality::notLive` działa tylko wtedy, gdy program był programem na żywo.
W tym przypadku domyślną wartością dla `topicality::firstBroadcastDone` nie jest 0, ale 1.0, co oznacza, że program na żywo automatycznie traci znaczną część swojej maksymalnej aktualności (chyba że skonfigurowano inaczej) z powodu pierwszej emisji.

Modyfikatory betty mogą być używane do wpływania na przyznawane punkty.
Z `betty::pointsabsolute`, zapisana liczba punktów jest przyznawana niezależnie od tego, jaki byłby wynik automatycznych obliczeń (wartość 1 odpowiada 0,01%, 50 odpowiada 0,5%, 125 odpowiada 1,25%).
`betty::rawquality` nadpisuje rzeczywistą jakość programu (pomiędzy 0 a 1) dla obliczeń - więcej punktów może zostać przyznanych pomimo słabej jakości lub mniej punktów pomimo dobrej jakości.
W przeciwieństwie do punktów bezwzględnych, rzeczywistość programu jest brana pod uwagę.


### Programmkinder (children)

W przypadku serii, odcinki mogą być zdefiniowane w głównym węźle serii
w węźle `children` mogą być również zdefiniowane jako `programmes`. Przykłady znajdują się poniżej.

## Konkretne wartości dla programów

| **Kanał dystrybucji** | Znaczenie |
| ------------------- | --------- |
| 0 | nieznany |
| 1 | Kino |
| 2 | Telewizja |
| 3 | Video (VHS/DVD itp.) |

(Kod źródłowy: `TVTProgrammeDistributionChannel`)

## Ponowne wykorzystanie istniejących danych programu

Możliwe jest ponowne wykorzystanie istniejących danych programu.
Może to być interesujące przy tworzeniu "wersji reżyserskiej" lub tańszej licencji, która może być emitowana tylko trzy razy.
Aby to zrobić, program bazowy jest przywoływany za pomocą `programmedata_id`.

```XML
<programme guid="myname-programme-testprogramme-limitcopy" programmedata_id="data-myname-programme-testprogramme" product="1" fictional="1" created_by="myname">
	<!-- licence_flags="4" means: remove from collection when reaching limit -->
	<data licence_flags="4" licence_broadcast_limit="3" price_mod="0.6" />
</programme>
```

## Przykłady

### minimalne 

```XML
<programme guid="auth-programme-test" product="1" licence_type="1" created_by="documentation">
	<title>
		<de>Reißerischer Titel</de>
		<de>Ripping title</de>
		<pl>Tytuł zgrywania</pl>
	</title>
	<description>
		<de>Ansprechende Beschreibung.</de>
		<en>Attractive description.</en>
		<pl>Atrakcyjny opis.</pl>
	</description>
	<staff>
		<member index="0" function="1">PersonGUID</member>
	</staff>
	<groups target_groups="32" />
	<data country="D" year="2021" distribution="2" maingenre="10" flags="16" blocks="4" />
	<ratings critics="5" speed="2" outcome="90" />
</programme>
```

Długometrażowy film fantasy wyprodukowany dla telewizji w Niemczech w 2021 roku, który przemawia w szczególności do menedżerów.
Chociaż krytycy nie byli przekonani, a film jest śmiertelnie nudny, odniósł on spory sukces komercyjny; nawet pomimo braku obsady i tylko jednego reżysera.

### Serie

```XML
<programme guid="7ad20bf5-c4c6-4237-b52a-b7b189ede0bf" product="7" licence_type="3" tmdb_id="0" imdb_id="" creator="5578" created_by="Ronny">
	<title>
		<de>Rolf Krall besucht...</de>
		<en>Rolf Krall visits...</en>
		<pl>Rolf Krall odwiedza...</pl>
	</title>
	<description>
		<de>Der bekannte Moderator [1|Full] ...</de>
		<en>Well-known presenter [1|Full] ...</en>
		<pl>Znany prezenter [1|Full] ...</pl>
	</description>
	<staff>
		<member index="0" function="1">3bb46451-4b1c-4ae7-90a4-8dbbe66f3bd1</member>
		<member index="1" function="2">a6055f37-ab53-425e-9332-14e0dfabc424</member>
	</staff>
	<groups target_groups="64" pro_pressure_groups="0" contra_pressure_groups="0" />
	<data country="D" distribution="2" maingenre="6" subgenre="" flags="4" blocks="1" price_mod="0.85" />
	<releaseTime year_relative="-1" year_relative_min="1985" year_relative_max="1990" />
	<ratings critics="20" speed="42" outcome="35" />
	<children>
		<programme guid="8258fb18-d138-49b4-b07c-0519eec12d2c" product="7" licence_type="2" tmdb_id="0" imdb_id="" creator="5578" created_by="Ronny">
			<title>
				<de>Rolf Krall besucht... Madame Krussaud</de>
				<en>Rolf Krall visits... Madame Krussaud</en>
				<pl>Rolf Krall odwiedza... Madame Krussaud</pl>
			</title>
			<description>
				<de>Im Schatten ihrer Schwester ...</de>
				<en>In the shadow of his sister ...</en>
				<pl>W cieniu swojej siostry ...</pl>
				<en></en>
			</description>
			<ratings critics="28" speed="32" />
		</programme>
		<programme ...>
		...
		</programme>
	</children>
</programme
```
Ten dokument telewizyjny został nakręcony rok przed rozpoczęciem gry i jest skierowany głównie do emerytów.
Podstawowe dane są zdefiniowane dla serii (typ licencji 3) jako całości, poszczególne odcinki (dzieci z typem 2) następnie tylko nadpisują żądane wartości (w szczególności tytuł i opis).

### Program_na_żywo_LIVE

WAŻNE Data wydania musi być ustawiona dla Live (data Live lub data pierwszej dostępności dla Always-Live).
W przypadku seriali na żywo najlepiej jest użyć Always-Live lub osobnej daty premiery dla każdego odcinka (w przeciwnym razie nie będzie możliwe wyemitowanie wszystkich odcinków na żywo).

DO ZROBIENIA

## DO_ZROBIENIA_i_pytania

### Dokumentacja

* dane - obsługa i opis innych importowanych pól
* dowiedzieć się o możliwych modyfikatorach

### Ogólne

* ze względu na konfigurowalną liczbę dni, dzień z releaseTime musi być interpretowany inaczej
* Konwertowanie odwołań z innych programów w edytorze
* Wyjaśnij wpływ grupy lobbingowej: czy nadawanie programu zmienia mój wizerunek w danej grupie lobbingowej?