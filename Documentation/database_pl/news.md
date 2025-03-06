# Wiadomości (news)

Wpisy wiadomości są osadzone w tagu `allnews` jako lista elementów podrzędnych `news`.

```XML
<allnews>
		<news guid="X-news-geld1" thread_guid="X-news-geld" type="0">
			<title>
				<de>Straßenfeger findet 1.000 Mark</de>
				<en>Street sweeper finds 1,000 marks</en>
				<pl>Zamiatacz ulic znajduje 1 000 marek</pl>
			</title>
			<description>
				<de>Besser hätte der Morgen ...</de>
				<en>The morning couldn't ...</en>
				<pl>Poranek nie mógł ...</pl>
			</description>
			<effects>
				<effect trigger="happen" type="triggernews" news="X-news-geld2" time="1,10,15" />
			</effects>
			<data genre="4" price="1.4" quality="19" />
			<availability year_range_from="-1" year_range_to="2001" />
		</news>
</allnews>
```

Dostępny do 2001 roku (`year_range_to`), ten przeceniony (`price`) codzienny news (`genre`) o niskiej jakości (`quality`) ma niemieckie, angielskie i polskie tytuły i teksty newsów (`title`, `description`) i wywołuje (`effect`) wiadomość follow-up z GUID X-news-geld2 w ciągu 10 do 15 godzin (`time`).
(W tym przykładzie, który został nieznacznie zaadaptowany z bazy danych, ograniczenie roku mogło również zostać pominięte, a waluta użyta za pośrednictwem globalnej zmiennej waluty).



## Właściwości wiadomości

| Nazwa | Typ | Opis |
| ---- | --- |------------- |
| guid | Obowiązkowe | [GUID](main.md#guid), szczególnie w przypadku odwoływania się w kolejnych wiadomościach |
| type | Obowiązkowe | Typ wiadomości; patrz poniżej 0=wiadomość początkowa, 2=wiadomość uzupełniająca |
| thread_guid | opcjonalny | GUID tematu wiadomości - wiadomości, które należą do siebie |
| creator | Metadane opcjonalne | [Standardowa właściwość](main.md#creator) |
| created_by | Metadane opcjonalne | [Standardowa właściwość](main.md#created_by) |
| comment |  informativ  |[Standardowa właściwość](main.md#comment) |

### Znaczenie `thread_guid`

Do wersji 0.8.0 wartość ta miała charakter czysto informacyjny i nie była analizowana
(Identyczny) `thread_guid` był zwykle przypisywany do wiadomości powiązanego łańcucha wiadomości z wiadomością początkową i kolejnymi wiadomościami.
Od wersji 0.8.1, `thread_guid` ma inne ważne znaczenie.

Podobnie jak szablony skryptów, wiadomości są w rzeczywistości szablonami, z których tworzone są wiadomości, które mogą być faktycznie nadawane.
Gra oznacza szablon, aby nie został zbyt szybko ponownie użyty.
Od wersji 0.8.1, oznaczony jest również `thread_guid`.

Jeśli więc dwie wiadomości startowe mają ten sam `thread_guid`, wybór jednej z nich blokuje drugą.
Gwarantuje to, że nie pojawi się zbyt wiele wiadomości na ten sam temat w tym samym czasie.

## Elementy podrzędne wiadomości

Standardowe elementy dla tytułu [title](main.md#title), opisu [description](main.md#description) są przydatne do zdefiniowania, zmienne [variables](variables.md) są niezbędne, jeśli mają być użyte w tytule lub opisie, a dzięki (czasowej) dostępności [availability](time.md#availability) można kontrolować, kiedy wiadomości mogą być publikowane.

Od wersji 0.8.1 zmienne są przekazywane do wyzwalanych wiadomości.
Dzięki temu łańcuchy wiadomości mogą być bardziej zróżnicowane, ponieważ nazwy kostek itp. mogą być również konsekwentnie używane w późniejszych wiadomościach.
Aby to zrobić, wszystkie używane zmienne powinny być zdefiniowane w komunikacie startowym.
Jeśli definicje zmiennych w bieżącym i poprzednim komunikacie nie są zgodne, program może zostać przerwany.



### Dane (data)

| Nazwa | Typ | Opis |
| ---- | --- |------------- |
| genre | Obowiązkowe | Gatunek; wartości 0-5, patrz poniżej |
| price | Obowiązkowe | Cena*współczynnik*; np. 1, 0,4, 0,9 lub 1,5 |
| quality | Obowiązkowe* | Jakość; wartości nat. liczby 0-100 |
| flags | opcjonalny | siehe unten; häufigster Anwendungsfall "2": Nachricht steht nur einmalig zur Verfügung |
| happen_time | opcjonalny | Wiadomość musi zostać wysłana do zdefiniowanego czasu [Czas](time.md#Atrybuty_czasu) pojawiania się |
| min_subscription_level | opcjonalny | Poziom subskrypcji (1,2,3), z którego wiadomość jest dostępna |
| keywords | opcjonalny | Kluczowe terminy, które mogą być używane przez sztuczną inteligencję do rozpoznawania wiadomości z wiadomości |
| available | opcjonalny |  Wartość prawdy - czy wiadomość jest dostępna |
| fictional | informativ | [Standardowa właściwość](main.md#fictional) |

Zamiast `quality` można również zdefiniować `quality_min`, `quality_max` i `quality_slope`.
Daje to wiadomości losową jakość w zakresie od min do max (zobacz także [script-values](scripts.md#losowe_wartości_dla_skryptu_i_wyniku)).

Właściwość `available` jest interesująca w połączeniu z typem efektu `modifyNewsAvailability`.
Można utworzyć ciąg wiadomości, który jest początkowo nieaktywny, a następnie aktywować go inną wiadomością.

W przeciwieństwie do dostępności (`availability`), która kontroluje, kiedy wiadomość może się pojawić, publikacja jest wymuszana przez `happen_time`; ma to jednak sens tylko dla początkowych wiadomości, ponieważ kolejne wiadomości mogą być kontrolowane przez czas zdefiniowany w efekcie.

Przykład: `... happen_time="4,1995,3,7,14,25"...`

`keywords` jest obecnie używany do wiadomości związanych z terroryzmem i raportów pogodowych.
Nie są one jeszcze przypisane do bazy danych, ale mogą zostać wykorzystane do osiągnięcia sukcesu.

### Efekty (effects)

Jest to prawdopodobnie najbardziej interesujący element dla wiadomości, ponieważ efekty mogą być wykorzystywane, na przykład, do wywoływania kolejnych wiadomości lub wpływania na popularność gatunków lub osób.
Składnia jest taka sama dla efektów wiadomości/programu/scenariusza ([Efekty](main.md#effects)).

Dla efektów wiadomości obsługiwane są następujące wyzwalacze

* `happen`- efekt występuje w każdym przypadku; np. wiadomości uzupełniające pojawiają się, nawet jeśli nikt nie wysłał wiadomości.
* `broadcast` - efekt występuje na początku *każdej* emisji
* `broadcastDone` - efekt występuje pod koniec *każdej* emisji
* `broadcastFirstTime` - efekt pojawia się, gdy tylko wiadomość zostanie wysłana po raz pierwszy
* `broadcastFirstTimeDone` - efekt pojawia się na końcu pierwszej transmisji (na rozpoczęty łańcuch wiadomości, tj. nie tylko raz w całym czasie odtwarzania).

`broadcastFirstTime` byłaby używana, na przykład, jeśli wiadomości uzupełniające powinny być dostępne tylko po wysłaniu wyzwalacza ("Obywatele reagują szokiem na wiadomość...").
Jeśli ta sama oryginalna wiadomość pojawi się ponownie w późniejszym czasie, efekt "broadcastFirstTime" zadziała ponownie.

`broadcast` może być stosowany, jeśli atrakcyjność genu ma się zmieniać z każdą transmisją.

Przykład:

```
	<effects> 
		<effect trigger="happen" type="triggernews" time="1,2,3" news="ronny-news-drucktaste-02b1" />
		<effect trigger="happen" type="modifyNewsAvailability" enable="0" news="ronny-news-drucktaste-1" />
	</effects>
```

### Atrakcyjność dla grupy docelowej (targetgroupattractivity)

Zobacz [Standard child element](main.md#targetgroupattractivity).
Obecnie w bazie danych nie ma żadnych przykładów.

### Korekty wartości (modifiers)

Zobacz [Standardowy element podrzędny](main.md#modifiers).
Obecnie w bazie danych nie ma żadnych przykładów.

## Konkretne wartości dla wiadomości

| **NewsType** | Znaczenie |
|------------- | --------- |
| 0 | InitialNews - pierwsza wiadomość łańcucha |
| 1 | InitialNewsByInGameEvent - Pierwsza wiadomość wywołana przez grę |
| 2 | FollowingNews - Wiadomość uzupełniająca |
| 3 | TimedNews - Komunikat sterowany czasem |

Typ 1 jest używany tylko w grze, a typ 3 jest przestarzały ze względu na opcje kontrolowania dostępności wiadomości.

| **Genre** | Znaczenie |
|---------- | --------- |
| 0 | Polityka/ekonomia |
| 1 | Showbiznes |
| 2 | Sport |
| 3 | Media/Technologia |
| 4 | Sprawy bieżące |
| 5 | Kultura|

| **NewsFlag** | Znaczenie |
|------------- | --------- |
| 1 | sendImmediately | Wiadomość jest gotowa bez opóźnień |
| 2 | uniqueEvent | unikalna wiadomość; nie zostanie opublikowana po raz drugi |
| 4 | unskippable | jeśli nikt nie otrzyma wiadomości (poziom subskrypcji), zostanie ona opublikowana |
| 8 | sendToAll | Wiadomość jest wysyłana do wszystkich, niezależnie od poziomu subskrypcji |
| 16 | keepTickerTime | Nie *opóźniaj* innych wiadomości tego gatunku (flaga szczególnie dla początkowych wiadomości).|
| 32 | resetTickerTime | inne wiadomości tego typu *będą* opóźnione (szczególnie w przypadku wiadomości uzupełniających) |
| 64 | resetHappenTime | zignorować początkowo ustawiony happen_time ze względu na możliwość ponownego użycia wiadomości *then |
| 128 | specialEvent | Wiadomość specjalna - wyróżnienie wizualne |
| 256 | invisibleEvent | Niewidoczna wiadomość - wykonywane są tylko efekty |

Flagi wiadomości to wartość flagi, tzn. w jednej liczbie można zakodować kilka wartości.
Aby to zrobić, należy zsumować wartości.
`flags="138"` byłaby unikalną wiadomością, która jest dostępna dla wszystkich graczy, nawet jeśli nie zasubskrybowali gatunku. Jest ona również wyróżniona wizualnie.

## Przykłady

### minimalny 

Drogi, niskiej jakości przekaz kulturowy bez ograniczeń dostępności i efektów.

```XML
<news guid="ronny-news-tarotimwandel-01" type="0" creator="5578" created_by="Ronny">
	<title>
		<de>"Tarot im Wandel der Zeit" auf Tour</de>
		<en>"Tarot in the course of time" on tour</en>
		<pl>"Tarot z biegiem czasu" na trasie koncertowej</pl>
	</title>
	<description>
		<de>Die Ausstellung der "Zunft" ...</de>
		<en>The exhibition of the "guild" ...</en>
		<pl>Wystawa "gildii" ...</pl>
	</description>
	<data genre="5" price="1.2" quality="23" />
</news>
```

### prosty

Komunikat dotyczący polityki dostępny w latach 2001-2009 wywołuje komunikat uzupełniający, którego typ `type="2"` wskazuje, że nie jest on dostępny podczas losowego określania możliwych komunikatów.

```XML
<news guid="6b1065dd-36d5-4b4b-9904-1a8b7fd1d9c1" thread_guid="0328d075-c155-43c9-b0c1-e130eb972f38" type="0" creator="">
	<title>
		<de>Terrorismusbekämpfung im Weltall</de>
		<en>Fighting terrorism in the universe</en>
		<pl>Walka z terroryzmem we wszechświecie</pl>
	</title>
	<description>
		<de>US-Präsident Baush ...</de>
		<en>For safety reasons ...</en>
		<pl>Ze względów bezpieczeństwa ...</pl>
	</description>
	<effects>
		<effect trigger="happen" type="triggernews" news="7c2911a9-c9b4-40d1-b4f6-02fb0025358a" />
	</effects>
	<data genre="0" price="1.0" quality="58" />
	<availability year_range_from="2001" year_range_to="2009" />
</news>

<news guid="7c2911a9-c9b4-40d1-b4f6-02fb0025358a" thread_guid="0328d075-c155-43c9-b0c1-e130eb972f38" type="2" creator="">
	<title>
		<de>Terrorismusbekämpfung – jetzt 2 Shuttles</de>
		<en>Fighting terrorism - now 2 shuttles</en>
		<pl>Fighting terrorism - now 2 shuttles</pl>
	</title>
	...
</news>
```

### złożone

Główny komunikat uruchamia jeden z czterech możliwych komunikatów uzupełniających o różnym prawdopodobieństwie.

```XML
<news guid="news-jorgaeff-racing-01" type="0" thread_guid="news-jorgaeff-racing" creator="8936" created_by="jorgaeff">
	<title>
		<de>Formel X: Wer holt sich die Fahrer-WM?</de>
		<en>Formula X: Who will win the drivers' world championship?</en>
		<pl>Formuła X: Kto zdobędzie mistrzostwo świata kierowców?</pl>
	</title>
	<description>
		<de>Zu einem Dreikampf...</de>
		<en>Triple battle...</en>
		<pl>Trójstronna bitwa...</pl>
	</description>
	<data genre="2" price="0.45" quality="45" fictional="True" />
	<effects>
		<!-- "Możliwy efekt: transmisja na żywo" -->
		<!-- "jutro 6-12 rano / wiadomości a, b, c lub d" -->
		<effect trigger="happen" type="triggernewschoice" choose="or" probability="100" time="2,1,1,6,12"
			news1="news-jorgaeff-racing-02a" probability1="30"
			news2="news-jorgaeff-racing-02b" probability2="30"
			news3="news-jorgaeff-racing-02c" probability3="30"
			news4="news-jorgaeff-racing-02d" probability4="10"
		/>
	</effects>
</news>
```

### Łańcuch wiadomości z przekazanymi zmiennymi

Komunikat główny uruchamia komunikat uzupełniający.
Zdefiniowane zmienne są przekazywane do kolejnych komunikatów, a zamiany, które zostały już wykonane, są konsekwentnie stosowane.
Jeśli główna wiadomość zostanie wysłana później, rzucana jest nowa kostka.

```
<news guid="carStrike_0" thread_guid="carStrike" type="0">
	<title>
		<de>${brand} schreibt Verluste</de>
		<en>${brand} records losses</en>
		<pl>${brand} odnotowuje straty</pl>
	</title>
	<description>...
	</description>
	<effects>
		<effect trigger="happen" type="triggernews" news="carStrike_1" time="1,8,12" />
	</effects>
	<data genre="3" price="1.0" quality="19" />
	<variables>
		<brand>
			<de>Fort|Bucki|Admiral Motors|Lilaccats|Abraham|Evade</de>
		</brand>
		<jobs>
			<de>4.000|5.000|6.000|7.500</de>
			<en>4,000|5,000|6,000|7,500</en>
			<pl>4,000|5,000|6,000|7,500</pl>
		</jobs>
	</variables>
</news>
<news guid="carStrike_1" thread_guid="carStrike" type="2">
	<title>
		<de>${brand} will ${jobs} Stellen streichen</de>
		<en>${brand} to cut ${jobs} jobs</en>
		<pl>${brand} zwalnia ${jobs} pracowników</pl>
	</title>
	<description>
		<de>Der Amerikanische Autokonzern will aufgrund der hohen Verluste ${jobs} Mitarbeiter entlassen.</de>
		<en>The American car company plans to lay off ${jobs} employees due to the high losses.</en>
		<pl>Amerykańska firma motoryzacyjna planuje zwolnić ${jobs} pracowników z powodu wysokich strat.</pl>
	</description>
	...
</news>
```

Innym przykładem użycia zmiennych są wiadomości giełdowe (GUID `news-stockexchange-generic`) w pliku `user/kieferer.xml`.
Te wyzwalają się ponownie.
W tym przypadku dopuszczalne jest, aby kolejne wiadomości zawierały definicje zmiennych.

## DO ZROBIENIA i pytania

### Dokumentacja

* Wyjaśnienie, które modyfikatory są dostępne i obsługiwane dla wiadomości. (Ronny: użyj modyfikatorów, aby ograniczyć efekt transmisji do X godzin)

### DB-Cleanup

* Istnieje wiele wiadomości, które są dostępne tylko raz. W tym przypadku należy ponownie przeanalizować, które z nich byłyby odpowiednie do częstszego wysyłania.
* Sprawdź gatunek wiadomości (zarys edytora jest odpowiedni do łatwego rozpoznania gatunku).

### Ogólne

* Istnieje niewiele wiadomości, które dostosowują atrakcyjność gatunku lub postaci. Gdyby role filmowe były częściej wykorzystywane, atrakcyjność ról również mogłaby zostać dostosowana (nowy film Yams Pond, zmarły aktor Yams Pond) - (zapowiedzi filmów kinowych są już generowane)
* Sprawdź użycie flagi wiadomości 64: Jeśli news jest "unikalny", to i tak nie może pojawić się drugi raz, jeśli nie jest "unikalny", to ewentualnie ustawiony happen_time i tak musi zostać usunięty po pierwszej publikacji (flaga zbędna?)
* Flaga wiadomości 16/32 w wyjaśnieniu, czy flagi mogą być łączone w jedną; inna standardowa obsługa wiadomości początkowych i uzupełniających.


