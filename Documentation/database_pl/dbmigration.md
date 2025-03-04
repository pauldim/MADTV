# Przewodnik po migracji bazy danych

## 0.8.2 -> 0.8.3

Przetwarzanie [zmiennych](variables.md) zostało zmienione w wersji 0.8.3.
Wprowadzono również dalsze porządki w składni bazy danych.
Oto przykładowa lista najważniejszych zmian.
Zazwyczaj stara składnia zmiennych została przekonwertowana na nową składnię wyrażeń.
Sprawdzenie kompletności migracji jest możliwe poprzez wyszukanie znaków procentowych w pliku wyników.
Powinny one pojawić się (oprócz komentarzy) tylko w miejscach, w których znak procentu powinien pojawić się w tekście.



* **Variablensyntax**: `%Varibalenname%` -> `${Variablenname}`
* **Referenzen auf Besetzung**: `[1|Full]` itp. -> `${.self:cast:1:"fullname"}` itp.
* **Referenzen auf Rollen**: `%ROLE1%` bzw. `%ROLENAME1%` -> `${.self:"role":1:"fullname"}` bzw. `${.self:"role":1:"firstname"}`
* **Personengenerator**: `%PERSONGENERATOR_NAME(de,2)%` itp. -> `${.persongenerator:"fullname":"de":"female"}` itp.
* **Zeitreferenzen**: `%WORLDTIME:XXX%` -> `${.worldtime:"xxx"}`
* **Zufallsstädtenamen**: `%STATIONMAP:RANDOMCITY%` -> `${.stationmap:"randomcity"}`

Odniesienia czasowe występują również w przypadku porównań i operatorów logicznych w definicji dostępności filmów/newsów/szablonów scenariuszy.

* **Porównanie =**: `X=Y` -> `${.eq:X:Y}`
* **Porównanie <=**: `X<=Y` -> `${.lte:X:Y}`
* **Porównanie <**: `X<Y` -> `${.lt:X:Y}`
* **Porównanie >=**: `X>=Y` -> `${.gte:X:Y}`
* **Porównanie >**: `X>Y` -> `${.gt:X:Y}`
* **logiczne lub**: `X||Y` -> `${.or:X:Y}`
* **logiczne i**: `X&amp;&amp;Y` -> `${.and:X:Y}`

Ponadto zmieniono nazwy atrybutów XML, aby wyraźnie oddzielić numeryczny identyfikator w grze od alfanumerycznego identyfikatora GUID używanego w bazie danych:

* `person id=` -> `person guid=`
* `programme id=` -> `programme guid=`
* `programmedata_id=` -> `programmedata_guid=`
* `news id=` -> `news guid=`
* `thread_id=` -> `thread_guid=`
* `achievement id=` -> `achievement guid=`
* `task id=` -> `task guid=`
* `reward id=` -> `reward guid=`
* `ad id=` -> `ad guid=`

Za pomocą poniższego skryptu (Linux), niektóre z tych zamian mogą być wykonywane automatycznie.
Stara składnia dla `<dostępność ... script=...` musi zostać dostosowana ręcznie do nowej składni wyrażenia!

```
#!/bin/bash
# skrypt do migracji większości starych zmiennych/wyrażeń do nowej składni
# oparty na kodzie autorstwa Ronny'ego - patrz https://github.com/TVTower/TVTower/pull/1189
# wyrażenia skryptu dostępności muszą być aktualizowane ręcznie
# szukaj "script=" w plikach bazy danych

# Znajduje wszystkie pliki XML w bieżącym katalogu i podkatalogach
find . -type f -name "*.xml" | while read -r file; do
    # Zastąp referencje do obsady [x|y] 
    # z prawidłowym formatem, w tym konkretnymi nazwami (imię, nazwisko, itp.).
    sed -E -i '
    s/\[([0-9]+)\|([Ff]ull)\]/${.self:\"cast\":\1:\"fullname\"}/g;
    s/\[([0-9]+)\|([Ll]ast)\]/${.self:\"cast\":\1:\"lastname\"}/g;
    s/\[([0-9]+)\|([Nn]ick)\]/${.self:\"cast\":\1:\"nickname\"}/g;
    s/\[([0-9]+)\|([Ff]irst)\]/${.self:\"cast\":\1:\"firstname\"}/g
    ' "$file"

    # Zastąpienie odniesień do ról (teraz opartych na indeksie, więc liczba jest zmniejszana o 1)
    # Pętla przez numery od 1 do 15 dla symboli zastępczych ROLENAME i ROLE
    for i in $(seq 1 15); do
        # Oblicz (i-1) - przestarzałe
        j=$((i))

        sed -E -i "s/%ROLENAME$i%/\${.self:\"role\":$j:\"firstname\"}/g" "$file"
        sed -E -i "s/%ROLE$i%/\${.self:\"role\":$j:\"fullname\"}/g" "$file"
    done

    # Zastąp wpisy generatora osób
    sed -E -i 's/%PERSONGENERATOR_([a-zA-Z]+)\(([uU][nN][kK]),([0-9])\)%/\${.persongenerator:\"\L\1\":\"\":\3}/g' "$file"
    sed -E -i 's/%PERSONGENERATOR_([a-zA-Z]+)\(([a-zA-Z]+),([0-9])\)%/\${.persongenerator:\"\L\1\":\"\L\2\":\3}/g' "$file"
    sed -E -i 's/\$\{.persongenerator:([^:]*):([^:]*):1\}/${.persongenerator:\1:\2:\"male\"}/g' "$file"
    sed -E -i 's/\$\{.persongenerator:([^:]*):([^:]*):2\}/${.persongenerator:\1:\2:\"female\"}/g' "$file"
    sed -E -i 's/\$\{.persongenerator:\"name\"/${.persongenerator:\"firstname\"/g' "$file"

    # Zastąp czas światowy (niekompletny!!)
    sed -E -i 's/%WORLDTIME:YEAR%/${.worldtime:\"year\"}/g' "$file"
    sed -E -i 's/%WORLDTIME:GAMEDAY%/${.worldtime:\"dayplaying\"}/g' "$file"

    # Zastąp losowe miasto
    sed -E -i 's/%STATIONMAP:RANDOMCITY%/${.stationmap:"randomcity"}/g' "$file"

    # Zastąpienie regularnych odwołań do zmiennych %name% przez ${name} 
    # gdzie nazwa może zawierać litery, cyfry lub podkreślenia
    sed -E -i 's/%([a-zA-Z0-9_]+)%/\${\1}/g' "$file"

    # Przywróć zastąpione instancje komentarzy (zwykle w adresie URL ze znakami specjalnymi).
    sed -E -i 's/\$\{C3\}/%C3%/g' "$file"
    sed -E -i 's/\$\{E2\}/%E2%/g' "$file"
    sed -E -i 's/\$\{C8\}/%C8%/g' "$file"

	# Refaktoryzacja nazw identyfikatorów
	sed -E -i 's/programme id=/programme guid=/g' "$file"
	sed -E -i 's/person id=/person guid=/g' "$file"
	sed -E -i 's/news id=/news guid=/g' "$file"
	sed -E -i 's/thread_id=/thread_guid=/g' "$file"
	sed -E -i 's/achievement id=/achievement guid=/g' "$file"
	sed -E -i 's/task id=/task guid=/g' "$file"
	sed -E -i 's/reward id=/reward guid=/g' "$file"
	sed -E -i 's/ad id=/ad guid=/g' "$file"
	sed -E -i 's/programme id=/programme guid=/g' "$file"
	sed -E -i 's/programmedata_id=/programmedata_guid=/g' "$file"
    echo "Processed $file"
done


#fragmenty zastępujące pojedynczy krok
#find . -type f -name "*.xml" -print0 | xargs -0 sed -i -e 's/%STATIONMAP:RANDOMCITY%/${.stationmap:"randomcity"}/g'
#find . -type f -name "*.xml" -print0 | xargs -0 sed -i -e 's/%\([[:alnum:]_]*\)%/${\1}/g'
```