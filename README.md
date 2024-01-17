# Filmas izvēle
## Situācijas apraksts
Viens no visizplatītākajiem veidiem, kā atpūsties, ir paskatīties filmu. Mums par laimi filmu industrija turpina attīstīties un priecē mūs ar jaunām filmām, stāstiem un aktieriem. Taču tik liela izvēle bieži noved pie tā, ka filmas atrašana aizņem daudz laika un samazina vēlmi kaut ko noskatīties.
## Projekta uzdevums
Samazināt laiku, kas nepieciešams, lai atrastu piemērotu filmu. Kad ir vēlme kaut ko paskatīties, bet nav laika izvēlēties filmu, lasot anotācijas, komentārus un skatoties treilerus, var uzticēt filmas izvēli laimes ratam. Izmantojot pasaulē populārāko un uzticamāko filmu, televīzijas un slavenību satura avotu — IMDb, programma izveidos sarakstu no lietotājam piedāvātam divām opcijām:
- izvēlas meklēt filmas noteiktā žanrā, lai atlasītu filmas, kas vislabāk atbilst viņu vēlmēm;
- pilnībā uzticēt izvēli liktenim un izmantos 250 populārākas filmas.

Pēc tam šo sarakstu programma ielādēs ritenī un tas nejaušā veida izvēlēsies filmu, tomēr ja filma ir jau redzēta, tad šo filmu izdzēsis no saraksta un griezis riteni atkal. 

## Izmantotas Python bibliotēkas
- Selenium - Elementu meklēšana pēc identifikatora, klases un nosaukuma, kas ļauj automatizēt darbības, kas saistītas ar noklikšķināšanu uz pogām, elementu atlasi nolaižamajos sarakstos un teksta ievadīšanu.
- Selenium webdriver - ļauj kontrolēt tīmekļa pārlūkprogrammu (Chrome) , atvērt pārlūkprogrammas logus.
- Time - aizkavē darbības izpildi uz noteiktu sekunžu skaitu.
- Expected conditions – konkrētu notikumu vai stāvokļu gaidīšana.
- WebDriverWait - nodrošina gaidīšanas režīmu, līdz tiks izpildīts noteikts nosacījums, pirms turpināt koda izpildi.
- Keys - ierakstīšana ievades laukos.
- Service - ChromeDriver servera palaišana.
- By – elementu atrašana.
