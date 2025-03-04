# Zmienne_i_wywołania_funkcji

Przetwarzanie zmiennych i innych dynamicznych treści zostało zmienione w wersji 0.8.3.
Celem było osiągnięcie bardziej znormalizowanej składni i większej elastyczności w tym samym czasie.
Następujące podstawowe koncepcje nadal istnieją

* Własne definicje zmiennych
* Alternatywy w szablonach, z których jedna jest wybierana (np. dla określonej wiadomości)
* Dynamiczna zawartość dostarczana przez grę

Dodano następujące elementy

* Wykorzystanie warunków nie tylko w skrypcie dostępności, ale wszędzie tam, gdzie zmienne są dozwolone.
* Funkcje umożliwiające dostęp do innych elementów bazy danych (np. odniesienie do osób, które nie są częścią obsady)
* Funkcje pozwalające na bardziej kompaktową notację dynamicznej zawartości
* [Zmienne globalne](lang.md) dla możliwości ujednoliconego nazewnictwa bez wielokrotnych definicji (lub zduplikowanych zwykłych tekstów).



Głównym zastosowaniem zmiennych jest tworzenie wariancji w tekstach (wiadomościach, skryptach), ale także odwoływanie się do osób, na przykład bez trwałego przechowywania ich nazw w tekstach.
Może to być przydatne na przykład w przypadku wprowadzania zmian w definicjach osób lub ról w bazie danych.
Tytuły lub opisy filmów nie muszą być wówczas odpowiednio korygowane.
Zazwyczaj zmienne są używane we wszystkich miejscach, w których występują teksty specyficzne dla danego języka.



```XML
...
	<title>
		<de>Es tanzt ${animal}</de>
		...
	</title>
...
	<variables>
		<animal>
			<de>der Bär|die Maus</de>
			...
		</animal>
	</variables>
...
```

## Podstawy_składni

Ponieważ nie mamy już do czynienia z prostymi zmiennymi i dostępem do wartości z gry za pomocą stałych, mówimy o *wyrażeniach*.
Podstawową strukturą wyrażenia, która jest oceniana tylko w czasie gry, jest `${do oceny}`.
Zaczyna się od `${` i kończy `}`.
Tak jak w powyższym przykładzie, `do oceny` może być nazwą samodzielnie zdefiniowanej zmiennej lub może mieć bardziej złożoną strukturę, np. zawierać samo wyrażenie.



* `${simpleVariable}`
* `${variablenPraefix_${suffixFirstEvaluated}}`
* `${.funktionsName:parameter1:parameter2...}`

### Definicja_zmiennej

Wiele struktur bazy danych pozwala na definiowanie zmiennych, np. w celu zapewnienia większej różnorodności tekstów i opisów.
Same zmienne i ich możliwe przypisania są zdefiniowane w głównym węźle `variables`, przy czym dla każdej zmiennej dozwolonych jest kilka wariantów językowych.
Różne opcje zastąpienia zmiennej są oddzielone pionowymi liniami `|`.


```XML
	<variables>
		<animal>
			<de>der Bär|die Maus|das Kamel</de>
			<en>the bear|the mouse|the camel</en>
			<pl>niedźwiedź|mysz|wielbłąd</pl>
		</animal>
		<rndcity>${.stationmap:"randomcity"}</rndcity>
		<city>Berlin|Bonn|Trier|${.stationmap:"randomcity"}</city>
		<name>
			<all>Peter|Paul|Mary</all>
		</name
	</variables>
```

W tym przykładzie zdefiniowano cztery zmienne: `animal`, `rndcity`, `city` i `name`.
Zazwyczaj w definicji znajdują się znaczniki dla różnych języków, dzięki czemu można tworzyć teksty specyficzne dla danego języka.
Dla `animal` istnieje niemiecki, angielski i polski wariant.
Definicja ta zawiera alternatywy (`wariant 1|wariant 2|wariant 3`), które są oddzielone przez `|`.
W czasie ewaluacji liczba jest rzucana raz dla zmiennej (w zależności od liczby alternatyw), a następnie używana dla wszystkich języków.
Puste alternatywy są dozwolone (`<en>||big </en>` - przymiotnik pojawiłby się tylko w jednej trzeciej przypadków).
Tak więc, jeśli wyrzucono 2, wartością `animal` będzie `die Maus` w języku niemieckim i `the mouse` w języku angielskim i `mysz` w języku polskim.



Jeśli jednak tekst powinien być zawsze dokładnie taki sam dla wszystkich języków, znacznik języka można pominąć od wersji 8.3.0.
`<rndcity>${.stationmap: "randomcity"}</rndcity>` czyni unikalnie wygenerowaną nazwę miasta dostępną dla wszystkich języków (dla funkcji dostarczanych przez grę, zobacz poniżej) pod zmienną `rndcity`.

Dla `name` określony język to `all`.
Jest to skrót dla kopii tego samego wpisu dla wszystkich języków, dla których istnieją oficjalne tłumaczenia bazy danych (obecnie angielski, niemiecki i polski).
Ale po co używać `all`, skoro nie ma żadnych zmiennych, więc wynik i tak byłby identyczny dla wszystkich języków?
W pewnym momencie można dodać język, w którym jedna z nazw ma inną pisownię.
W takim przypadku można po prostu dodać kolejną definicję języka bez konieczności zmiany struktury wpisu w wykazie.



Definicje zmiennych mogą oczywiście same zawierać odniesienia do innych zmiennych.
Oczywiście nie mogą występować cykle (v1 zależy od oceny v2, a v2 zależy od oceny v1).

### Proste_zmienne

W najprostszym przypadku, zmienna zdefiniowana w ten sposób jest dostępna poprzez wyrażenie `${variablenname}`.
Dla zmiennych zdefiniowanych powyżej byłyby to wyrażenia `${animal}`, `${rndcity}` i `${city}`.
Mogą one być używane w tytule, opisie, ale także w innych definicjach zmiennych.
Przed określeniem wartości zmiennej, wszystkie wyrażenia w definicji są najpierw w pełni oceniane.
(Definicje zmiennych nie mogą zatem odnosić się do siebie nawzajem).



### Ważna uwaga dotycząca skopiowanych wpisów językowych

Jeśli na przykład tytuł skryptu ma być generowany losowo i obsługiwać kilka wariantów, można użyć następującego schematu:

```XML
...
	<title>
		<de>${theTitle}</de>
		<en>${theTitle}</en>
		<pl>${theTitle}</pl>
	</title>
...
	<variables>
		<theTitle>
			<de>Die Saga von ...|Das Geheimnis von ...</de>
			<en>The Saga of ...|The Secret of ...</en>
			<pl>Saga o ...|Sekret ...</pl>
		</theTitle>
	</variables>
...
```

Nawet jeśli wpisy językowe dla `title` są takie same dla wszystkich języków i składają się tylko z odniesienia do zmiennej, nie można użyć skróconej notacji `<title>${theTitle}</title>`.
W tym przypadku wszystkie języki otrzymałyby ten sam tytuł - wyrażenie jest obliczane tylko raz, a następnie używane dla wszystkich języków.
Aby uzyskać skróconą notację, można użyć tagu języka `all` i napisać go zamiast tego:



```XML
	<title>
		<all>${theTitle}</all>
	</title>
```

Kopia wpisu jest tworzona tutaj dla wszystkich (obsługiwanych) języków.

Z tego samego powodu nie można użyć następującej definicji zmiennej:

```XML
	<variables>
		<city>
			<de>Lissabon|${.stationmap:"randomcity"}</de>
			<en>Lisbon|${.stationmap:"randomcity"}</en>
			<pl>Lisbona|${.stationmap:"randomcity"}</pl>
		</city>
	</variables>
```

Jeśli w czasie gry zostanie wyrzucona alternatywa druga, losowa nazwa miasta zostanie ustalona zarówno dla języka niemieckiego, jak i angielskiego i polskiego.
W tekstach pojawiłyby się różne miasta, co prawdopodobnie nie jest pożądanym rezultatem.
Prawidłowym wyborem byłoby

```XML
	<variables>
		<rndcity>${.stationmap:"randomcity"}</rndcity>
		<city>
			<de>Lissabon|${rndcity}</de>
			<en>Lisbon|${rndcity}</en>
			<pl>Lisbona|${rndcity}</pl>
		</city>
	</variables>
```

Ponieważ `rndcity` jest zdefiniowane niezależnie od języka, a wartość zmiennej jest określana tylko raz, alternatywa czasowa `city` zwraca to samo miasto, co było pożądane.

### Zmienne zagnieżdżone

Ponieważ same wyrażenia mogą zawierać wyrażenia, które są obliczane od wewnątrz na zewnątrz, można użyć zagnieżdżonych zmiennych `${varpraefix_${variant}}`.
Najpierw rozwiązywany jest wariant, co określa, która "główna zmienna" jest używana.

```XML
...
	<title>
		<de>${wer_${geschlecht}} und ${pronomen_${geschlecht}} ${adj}${was}</de>
		<en>${wer_${geschlecht}} and ${pronomen_${geschlecht}} ${adj}${was}</en>
		<pl>${wer_${geschlecht}} i ${pronomen_${geschlecht}} ${adj}${was}</pl>
	</title>
...
	<variables>
		<geschlecht>maennl|weibl</geschlecht>
		<wer_maennl>
			<de>Der Anwalt|Der Bäcker|Der König</de>
			<en>Attorney|Baker|King</en>
			<pl>Prawnik|Piekarz|Król</pl>
		</wer_maennl>
		<wer_weibl>
			<de>Die Lehrerin|Die Ärztin|Die Königin</de>
			<en>Teacher|Doctor|Queen</en>
			<pl>Nauczycielka|Doktorka|Królowa</pl>
		</wer_weibl>
		<pronomen_maennl>
			<de>seine</de>
			<en>his</en>
			<pl>jego</pl>
		</pronomen_maennl>
		<pronomen_weibl>
			<de>ihre</de>
			<en>her</en>
			<pl>jej</pl>
		</pronomen_weibl>
		<adj>
			<!--pierwsza alternatywa pusta - tj. bez przymiotnika-->
			<de>|teuren |neusten |früheren </de>
			<en>|expensive | latest | previous </en>
			<pl>|drogie | najnowsze | wcześniejsze </pl>
		</adj>
		<was>
			<de>Autos|Liebschaften|Pferde|Probleme</de>
			<en>cars|romans|horses|problems</en>
			<pl>samochody|romanse|konie|problemy</pl>
		</was>
	</variables>
...
```

Jest to sposób na tworzenie poprawnych gramatycznie tekstów.
Po pierwsze, płeć jest określana raz, przy czym `${who_${gender}}` staje się albo `${who_maennl}` albo `${who_weibl}`.
Jest to wtedy prosta zmienna, którą można rozwiązać bezpośrednio.

Możliwe tytuły w tym przykładzie to
* Prawnik i jego drogie romanse
* Nauczycielka i jej samochody
* Król i jego wcześniejsze konie

Inną opcją dostępną od wersji 0.8.3 do tworzenia takich złożonych tekstów jest funkcja csv - patrz poniżej.

### Wywołania_funkcji

Oprócz rozwiązywania samodzielnie zdefiniowanych zmiennych, wyrażenia mogą być również używane do oceny funkcji.
Są one na stałe przechowywane w grze i oceniane w zależności od kontekstu użycia i aktualnego stanu gry.

Podstawową strukturą wywołania funkcji jest `${.functionName:parameter1:parameter2...}`, przy czym liczba parametrów i ich typ zależą od funkcji i kontekstu użycia.
Możliwe typy parametrów to

* Ciąg znaków (`"wartość"` - w cudzysłowie)
* Zmienna (`variablenName` - bez cudzysłowów)
* Liczba (`17`, `0.25`)
* wartość prawdy (`0`, `1`, `true`, `false`)

Oczywiście wyrażenie może być również użyte jako parametr, którego wartość jest najpierw określana, zanim zostanie użyta jako parametr funkcji.
Jeśli oczekiwany jest parametr łańcuchowy, ale jego wartość zależy od zmiennej, rozdzielenie zmiennej można przeprowadzić w cudzysłowie `${.function:"${variableOrExpression}"}`.

Istnieją *globalne* funkcje, które mogą być używane w dowolnym momencie.
Przykładem tego jest już używane rzucanie kostką nazw miast, funkcje do określania bieżących wartości czasu gry lub warunków

* `${.stationmap: "randomcity"}` - losowo określona nazwa miasta
* `${.worldtime: "year"}` - bieżący rok w grze
* `${.if:${.eq:${.worldtime: "weekday"}:0}: "Monday": "not Monday"}` - jeśli bieżący dzień tygodnia wynosi 0 (odpowiada poniedziałkowi), to całe wyrażenie jest obliczane na `Monday` w przeciwnym razie na `not Monday`.
* `${.person: "123abc": "fullname"}` - pełna nazwa osoby z GUID 123abc


Inne funkcje są zależne od kontekstu i dlatego mogą być używane tylko w niektórych obiektach bazy danych.
Na przykład `${.self: "role":1: "fullname"}` zwraca pełną nazwę roli z indeksem 1.
Wyrażenie to ma jednak sens tylko w szablonie programu lub skryptu.
W wiadomościach nie ma ról.

## Przegląd_ważnych_funkcji

Punkty wejścia dla zdefiniowanych funkcji to `game.gamescriptexpression.bmx` dla funkcji specyficznych dla TVTower i `base.util.scriptexpression_ng.bmx` dla funkcji ogólnych (warunki itp.).
Wyszukiwanie tekstowe dla `RegisterFunctionHandler` daje szybki przegląd tego, co jest dostępne i gdzie jest zdefiniowane.
Możliwe parametry można następnie prześledzić w zarejestrowanej funkcji `SEFN_`.
Wymienione poniżej funkcje i parametry niekoniecznie są kompletne!



### stationmap

Funkcja `.stationmap` zapewnia niezależny od kontekstu dostęp do informacji o mapie aktualnie używanej w grze (obecnie tylko Niemcy).
Należy podać dokładnie jeden parametr łańcuchowy.

* `${.stationmap:"randomcity"}` - losowa nazwa miasta
* `${.stationmap:"population"}` - Wielkość populacji
* `${.stationmap:"mapname"}` - Nazwa kraju
* `${.stationmap:"mapnameshort"}` - Kod kraju ISO

### worldtime

Funkcja `.worldtime` zapewnia niezależny od kontekstu dostęp do aktualnego czasu w grze.
Należy podać dokładnie jeden parametr string.

* `${.worldtime:"year"}` - Bieżący rok
* `${.worldtime:"month"}` - Bieżący miesiąc (jako liczba)
* `${.worldtime:"day"}` - Bieżący dzień (jako kolejny numer)
* `${.worldtime:"dayofmonth"}` - Dzień miesiąca (1-31)
* `${.worldtime:"hour"}` - Bieżąca godzina dnia (0-23)
* `${.worldtime:"minute"}` - bieżąca minuta (0-59)
* `${.worldtime:"daysplayed"}` - Liczba zakończonych dni
* `${.worldtime:"dayplaying"}` - bieżący dzień gry
* `${.worldtime:"yearsplayed"}` - Liczba ukończonych lat
* `${.worldtime:"weekday"}` - Bieżący dzień tygodnia (jako liczba; 0=poniedziałek)
* `${.worldtime:"season"}` - bieżąca pora roku (jako liczba; 1=wiosna, 4=zima), gdzie wiosna to okres od marca do maja

### generator_osób

Funkcja `.persongenerator` pozwala na generowanie nazwisk specyficznych dla kraju niezależnie od kontekstu.
Nie jest możliwe bezpośrednie utworzenie osoby, a następnie uzyskanie dostępu do różnych składników imienia (imię, nazwisko itp.).
Podstawowe wywołanie to `${.persongenerator: "NameType": "Country": "Gender":ProbabilityForTitle}.
Tylko pierwszy parametr name type jest obowiązkowy i oprócz prawdopodobieństwa dla tytułu (np. akademickiego) (liczba od 0 do 1), wszystkie parametry są ciągami znaków.



Dozwolone typy nazw to
* "name", "firstname" - imię
* "lastname" - nazwisko
* "fullname" - pełne imię i nazwisko wraz z tytułem
* "title" - tytuł (akademicki)

Jeśli kod kraju nie jest określony, jest pusty lub nieznany, używany jest losowy kraj.
Punktem wejścia dla dalszych wyszukiwań jest `base.util.persongenerator.bmx`.
Obecnie znane skróty to: aut, de, uk, cn, ru, tr, us, dk, gr, ug, es, fr, pl.
Kilka innych odnosi się do podobnych krajów (sco, e, irl, nor, swe, se, sui, bra, por, mex, d).

Obsługiwane są następujące wartości dla płci

* męska: `"m"`, `"1"`, `"male"`
* female: `"f"`, `"2"`, `"female"`
* dla innych wartości wybierana jest losowa płeć

Przykłady:

* `${.persongenerator:"firstname"}` - dowolne imię
* `${.persongenerator:"firstname":"us":"male"}` - Amerykańskie imię męskie
* `${.persongenerator:"fullname":"":"female":0.9}` - imię żeńskie z 90% prawdopodobieństwem

### lokalność

Funkcja `.locale` zapewnia niezależny od kontekstu dostęp do plików tłumaczeń (`res/lang/...`).
Nie można jednak przekazywać żadnych parametrów ani wybierać losowych wariantów używanych w grze.
Oprócz klucza, opcjonalnie można określić kod kraju (w przeciwnym razie używany jest język aktualnie ustawiony w grze).

* ${.locale:"HOUR"} - Rozdzielczość klucza "HOUR" z `genSettings_...` - godzina po niemiecku, heure po francusku
* ${.locale:"MOVIES","es"} - Pobranie klucza "MOVIES" z pliku `programme_es.txt` - Peliculas

Ponieważ pliki lokalizacyjne mogą się zmieniać między wersjami gry, ale baza danych jest przechowywana w zapisie gry, należy uważać, aby nie używać żadnych kluczy w bazie danych, które mogą zostać usunięte / zmienione w przyszłych wersjach.

### Odniesienie do własnej obsady

W programach można uzyskać dostęp do nazw własnej obsady; w programach i szablonach skryptów można uzyskać dostęp do ról.
Podstawowa struktura funkcji jest zawsze taka sama `${.self: "type":index: "attribute":includingtitle}`.
`.self` jest wskaźnikiem, że ewaluacja odbywa się w kontekście definiującego obiektu.
Typ może być `cast` (tylko programy, ponieważ rzeczywista obsada nie została jeszcze określona w skrypcie) lub `role` dla roli.
Indeks jest pozycją żądanej wartości na liście obsady/zadania w bazie danych i powinien być zgodny z atrybutem indeksu zdefiniowanym dla wpisu (indeks 0 jest pierwszym wpisem na liście).
Indeks znajdujący się poza liczbą spotkań prowadzi do błędu.
Wartość prawdy `includingTitle` jest opcjonalna i określa, czy nazwisko lub pełna nazwa powinna zostać zwrócona wraz z tytułem (domyślnym przypadkiem jest no).



Najważniejsze możliwe wartości dla `Attribute` odpowiadają (prawie) wartościom dla losowych nazw
* `firstname` - Imię
* `lastname` - Nazwisko
* `fullname` - Imię i nazwisko
* `tilte` - Tytuł
* `nickname` - Pseudonim (imię, jeśli nie zdefiniowano pseudonimu)

Jeśli w szablonach scenariuszy znajduje się odwołanie do roli, która nie jest jawnie przechowywana na liście zadań (brak atrybutu `role_guid`), rola jest tworzona automatycznie, tj. nowa rola z nową nazwą jest tworzona za każdym razem, gdy scenariusz jest tworzony na podstawie szablonu.
W ten sposób niekoniecznie trzeba samodzielnie wymyślać nazwy za pomocą generatora osób lub różnych zmiennych.
W przypadku gotowych programów można oczywiście odwoływać się tylko do ról przechowywanych w bazie danych



Zakładając, że reżyser jest zawsze definiowany z indeksem 0, a wszyscy pozostali są aktorami, otrzymamy następujące przykłady

* `${.self: "cast":0: "fullname":true}` - pełne imię i nazwisko reżysera wraz z tytułem (w definicji programu)
* `${.self: "cast":2: "firstname"}` - imię aktora z indeksem 2
* `${.self: "role":1: "nickname"}` - pseudonim roli, który jest przechowywany dla indeksu 1 (lub jest tworzony w razie potrzeby)



### Warunki

Warunki są wymagane w szczególności w przypadku skryptów dostępności, np. w celu sprawdzenia, czy upłynęła wystarczająca liczba dni gry, zanim szablon skryptu stanie się dostępny.
Mogą być one jednak również pomocne przy generowaniu tekstów.
Na przykład we wcześniejszych wersjach konieczne było zdefiniowanie kilku łańcuchów komunikatów w celu obsługi zmieniających się w czasie walut lub nazw miast.
Teraz teksty te mogą być generowane dynamicznie przy użyciu warunków.



Najważniejszym punktem wyjścia dla rozróżniania przypadków jest `${.if:Condition:ResultIfYes:ResultIfNo}`.
Parametry wyniku są opcjonalne i jeśli ich brakuje, zwracana jest odpowiednia wartość prawdy warunku.

* `${.if:${.worldtime:"year"}==2000:"zweitausend":"nicht 2000"}` - jeśli bieżący rok to 2000, wynikiem jest "dwa tysiące", w przeciwnym razie "nie 2000".
* `${.if:"${var}"=="foo":"bar":"karte"}` - jeśli zmienna `var` jest obliczana na `foo`, wynikiem jest "bar", w przeciwnym razie "karte"
* `${.if:${.gt:${.worldtime:"hour"}:21}:"spät":"nicht spät"}` - Jeśli jest po 22:00, pojawia się "późno", w przeciwnym razie "nie późno"
* `${.if:var:"nicht leer":"leer"}` - jeśli zmienna `var` jest obliczana na pusty łańcuch, wynikiem jest "empty", w przeciwnym razie "not empty".

Ostatni przykład pokazuje, w jaki sposób wyniki oceny mogą być przekazywane przy użyciu doprawidłowychbrych nazw zmiennych.

```XML
<variables>
	<geschlecht>m|f</geschlecht>
	<maennl>${{.if:"${geschlecht}"=="m"}:"true":""}</maennl>
	<artikel>
		<de>
			${.if:maennl:"Der:"Die"}
		</de>
	</artikel>
...
```
Płeć jest zrolowana.
Jeśli `f` wyjdzie, zawartość zmiennej `maennl` jest pusta i zwraca wartość false w sprawdzeniu If.

Dostępnych jest kilka funkcji do porównywania.
Równość z `==` została sprawdzona powyżej.
Ponieważ użycie nawiasów kątowych w XML nie jest zalecane, z wyjątkiem tagów, użycie normalnych operatorów (`<`,`<=`,`>`,`>=`,`<>`) nie jest zalecane.
Zamiast tego, odpowiednie funkcje porównania powinny być użyte do porównania `p1` i `p2`.

* `${.eq:p1:p2}` - true gdw (dokładnie jeśli) p1 jest równe p2
* `${.neq:p1:p2}` - true gdw p1 nie jest równe p2
* `${.gt:p1:p2}` - true gdw p1 jest większe niż p2
* `${.gte:p1:p2}` - true gdw p1 jest większe lub równe p2
* `${.lt:p1:p2}` - true gdw p1 jest mniejsze niż p2
* `${.lte:p1:p2}` - true gdw p1 jest mniejsze lub równe p2

Ponieważ prosty if-then-else występuje bardzo często, a zagnieżdżone wywołania funkcji nie są łatwe do odczytania, oprócz porównania istnieje również notacja skrócona, która zwraca wartość prawdy.
`${.cmp:p1:p2:ResultIfYes:ResultIfNo}` - w zależności od wyniku porównania p1 i p2, wynik jest przedostatnim lub ostatnim parametrem.

* `${.eq:gender: "m": "The": "The"}` - Jeśli wartością zmiennej `gender` jest `m`, wynikiem jest `The`, w przeciwnym razie `The`.
* `${.gte:${.worldtime: "year"}:2002: "Euro": "DM"}` - od 2002 Euro, przed DM.

Warunek można zanegować za pomocą `${.not:condition}`.
Możliwe są również kombinacje AND i OR dwóch lub więcej warunków.

* `${.and:p1:p2}` - prawda jeśli wszystkie warunki (p1 i p2) są prawdziwe
* `${.and:p1:p2:p3:p4}` - true jeśli wszystkie warunki (p1 do p4) są prawdziwe
* `${.or:p1:p2}` - true jeśli przynajmniej jeden z warunków (p1 lub p2) jest prawdziwy
* `${.or:p1:p2:p3:p4}` - true jeśli przynajmniej jeden z warunków jest prawdziwy

Jest rzeczą oczywistą, że parametry porównań itp. mogą same być złożonymi wyrażeniami (z prawidłowym typem).
Należy jednak zachować szczególną ostrożność, aby zapewnić, że ciągi znaków wyrażeń wewnętrznych nie staną się nagle nazwami zmiennych w wyrażeniu zewnętrznym, co doprowadzi do nieoczekiwanego zachowania.

Przykład takiej pułapki:

`${.eq:0:1:"foo":${.eq:0:1:"bar":"baz"}}` -> `${.eq:0:1:"foo":baz}}` -> Wartość prawdopodobnie niezdefiniowanej zmiennej baz.
Intencją było prawdopodobnie bardziej `${.eq:0:1:"foo":"${.eq:0:1:"bar":"baz"}"}` -> `${.eq:0:1:"foo":"baz"}}`.
Zwróć uwagę na cudzysłów wokół wewnętrznego wyrażenia.


### csv

Do tej pory poprawne gramatycznie zdania można było realizować tylko za pomocą zmiennych zagnieżdżonych.
Dzięki funkcjom istnieje teraz dodatkowa opcja, która może prowadzić do lepszej czytelności w bazie danych.
Podstawową ideą jest dostarczenie listy rekordów danych, z których każdy zawiera wszystkie niezbędne informacje.
Funkcja `.csv` umożliwia następnie dostęp do poszczególnych elementów rekordu danych.
Podstawowa struktura wywołania funkcji to `${.csv: "Record":Index: "Separator":SpaceRemove}`.
Obowiązkowymi parametrami są zestaw danych (ciąg znaków) i indeks (która część zestawu danych jest zwracana).
Jeśli separator w zestawie danych nie jest średnikiem (`;`), separator może być opcjonalnie określony.
Zwykle spacje, tabulatory itp. są automatycznie usuwane przed i po całym rekordzie danych.
Można temu zapobiec za pomocą czwartego parametru (wartość prawdy).



Proste przykłady:
* `${.csv:"a;b;c":0}` dostarcza `a`
* `${.csv:"a;b;c":2}` dostarcza `c`
* `${.csv:"a,b,c":1:","}` dostarcza `b`

Poniższy przykład ma na celu zilustrowanie możliwości kombinacji alternatyw, zmiennych zagnieżdżonych i rekordów danych csv.

```XML
...
	<title>
		<de>${wer_${geschlecht}} und ${pron_nom_${geschlecht}} ${adj}${was}</de>
		<en>${wer_${geschlecht}} and ${pron_nom_${geschlecht}} ${adj}${was}</en>
		<pl>${wer_${geschlecht}} i ${pron_nom_${geschlecht}} ${adj}${was}</pl>
	</title>
	<description>
		<de>Wie alle ${wer_plural_${geschlecht}} kämpft ${name} mit ${pron_gen_${geschlecht}} Vorliebe für ${was}.</de>
		<en>Like ${all_plural_${geschlecht}} ${wer_plural_${geschlecht}}, ${name} is struggling with ${pron_gen_${geschlecht}} preference for ${was}.</en>
		<pl>Jak ${all_plural_${geschlecht}} ${wer_plural_${geschlecht}}, ${name} zmaga się z ${pron_gen_${geschlecht}} sprawami.</pl>
	</description>
...
	<variables>
		<geschlecht>m|f</geschlecht>
		<name>${.persongenerator:"firstname":"de":geschlecht}</name>
		<werData>
			<!--Dla lepszej czytelności, każdy rekord danych ma swój własny wiersz.
			    Obejmuje to również automatyczne usuwanie spacji przed i po rekordzie danych.

				Dla języka angielskiego i polskiego musimy pozmieniać parę zmiennych aby była poprawna wersja gramatyczna, przykład jest poprawny dla jezyka niemieckiego
			-->
			<de>
				Anwalt;Anwälte;Anwältin;Anwältinnen|
				Bäcker;Bäcker;Bäckerin;Bäckerinnen|
				König;Könige;Königin;Königinnen|
				Lehrer;Lehrer;Lehrerin;Lehrerinnen|
				Arzt;Ärzte;Ärztin;Ärztinnen
			</de>
			<en>
				lawyer;lawyers;female lawyer;female lawyers;every;all;every;all|
				baker;bakers;female baker;female bakers;every;all;every;all|
				king;kings;queen;queens;every;all;every;all|
				teacher;teachers;female teacher;female teachers;every;all;every;all|
				doctor;doctors;female doctor;female doctors;every;all;every;all
			</en>
			<pl>
				prawnik;prawnicy;prawniczka;prawniczki;każdy;wszyscy;każda;wszystkie|
				piekarz;piekarze;piekarka;piekarki;każdy;wszyscy;każda;wszystkie|
				król,królowie,królowa,królowe;każdy;wszyscy;każda;wszystkie|
				nauczyciel;nauczyciele;nauczycielka;nauczycielki;każdy;wszyscy;każda;wszystkie|
				lekarz;lekarze;lekarka;lekarki;każdy;wszyscy;każda;wszystkie
			</pl>
		</werData>
		<wer_m>
			<de>Der ${.csv:werData:0}</de>
			<en>${.csv:werData:0}</en>
			<pl>${.csv:werData:0}</pl>
		</wer_m>
		<wer_f>
			<de>Die ${.csv:werData:2}</de>
			<en>${.csv:werData:2}</en>
			<pl>${.csv:werData:2}</pl>
		</wer_f>
		<wer_plural_m>
			<de>${.csv:werData:1}</de>
			<en>${.csv:werData:1}</en>
			<pl>${.csv:werData:1}</pl>
		</wer_plural_m>
		<wer_plural_f>
			<de>Die ${.csv:werData:3}</de>
			<en>${.csv:werData:3}</en>
			<pl>${.csv:werData:3}</pl>
		</wer_plural_f>
		<!--Dla języka angielskiego i polskiego musimy pozmieniać parę zmiennych aby była poprawna wersja gramatyczna, przykład jest poprawny dla jezyka niemieckiego
			-->
		<all_m>
			<en>${.csv:werData:5}</en>
			<pl>${.csv:werData:5}</pl>
		</all_m>
		<all_f>
			<en>${.csv:werData:7}</en>
			<pl>${.csv:werData:7}</pl>
		</all_f>
		<all_plural_m>
			<en>${.csv:werData:6}</en>
			<pl>${.csv:werData:6}</pl>
		</all_plural_m>
		<all_plural_f>
			<en>${.csv:werData:8}</en>
			<pl>${.csv:werData:8}</pl>
		</all_plural_f>
		<pron_nom_m>
			<de>seine</de>
			<en>his</en>
			<pl>jego</pl>
		</pron_nom_m>
		<pron_gen_m>
			<de>seiner</de>
			<en>her</en>
			<pl>jej</pl>
		</pron_gen_m>
		<pron_nom_f>
			<de>ihre</de>
			<en>their</en>
			<pl>ich</pl>
		</pron_nom_f>
		<pron_gen_f>
			<de>ihrer</de>
			<en>their</en>
			<pl>ich</pl>
		</pron_gen_f>
		<adj>
			<de>|teuren |neusten |früheren </de>
			<en>|cheap |latest |earlier </en>
			<pl>|tanie |najnowsze |wcześniejsze </pl>
		</adj>
		<was>
			<de>Autos|Liebschaften|Pferde|Probleme</de>
			<en>cars|romances|horses|problems</en>
			<pl>samochody|romanse|konie|problemy</pl>
		</was>
	</variables>
...
```

Alternatywnie można również powielić informacje gramatyczne w rekordach danych i użyć warunków, aby uzyskać mniej zmiennych.

```XML
...
	<title>
		<de>${wer} und ${pron_nom} ${adj}${was}</de>
	</title>
	<description>
		<de>Wie alle ${wer_plural} kämpft ${name} mit ${pron_dat} Vorliebe für ${was}.</de>
	</description>
...
	<variables>
		<werData>
			<!--Dla lepszej czytelności, każdy rekord danych ma swój własny wiersz.
			    Obejmuje to również automatyczne usuwanie spacji przed i po rekordzie danych.
			-->
			<de>
				Anwalt;Anwälte;m|
				Anwältin;Anwältinnen;f|
				Bäcker;Bäcker;m|
				Bäckerin;Bäckerinnen;f|
				König;Könige;m|
				Königin;Königinnen;f|
				Lehrer;Lehrer;m|
				Lehrerin;Lehrerinnen;f|
				Arzt;Ärzte;m|
				Ärztin;Ärztinnen;f
			</de>
		</werData>
		<maennl>${.if:${.eq:"${.csv:werData:2}":"m"}:"true":""}</maennl>
		<wer>
			<de>${.if:maennl:"Der":"Die"} ${.csv:werData:0}</de>
		</wer>
		<name>${.persongenerator:"firstname":"de":"${.csv:werData:2}"}</name>
		<wer_plural>
			<de>${.csv:werData:1}</de>
		</wer_plural>
		<pron_nom>
			<de>${.if:maennl:"seine":"ihre"}</de>
		</pron_nom>
		<pron_dat>
			<de>${.if:maennl:"seiner":"ihrer"}</de>
		</pron_dat>
		<adj>
			<de>|teuren |neusten |früheren </de>
		</adj>
		<was>
			<de>Autos|Liebschaften|Pferde|Probleme</de>
		</was>
	</variables>
...
```

Używając warunków w wyrażeniach, można zapisać kolejne zmienne.

### Globalne odniesienie do obiektów bazy danych

Dostęp do osób, ról i programów można uzyskać z dowolnej lokalizacji za pośrednictwem ich identyfikatora GUID przypisanego w bazie danych.
Oto kilka przykładów.
W `game.gamescriptexpression.bmx` można sprawdzić, czy potrzebne informacje są już dostępne.

* `${.person:"836b4aa3-b5c6-4529-b30d-4501594cdf13":"nickname"}` - Pseudonim osoby o podanym identyfikatorze GUID
* `${.person:"3342a0e3-66f3-4f30-922c-ebe1b0611a00":"age"}` - Wiek osoby
* `${.programme:"04439fd1-e89f-4922-a48e-6f8ddf96f7ab":"episodecount"}` - Liczba odcinków serialu
* `${.programme:"35190c1d-aa55-4e84-967f-72a374e84dcf":"year"}` - Rok publikacji programu
* `${.programme:"02d0dfa5-dbcf-40b5-abb4-7e20a58d8efa":"cast":1:"fullname"}` - Pełna nazwa obsady z indeksem 1 (podobnie jak w przypadku odniesień do własnej obsady, indeks 0 jest zazwyczaj pierwszym wpisem na liście).
* `${.programme:"a61e7775-7565-48cd-ab4a-e5faea09d70d":"title"}` - Tytuł programu
* `${.role:"1d1f05ea-43ff-4399-81d9-f00239460700":"fullname"}` - Pełna nazwa stanowiska 1d1f05ea-43ff-4399-81d9-f00239460700



### Operacje na ciągach znaków

Za pomocą `.ucfirst:parameter` można przekonwertować pierwszą literę parametru na wielką literę.
Jest to przydatne, jeśli nie chcesz definiować słów dla początku i końca zdania w dwóch wariantach.