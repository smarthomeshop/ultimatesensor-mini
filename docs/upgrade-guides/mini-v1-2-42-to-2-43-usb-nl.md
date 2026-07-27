# E-mail: verplichte UltimateSensor Mini V1 USB-C-update

> **Status:** gereed voor versie 2.43 nadat de releasecontrole onderaan is
> afgerond.

## Onderwerp

Actie vereist: flash de nieuwe UltimateSensor Mini V1-firmware via USB-C

## E-mailtekst

Beste klant,

Er is een nieuwe productieversie van de firmware voor de UltimateSensor Mini
V1 beschikbaar: versie 2.43.

**Belangrijk: deze update moet éénmalig via USB-C worden geïnstalleerd. Gebruik
hiervoor [smarthomeshop.io/firmware](https://smarthomeshop.io/firmware). Voer
deze overgang niet uit via de draadloze OTA-update in Home Assistant.**

De interne firmwarebasis verandert van Arduino naar ESP-IDF. Daarom is voor
deze specifieke overgang een volledige USB-C-installatie nodig. Nadat versie
2.43 via USB-C is geïnstalleerd, werken volgende firmware-updates weer gewoon
draadloos.

Dit geldt voor apparaten met de gewone V1-productiefirmware 2.42 of ouder én
voor apparaten met de eerdere V1-betafirmware. De aparte beta wordt niet meer
voortgezet: kies bij het flashen altijd een normale **UltimateSensor Mini V1**
productievariant.

Deze versie brengt de verbeteringen uit de eerdere betafirmware naar de gewone
V1-firmware. De belangrijkste vernieuwingen zijn:

- lokale wake-wordherkenning op de sensor;
- vernieuwde LD2450-aanwezigheidsdetectie op basis van de standaard
  ESPHome-integratie;
- live positietracking van maximaal drie personen;
- vier vrije polygonzones in plaats van alleen rechthoekige zones;
- twee uitsluitingszones om ongewenste detectie te negeren;
- twee virtuele tellijnen met in/uit-richting;
- een permanente personenteller;
- lokaal opgeslagen opstartgeluid, zonder download tijdens het opstarten.

De update blijft beschikbaar voor zowel de Basic- als Complete-uitvoering. De
Complete-uitvoering bevat ook de fijnstofmetingen. De lokale Home
Assistant-firmware en de SmartHomeShop App-firmware blijven afzonderlijk
beschikbaar.

## Voorbereiding

1. Maak schermafbeeldingen van uw huidige zonegrenzen en noteer eventuele
   vertragingen.
2. Controleer in Home Assistant welke automatiseringen en dashboards gebruik
   maken van aanwezigheid, zones of LD2450-doelposities.
3. Noteer of u de Basic- of Complete-firmware en de lokale of SmartHomeShop
   App-variant gebruikt.
4. Zorg voor een USB-C-kabel die ook data ondersteunt. Sommige laadkabels
   ondersteunen geen gegevensoverdracht.

## Installeren via USB-C

1. Sluit de UltimateSensor Mini V1 rechtstreeks met USB-C aan op een computer.
2. Open Chrome of Edge en ga naar
   [smarthomeshop.io/firmware](https://smarthomeshop.io/firmware).
3. Kies **UltimateSensor Mini V1**. Kies niet voor V2.
4. Kies **Basic** wanneer uw model geen fijnstofsensor heeft, of **Complete**
   wanneer uw model wel fijnstof meet.
5. Kies vervolgens de lokale Home Assistant-versie of de SmartHomeShop
   App-versie die u nu gebruikt.
6. Start de installatie en laat de USB-C-kabel aangesloten totdat de website
   meldt dat het flashen gereed is.
7. Verbind de sensor opnieuw met WiFi en voeg hem zo nodig opnieuw toe aan Home
   Assistant.

Door de volledige USB-C-installatie kunnen opgeslagen WiFi- en
zone-instellingen worden gewist. Houd uw WiFi-wachtwoord daarom bij de hand.

## Wat verandert er voor zones?

De oude rechthoekige zone-instellingen worden niet automatisch omgezet naar de
nieuwe polygonzones. Na de update moet u uw zones daarom opnieuw tekenen of
instellen.

De nieuwe tracking ondersteunt:

- `Polygon Zone 1` tot en met `Polygon Zone 4`;
- `Polygon Exclusion 1` en `Polygon Exclusion 2`;
- `Entry Line 1` en `Entry Line 2`;
- `People Count`;
- `Last Crossing Direction`.

Gebruik de SmartHomeShop Room Designer in Home Assistant om de zones en
tellijnen naar de sensor te sturen. Raadpleeg hiervoor de actuele documentatie
op [docs.smarthomeshop.io](https://docs.smarthomeshop.io).

## Controle na de update

1. Wacht tot de sensor opnieuw met WiFi en Home Assistant is verbonden.
2. Controleer of temperatuur, luchtvochtigheid, CO2, VOC, licht en aanwezigheid
   actuele waarden tonen.
3. Controleer bij een Complete-model ook de fijnstofwaarden.
4. Loop door de ruimte en controleer of de drie LD2450-doelposities veranderen.
5. Stel de polygonzones en eventuele uitsluitingszones opnieuw in.
6. Controleer automatiseringen en dashboards. Werk entiteitsnamen bij wanneer
   Home Assistant een nieuwe of gewijzigde entiteit heeft aangemaakt.
7. Test het wake word en de spraakassistent.

Heeft u hulp nodig? Gebruik dan de handleidingen op
[docs.smarthomeshop.io](https://docs.smarthomeshop.io) of neem contact op met
SmartHomeShop Support.

Met vriendelijke groet,

SmartHomeShop

## Interne releasecontrole

Deze e-mail mag pas worden verstuurd nadat:

- de productieprojectnaam `smarthomeshop.ultimatesensor_mini` is gebleven;
- de standaard apparaatnaam `ultimatesensor-mini` is gebleven;
- Basic lokaal compileert;
- Complete lokaal compileert;
- Basic SmartHomeShop App compileert;
- Complete SmartHomeShop App compileert;
- de USB-C-installatie vanaf een apparaat met productieversie 2.42 is getest;
- Home Assistant geen tweede apparaat aanmaakt;
- de firmwarevariantkiezer naar alle vier productie-manifests verwijst;
- bestaande belangrijke entiteitsnamen waar mogelijk zijn behouden;
- de nieuwe versie en release notes op GitHub en GitHub Pages staan.
