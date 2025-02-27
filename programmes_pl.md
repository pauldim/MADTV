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

## Elementy programu dotyczące dzieci

Standardelemente für Titel [title](main.md#title) und Beschreibung [description](main.md#description) sind sindvollerweise zu definieren.
Analog zum Titel kann der urspüngliche Titel unter `title_original` angegeben werden.
Die aus Nachrichten oder Drehbüchern bekannten Variablen kommen bei Programmen aktuell nicht vor, aber der Spezialfall [Besetzungsvariablen](main.md#Besetzungsvariablen) um Namen direkt aus der Besetzung in Titel und Beschreibung zu übernehmen.

Ebenfalls benötigt werden Daten (`data`) und die Bewertung des Programminhalts (`ratings`).

### Mitwirkende (staff)

Im Hauptknoten `staff` kann eine Liste von Mitwirkenden (`member`) definiert werden.
Im Normalfall wird es sich um eine Referenz auf in der Datenbank definierte Personen handeln.
Die Eigenschaft `index` gibt die Position (0,1,2,...) an, um die Einträge in Variablen referenzieren zu können, `function` definiert den [Beruf](main.md#Job).
Wenn eine Besetzung komplett zufällig erzeugt werden soll, kann sie auch mittels `generator` definiert werden.
Das Attribut `role_guid` kann verwendet werden, um eine Besetzung mit einer definierten Rolle zu verknüpfen.

* `<member index="1" function="2">person-0815</member>` - die Person mit der GUID `person-0815` ist als Schauspieler in der Besetzung
* `<member index="2" function="64" generator="es,0"></member>` - spanischer Gast männlich oder weiblich
* `<member index="1" function="2" role_guid="role_hercules">person-4711</member>` - die [Rolle](persons.md#Filmrollen) Herkules war in dem Film mit dem Schauspieler mit der GUID `person-4711` besetzt.

### Ziel- und Lobbygruppen (groups)

| Name | Art | Beschreibung |
| ---- | --- |------------- |
| target_groups | Pflicht | definitiv verwendete [Zielgruppe](main.md#Zielgruppe) |
| pro_pressure_groups | optional | angesprochene [Lobbygruppe](main.md#Lobbygruppe) |
| contra_pressure_groups | optional | abgeschreckte [Lobbygruppe](main.md#Lobbygruppe) |

Beispiel: `<groups target_groups="128" pro_pressure_groups="8" contra_pressure_groups="4" />` - Zielgruppe Frauen, Pazifisten zufrieden, Waffenlobby verärgert.

### Zielgruppenattraktivität (targetgroupattractivity)

Siehe [Standardkindelement](main.md#targetgroupattractivity).

### Bewertung (ratings)

Dies ist die entscheidende Stelle für die Definition der Qualität eines Programms - die Werte für Tempo (`speed`), Kritikermeinung (`critics`) und kommerzieller Erfolg (`outcome`).
Die möglichen Werte sind jeweils zwischen 0 und 100.

Beispiel: `<ratings critics="45" speed="30" outcome="40" />`

### Daten (data)

| Name | Art | Beschreibung |
| ---- | --- |------------- |
| country | Pflicht | produziert in [Land](main.md#Länder) |
| year | optional | Produktionsjahr |
| distribution | optional | Verbreitungsweg siehe unten |
| maingenre | Pflicht | [Hauptgenre](main.md#Genre) des Programms |
| subgenre | optional  | [Untergenre](main.md#Genre) des Programms |
| flags | optional | [Programmflags](main.md#Programmflags) |
| licence_flags | optional | [Lizenzflags](main.md#Lizenzflags) |
| blocks | optional | Länge in Stunden (default und Minimum 1, Maximum 12) |
| price_mod | optional | Faktor für die Preisberechnung |
| broadcast_time_slot_start | optional | Frühester Start des ersen Blocks |
| broadcast_time_slot_end | optional | Spätestes Ende des letzten Blocks |
| broadcast_limit | optional | Anzahl der möglichen Ausstrahlungen |
| broadcast_flags | optional | [Ausstrahlungsflags](main.md#Ausstrahlungsflags) |
| licence_broadcast_limit | optional | Anzahl der möglichen Ausstrahlungen (nur für diese Lizenz) |
| licence_broadcast_flags | optional | [Ausstrahlungsflags](main.md#Ausstrahlungsflags) (nur für diese Lizenz) |
| available | optional | Wahrheitswert - ist die Lizenz initial verfügbar |


`country` und `maingenre` sind Pflicht für "Hauptprogramme", für Serienfolgen werden die Werte des Elternelements übernommen.
`year` sollte angegeben werden.
Wenn man allerdings zum Spielstart relative Jahre oder genauere Daten angeben möchte, kann man `year` weglassen und den `releaseTime`-Knoten verwenden.
In Kombination mit Live-Programmen, Einschränkung der Ausstrahlungszeit oder -häufigkeit sind die Ausstrahlungsflags interessant.

Ab Version 0.8.2 werden sowohl `maingenre` also auch `subgenre` in die Beliebtheits-/Zuschauerberechnung einbezogen.

Ab Version 0.8.2 kann eine Lizenz mittels `available="0"` initial deaktiviert werden.
Die Aktivierung erfolgt dann durch einen Effekt (`modifyProgrammeAvailability` siehe [Effekte](main.md#effects)), z.B. durch das Erscheinen einer Nachricht oder die Ausstrahlung eines anderen Programms.
Anwendungsfall für dieses Flag wäre z.B. die Definition von vielen Staffeln einer Serie, wobei die Folgestaffeln erst verfügbar werden soll, wenn die Vorgängerstaffel verwendet wurde.

### Veröffentlichung (releaseTime)

Die Veröffentlichung eines Programms kann auch (spiel-)taggenau angegeben werden.

Beispiel: `<releaseTime year="1986" day="4" hour="12" />` - Veröffentlichung am 4. Spieltag des Jahres 1986 um 12 Uhr.

Die Steuerung ist allerdings noch feingranularer möglich.
Folgende Eigenschaften werden unterstützt.

| Name | Bedeutung |
| -----| --------- |
| year | absolute Jahreszahl |
| year_relative | Jahre relativ zum Spielbeginn (-2, +4) |
| year_relative_min | minimale absolutes Jahr |
| year_relative_max | maximale absolutes Jahr |
| day | Tag des Jahres |
| day_random_min | minimaler Zufallstag |
| day_random_max | maximaler Zufallstag |
| day_random_slope |  |
| hour | Stunde |
| hour_random_min | minimale Zufallsstunde |
| hour_random_max | maximale Zufallsstunde |
| hour_random_slope |  |

Die relativen Jahresangaben können positiv (ab Startspieljahr) und negativ (vor Startspieljahr) sein. Beispiel `<releaseTime year_relative="-4" year_relative_min="1983" year_relative_max="1995" />` - vier Jahre vor Spielstart aber zwischen 1983 und 1995.

Für Live-Programme, die nicht als "immer live" markiert sind, ist der Releasezeitpunkt auch der Zeitpunkt, zu dem das Programm live ausgestrahlt werden kann.
Später ist es nur noch eine Aufzeichnung.

### Effekte (effects)

Ab Version 0.8.2 werden auch für Programme Effekte unterstützt.
Die Syntax ist analog zu den Effekten in den Nachrichten ([Effekte](main.md#effects)).
Für Programmeffekte werden die folgenden Trigger unterstützt (`happen` wie bei den Nachrichten ist insb. nicht dabei).

* `broadcast` - der Effekt tritt zu Beginn *jeder einzelnen* Ausstrahlung ein
* `broadcastDone` - der Effekt tritt am Ende *jeder einzelnen* Ausstrahlung ein
* `broadcastFirstTime` - der Effekt tritt ein, sobald die allererste Ausstrahlung (egal welchen Spielers) beginnt
* `broadcastFirstTimeDone` - der Effekt tritt am Ende der allerersten Ausstrahlung (egal welchen Spielers) ein

```
	<effects> 
		<effect trigger="broadcastFirstTime" type="modifyProgrammeAvailability" guid="ronny-programme-livereportage-raketenstart1" />
	</effects>
```

### Modifier

Syntax siehe auch [modifiers](main.md#modifiers).
Mögliche Anpassungen sind

| Name | Bedeutung |
| -----| --------- |
| price | Preis (entspricht `price_mod`) |
| topicality::age | Einfluss Alter auf Max.-Aktualität (0.8 geringer, 1.2 stärker) |
| topicality::refresh | Erholung nach Ausstrahlung (0.8 langsamer, 1.2 schneller) |
| topicality::trailerRefresh | Erholung der Programmvorschau nach Ausstrahlung (0.8 langsamer, 1.2 schneller) |
| topicality::wearoff | Aktualitätsverlust bei Ausstrahlung (0.8 weniger, 1.2 mehr) |
| topicality::trailerWearoff | Aktualitätsverlust bei Ausstrahlung als Trailer (0.9 weniger, 1.2 mehr) |
| topicality::firstBroadcastDone | Einfluss Erstausstrahlung auf Max.-Aktualität (Default 0 keiner, 0.1 gering, 1.0 stark) |
| topicality::notLive | Einfluss "nicht mehr live" auf Max.-Aktualität (0.8 weniger, 1.2 mehr) |
| topicality::timesBroadcasted | Einfluss Ausstrahlungsanzahl auf Max.-Aktualität (0.8 weniger, 1.2 mehr) |
| callin::perViewerRevenue | Einnahmen für Call-In-Shows (0.8 weniger, 1.2 mehr) |
| betty::pointsabsolute | für den Spieler direkt vergebene Bettypunkte (100 = 1%, -50 = -0.5%) |
| betty::rawquality | Programmqualität für die automatische Berechnung der Bettypunkte (0.0-1.0) |
| betty::pointsmod | Faktor für die automatische Berechnung der Bettypunkte (0.8 weniger, 1.2 mehr) |

Beispiel: `<modifier name="topicality::age" value="1.6" />` - das Programm altert deutlich schneller als normal.

`topicality::notLive` hat ausschließlich dann einen Einfluss, wenn das Programm überhaupt ein Live-Programm war.
In diesem Fall ist auch der Default für `topicality::firstBroadcastDone` nicht 0 sondern 1.0, d.h. ein Live-Programm verliert (falls nicht anders konfiguriert) durch die Erstausstrahlung automatisch einen erheblichen Anteil an maximaler Aktualität.

Mit den betty-Modifiern kann Einfluss auf die vergebenen Punkte genommen werden.
Mit `betty::pointsabsolute` wird die hinterlegte Punktzahl vergeben egal, was die automatische Berechnung ergeben hätte (Wert 1 entspricht 0.01%, 50 entspricht 0.5%, 125 entspricht 1.25%).
`betty::rawquality` überschreibt die tatsächliche Programmqualität (zwischen 0 und 1) für die Berechnung - es könnten trotz schlechter Qualität mehr Punkte vergeben werden oder aber weniger Punkte trotz guter Qualität.
Im Gegensatz zu den absoluten Punkten wird die Aktualität des Programms berücksichtigt.


### Programmkinder (children)

Für Serien können unter dem Serienhauptknoten die Episoden 
im `children`-Knoten auch wieder als `programme` definiert werden. Beispiele siehe unten.

## spezifische Werte für programme

| **Verbreitungsweg** | Bedeutung |
| ------------------- | --------- |
| 0 | unbekannt |
| 1 | Kino |
| 2 | Fernsehen |
| 3 | Video (VHS/DVD etc.) |

(Quellcode: `TVTProgrammeDistributionChannel`)

## Wiederverwendung bestehender Programmdaten

Es ist möglich, bestehende Programmdaten wiederzuverwenden.
Das kann interessant sein, um einen "Director's Cut" oder  eine preiswertere aber dafür nur 3x ausstrahlbare Lizenz zu erstellen.
Dafür wird das zugrundeliegende Programm mit `programmedata_id` referenziert.

```XML
<programme guid="myname-programme-testprogramme-limitcopy" programmedata_id="data-myname-programme-testprogramme" product="1" fictional="1" created_by="myname">
	<!-- licence_flags="4" means: remove from collection when reaching limit -->
	<data licence_flags="4" licence_broadcast_limit="3" price_mod="0.6" />
</programme>
```

## Beispiele

### minimal 

```XML
<programme guid="auth-programme-test" product="1" licence_type="1" created_by="documentation">
	<title>
		<de>Reißerischer Titel</de>
	</title>
	<description>
		<de>Ansprechende Beschreibung.</de>
	</description>
	<staff>
		<member index="0" function="1">PersonGUID</member>
	</staff>
	<groups target_groups="32" />
	<data country="D" year="2021" distribution="2" maingenre="10" flags="16" blocks="4" />
	<ratings critics="5" speed="2" outcome="90" />
</programme>
```

Ein 2021 in Deutschland für das Fernsehen produzierter, langer Trash-Fantasyfilm, der insb. Manager anspricht.
Obwohl Kritiker nicht überzeugt waren und der Film totlangweilig ist, war er ein ziemlicher kommerzieller Erfolg; und das obwohl es keine Darsteller sondern nur einen Regisseur gab.

### Serie

```XML
<programme guid="7ad20bf5-c4c6-4237-b52a-b7b189ede0bf" product="7" licence_type="3" tmdb_id="0" imdb_id="" creator="5578" created_by="Ronny">
	<title>
		<de>Rolf Krall besucht...</de>
		<en></en>
	</title>
	<description>
		<de>Der bekannte Moderator [1|Full] ...</de>
		<en></en>
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
				<en></en>
			</title>
			<description>
				<de>Im Schatten ihrer Schwester ...</de>
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
Diese Fernsehdokumentation wurde ein Jahr vor Spielstart gedreht und spricht vor allem Rentner an.
Die grundsätzlichen Daten werden für die Serie (lizentyp 3) als ganzes definiert, die Einzelfolgen (children mit typ 2) überschreiben dann nur die gewünschten Werte (insb. Titel und Beschreibung).

### Program na żywo LIVE

WAŻNE Data wydania musi być ustawiona dla Live (data Live lub data pierwszej dostępności dla Always-Live).
W przypadku seriali na żywo najlepiej jest użyć Always-Live lub osobnej daty premiery dla każdego odcinka (w przeciwnym razie nie będzie możliwe wyemitowanie wszystkich odcinków na żywo).

DO ZROBIENIA

## DO ZROBIENIA i pytania

### Dokumentacja

* dane - obsługa i opis innych importowanych pól
* dowiedzieć się o możliwych modyfikatorach

### Ogólne

* ze względu na konfigurowalną liczbę dni, dzień z releaseTime musi być interpretowany inaczej
* Konwertowanie odwołań z innych programów w edytorze
* Wyjaśnij wpływ grupy lobbingowej: czy nadawanie programu zmienia mój wizerunek w danej grupie lobbingowej?