# 2. LLM Landskab og Kapaciteter (45 minutter)

### Forståelse af Forskellige LLM Arkitekturer
- Foundation modeller vs. specialiserede kodningsmodeller
  * **Foundation Modeller:** Store, generelle LLM'er trænet på omfattende datasæt, i stand til at udføre en bred vifte af opgaver, herunder kodning, men ikke specifikt optimeret til det.
  * **Specialiserede Kodningsmodeller:** LLM'er der er finjusteret eller specifikt designet til koderelaterede opgaver, ofte med ekspertise inden for kodegenerering, fejlfinding og forståelse af programmeringssprog.
- GPT-4, Claude, Llama: styrker og svagheder ved kodning
  * **GPT-4 (OpenAI):** Kendt for stærk generel ræsonnement, kreativ kodegenerering og forståelse af komplekse instruktioner. Kan nogle gange producere ordrig eller mindre optimeret kode.
  * **Claude (Anthropic):** Udmærker sig i konversationsforståelse, sikkerhed og generering af klar, veldokumenteret kode. Kan være mere konservativ i sin kodegenerering.
  * **Llama (Meta):** Open-source modeller, der kan finjusteres til specifikke kodningsopgaver, hvilket giver fleksibilitet og kontrol. Ydeevnen varierer baseret på finjustering og modelstørrelse.
- Kontekstvinduer og deres indvirkning på udviklingsopgaver
  * **Kontekstvindue:** Den maksimale mængde tekst (tokens), som en LLM kan behandle på én gang. Et større kontekstvindue giver modellen mulighed for at forstå mere af kodebasen eller problembeskrivelsen, hvilket fører til mere sammenhængende og præcis kodegenerering, især for større projekter eller komplekse problemer.

### Nøgledifferentiatorer i Kodnings-LLM'er
- Instruktionsfølgning vs. kreativ problemløsning
  * **Instruktionsfølgning:** En LLM's evne til nøjagtigt at udføre eksplicitte kommandoer eller krav i en prompt, afgørende for forudsigelig kodegenerering.
  * **Kreativ Problemløsning:** LLM'ens kapacitet til at udtænke nye løsninger, foreslå alternative tilgange eller generere kode til dårligt definerede problemer, der går ud over direkte instruktioner.
- Koderæsonneringsevner på tværs af forskellige modeller
  * Dette refererer til en LLM's evne til at forstå logikken, strukturen og hensigten bag kode, hvilket gør den i stand til at fejlfinde, omstrukturere og generere funktionelt korrekte og effektive løsninger.
- Værktøjsbrugende og API-kaldende kapaciteter
  * Avancerede LLM'er kan interagere med eksterne værktøjer (f.eks. kompilere, linters, databaser) eller kalde API'er for at indsamle information, udføre kode eller udføre handlinger, hvilket udvider deres anvendelighed ud over tekstgenerering.
- Struktureret outputgenerering
  * Moderne LLM'er er gode til at producere strukturerede svar som JSON, XML eller CSV, hvilket muliggør problemfri integration med automatiserede systemer, dataflow og programmatiske arbejdsgange. Denne kapacitet er afgørende for at skabe konsistente, analyserbare outputs, der kan forbruges direkte af applikationer uden yderligere behandling.

### Praktisk Sammenligning
- Samme prompt, forskellige outputs: analyse af modelresponser
  * Sammenligning af kode genereret af forskellige LLM'er for en identisk prompt afslører deres distinkte kodningsstile, fejlhåndtering og tilgang til problemløsning, hvilket fremhæver deres individuelle styrker.
- Fejlfindingsstrategier på tværs af forskellige LLM'er
  * Forskellige LLM'er kan anvende varierede tilgange til fejlfinding, fra at foreslå specifikke koderettelser til at give konceptuelle forklaringer af fejl eller anbefale testmetodologier.
- Optimering af prompts til specifikke modelarkitekturer
  * Tilpasning af prompts for at udnytte de unikke styrker og afbøde svaghederne ved en bestemt LLM-arkitektur (f.eks. at fremhæve klarhed for Claude eller give detaljerede eksempler for GPT-4) kan markant forbedre outputkvaliteten.

#### Live Demo: Sammenligning af LLM-Responser
For at demonstrere disse koncepter i praksis har vi skabt en live demo i mappen `examples/02-right-model/`. Denne demo giver dig mulighed for at sende identiske prompts til flere LLM-modeller via OpenRouter og sammenligne deres svar side om side.

**Hvad du kan forvente i demoen:**

1. **Forskellige responsstile og kapaciteter**
   * Observer hvordan modeller som GPT-4o, Claude 3 Opus, Llama 3 og Mistral 7B reagerer forskelligt på samme prompt
   * Bemærk variationer i skrivestil, responsstruktur, detaljeniveau og ræsonnementsmønstre

2. **Opgavespecifikke præstationsvariationer**
   * Demoen inkluderer fire forskellige typer prompts for at fremhæve, hvordan modeller præsterer på tværs af opgavetyper:
     - Generel viden (`main.py`): Tester faktuel genkaldelse om et specifikt emne
     - Kreativ skrivning (`creative_comparison.py`): Tester evnen til at generere et kort digt
     - Teknisk forklaring (`technical_comparison.py`): Tester evnen til at forklare komplekse koncepter
     - Websøgningsintegration (`web_search_comparison.py`): Tester evnen til at inkorporere realtidsinformation

3. **Indsigter i prompt-optimering**
   * Ved at sammenligne svar kan du identificere, hvilke modeller der udmærker sig ved hvilke opgaver
   * Denne information hjælper med at optimere prompts til specifikke modelarkitekturer
   * For eksempel kan du bemærke, at Claude giver mere detaljerede forklaringer, mens GPT-4 udmærker sig ved kreative opgaver

**Kørsel af demoen:**
For at køre demoen, følg instruktionerne i filen `examples/02-right-model/README.md`. Du skal bruge en OpenRouter API-nøgle og et grundlæggende Python-miljø.
