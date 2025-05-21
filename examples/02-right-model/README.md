# LLM Sammenligning via Openrouter

Dette projekt demonstrerer forskellene mellem forskellige LLM-modeller ved at sende den samme prompt til flere modeller via Openrouter API'en og vise deres svar side om side.

## Formål

Scriptet er designet til at vise, hvordan forskellige LLM-modeller (fra state-of-the-art til mindre kapable) reagerer på den samme prompt. Dette er nyttigt for at forstå:

1. Hvordan modellernes svar varierer i stil, indhold og kvalitet
2. Hvilke modeller der er bedst egnede til bestemte typer af opgaver
3. Hvordan man kan optimere prompts til specifikke modelarkitekturer

## Opsætning

### Forudsætninger

- Python 3.7 eller nyere
- En Openrouter API-nøgle (kan fås på [openrouter.ai](https://openrouter.ai))

### Installation

1. Opret et virtuelt miljø:

```bash
python -m venv venv
```

2. Aktiver det virtuelle miljø:

På Windows:
```bash
.\venv\Scripts\activate
```

På macOS/Linux:
```bash
source venv/bin/activate
```

3. Installer de nødvendige pakker:

```bash
pip install requests python-dotenv
```

4. Opret en `.env` fil i projektets rodmappe (ikke i examples/02-right-model mappen, men i roden af projektet) med din Openrouter API-nøgle:

```
OPENROUTER_API_KEY=din_openrouter_api_nøgle_her
```

## Kørsel af scriptet

Fra projektets rodmappe, kør et af følgende scripts:

```bash
# Kør alle sammenligninger i rækkefølge
python examples/02-right-model/run_all_comparisons.py

# Eller kør individuelle sammenligninger:

# Generel viden prompt (vedvarende energi)
python examples/02-right-model/main.py

# Kreativ prompt (digt om AI)
python examples/02-right-model/creative_comparison.py

# Teknisk prompt (prompt-optimering)
python examples/02-right-model/technical_comparison.py

# Web søgning prompt (kvantecomputere i 2025)
python examples/02-right-model/web_search_comparison.py
```

Hvert script bruger en forskellig prompt for at vise, hvordan modellerne reagerer på forskellige typer af opgaver:

1. **main.py**: Tester modellernes evne til at forklare et generelt emne (vedvarende energi)
2. **creative_comparison.py**: Tester modellernes kreative evner (skrive et digt)
3. **technical_comparison.py**: Tester modellernes tekniske forståelse (prompt-optimering)
4. **web_search_comparison.py**: Tester modellernes evne til at søge på nettet og inkorporere aktuel information (kvantecomputere i 2025)

## Forventet output

Scriptet vil:

1. Vise den prompt, der sendes til alle modeller
2. For hver model:
   - Vise modellens navn
   - Vise modellens svar på prompten
   - Adskille svarene med tydelige separatorer for nem sammenligning

Eksempel på output:

```
**********************************************************************
PROMPT: Beskriv kort fordelene ved at bruge vedvarende energi i et samfund.
**********************************************************************

Henter svar fra GPT-4o (SOTA)...

==================================================
MODEL: GPT-4o (SOTA)
==================================================
Vedvarende energi giver flere fordele for samfundet:

1. Miljømæssige fordele: Reducerer luftforurening og CO2-udledning, hvilket bekæmper klimaforandringer.

2. Økonomiske fordele: Skaber nye jobs, reducerer energiomkostninger på lang sigt og mindsker afhængigheden af importerede fossile brændstoffer.

3. Energisikkerhed: Diversificerer energiforsyningen og reducerer sårbarhed over for prissvingninger på fossile brændstoffer.

4. Sundhedsmæssige fordele: Forbedrer luftkvaliteten, hvilket fører til færre respiratoriske sygdomme og lavere sundhedsudgifter.

5. Bæredygtighed: Sikrer energiressourcer for fremtidige generationer uden at udtømme naturressourcer.
==================================================

Henter svar fra Claude 3 Opus (SOTA)...

==================================================
MODEL: Claude 3 Opus (SOTA)
==================================================
[Modellens svar vises her]
==================================================

...
```

## Tilpasning

Du kan ændre prompten eller de modeller, der sammenlignes, ved at redigere filerne:

- For at ændre prompten, opdater `prompt` variablen i bunden af den relevante fil
- For at ændre modellerne, opdater `get_models()` funktionen i den relevante fil
- For at tilføje en ny sammenligning, kopier en af de eksisterende filer og ændr prompten

Alle scripts bruger samme grundlæggende kode, men med forskellige prompts for at vise variationen i modellernes svar.
