# Die TVTower-Datenbank

Dane używane przez TVTower są podzielone na kilka plików w katalogu `res/database/`.
Zasadniczo może być obsługiwanych kilka baz danych.
Domyślna baza danych znajduje się w podkatalogu `Default`.
Dane są przechowywane w [strukturze XML] (main.md#general-structure-of-an-element).
Typowym sposobem na rozpoczęcie tworzenia własnych wpisów jest wyszukanie istniejących podobnych wpisów, które są szczególnie zbliżone do pożądanego zachowania, skopiowanie ich i dostosowanie.
Zaleca się gromadzenie własnej zawartości w nowym pliku w podkatalogu `user`.


Krótka uwaga na temat tytułów, nazwisk itp.: zostały one celowo zmienione na potrzeby gry - chyba że i tak są fikcyjne - aby uniknąć problemów prawnych.
Jednak niektóre identyfikatory baz danych filmów i oryginalne nazwy zostały zapisane w bazie danych TVTower, aby ułatwić wyszukiwanie, rozpoznawanie i unikanie duplikatów.

W wersji 0.8.3 nastąpiła poważna reorganizacja w odniesieniu do [variables](variables.md).
Przyszłe wersje nie będą już obsługiwać starego formatu, a niestandardowe pliki baz danych muszą zostać przekonwertowane na nowy format.
Instrukcje dotyczące konwersji są podsumowane w [Migration-Guide](dbmigration.md).

## Podstawowa struktura pliku bazy danych TVTower

```XML
<?xml version="1.0" encoding="utf-8"?>
<tvtdb>
	<version value="3" comment="optionaler Kommentar"/>
	<!-- nun folgen die eigentlichen Daten-->

	<!-- Nachrichten -->
	<allnews>
		...
	</allnews>

	<!-- Werbung -->
	<allads>
		...
	</allads>

	<!-- Programme -->
	<allprogrammes>
		...
	</allprogrammes>

	<!-- usw.-->
</tvtdb>
```

Po nagłówku XML, wszystkie elementy są osadzone w tagu `tvtdb`.
Po węźle dla informacji o wersji następuje możliwa lista podrzędna.
Każda lista podrzędna może - ale nie musi - występować w pliku.
Niniejsza dokumentacja opisuje format aktualnie używanej bazy danych w wersji 3.

### Elementy_podrzędne_tvtdb

Poniższa tabela zawiera wszystkie możliwe główne węzły bazy danych.
Struktura ich elementów podrzędnych jest udokumentowana osobno.

| Tag | Link zur Dokumentation |
| --- | ---------------------- |
| allads | [Reklama](ads.md) |
| allnews | [Wiadomości](news.md) |
| allachievements | [Osiągnięcia](achievements.md) |
| allprogrammes | [Programy](programmes.md)
| scripttemplates | [Szablony scenariuszy](scripts.md)
| celebritypeople | [Główne postacie](persons.md#Hauptpersonen) - z dużą ilością przechowywanych danych |
| insignificantpeople | [Postacie drugoplanowe](persons.md#Nebenpersonen) - tylko z najbardziej niezbędnymi danymi|
| programmeroles | [Role w filmie](persons.md#Filmrollen)|

Każdy z tych głównych węzłów jest opcjonalny, tj. plik bazy danych może zawierać tylko reklamy lub wszystkie dane.

## Nazwy specyficzne dla języka

Tytuły i opisy są tłumaczone bezpośrednio w odpowiedniej strukturze bazy danych.
Format bazy danych dla osób i ról nie pozwala na to w ten sam sposób.
Jeśli tłumaczenia są wymagane w indywidualnych przypadkach, mogą być przechowywane w [oddzielnych plikach](lang.md).

## Struktury używane przez kilka elementów

Niektóre właściwości lub podstruktury podrzędne występują w różnych miejscach.
Poniższe opisy są następnie przywoływane z innych miejsc w dokumentacji.

### Właściwości standardowe

#### guid

`guid` to właściwość, za pomocą której element jest jednoznacznie identyfikowany globalnie.
Pomocnym schematem dla unikalności jest `author-type-title` (np. `jim-news-homerun` lub `david-programme-yfiles-season1-episode3`).

Technicznie rzecz biorąc, istnieje rozróżnienie między numerycznym identyfikatorem wewnętrznym programu a tekstowym identyfikatorem GUID.
Identyfikatory GUID są zdefiniowane w bazie danych i zazwyczaj są one przywoływane, ponieważ identyfikator techniczny nie jest znany w bazie danych.

#### creator

`creator` jest opcją, właściwością informacyjną, która identyfikuje twórcę (lub twórców) wpisu.
Używany jest tutaj identyfikator forum.
Przykład: `... creator="5578" ... `

#### created_by

`created_by` jest opcjonalną właściwością, która zawiera czytelną nazwę twórcy.
W konfiguracji `DEV.xml`, która jest używana do rozpoczęcia nowej gry, można ograniczyć, które elementy mają być wczytane lub wykluczone przez którego twórcę.
Przykład: `... created_by="Ronny" ...`

#### comment

`comment` jest opcjonalną, informacyjną właściwością, w której można wprowadzić komentarz.
Przykład: `... comment="przyszło mi do głowy podczas brania prysznica" ...`

#### fictional

`fictional` jest wartością prawdy i wskazuje, czy jest to fikcyjny wpis.
Możliwe wartości to `1` (tak fikcyjny) lub `0` (nie prawdziwy).
Przykład: `... fictional="1" ...`

W niektórych przypadkach informacje te są raczej informacyjne, w innych mają wpływ na zachowanie gry (np. brak randomizacji dat urodzenia prawdziwych osób).

#### tmdb_id

`tmdb_id` to identyfikator programu lub osoby w bazie danych filmów. [Baza danych filmów](https://www.themoviedb.org/).

#### imdb_id

`imdb_id` to identyfikator programu lub osoby w bazie danych filmów [IMDb](https://www.imdb.com/).

### Struktura wpisów "Język"

W przypadku danych w różnych językach odpowiednie tłumaczenia są określane jako elementy podrzędne węzła głównego.
Ogólnie rzecz biorąc, wpis wygląda następująco:

```XML
<tag>
	<sprache1>Text in Sprache 1</sprache1>
	<sprache2>Tekst w języku 2</sprache2>
</tag>
```

lub na przykładzie tytułu filmu

```XML
<title>
	<de>Die Locken Horror Show</de>
	<en>The curly horror show</en>
	<pl>Horror z kręconymi włosami</pl>
</title>
```

Obecnie używane języki to niemiecki (de), angielski (en) i polski (pl).
Jednak nie musi tak być w dłuższej perspektywie.
Wpisy językowe mogą również zawierać zmienne - ale są one opisane w [oddzielnej sekcji](variables.md).

Seit der Umstellung ab Version 0.8.3 auf die neue Variablensyntax (`${...}` statt `%...%`) sind Alternativen (`Variante 1|Variante 2`) nur noch in Variablendefinitionen und nicht mehr direkt im Titel der in der Beschreibung erlaubt.

### Standardowe elementy

#### title

Węzeł `title` zawiera tytuły skryptów, filmów itp.
Obsługiwane są różne języki i [zmienne](variables.md).

```XML
<title>
	<de>Reise nach ${WHERE}</de>
	<en>Voyage to ${WHERE}</en>
	<pl>Podróż do ${WHERE}</pl>
</title>
```

Jeśli tytuł ma być całkowicie identyczny we wszystkich językach, można użyć skróconej pisowni bez indywidualnych znaczników językowych.

```XML
<title>[li3o9n8e0l1]</title>
```

Uwaga: Jeśli w grę wchodzą zmienne, które mają dostarczać różne wartości dla różnych języków, można użyć skrótu **not**.
`<title>${showname}</title>` zwróci tę samą wartość we wszystkich językach, nawet jeśli definicja zmiennej zawiera tłumaczenia.
W tym przypadku należy użyć wariantu szczegółowego.

```XML
<title>
	<de>${showname}</de>
	<en>${showname}</en>
	<pl>${showname}</pl>
</title>
```

#### description

Atrybut `description` zawiera opis. Przykład:

```XML
<description>
	<de>Wie analysiere ich die Industriekraft...</de>
	<en>How to analyse the industrial power...</en>
	<pl>Jak analizować potęgę przemysłową...</pl>
</description>
```

Uwagi dotyczące [zmiennych](variables.md) i skrótów również mają tutaj zastosowanie, podobnie jak w przypadku tytułu.

#### text

Atrybut `text` zawiera tekst.
Obsługiwane są również różne języki i [zmienne](variables.md).

#### availability

Zobacz [Dostępność](time.md#Dostępność) w opisie definicji czasu.

#### targetgroupattractivity

Współczynnik atrakcyjności (od 0 do 2) może być określony dla poszczególnych grup docelowych.
Przyrostek `_male` i `_female` w grupie docelowej może być również użyty do ograniczenia grupy docelowej do przedstawicieli płci męskiej / żeńskiej.
Nazwy grup docelowych to: `teenagers`, `managers`, `housewives`, `employees`, `women`, `men`, `pensioners`, `unemployed`.

Przykład: `<targetgroupattractivity teenagers_male="0.7" pensioners="1.6" />` - Mniej atrakcyjne dla młodych mężczyzn, bardziej atrakcyjne dla emerytów.

Atrakcyjność grupy docelowej obliczona na podstawie podstawowych wartości dla gatunku, czasu itp. jest następnie mnożona przez tę wartość.
Należy zauważyć, że sama atrakcyjność nie determinuje liczby widzów.
Jeśli współczynnik jest ustawiony na 0, nie oznacza to, że nie będzie żadnych widzów w tej grupie, tylko znacznie mniej.

#### modifiers

W głównym atrybuie `modifiers` można określić listę elementów `modifier`, które mogą definiować różne dostosowania w zależności od węzła nadrzędnego.
Każdy `modifier` ma nazwę `name` i wartość `value`, które określają co jest dostosowywane i w jaki sposób.

```XML
<modifiers>
	<!-- starzeje się szybciej niż zwykle -->
	<modifier name="topicality::age" value="1.5" />
	<!-- Taniej niż zwykle -->
	<modifier name="price" value="0.7" />
</modifiers>
```

Obsługiwane modyfikatory zależą od głównego elementu.
Należy zauważyć, że 0 nie zawsze daje "0" jako wynik, ponieważ w obliczeniach mogą być używane wartości minimalne.

#### effects

Lista elementów `effects` może być określona w głównym węźle `effects`, który może definiować różne dostosowania w zależności od węzła nadrzędnego.

Następujące właściwości mogą być zdefiniowane dla wszystkich typów efektów:

| Nazwa | Typ | Opis |
| ---- | --- |------------- |
| trigger | Wymagane | patrz poniżej |
| type | Wymagane | Zobacz poniżej możliwe wartości; najczęściej "triggernews" - wyzwalacz wiadomości uzupełniającej |
| time | opcjonalny | Kiedy ma miejsce efekt; format - patrz [Kontrola czasu](time.md#Zeitattribute) |
| probability | opcjonalny | Prawdopodobieństwo wystąpienia tego efektu |

Węzeł `effect` zawsze posiada właściwość `trigger`, która kontroluje warunek, w którym efekt występuje.
Pozostałe pola zależą od typu efektu `type`.
time` jest używany w szczególności do wyzwalania wiadomości uzupełniających, ale może być również używany do kontroli dostępności.
Najpopularniejsze warianty kontroli czasu to 1 (`"1,3,7"` - w ciągu 3 do 7 godzin), 2 (`"2,1,2,6,14"` - w ciągu 1 do 2 dni między 6 rano a 2 po południu).
"Prawdopodobieństwo" wynosi od 0 do 100 (jeśli nie jest zdefiniowane, przyjmuje się 100).


##### trigger

Właściwość "trigger" ma stały zakres wartości w zależności od głównego elementu (komunikaty, programy itp.).
Typowe wartości to

* `happen`- efekt pojawia się w każdym przypadku (obecnie jest uruchamiany tylko wtedy, gdy pojawiają się wiadomości)
* `broadcast` - efekt występuje na początku *każdej* emisji
* `broadcastDone` - efekt występuje pod koniec *każdej* emisji
* `broadcastFirstTime` - efekt występuje na początku pierwszej emisji
* `broadcastFirstTimeDone` - efekt występuje pod koniec pierwszej emisji
* `productionStart` - efekt występuje na początku produkcji w studio

Przykład: `... trigger="happen" ... `

##### `type="triggernews"`

Uruchomiona zostanie wiadomość uzupełniająca A*.
Wartość `news` (obowiązkowa dla tego typu) zawiera identyfikator GUID wywołanej wiadomości uzupełniającej.

`<effect trigger="happen" type="triggernews" news="ronny-news-drucktaste-02b1" />`

Ponieważ można zdefiniować listę efektów, można oczywiście uruchomić kilka kolejnych wiadomości.

##### `type="triggernewschoice"`

Aby włączyć różne sekwencje w łańcuchach komunikatów, można użyć tego typu efektu do wyzwolenia *jednego* z wymienionych komunikatów.
Dla każdego komunikatu można określić prawdopodobieństwo.

`<effect trigger="happen" type="triggernewschoice" choose="or" news1="newsId1" probability1="30" news2="newsId2 probability2="70" />`

Zgodnie z kodem źródłowym `Init:TGameModifierNews_TriggerNews`, można również określić różne czasy wyzwalania (`time1...timeX`).
Jednak obecnie nie jest to wykorzystywane (powrót do tego samego czasu `time` dla wszystkich kolejnych wiadomości).

##### `type="modifyPersonPopularity"`

Popularność osoby, do której się odwołujemy, jest dostosowywana.

* `<effect trigger="happen" type="modifyPersonPopularity" guid="personId" valueMin="0.1" valueMax="0.2" />` - 
popularność osoby z identyfikatorem GUID personId jest dostosowywana o wartość od 0,1 do 0,2 niezależnie od emisji wiadomości.
* `<effect trigger="broadcast" type="modifyPersonPopularity" guid="personId" valueMin="0.02" valueMax="0.05" />` - 
popularność osoby z identyfikatorem GUID personId jest dostosowywana o wartość od 0,02 do 0,05 za każdym razem, gdy wiadomość jest nadawana.

##### `type="modifyMovieGenrePopularity"`

Popularność określonego gatunku jest dostosowywana.

* `<effect trigger="happen" type="modifyMovieGenrePopularity" genre="13" valueMin="0.5" valueMax="2.0" />`- die Beliebtheit von Monumentalfilmen jest dostosowywana o wartość od 0,5 do 2, niezależnie od nadawanego komunikatu.
* `<effect trigger="broadcastFirstTime" type="modifyMovieGenrePopularity" genre="3" valueMin="0.2" valueMax="0.7" />`- popularność filmów animowanych jest korygowana o wartość od 0,2 do 0,7, gdy wiadomość jest emitowana po raz pierwszy.

##### `type="modifyNewsAvailability"`

Status dostępności wiadomości jest dostosowywany.

* `<effect trigger="happen" type="modifyNewsAvailability" enable="1" news="ronny-news-drucktaste-1" />`- właściwość `available` (dostępny) wiadomość z GUID "ronny-news-print-button-1" jest ustawiona na Tak.
* `<effect trigger="happen" type="modifyNewsAvailability" enable="0" news="ronny-news-drucktaste-1" />`- właściwość `available` (dostępny) wiadomości z GUID "ronny-news-print-button-1" jest ustawiona na Nie.

##### `type="modifyProgrammeAvailability"`

Status licencji programu został skorygowany.

* `<effect trigger="broadcastFirstTime" type="modifyProgrammeAvailability" enable="1" guid="ronny-programme-livereportage-raketenstart1" time="1,48,96" />`- 48 do 96 godzin po rozpoczęciu pierwszej transmisji, właściwość `available` (dostępny) licencji z GUID "ronny-programme-livereportage-rocket-launch1" jest ustawiona na Yes. Można również pominąć `enable="1"`. Jeśli atrybut nie jest ustawiony, automatycznie przyjmuje się, że jest to "yes".

* `<effect trigger="broadcastFirstTimeDone" type="modifyProgrammeAvailability" enable="0" guid="ronny-programme-livereportage-raketenstart1" />`- Pod koniec pierwszej transmisji właściwość `available` (dostępny) licencji z GUID "ronny-programme-livereportage-raketenstart1" jest ustawiona na No.

##### `type="modifyScriptAvailability"`

Status szablonu skryptu jest dostosowywany.

* `<effect trigger="broadcast" type="modifyScriptAvailability" enable="1" guid="scripttemplate-ron-musiksterneamabend" />`- Na początku każdej transmisji, właściwość `available` (dostępny) szablonu skryptu z GUID "scripttemplate-ron-musiksterneamabend" jest ustawiona na Yes. Można również pominąć `enable="1"`. Jeśli atrybut nie jest ustawiony, automatycznie przyjmuje się, że jest to "yes".

* `<effect trigger="broadcastDone" type="modifyScriptAvailability" enable="0" guid="scripttemplate-ron-musiksterneamabend" />`- Pod koniec każdej transmisji właściwość `available` (dostępny) szablonu skryptu z GUID "scripttemplate-ron-musiksterneamabend" jest ustawiona na "No".

* `<effect trigger="productionStart" type="modifyScriptAvailability" enable="0" guid="scripttemplate-ron-musiksterneamabend" />`- Na początku tworzenia skryptu, dla którego zdefiniowano ten efekt, szablon skryptu z identyfikatorem GUID "scripttemplate-ron-musiksterneamabend" jest ustawiony na niedostępny.

##### `type="modifyBettyLove"`

Punkty czułości Betty są regulowane.
Wewnętrznie wartość 100 odpowiada jednemu procentowi, więc 25 to 0,25%, a -123 to -1,23%.

* `<effect trigger="broadcast" type="modifyBettyLove" valueMin="25" valueMax="50" />`- Z każdą emisją czułość wzrasta o wartość od 0,25% do 0,5%.

* `<effect trigger="broadcastFirstTimeDone" type="modifyBettyLove" valueMin="-100" valueMax="-100" />`- uczucie zmniejsza się dokładnie o 1% przy pierwszej emisji.

Należy zauważyć, że efekt ten działa jako dodatek do automatycznych dostosowań dokonywanych przez grę.
Flaga emisji 2048 (ignorowana przez Betty) (tylko) wyłącza automatyczne dostosowanie, flaga nie ma wpływu na samodzielnie zdefiniowane efekty.

### Variablen

Wraz z konwersją rozdzielczości zmiennej i rozszerzeniem na ewaluację funkcji, temat ten zyskuje własną postać [Hauptkapitel](variables.md).

## Standardwertebereiche

Składniowo wartości właściwości są zawsze ciągami znaków ujętymi w podwójne cudzysłowy.
Aby jednak wartość była poprawna, może podlegać dalszym ograniczeniom.
Możliwe ograniczenia obejmują 

* Stałe listy wartości, takie jak
    * "1", "2" lub "3"
    * "reachAudience", "money"
    * Wartości prawdy - "0" dla "nie", "1" dla "tak".
* Typy danych
    * liczby naturalne (
    * Współczynnik: Liczba z miejscami dziesiętnymi wokół 1 ("0.7", "1", "1.00", "1.3")
* identyfikatory GUID zdefiniowane w innym miejscu bazy danych
* Flagi, tj. liczby naturalne, w których każdy bit w reprezentacji binarnej ma specjalne znaczenie. Liczba reprezentuje kombinację właściwości aktywowanych bitów.
* [Atrybuty czasu](time.md)

Poniższe sekcje zawierają listę zakresów wartości używanych przez kilka elementów.
W kodzie źródłowym są one zdefiniowane w `game.gameconstants.bmx`.

### Gatunek

| Wartość | Znaczenie |
| ---- | --------- |
| 0 | Inne |
| 1 | Przygodowy |
| 2 | Akcja |
| 3 | Film animowany |
| 4 | Kryminał |
| 5 | Komedia |
| 6 | Dokument |
| 7 | Dramat |
| 8 | Erotyczny |
| 9 | Familijny |
| 10 | Fantasy |
| 11 | Historyczny |
| 12 | Horror |
| 13 | Monumentalny |
| 14 | Tajemniczy |
| 15 | Film miłosny - Romans |
| 16 | SciFi |
| 17 | Thriller |
| 18 | Western |
| 100 | Show |
| 101 | Rozmowy polityczne |
| 102 | Program muzyczny |
| 103 | Talkshow |
| 104 | Teleturniej |
| 200 | Wydarzenie |
| 201 | Polityka |
| 202 | Muzyka i śpiew |
| 203 | Sport |
| 204 | Program plotkarski |
| 300 | Reportaż |
| 301 | Bulwar |
| 400 | Infomercial |
| 401 | Specjalny program informacyjny |

(Kod źródłowy: `TVTProgrammeGenre`)

### Typ programu

| Wartość | Znaczenie |
| ---- | --------- |
| 0 | undefiniert |
| 1 | Film |
| 2 | Serie |
| 3 | Show |
| 4 | Feature (Reportage) |
| 5 | Infomercial (Dauerwerbesendung) |
| 6 | Event |
| 7 | Sonstiges |

(Quellcode: `TVTProgrammeProductType`)

### Flagi programu

Flagi programu są wartością flagi, tzn. kilka wartości może być zakodowanych w jednej liczbie.
W tym celu wartości są sumowane.

| Wartość | Znaczenie | Wpływ |
| ---- | --------- |----------- |
| 1 | Program na żywo | bonus ogólny |
| 2 | Film animowany | Bonus dla dzieci / młodzieży. Kara dla emerytów / menedżerów. |
| 4 | Kultura | Bonus z Betty i z menedżerami |
| 8 | Kultowy | wiek filmu ma mniejszy negatywny wpływ, premia dla emerytów, wyższa lojalność wobec serii |
| 16 | Śmieciowy | Premia dla bezrobotnych i gospodyń domowych. Kara dla pracowników i menedżerów. Premia rano i w porze lunchu |
| 32 | B-Movie | Znacznie niższa cena, wiek filmu ma mniejszy negatywny wpływ, bonus dla młodych ludzi, malus dla wszystkich innych, bonus w	nocy |
| 64 | FSK 18 | Bonus dla młodych ludzi, pracowników, bezrobotnych (mężczyzn). Niewielka kara dla dzieci, gospodyń domowych, emerytów (kobiety) |
| 128 | Pokazy telefoniczne | |
| 256 | Serie | |
| 512 |"umieszczony" | |
| 1024 | wyprodukowane w grze | |
| 2048 | niewidoczny | nie jest wyświetlany w narzędziu do planowania programu |
| 4096 | RE-Live | Program na żywo emitowany później |

(Kod źródłowy: `TVTProgrammeDataFlag`)

`flags="12"` opisałby kultowy program kulturalny.

### Typ licencji

| Wartość | Znaczenie |
| ---- | --------- |
| 0 | nieznany |
| 1 | Pojedyncza licencja |
| 2 | Odcinek serialu |
| 3 | Serial |
| 4 | Kolekcja |
| 5 | Element kolekcji |
| 6 | Franczyza |

(Kod źródłowy: `TVTProgrammeLicenceType`)

Kolekcja: Pakiet licencji - ale nie innych indywidualnych licencji na programy.
Kolekcja "the ultimate Betty collection" może zawierać wpisy jako elementy podrzędne, które odnoszą się do programów z Betty jako główną bohaterką.

Franczyza: Filmy/seriale tego samego "bandwagonera" ("Spa Wars")

Typy 4, 5 i 6 nie powinny być obecnie używane, ponieważ nadal mogą tu wystąpić zmiany.

### Flagi_licencyjne

Flagi licencyjne są wartością flagi, tzn. kilka wartości może być zakodowanych w jednej liczbie.
W tym celu wartości są sumowane.

| Wartość | Znaczenie |
| ---- | --------- |
| 1 | może być przedmiotem obrotu |
| 2 | Automatyczna sprzedaż po osiągnięciu limitu emisji |
| 4 | Automatyczne usuwanie po osiągnięciu limitu emisji  |
| 8 | Liczba transmisji jest resetowana po powrocie do sprzedawcy (po osiągnięciu limitu). |
| 16 | Rzeczywistość jest resetowana do wartości maksymalnej po zwróceniu do sprzedawcy |
| 32 | program nie może zostać zakupiony ponownie po zwróceniu go do sprzedawcy |

(Kod źródłowy: `TVTProgrammeLicenceFlag`)

`licence_flags="37"` byłaby początkowo licencją zbywalną, ale po osiągnięciu maksymalnej liczby transmisji byłaby automatycznie zwracana sprzedawcy bez zwrotu kosztów i nie mogłaby zostać ponownie zakupiona.

### Flagi_transmisji

Flagi emisji są wartością flagi, tzn. kilka wartości może być zakodowanych w jednej liczbie.
W tym celu wartości są sumowane.

| Wartość | Znaczenie |
| ---- | --------- |
| 0 | nieznany |
| 1 | Materiały stron trzecich |
| 2 | nie do kontrolowania |
| 4 | Pierwsza transmisja  |
| 8 | Specjalna pierwsza transmisja |
| 16 | Pierwsza transmisja |
| 32 | odbywa się specjalna pierwsza transmisja |
| 64 | niedostępny |
| 128 | Ukryj cenę |
| 256 | aktywowana ograniczona częstotliwość nadawania |
| **512** | zawsze Live |
| 1024 | Poziom trudności jest ignorowany |
| **2048** | ignorowany przez Betty|
| 4096 | Zignorowane przez sukcesy |
| 8192 | Wyłącznie dla jednego gracza |
| 16384 | przestarzałe - (czas na żywo jest stały) |
| **32768** | Utrzymanie ograniczenia czasu nadawania |

(Kod źródłowy: `TVTBroadcastMaterialSourceFlag`)

Większość nadawanych flag może być używana tylko w ramach programu.
Jednak niektóre z nich są również interesujące dla definicji w bazie danych.
Domyślnie limit czasu emisji dotyczy tylko pierwszej emisji.
Jeśli ma on również dotyczyć kolejnych emisji, flaga 32768 musi być również ustawiona.

Flaga 2048 (ignorowana przez Betty) ma wpływ tylko na obliczoną korektę w grze.
Samodzielnie zdefiniowane efekty dostosowania punktów Betty występują w każdym przypadku.


### Płeć

| Wartość | Znaczenie |
| ---- | --------- |
| 0 | nieokreślony |
| 1 | Mężczyzna |
| 2 | Kobieta |

(Kod źródłowy: `TVTPersonGender`)

### Praca

Zawód jest wartością flagową, tzn. kilka zawodów może być zakodowanych w jednym numerze.
Wartości odpowiednich zawodów są sumowane.

| Wartość | Znaczenie |
| ---- | --------- |
| 0 | nieznany |
| 1 | Reżyser |
| 2 | Aktor |
| 4 | Scenarzysta |
| 8 | Moderator/gospodarz |
| 16 | Muzyk |
| 32 | Aktor drugoplanowy |
| 64 | Gość |
| 128 | Reporter |
| 256 | Polityk |
| 512 | Malarz |
| 1024 | Autor |
| 2048 | Model |
| 4096 | Sportowiec |

(Kod źródłowy: `TVTPersonJob`)

`job="18"` oznaczałoby zatem aktora i muzyka.

### Kraje

Następujące kraje są obecnie uwzględnione w bazie danych (kraje pochodzenia osób, kraje, w których wyprodukowano programy).
Należy pamiętać, że wartości tych nie należy mylić ze skrótami językowymi.

| Skrót | Kraj |
| ------ | ---- |
| A | Austria |
| AFG | Afghanistan |
| AM | Armenia |
| AUS | Australia |
| B | Belgia |
| BG | Bulgaria |
| BIH | Bośnia i Hercegowina |
| BM | Bermuda |
| BOL | Boliwia |
| BR | Brazylia |
| BW | Botswana |
| C| Kuba |
| CDN | Kanada |
| CH | Szwajcaria |
| CHN | China |
| CL | Sri Lanka |
| CO | Kolumbia |
| CS | CSSR |
| CZ | Republika Czeska |
| D | Niemcy |
| DDR | DDR |
| DK | Dania |
| E | Hiszpania |
| F | Francja |
| FL | Liechtenstein |
| GB | Wielka Brytania |
| GH | Ghana |
| GR | Grecja
| H | Węgry |
| HK | Hongkong |
| HR | Chorwacja |
| I | Włochy |
| IL | Izrael |
| IND | Indie |
| IRL | Irlandia|
| J | Japonia |
| KN | Grenlandia |
| KSA | Arabia Saudyjska |
| L | Luxemburg |
| LT | Litwa |
| M | Malta |
| MA | Maroko |
| MEX | Meksyk |
| N | Norwegia |
| NL | Holandia |
| NZ | Nowa Zelandia |
| P | Portugalia |
| PA | Panama |
| PE | Peru |
| PL | Polska |
| RA | Argentyna |
| RC | Taiwan |
| RM | Republika Molwanii |
| RO | Rumunia |
| ROK | Korea Południowa |
| RP | Philippinen |
| RUS | Rosja |
| S | Szwecja |
| SCO | Schottland |
| SU | ZSSR |
| T | Tajlandia |
| TN | Tunezja |
| TR | Turcja |
| USA | USA |
| YU | Jugosławia|
| ZA | Republika Południowej Afryki |
| ZW | Zimbabwe |

Podstawą standaryzacji czyszczenia bazy danych była lista tablic rejestracyjnych (https://de.wikipedia.org/wiki/Liste_der_Kfz-Nationalit%C3%A4tszeichen).
W przypadku koprodukcji kraje są oddzielone ukośnikiem i bez spacji (`F/CDN`).

### Zielgruppe

Grupa docelowa jest wartością flagową, tzn. kilka grup docelowych może być zakodowanych w jednym numerze.
Wartości odpowiednich grup są sumowane.

| Wartość | Znaczenie |
| ---- | --------- |
| 0 | wszystko |
| 1 | Dzieci |
| 2 | Nastolatki |
| 4 | Gospodynie domowe - "Kury domowe"|
| 8 | Pracownicy |
| 16 | Bezrobotny |
| 32 | Menedżer |
| 64 | Emeryt |
| 128 | Kobiety |
| 256 | mężczyźni |

(Kod źródłowy: `TVTTargetGroup`)

`target_group="65"` obejmowałyby zatem dzieci i emerytów.

Jeśli grupa jest zdefiniowana jako grupa docelowa (np. dla reklam lub programów), nieco wyższa wartość atrakcyjności jest przyjmowana jako normalna podstawa przy obliczaniu liczby widzów dla tej grupy.

### Lobbygruppe

Grupa lobby jest wartością flagową, tzn. kilka grup lobby może być zakodowanych w jednym numerze.
Wartości odpowiednich grup są sumowane.

| Wert | Bedeutung |
| ---- | --------- |
| 0 | brak |
| 1 | Palacze |
| 2 | Niepalący |
| 4 | Lobby broni |
| 8 | Pacyfiści |
| 16 | Kapitaliści |
| 32 | Komuniści |

(Kod źródłowy: `TVTPressureGroup`)

`pro_pressure_group="9"` byliby palacze i pacyfiści.

## allgemeiner Aufbau eines Elements

```XML
<tag eigenschaft1="Wert1" eigenschaft2="Wert2">
	<kindTag1 e1="w1" w2="w2" />
	<kindTag2 e="w">
		<enkelTag />
		<enkelTag />
	</kindTag2>
</tag>
```

Tag (lub węzeł) zaczyna się od nawiasu otwierającego i nazwy tagu (`<tagname ...`).
Po tym następuje lista właściwości z wartością (`... e1="w1" e2=w2"...`), przy czym możliwe właściwości i zakresy wartości zależą od tagu.
Właściwości mogą być obowiązkowe lub opcjonalne - w pierwszym przypadku muszą być określone, w drugim mogą być określone lub pominięte.
Jeśli znacznik nie zawiera żadnych elementów podrzędnych, można go zamknąć bezpośrednio (`.../>`).
Oznacza to, że po nawiasie otwierającym następuje ukośnik po nazwie i właściwościach, a następnie nawias zamykający.
Jeśli elementy podrzędne są obecne, znacznik jest najpierw zamykany nawiasem zamykającym (`...>`), następnie elementy podrzędne, a cały znacznik jest kończony znacznikiem zamykającym (`</tagname>`).

Węzły podrzędne są wcięte dla lepszej czytelności.
Węzły nadrzędne określają, czy węzeł podrzędny jest opcjonalny (nie musi wystąpić) czy obowiązkowy (musi wystąpić) oraz czy może wystąpić co najwyżej raz (pojedynczy węzeł podrzędny) czy wiele razy (lista).
W przypadku listy może zatem istnieć kilka znaczników o tej samej nazwie.

## Zadania do wykonania i pytania

### Dokumentation

* zaznaczyć typowe flagi pogrubioną czcionką?
* modyfikatory są bardzo ogólne; jaki jest najlepszy sposób na wyciągnięcie dostępnych modyfikatorów?

### Generell

* Gatunek 401 nie ma jeszcze żadnej lokalizacji. Czy jest to w ogóle uwzględnione w kodzie?
