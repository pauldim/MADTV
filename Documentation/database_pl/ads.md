# Reklama (ad)

Wpisy reklamowe są osadzone w tagu `allads` jako lista elementów podrzędnych `ads`.

```XML
<allads>
	<ad guid="527e41eb-a641-49b9-a521-e921ec652e23">
		<title>
			<de>Plöpp-Bier</de>
			<en>Pop'Beer</en>
			<pl>Piwo Pop</pl>
		</title>
		<description>
			<de>Prickelndes Hopfengold...</de>
			<en>Tingling hop gold...</en>
			<pl>Chmielowe złoto...</pl>
		</description>
		<conditions min_audience="1.56" min_image="4" target_group="256" pro_pressure_groups="0" contra_pressure_groups="0"/>
		<data quality="15" repetitions="3" duration="3" profit="976" penalty="1550" infomercial_profit="97" fix_infomercial_profit="1"/>
	</ad>
</allads>
```

Aby wypełnić ten kontrakt reklamowy, określona liczba (`min_audience`) mężczyzn (`target_group`) w zależności od zasięgu musi być wyświetlony trzy razy (`repititions`) w ciągu trzech dni (`duration`).
Aby reklama była w ogóle oferowana, wymagany jest obraz o wartości co najmniej 4% (`min_image`).


## Właściwości reklam

| Nazwa | Typ | Opis |
| ---- | --- |------------- |
| guid | Obowiązkowe | [GUID](main.md#guid), szczególnie w przypadku odwoływania się w kolejnych wiadomościach |
| creator | Metadane opcjonalne | [Standardowa właściwość](main.md#creator) |
| created_by | Metadane opcjonalne | [Standardowa właściwość](main.md#created_by) |
| comment |  informatyczny  |[Standardowa właściwość](main.md#comment) |

## Elementy podrzędne reklam

Standardowe elementy dla tytułu [Tytuł](main.md#title), opisu [Opis](main.md#description)
są obowiązkowe, podobnie jak opisane poniżej elementy dla warunków ([Warunki](ads.md#Warunki)) i danych specyficznych dla reklamy ([Dane](ads.md#Dane)).
[Dostępność](time.md#Dostępność) może być używana do kontrolowania, kiedy reklama jest ogólnie dostępna.

### Warunki

| Nazwa | Typ | Opis |
| ---- | --- |------------- |
| min_audience | opcjonalnie | Minimalny udział w widowni |
| min_image | opcjonalnie | Minimalny wizerunek stacji (0-100) |
| max_image | opcjonalnie | Maksymalny wizerunek stacji (0-100) |
| target_group | opcjonalnie | [Grupy docelowe](main.md#Grupy_docelowe) dla liczby widzów, którzy mają zostać osiągnięci |
| allowed_genre | opcjonalnie | dozwolone gatunki główne [Gatunek główny](main.md#Gatunek_główny) |
| prohibited_genre | opcjonalnie | zabroniony gatunek [Gatunek główny](main.md#Gatunek) (jeszcze nieobsługiwane) |
| allowed_programme_flag | opcjonalnie | dozwolona flaga programu [Flagi programu](main.md#Flagi_programu) |
| prohibited_programme_flag | opcjonalnie | zabroniona flaga programu [Flagi programu](main.md#Flagi_programu) (jeszcze nieobsługiwane) |

Minimalny udział widowni "min_audience" odnosi się do możliwej widowni w bieżącym obszarze nadawania.
Przełączniki zakazanych gatunków i flag nie są jeszcze obsługiwane przez program.

### Dane

| Nazwa | Typ | Opis |
| ---- | --- |------------- |
| available | opcjonalnie | dostępny (wartość prawdy) |
| type | opcjonalnie | Typ kontraktu (0=normalny, 1=tylko dla wydarzeń związanych z grami) |
| quality | opcjonalnie | Jakość (domyślnie 10) |
| repetitions | Obowiązkowe | Liczba powtórzeń |
| duration | Obowiązkowe | Liczba dozwolonych dni |
| profit | Obowiązkowe | Podstawa obliczania wydajności na spot |
| penalty | Obowiązkowe | Podstawa naliczania kary umownej za każdy punkt|
| fix_price | opcjonalnie | Wartość prawdy, zysk i kara nie skalują się z zakresem (poziomem). |
| infomercial | opcjonalnie | dozwolony jako stały program reklamowy (wartość prawdy) |
| infomercial_profit | opcjonalnie | Podstawa obliczania wydajności Infomercial |
| fix_infomercial_profit | opcjonalnie | Wartość prawdy, przychody z reklam nie są obliczane dynamicznie |
| blocks | opcjonalnie | Liczba wyemitowanych bloków reklam|
| pro_pressure_groups | opcjonalnie | adresowana grupa lobbystów [Grupa lobbystów](main.md#Grupy_lobbystów) |
| contra_pressure_groups | opcjonalnie | przeciwna grupa lobbystów [Grupa lobbystów](main.md#Grupy_lobbystów) |

Jeśli wartości nie zostały oznaczone jako niezmienne (`fix_price`), wartość `profit` jest mnożona przez współczynnik obliczany na podstawie obrazu, zasięgu, jakości itp.
Dlatego nawet wysoka wartość `profit` może skutkować niższym przychodem na spot niż niska wartość `profit`.


### Modyfikatory

Składnia patrz także [Modyfikatory](main.md#modifiers).
Możliwe atrybuty to

| Nazwa | Znaczenie |
| -----| --------- |
| topicality::infomercialRefresh | Odzyskiwanie aktualności po emisji jako reklama (0,8 wolniej, 1,2 szybciej) |
| topicality::infomercialWearoff | Utrata aktualności po emisji jako reklama informacyjna (0,8 mniej, 1,2 więcej) |

Przykład: `<modifier name="infomercialWearoff" value="0.7" />`

Jednak wpływ modyfikatorów (zwłaszcza zużycia) powinien być praktycznie nieistotny, ponieważ obliczone wartości praktycznie zawsze znajdują się poza limitami min-max ze względu na niską liczbę widzów.

## DO ZROBIENIA i pytania

### Dokumentacja

* sprawdź ponownie z importem DB
* Zysk wpływa na nagrodę za spot - opisz bardziej szczegółowo
* Opisz zysk z reklamy bardziej szczegółowo
* Jakość danych=sprawdź ponownie wpływ (nie tylko infomercial)

### Ogólne

* warunki: pro_pressure_groups, contra_pressure_groups, forbidden..., jeszcze nie ocenione
* kod źródłowy nadal obsługuje efekty i modyfikatory, które nie występują w bieżącej bazie danych i nie są obsługiwane przez gramatykę
* allowed/prohibited_genre nie powinien być raczej listą. Biorąc pod uwagę dużą liczbę gatunków, nie zawsze ma sens zezwalanie/zakazywanie tylko jednego.