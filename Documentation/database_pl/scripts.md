# Szablony scenariuszy (scripttemplates)

Wpisy szablonów skryptów są osadzone jako lista elementów podrzędnych `scripttemplate` w znaczniku `scripttemplates`.

```XML
<scripttemplates>
	<scripttemplate product="1" licence_type="1" guid="scripttemplate-random-ron-foodformealtime01">
		<title>
			<de>${food} zum ${mealtime}</de>
			<en>${food} for ${mealtime}</en>
			<pl>${food} ${mealtime}</pl>
		</title>
		<description>
			<de>...</de>
			<en>...</en>
			<pl>...</pl>
		</description>

	<variables>
			<food>
				<de>Kinder|Liebe|Joghurt</de>
				<en>Children|Love|Joghurt</en>
				<pl>Dzieci|Miłość|Jogurt</pl>
			</food>
			<mealtime>
				<de>Frühstück|Mittagessen|Abendessen|Brunch</de>
				<en>breakfast|lunch|dinner|brunch</en>
				<pl>na śniadanie|na lunch|na kolację|na brunch</pl>
			</mealtime>
		</variables>

		<jobs>
			<job index="0" function="1" required="1" />
			<job index="1" function="2" required="1" gender="2" />
			<job index="2" function="2" required="1" gender="1" />
			<!-- there might be up to 2 additional roles without further specifications -->
			<job index="3" function="32" required="0" role_guid="script-roles-ron-001" />
			<job index="4" function="32" required="0" />
		</jobs>
		<genres maingenre="15" subgenres="5" />
		<blocks min="2" max="3" slope="30" />
		<price min="12000" max="17000" slope="60" />
		<potential min="50" max="70" slope="45" />
		<outcome min="25" max="35" slope="40" />
		<review min="45" max="65" slope="40" />
		<speed min="35" max="65" slope="50" />
	</scripttemplate>
```

Film (`product`) powinien być możliwy do stworzenia tutaj jako pojedyncza licencja (`licence_type`); film romantyczny (`maingenre`) trwający dwie lub trzy godziny (`blocks`), który ma również części komediowe (`subgenres`).
Tytuł może brzmieć "Miłość na kolację", ale także "Jogurt na śniadanie" (`title` z [variables](variables.md)).
Reżyser (`job index 0`), kobieta i mężczyzna grający główną rolę (`job index 1,2`) są obowiązkowi (`required=1`).
Jednakże, dwóch aktorów drugoplanowych może być również wymaganych do filmowania; [rola filmowa](persons.md#film_roles) jest zdefiniowana dla jednego z aktorów drugoplanowych (`role_guid`).
Cena (`price`) za scenariusz wynosi od 12,000 (`min`) do 17,000 (`max`) z lekką tendencją do wyższej ceny (`slope`).
Zakresy oceny (tempo itp.) są zdefiniowane na końcu wpisu (średnia ocena krytyków i tempo, słaby wynik komercyjny).
Następnie gra wykorzystuje ten szablon do wygenerowania rzeczywistego scenariusza z określonymi wartościami, na podstawie którego można następnie nakręcić film.
Z jednego szablonu można również utworzyć kilka scenariuszy.
Jeśli tytuły są identyczne, do scenariusza dodawany jest licznik.



Najbardziej decydującą różnicą w treści między szablonami scenariuszy a "gotowymi" programami jest użycie zmiennych w celu stworzenia wariancji, zwłaszcza w tytule i definicji obsady.
Zamiast określać osoby występujące w filmie, definiuje się wymagania dotyczące obsady.
Kategorie oceny (tempo itp.) są również często określane jako zakres.

## Właściwości_szablonu_skryptu

| Nazwa | Typ | Opis |
| ---- | --- |------------- |
| guid | Obowiązkowe | [GUID](main.md#guid) |
| product | Obowiązkowe  | [Programmtyp](main.md#Programmtyp) |
| licence_type | Obowiązkowe | [Lizenztyp](main.md#Lizenztyp) |
| index | opcjonalnie | Sekwencja dla serii|
| creator | Metadane opcjonalne | [Standardeigenschaft](main.md#creator) |
| created_by | Metadane opcjonalne | [Standardeigenschaft](main.md#created_by) |
| comment |  informativ  |[Standardeigenschaft](main.md#comment) |

## Rodzaje szablonów skryptów

Standardowe elementy title [title](main.md#title) i description [description](main.md#description) muszą być zdefiniowane w całości.
Zmienne [variables](variables.md) są również często używane dla tytułu i opisu.
Element [availability](time.md#availability) może być użyty do ograniczenia dostępności gotowego skryptu.

(We wcześniejszej wersji dokumentacji błędnie opisano, że grupy docelowe można definiować analogicznie do programów w węźle grup.
Jednak TVTower nigdy nie czytał tego węzła.
Grupy docelowe można określić w węźle `data`).

### Gatunek (genres)

Główny gatunek (Obowiązkowe) i opcjonalne podgatunki (oddzielone przecinkami) mogą być zdefiniowane w węźle `genres`.
Możliwe wartości to [Genres](main.md#Genre), które są również używane dla programów.

Przykłady:

* `<genres maingenre="4" />` Kryminał
* `<genres maingenre="13" subgenres="2"/>` Monumentalny film z elementami akcji
* `<genres maingenre="7" subgenres="5,15"/>` komediowy dramat romantyczny

### Wymagany personel (jobs)

Lista zadań (`job`), które muszą być wypełnione dla sesji może być zdefiniowana w głównym węźle `jobs`.
Dla każdego `job` można zdefiniować następujące właściwości.

| Nazwa | Typ | Opis |
| ---- | --- |------------- |
| index | Obowiązkowe | Kolejność na liście |
| function | Obowiązkowe | [Job](main.md#Job) |
| required | Obowiązkowe | Wartość prawdy; czy ta pozycja musi być obsadzona |
| gender | opcjonalnie | Płeć |
| country | opcjonalnie | Kraj |
| role_guid | opcjonalnie | Identyfikator GUID [reel](person.md#film reels), który jest tutaj linkowany |
| random_role | opcjonalnie | Wartość prawdy |
| person | opcjonalnie | Wstępnie zdefiniowane zajęcie GUID/zmienna |

Przykłady:

* `<job index="0" function="1" required="1" />` - Reżyser musi być obsadzony, płeć nie jest określona
* `<job index="1" function="2" gender="2" required="1" />` - Główna aktorka musi zostać obsadzona
* `<job index="2" function="16" gender="1" required="0" />` - Gość płci męskiej może, ale nie musi pojawić się w gotowym scenariuszu

Tytuł i opis mogą odnosić się do obsadzonych ról (np. `${.self: "role":1: "firstname"}`).
Jeśli stała rola jest zdefiniowana za pomocą `role_guid`, używane są odpowiednie nazwy.
Flaga `random_role="1"` zapewnia, że nowa rola jest konsekwentnie tworzona dla każdego skryptu.
W szczególności dla serii zaleca się jawne ustawienie tej flagi, jeśli używane jest odniesienie do roli.
Atrybuty `gender` i `country` są następnie używane do rzucania kostką dla nazwy.



* `<job index="1" function="2" gender="1" country="it" required="1" />` - męskie włoskie imię jest generowane, gdy odnosi się do roli
* `<job index="2" function="2" country="us" required="1" random_role = "1" />` - dla każdego skryptu tworzona jest nowa rola z amerykańskim imieniem, płeć nie jest ustalona

Od wersji 0.8.4 baza danych może predefiniować zawód.
Aby to zrobić, identyfikator GUID osoby lub zmienna, która jest rozpoznawana jako identyfikator GUID, jest określana w atrybucie "person".
Odpowiednia osoba jest następnie wyświetlana w supermarkecie i nie można jej zmienić.
Na przykład można zaimplementować filmy określonego reżysera lub programy z określonym gospodarzem (X's Dracula, The Late Night Show z Y).



### Dane_skryptu (data)

| Nazwa | Typ | Opis |
| ---- | --- |------------- |
| flags | opcjonalnie | zdecydowanie używany [Flagi programu](main.md#Programmflags) |
| flags_opcjonalnie | opcjonalnie | używany losowo [Programmflags](main.md#Programmflags) |
| scriptflags | opcjonalnie | Flagi dla tego szablonu (ScriptFlags patrz poniżej) |
| production_licence_flags | opcjonalnie | [Lizenzflags](main.md#Lizenzflags) |
| production_broadcast_flags | opcjonalnie | [Ausstrahlungsflags](main.md#Ausstrahlungsflags) |
| production_broadcast_limit| opcjonalnie | jak często program może być nadawany |
| production_limit | opcjonalnie | ile odcinków można wyprodukować (np. program bez określonych odcinków) |
| live_date | opcjonalnie | [Czas](time.md#Atrybuty_czasu) nadawanie programów na żywo |
| broadcast_time_slot_start | opcjonalnie | Najwcześniejszy początek pierwszego bloku |
| broadcast_time_slot_end | opcjonalnie | Ostatni koniec ostatniego bloku |
| available | opcjonalnie | Wartość prawdy - czy skrypt jest początkowo dostępny |
| target_groups | opcjonalnie | zdecydowanie używany [Grupa docelowa](main.md#Grupy_docelowe) |
| target_groups_opcjonalnie | opcjonalnie | prawdopodobnie używany [Grupa docelowa](main.md#Grupy_docelowe) |


Tutaj, `flags` i `flags_opcjonalnie`, jak również `target_groups` i `target_groups_opcjonalnie` są prawdopodobnie najważniejsze dla wpływu na końcowy rezultat.
Jeśli produkujesz program na żywo, należy zdefiniować live_date lub ustawić flagę "zawsze na żywo".

Jeśli zdefiniujesz `flags_opcjonalnie` w głównym wpisie dla serii, flagi te są określane raz podczas faktycznego tworzenia skryptu, a następnie używane dla wszystkich odcinków serii.
Z flagą opcjonalnie live, wszystkie odcinki są zawsze live lub żadne.

Oczywiście można również zdefiniować `flags_opcjonalnie` w węźle `data` pojedynczego odcinka (w `children`).
Losowa wartość tych flag jest wtedy używana tylko dla tej sekwencji.
Można to wykorzystać na przykład do upewnienia się, że tylko jeden odcinek jest prawdopodobnie FSK-18, a nie cała seria.



Od wersji 0.8.2 szablon skryptu może być początkowo oznaczony jako niedostępny (`available="0"`).
Następnie jest aktywowany przez efekt (`modifyScriptAvailability` patrz [Efekty](main.md#effects)), np. przez pojawienie się wiadomości lub emisję programu.
Przypadkiem użycia tej flagi byłaby na przykład definicja skryptu dla kontynuacji/sequela, przy czym oryginał musi zostać wyemitowany jako pierwszy.

### (Losowe) wartości dla skryptu i wyniku



Dla niektórych właściwości można zdefiniować stałą wartość lub zakres do losowego określenia.
Podstawowa struktura to `<property value="Value" />` dla wartości stałych i `<property min="MinValue" max="MaxValue" slope="SlopeValue" />` dla wartości losowych, gdzie `slope` jest opcjonalnie i kontroluje losowy rozkład między wartością minimalną i maksymalną.
Taka definicja jest możliwa dla następujących właściwości.



| Nazwa | Opis |
| ---- | ------------ |
| blocks | Długość programu w godzinach |
| price | Cena skryptu |
| potential | Potencjał scenariusza |
| speed | Tempo |
| review | Opinia krytyków |
| outcome | Sukces komercyjny |
| studio_size | Rozmiar wymaganego studia |
| production_time | Podstawowy czas produkcji w minutach |
| episodes | Liczba odcinków serialu |

Beispiele:

* `<blocks value="3" />` - Program powinien wtedy składać się dokładnie z 3 bloków (godzin).
* `<speed min="20" max="50" />` - prędkość programu powinna wynosić od 20 do 50
* `<price min="10000" max="20000" slope="20" />` - Cena powinna wynosić od 10 000 do 20 000, ale zwykle jest tańsza.

`episodes` może być używana w dwóch różnych, wzajemnie wykluczających się wariantach.
Definicja w głównym szablonie skryptu ogranicza liczbę odcinków.
Na przykład, można zdefiniować 20 możliwych szablonów podrzędnych i powiedzieć, że tylko 5 do 8 powinno należeć do serii.
Kolejność odcinków zostaje zachowana.
Pierwszy szablon jest zawsze wybierany domyślnie (= odcinek pilotażowy, który powinien być zawsze dołączony - zobacz np. `scripttemplate-ron-visiting` w bazie danych).
Jeśli chcesz, aby pierwszy odcinek również był jednym z losowo wybranych, możesz oznaczyć go jako opcjonalnie (`<episodes min="0" />` dla tego odcinka).



Drugim przypadkiem użycia jest definicja `epizodów` w jednym lub kilku szablonach podrzędnych bez określania liczby odcinków w głównym szablonie skryptu.
Gdy tworzony jest właściwy skrypt, szablon podrzędny jest następnie używany do utworzenia odpowiedniej liczby odcinków (dozwolone jest również 0).

Jeśli więc nie wszystkie zdefiniowane odcinki mają być zawsze tworzone, dostępne są dwie opcje: Ograniczyć całkowitą liczbę w głównym węźle lub skonfigurować odcinki, które można pominąć za pomocą `<episodes min="0" max="1" />`.



### Modyfikacja (programme_data_modifiers)

Od wersji 0.7.4 modyfikatory dla utworzonego programu mogą być przechowywane w szablonach skryptów.
W przeciwieństwie do wartości losowych, w tym przypadku nie są możliwe definicje zakresu, a jedynie wartości stałe.

```XML
<programme_data_modifiers>
	<!-- erholt sich nach einer Ausstrahlung langsamer als normal -->
	<modifier name="topicality::refresh" value="0.5" />
	<!-- billiger als normal -->
	<modifier name="price" value="0.7" />
</programme_data_modifiers>
```

Możliwe modyfikatory można znaleźć w [Programy](programmes.md#Modifier).

### Atrakcyjność dla grupy docelowej (targetgroupattractivity)

Od wersji 0.8.1 odwołanie do grupy docelowej można również zdefiniować dla szablonów skryptów.
Jest ona przekazywana w niezmienionej postaci do wynikowych danych programu.

Zobacz [Standardowy element łączący](main.md#targetgroupattractivity).

### Odcinki serialu (children)

Lista szablonów dla sekwencji może być zdefiniowana w głównym węźle `children` (ponownie jako węzeł `scripttemplate`). Następnie należy zdefiniować dla nich właściwość `index`.

### Efekty (effects)

Od wersji 0.8.2 efekty są również obsługiwane dla szablonów skryptów.
Składnia jest analogiczna do efektów w komunikatach ([efekty](main.md#effects)).
Zdefiniowane efekty są przekazywane do gotowej produkcji.
Pod tym względem obsługiwane są te same wyzwalacze, co w przypadku programów (`broadcast`, `broadcastDone`, `broadcastFirstTime`, `broadcastFirstTimeDone`).
Typowym przypadkiem użycia efektu szablonu skryptu będzie prawdopodobnie wydanie kolejnych szablonów (sezon drugi dla pierwszego sezonu, który właśnie został wyprodukowany).



```
	<effects> 
		<effect trigger="broadcastFirstTime" type="modifyScriptAvailability" guid="ronny-scripttemplate-seriesX-season2" />
	</effects>
```

## specyficzne wartości dla szablonu skryptu

| **ScriptFlags** | Znaczenie |
| ---- | --------- |
| 1 | może być przedmiotem obrotu |
| 2 | Automatyczna sprzedaż po osiągnięciu limitu produkcji |
| 4 | Automatyczne usuwanie po osiągnięciu limitu produkcji  |
| 8 | Limit produkcji jest resetowany po powrocie.
| 16 | po powrocie wartości prędkości itp. są zmieniane losowo|
| 32 | po zwrocie szablon nie może być zakupiony ponownie |

(Kod źródłowy: `TVTScriptFlag`)

## Przykłady

### Show

```XML
<scripttemplate product="3" licence_type="1" guid="scripttemplate-ron-morningshow">
			<title>
				<de>Goldene Morgenstunden</de>
				<en>Golden morning hours</en>
				<pl>Złote godziny poranne</pl>
			</title>
			<description>
				<de>Obudziłem się ...</de>
				<en>I woke up ...</en>
				<pl>Obudziłem się ...</pl>
			</description>

			<jobs>
				<job index="0" function="1" required="1" />
				<job index="1" function="8" required="1" />
				<job index="2" function="8" required="0" />
				<job index="3" function="16" required="0" />
			</jobs>

			<genres maingenre="103" subgenres="9" />
			<blocks value="3" />
			<price min="3000" max="5000" slope="60" />
			<potential min="40" max="60" slope="45" />
			<outcome min="30" max="50" slope="40" />
			<review min="40" max="50" slope="40" />
			<speed min="45" max="60" slope="50" />
			<!-- live whenever first broadcastd -->
			<!-- licence flags: 4 + 32 (REMOVE_ON_REACHING_BROADCASTLIMIT + LICENCEPOOL_REMOVES_TRADEABILITY) -->
			<data flags="1" broadcast_time_slot_start="5" broadcast_time_slot_end="10" production_limit="4" production_broadcast_limit="1" production_broadcast_flags="512" production_licence_flags="36" />
			<targetgroupattractivity unemployed_male="0.1" managers="2" />
		</scripttemplate>
```

Interesującą częścią tego programu (`product`) jest węzeł `data`.
Jest to program na żywo (`flags`), który musi być nadawany między 5 rano a 10 rano (`broadcast_time_slot_X`), najwcześniej następnego dnia (`live_date`), ale jest zawsze na żywo w tym okresie (`production_broadcast_flags`).
Cztery programy (`production_limit`) mogą być wyprodukowane (bez wyraźnej definicji `children`!), ale może być tylko jedna emisja na program (`production_broadcast_limit`).
Następnie program znika i nie jest już nigdy dostępny (`production_licence_flags`).
Bezrobotni uważają ten program za okropny, menedżerowie są zachwyceni.



### Serie

```XML
<scripttemplate product="2" licence_type="3" guid="TheRob-script-ser-dram-TVTintern">
	<title>
		<de>TVTs: ${object} im Hochhaus</de>
		<en>TVTs: ${object} In A Skyscraper</en>
		<pl>TVTs: ${object} W wieżowcu</pl>
	</title>
	<description>
		<de>Serie über ${object} im TV Tower Hochhaus</de>
		<en>Series about ${object} In The TV Tower Skyscraper</en>
		<pl>Seria o ${object} W wieżowcu telewizyjnym</pl>
	</description>
	<children>
		<scripttemplate index="0" product="2" licence_type="2" guid="TheRob-script-ser-dram-TVTintern-Ep1">
			<title>
				<de>TVTs Pilot</de>
				<en>TVTs Pilot</en>
				<pl>TVTs Pilot</pl>
			</title>
			<blocks min="2" max="4" />
		</scripttemplate>
		...
		<scripttemplate index="2" product="2" licence_type="2" guid="TheRob-script-ser-dram-TVTintern-Ep3">
			<title>
				<de>${attribute} macht eine Party</de>
				<en>${attribute} Invites To the Party</en>
				<pl>${attribute} Zaproszenia na imprezę</pl>
			</title>
		</scripttemplate>
		...
	</children>
	<variables>
		<attribute>
			<de>Die FR Duban|Die VR Duban</de>
			<en>The FR Duban|The VR Duban</en>
			<pl>FR Duban|The VR Duban</pl>
		</attribute>
		<object>
			<de>Intrigen|Hinterhalte|Wettkämpfe|...</de>
			<en>Intrigues|Ambushes|Competitions|...</en>
			<pl>Intrygi|Ambusy|Konkursy|...</pl>
		</object>
	</variables>
	<jobs>
		<job index="0" function="1" required="1"  />
		<job index="1" function="2" required="1" gender="2" />
		...
		<job index="5" function="32" required="0" />
		...
	</jobs>
	<data flags="8" flags_opcjonalnie="50" />
	<genres maingenre="7" subgenres="9" />
	<episodes min="9" max="12" />
	<blocks value="1" />
	<price min="95000" max="99000" />
	<potential min="50" max="90" slope="45" />
	<outcome min="75" max="95" slope="40" />
	<review min="45" max="85" slope="55" />
	<speed min="35" max="85" slope="50" />
</scripttemplate>
```

Ten serial (`product` i `licence_type` w głównym elemencie) ma kilka odcinków (`children` z innym `licence_type`!).
Jest to serial dramatyczny, ale może być również serialem familijnym jako podgatunek.
Jest to serial kultowy (`flags`), ale może być również filmem klasy B/trash/animacją (`flags_opcjonalnie`).
Odcinki mogą definiować różne atrybuty (`blocks` w filmie pilotażowym).
W przeciwnym razie dziedziczą dane głównego węzła.
(Szczególną pozycję zajmuje tutaj `flags_opcjonalnie`.
W tym przypadku odcinek nie dziedziczy flag, które mogą być opcjonalnie, ale końcową losową wartość flagi.
Ma to na celu zapewnienie, że seria jest spójna - wszystkie odcinki żyją lub są usuwane.
Jeśli chcesz uzyskać różne wartości dla odcinków, zdefiniuj `flags_opcjonalnie` dla poszczególnych odcinków).
Odcinki mogą mieć różne obsady (`job reqired="0"`).
Przy cenie 95,000-99,000 za odcinek, skrypt nie jest do końca tani, ale oceny są stosunkowo wysokie.
Od 9 do 12 dzieci jest wybieranych do scenariusza z dostępnych szablonów dzieci (`children`), przy czym pierwszy odcinek jest zawsze dołączony (`episodes`).



### Programy na żywo
	Do zrobienia

## DO ZROBIENIA i pytania

### Ogólne

* w kodzie, `keywords`, `live_time`, `production_time_mod` są nadal odczytywane w script-data; (nieużywane w DB, jeszcze nie w gramatyce)
* Oceniaj liczbę odcinków (zdefiniuj serię bez dzieci i określ liczbę odcinków)