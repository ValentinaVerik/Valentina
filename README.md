AV_BAIGIAMASIS_DARBAS

Baigiamasis projektas Vilnius Coding School duomenų analitikos ir python programavimo pagrindų kursui

Darbo autoriai: Alina Pimpė ir Valentina Verikė

Projekto tema: Vaistų Kainų Palyginimas Internetinėse Vaistinėse

Projekto tikslas: Šis projektas skirtas analizuoti ir palyginti vaistų kainas įvairiose internetinėse vaistinėse. 
Tikslas - identifikuoti kainų skirtumus, nustatyti pigiausias ir brangiausias vaistines, bei išsiaiškinti, 
kaip kainos skiriasi priklausomai nuo vaistinės vietos, vaistų prekės ženklo ar kitų veiksnių.

Pasirinktos duomenų bazės apimtis: 198916 eilučių, 16 stulpelių.

Darbas atliktas Python kalba, panaudojant Postgres duomenų bazę ir json failą.
PROJEKTO SEKA

SKREIPINIMAS.PY

Panaudotos bibliotekos: requests, pandas, json

    Suradome analizei reikalingus duomenis apie užkrečiamas ligas iš Lietuvos atvirų duomenų portale esančios Nacionalinio visuomenės sveikatos centro užkrečiamų ligų duomenų bazės;
    Išsirinktus duomenis suformatavome .json formatu;
    Gauti duomenys buvo žodyno formato, todėl atsirinkome raktus, pagal kuriuos išsifiltravome duomenis;
    Duomenis iš skreipinimo eksportavome dataframe formatu

DATABASE.PY

Panaudotos bibliotekos: requests, psycopg2, pandas

    Duomenis iš skreipinimo.py failo importavome dataframe formatu;
    Prisijungėme prie Postgres duomenų bazės, kad galėtume sukurti duomenų bazę;
    Sukūrėme naują duomenų bazę, kad galėtume lokaliai saugoti atsisiųstus duomenis;
    Sukūrėme funkcijas, kurių pagalba duomenis sukėlėme į susikurtą duomenų bazę;
    Sukūrėme funkciją, kuri duomenis iš naujos duomenų bazės eksportavo dataframe formatu

ANALYSIS.PY

Panaudotos bibliotekos: pandas, matplotlib, seaborn, datetime, numpy

    Suradome penkias labiausiai paplitusias užkrečiamas ligas ir nusibraižėme jų grafiką;
