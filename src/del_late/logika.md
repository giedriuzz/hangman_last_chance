
# Žaidimas vyksta spėjant 10 žodžių
## Žaidimo logika
[x] Spausdinamas sveikinimas.\
[x] Spausdinamas pasirinkimo meniu.\
[x] Kelintas žodis iš kelių liko.\
[x] Visa abėcėlė.\
[x] Tuščias žodis.\
[x] Prašoma spėti raidę arba žodį
### Spėjama įrašant raides
- [x] TIKRINAMA ar įvesta raidė yra ne skaičius, ne ženklas, ne LT raidė: 
- TIKRINAMA ar įvesta daugiau nei viena raidė.
    - jei raidė 'String' tikrinama ar yra žodyje\
    - jei raidė yra žodyje\
        - spausdinama 'You guessed a letter !'
        - tikrinama ar tai ne paskutinė atspėta raidė.
        - jei paskutinė raidė:
            - raidė įrašoma į žodį ir jis atspausdinamas su atspėta raide.
            - spausdinamas sveikinimas
            - klausiama ar norime tęsti žaidimą.
        - jei nepaskutinė raidė:
            - atspausdinamas žodis.
            - spausdinama kiek liko spėjimų
            - atspausdinamos panaudotos raidės
            - prašoma įvesti kitą raidę.
- jei raidės nėra žodyje:\
    - tai įrašoma į neatspėtų raidžių listą
    - atspausdinama pakaruoklio dalis
    - tikrinama ar neatspėtų ženklų liste nevirsyja 8
        - jei skaičius didesnis nei 8 atspausdinamas pakaruoklis, žaidimas baigtas.
    - atspausdinamas žodis
    - atspausdinama kiek liko spėjimų
        - jei spėjimų skaičius daugiau nei 10, žaidimas baigtas
        - atspausdinamos panaudotos raidės
        - prašoma įvesti kitą raidę.
- jei raidė kartojasi:
    - spausdinama kad raidė jau buvo panaudota
    - 
    - jei spėjamas žodis:\
        - žodis atspėtas spausdinamas žodis ir sveikinimas, užklausiama ar žaidžiama toliau.
            - jei žaidžiama toliau tai atsitiktine tvarka žodis ištraukiamas iš DB, žaidimas tęsiasi.
        - žodis neatspėtas, spausdinamas pakaruoklis, klausiama ar spėjamas kitas žodis.





