****_AV_BAIGIAMASIS_DARBAS_****

Baigiamasis projektas Vilnius Coding School duomenų analitikos ir Python programavimo pagrindų kursui

Darbo autoriai: Alina Pimpė ir Valentina Verikė

Projekto tema: Vaistų kainų palyginimas internetinėse vaistinėse

Projekto tikslas: Šis projektas skirtas analizuoti ir palyginti vaistų, turinčių "Paracetamol" veikliąją medžiagą,  asortimentą ir kainas  įvairiose internetinėse vaistinėse. 
Tikslas - identifikuoti arortimento ir kainų skirtumus, nustatyti pigiausias ir brangiausias vaistines.

Pasirinktos duomenų bazės apimtis: 
Panaudotos vaistinių "Eurovaistinė", "Gintarinė' ir "100 metų" internetinių puslapių duomenų bazės. 
Apimtis: trys lentelės, viso 169 eilutės, 21 stulpeliai.

Darbas atliktas Python kalba, panaudojant bidliotekas:  requests, pandas, json, matplotlib, beautifulsoup ir seaborn.

**_PROJEKTO SEKA_**

_Duomenys.py_

Panaudotos bibliotekos: requests, pandas, json, beautifulsoup 

Suradome analizei reikalingus duomenis apie vaistų, turinčių "Paracetamol" veikliąją medžiagą Lietuvos atvirų duomenų portaluose, 
tai yra trijų internetinių vaistinių "Eurovaistinė", "Gintarinė' ir "100 metų" internetinėse puslapiose;
Išsirinktus duomenis suformatavome .json formatu;
Duomenis eksportavome dataframe formatais kiekvienai vaistinei atskirai.
Suformavome tris .csv lenteles: eurovaistineVA.csv, gintarineVA.csv ir metuVa.csv

_Analize.py_

Panaudotos bibliotekos: pandas, matplotlib, seaborn, matplotlib ir beautifulsoup

Atlikome duomenų gryninimo veiksmus: padalinome stulpelius "Pavadinimas" į 4 naujus stulpelius, pagal požymį ",".
Patikslinome tris .csv lenteles: 2eurovaistineVA.csv, 2gintarineVA.csv ir 2metuVa.csv
Apskaičiavome kainų vidurkius kiekvienoje vaistinėje.
Bandėme apjungti tris lenteles į vieną, tačiau gavome nekorektiškus dumenis, geresnis rezultatas buvo jungiant tik dvi lenteles, 
todėl darbui toliau naudojame tris atskiras lenteles.

Atlikome vaistinių asortimentų analizes ir sudarėme vizualizacijas:



EUROVAISTINĖ VAISTINĖS ASORTIMENTO VIZUALIZACIJA

![img.png](img.png)

GINTARINĖ VAISTINĖS ASORTIMENTO VIZUALIZACIJA

![img_1.png](img_1.png)

100 METŲ VAISTINĖS ASORTIMENTO VIZUALIZACIJA

![img_2.png](img_2.png)




Atlikome kainų vidurkių analizę ir atvaizdavome grafike:

TRIJŲ VAISTINIŲ VIDUTINIŲ KAINŲ PALYGINIMO VIZUALIZACIJA

![img_5.png](img_5.png)


_**ANALIZĖS IŠVADOS**_

Palyginome vaistinių vaistų, turinčių "Paracetamol" veikliąją medžiagą, asortimentą ir nustatėme, kad didžiausias vaistų asortimentas yra  vaistinėje "Eurovaistinė".
Nustatėmė, kad vaistų kainos, vertinant kainų vidurkį yra didžiausios vaistinėje 'Gintarine', o mažiausios vaistinėje '100 metų'.


