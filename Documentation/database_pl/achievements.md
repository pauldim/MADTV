# Osiągnięcia (achievement)

Wpisy osiągnięć są osadzone jako lista elementów podrzędnych `achievement` w tagu `allachievements`.

```XML
<allachievements>
	<achievement guid="tvt-gameachievement-audience1" creator="5578" created_by="Ronny">
		<title>
			<de>Lokalsender</de>
			<en>Regional broadcaster</en>
			<pl>Nadawca regionalny</pl>
		</title>
		<tasks>
			<task guid="tvt-gameachievement-task-audience1" creator="5578" created_by="Ronny">
				<title>
					<de>Erreiche 250.000 Zuschauer</de>
					<en>Reach an audience of 250.000</en>
					<pl>Dotarcie do 250 000 odbiorców</pl>
				</title>
				<text>
					<de>Strahle ein Programm aus und erreiche damit mindestens 250.000 Zuschauer.</de>
					<en>Broadcast a programme and reach an audience of at least 250.000.</en>
					<pl>Nadawanie programu i dotarcie do co najmniej 250 000 widzów.</pl>
				</text>
				<data type="reachAudience" minAudienceAbsolute="250000" checkMinute="5" />
			</task>
		</tasks>
		<rewards>
			<reward guid="tvt-gameachievement-reward-audience1" creator="5578" created_by="Ronny">
				<data type="money" money="50000" />
			</reward>
		</rewards>
		<data flags="0" group="1" category="1" index="1" sprite_finished="gfx_datasheet_achievement_img_level1" sprite_unfinished="gfx_datasheet_achievement_img_level0" />
	</achievement>
</allachievements>
```

Istnieje nagroda za ukończenie jednego lub więcej zadań (zadanie).
Samo osiągnięcie często nie ma opisu (`text`), ponieważ jest on tworzony na podstawie zadania.
W powyższym przypadku, widownia (`reachAudience`) 250,000 (`minAudienceAbsolute`) musi zostać osiągnięta podczas programu (`checkminute` + `category`).
Następnie przyznawana jest nagroda w wysokości 50 000 pieniędzy (`type` + `money`).

## Właściwości osiągnięć

| Nazwa | Typ | Opis |
| ---- | --- |------------- |
| guid | Obowiązkowe | [GUID](main.md#guid), szczególnie w przypadku odwoływania się w kolejnych wiadomościach |
| creator | Metadane opcjonalne | [Standardowa właściwość](main.md#creator) |
| created_by | Metadane opcjonalne | [Standardowa właściwość](main.md#created_by) |
| comment |  informatyczny  |[Standardowa właściwość](main.md#comment) |

## Rodzaje osiągnięć

Standardowy tytuł elementu [title](main.md#title) musi być określony, tekst opisowy [text](main.md#text) jest opcjonalny i zazwyczaj jest tworzony automatycznie z zadania.

### Zadania (tasks)

Listę poszczególnych zadań, które muszą zostać wykonane, można zdefiniować w głównym węźle "zadania".
Zazwyczaj jest to dokładnie jedno zadanie.
Standardowe elementy podrzędne `title` i `text` są opcjonalne (i prawdopodobnie nie są w ogóle używane).
Zadanie ma takie same domyślne właściwości `id`, `creator` i `created_by` jak węzeł nadrzędny.

Decydującym elementem podrzędnym są dane zadania `data`.
Program używa ich do określenia, kiedy zadanie zostało zakończone.
Właściwość `type` (patrz poniżej) musi być zdefiniowana.
To, jakie inne elementy są wymagane, zależy od typu.

#### type="reachAudience"

| Nazwa | Typ | Opis |
| ---- | --- |------------- |
| minAudienceAbsolute | opcjonalny | Bezwzględna liczba widzów |
| minAudienceQuote | opcjonalny | Udział w widowni (0,2 odpowiada 20%)|
| limitToGenres | opcjonalny | Zadanie dotyczy tylko transmisji tego gatunku |
| limitToFlags | opcjonalny | Zadanie dotyczy tylko transmisji z tymi flagami |
| checkMinute | opcjonalny | Minuta, w której jest sprawdzana |
| checkHour | opcjonalny | Godzina wykonania testu |

Określając minutę, można ustalić, czy liczba widzów powinna zostać osiągnięta podczas normalnego programu, czy programu informacyjnego.
Ale nawet liczba widzów lub oceny są opcjonalne, więc można na przykład użyć gatunku i flag, aby nagrodzić gracza, który jako pierwszy nadaje program kulturalny.

`<data type="reachAudience" minAudienceAbsolute="1000000" checkMinute="5" checkHour="3">` - Um 3:05 Uhr müssen 1 Mio. Zuschauer eingeschaltet haben.

#### type="reachBroadcastArea"

| Nazwa | Typ | Opis |
| ---- | --- |------------- |
| minReachAbsolute | opcjonalny | Bezwzględna liczba widzów, którzy mają być osiągnięci w obszarze nadawania |
| minReachPercentage | opcjonalny | Procentowe pokrycie całego obszaru nadawania |

`<data type="reachBroadcastArea" minReachAbsolute="20000000">` - Obszar nadawania musi być w stanie dotrzeć do 20 milionów widzów.

#### type="BroadcastNewsShow"

Gatunek (`genre`), słowo kluczowe (`keyword`), minimalna jakość (`minQuality`) i maksymalna jakość (`maxQuality`) mogą być wymagane dla każdego slotu wiadomości.
Slot jest dołączany do identyfikatora jako liczba od 1 do 3.

`<type="BroadcastNewsShow" genre1="5" keyword2="weatherforecast" minQuality3="80">` - Program informacyjny z wiadomościami kulturalnymi w pierwszym slocie, prognozą pogody w drugim i wiadomościami o jakości co najmniej 80 w trzecim.

### Nagroda (rewards)

W głównym węźle `rewards` można zdefiniować listę indywidualnych nagród `reward`, które gracz otrzymuje po wykonaniu zadania.
Obecnie dostępne są tylko nagrody pieniężne.
Nagroda ma te same standardowe właściwości `id`, `creator` i `created_by` co węzeł nadrzędny.
Standardowe elementy podrzędne `title` i `text` dla opisu zadania są opcjonalne i mogą być określane automatycznie na podstawie danych nagrody.

Decydującym elementem podrzędnym są dane nagrody `data`.
Węzeł `data` ma następujące właściwości:



| Nazwa | Typ | Opis |
| ---- | --- |------------- |
| type | Obowiązkowe | Rodzaj nagrody (obecnie tylko pieniądze) |
| money | opcjonalny | Kwota nagrody pieniężnej|

Jeśli ponownie użyjesz tego samego `id` w nagrodzie, możesz "ponownie użyć" danych z poprzednio zdefiniowanej nagrody.

### Dane (data)

| Nazwa | Typ | Opis |
| ---- | --- |------------- |
| category | Obowiązkowe | AchievementCategory (patrz poniżej) |
| group | Obowiązkowe? | Numer dla grupowania sukcesów |
| index | Obowiązkowe | Pozycja w Grupie |
| flags | opcjonalny | Flagi (patrz poniżej) 0 i 2 najczęściej używane |
| sprite_finished | opcjonalny | Identyfikator obrazu po osiągnięciu sukcesu |
| sprite_unfinished | opcjonalny | identyfikator obrazu, jeśli sukces nie został jeszcze osiągnięty |

Sprite'y są przede wszystkim definiowane, gdy istnieją złote, srebrne i brązowe wersje tego samego osiągnięcia. (zobacz sekcję o osiągnięciach w `config/gfx.xml`)

## osiągnięcie określonych wartości

| **AchievementCategory** | Znaczenie |
|------------------------ | --------- |
| 0 | wszystkie |
| 1 | Program |
| 2 | Wiadomości |
| 4 | Obszar nadawania |
| 8 | Inne |

| **TaskType** | Znaczenie |
|------------- | --------- |
| reachAudience | osiągnięcie określonej liczby widzów/ocen podczas transmisji |
| reachBroadcastArea | osiągnąć określony rozmiar obszaru nadawania |
| BroadcastNewsShow | Wysyłanie określonego miksu wiadomości |

Zobacz `game.achievements.bmx` definicje RegisterCreators na końcu pliku.

| **AchievementFlag** | Znaczenie |
|-------------------- | --------- |
| 1 | może się nie udać (jednorazowy sukces) |
| 2 | wygrywa tylko ten, kto pierwszy wykona zadanie |

Tylko 0 i 2 są obecnie używane w bazie danych. 1 może być używany do spontanicznych osiągnięć w grze.

## Przykłady

## DO ZROBIENIA i pytania

### Dokumentacja

Jeśli zdefiniowano kilka zadań, czy muszą one zostać wykonane tego samego dnia? Na przykład, reachAudience trzy razy dla checkHour 6, 7, 8, aby sprawdzić określoną kwotę w telewizji śniadaniowej; lub program kulturalny przez cały czas największej oglądalności.

### Ogólne

* Jeśli istnieje już typ nagrody, czy nie byłoby bardziej sensowne, aby wartość była ogólna? (type="money" value="50000", type="betty" value="5", type="image" value="1")
* Flagi osiągnięć jeszcze nie w stałej klasie
* Obecna definicja checkHour może być zbyt restrykcyjna. Wydaje się, że nie jest możliwe sprawdzenie "w najlepszym czasie", tj. między 19:00 a 23:00. (Pierwszy program kulturalny w najlepszym czasie antenowym)

