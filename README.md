# Lösningsbeskrivning
Målbilden för programmet är som följer:
* Konkret lättläst kod
* Prestandavinst vid större filer
* 

## Programmets egenskaper:
* Beroende på vilken typ av disk programmet körs har programmet potential att vara I/O-bundet
* Använder man tillräckligt många trådar som läser samtidigt från samma disk kommer problemet att vara I/O-bundet
* Implementationen är begränsad att skala upp till och med antalet filer
* Implementationen kommer att skala sämre med låga läshastigheter på disken från vilken filen hämtas
* Beräkningsbördan för processerna är jämn om storleken på filer är jämn

## Implementationsbeskrivning
* En process-pool används för att parallellisera över tillgängliga filer
* En process exekverar hela flödet för en fil:
    * Initialisera lokalt set
    * Öppna filbuffer
    * För varje rad i filen:
        * Om första bokstaven är 'r' -> lägg till i set
    * Returnera set
* Huvudprocessen samlar in resultat från beräkningsprocesserna
* Resultaten slås samman sekventiellt

## Möjliga förbättringar
* Implementera parallellisering över enskilda filer för att möjliggöra ytterligare skalning
    * Kan vara en aning problematiskt i standardpython pga GIL
    * Vill man försatt göra en så liten operation som i lekexemplet kan det vara värt att fundera på att välja ett mer lågnivåspråk för att få maximal vinst av trådningen.
        * För detta bör man sannolikt välja ett API som stödjer en smidig modell av delat minne för att undvika överflödiga kopieringar tex. C, C++ med OpenMP
* Om man indexerar filernas innehåll borde det vara lättare att effektivt parallellisera inläsningen av chunks