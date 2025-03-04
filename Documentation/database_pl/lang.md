# Lokalizacja

Od wersji 0.8.1 możliwe jest lokalizowanie danych osób i ról.
Podobnie jak w przypadku tytułów filmów, możliwe jest zdefiniowanie pisowni lub wariantów nazw specyficznych dla danego języka.
Lokalizacja odbywa się w oddzielnych plikach, a nie w "głównych plikach" bazy danych.

Od wersji 0.8.3 możliwe jest również definiowanie zmiennych globalnych.
Umożliwia to standaryzację nazewnictwa (np. dla nazw marek) bez konieczności przechowywania tych samych stałych tekstów w każdym miejscu.
Odniesienie jest analogiczne do specyficznego dla wpisu [variables](variables.md) - `${nameGlobalVariable}`.
Domyślnym językiem jest angielski, tzn. wszystkie zmienne globalne są przechowywane w pliku językowym dla języka angielskiego.
Jeśli istnieją specyficzne dla języka, odbiegające wartości, odpowiednie zmienne są nadpisywane w odpowiednim pliku językowym.



Istnieje jeden plik `<skrót języka>.xml` dla każdego języka w katalogu `lang`, który znajduje się w katalogu bazowym bazy danych (np. `res/database/Default/lang/en.xml` dla języka angielskiego lub `res/database/Default/lang/fr.xml` dla języka francuskiego).
Skróty językowe są takie same jak te używane w plikach właściwości pod `res/lang` lub w tagach językowych dla tytułów filmów/zmiennych.

Standardowym językiem jest angielski.
Oznacza to, że dla każdego wpisu lokalizacji utworzonego dla danego języka musi istnieć również wpis dla języka angielskiego.

Wpisy person są osadzone jako lista elementów podrzędnych `person` w tagu `persons`, wpisy role jako lista elementów podrzędnych `programmerole` w tagu `programmeroles`.

## Charakterystyka osoby

| Nazwa | Typ | Opis |
| ---- | --- |------------- |
| guid | Obowiązkowe | Identyfikator GUID istniejącej osoby |
| first_name | Opcjonalnie | Imię |
| last_name | Opcjonalnie | Nazwisko |
| nick_name | Opcjonalnie | Pseudonim |
| title | Opcjonalnie | Tytuł |

Brakujące/puste wpisy również prowadzą do nadpisania oryginalnej wartości.
Dlatego nie można po prostu nadpisać imienia i pozostawić nazwiska bez zmian.

## Właściwości programmerole

| Nazwa | Typ | Opis |
| ---- | --- |------------- |
| guid | Obowiązkowe | Identyfikator GUID istniejącej roli |
| first_name | Opcjonalnie | Imię |
| last_name | Opcjonalnie | Nazwisko |
| nick_name | Opcjonalnie | Pseudonim |
| title | Opcjonalnie | Tytuł |

Brakujące/puste wpisy również prowadzą do nadpisania oryginalnej wartości.
Nie jest zatem możliwe proste nadpisanie imienia i pozostawienie nazwiska bez zmian.

## Globalne_zmienne

Oprócz miejsca, w którym są zdefiniowane, zmienne globalne są podobne do zmiennych specyficznych dla wpisu.
Mają nazwę i ("niezależną od języka") wartość `<name>value</name>`.
Ze względu na podział plików według języka, nie ma tu podtagów specyficznych dla języka.
Dostęp do zmiennych można uzyskać z dowolnego miejsca, w którym dozwolone są wyrażenia, nie tylko tam, gdzie można zdefiniować zmienne.

Na przykład, nie można definiować zmiennych we wpisach reklamowych, ale można uzyskać dostęp do zmiennych globalnych.
Składnia odpowiada dostępowi do normalnych zmiennych - `${name}` dla dostępu do zmiennej z góry.

Istnieje jednak ważna różnica w stosunku do zmiennych specyficznych dla wpisu.
Zmienne globalne nie obsługują alternatyw `a|b|c`, w których jedna z wartości jest wybierana losowo podczas ewaluacji.
Byłoby to również sprzeczne z celem zmiennych globalnych - spójnym nazewnictwem w całej bazie danych.
Warunki itp. są dozwolone.



## Przykład_pliku_lokalizacyjnego

```XML
<?xml version="1.0" encoding="utf-8"?>
<tvtdb>
	<persons>
		<person guid="common-amateur-actors" last_name="Laiendarsteller" nick_name="Laiendarsteller" />
		<person guid="common-amateur-director" first_name="" last_name="Regiepraktikant" nick_name="Regiepraktikant" />
/>
	</persons>
	<programmeroles>
		<programmerole guid="script-roles-ron-001" first_name="Vincent" last_name="Graf" title="" />
	</programmeroles>
	<globalvariables>
		<macrohard>Macrohard</macrohard>
		<germanCurrency>${.gte:${.worldtime:"year"}:2002:"Euro":"DM"}</germanCurrency>
	<globalvariables>
</tvtdb>
```