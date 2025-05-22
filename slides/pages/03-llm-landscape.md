---
layout: section
---

# 🧠 2. LLM Landskab og Kapaciteter

<style>
h1 {
  background-color: #2B90B6;
  background-image: linear-gradient(45deg, #4EC5D4 10%, #146b8c 20%);
  background-size: 100%;
  -webkit-background-clip: text;
  -moz-background-clip: text;
  -webkit-text-fill-color: transparent;
  -moz-text-fill-color: transparent;
}
</style>

---
layout: default
---

# 🔍 Forståelse af Forskellige LLM Arkitekturer

<div grid="~ cols-2 gap-4">
<div>

<v-clicks>

## 🏗️ Foundation vs. specialiserede modeller

- 🌐 **Foundation Modeller:** 
  * 🐘 Store, generelle LLM'er
  * 📚 Trænet på omfattende datasæt
  * 🎯 Bred vifte af opgaver

- 💻 **Specialiserede Kodningsmodeller:**
  * ⚙️ Finjusteret til koderelaterede opgaver
  * 🧩 Ekspertise inden for kodegenerering
  * 🔧 Optimeret til programmeringssprog

</v-clicks>

</div>
<div>

<v-clicks>

## 🪟 Kontekstvinduer

- 📏 Maksimal mængde tekst (tokens) en LLM kan behandle
- 📈 Større kontekstvindue giver:
  * 🧐 Bedre forståelse af kodebasen
  * 🔄 Mere sammenhængende kodegenerering
  * ✅ Præcisere løsninger for komplekse problemer

</v-clicks>

<div v-click class="mt-4">

```mermaid {scale: 0.6}
graph LR
    A[Lille kontekst] --> B[Begrænset forståelse]
    C[Stor kontekst] --> D[Dyb forståelse]
    
    style A fill:#ffcccc,stroke:#ff6666,stroke-width:2px
    style B fill:#ffdddd,stroke:#ff6666,stroke-width:1px
    style C fill:#ccffcc,stroke:#66cc66,stroke-width:2px
    style D fill:#ddffdd,stroke:#66cc66,stroke-width:1px
```

</div>

</div>
</div>

<style>
h1 {
  background-color: #2B90B6;
  background-image: linear-gradient(45deg, #4EC5D4 10%, #146b8c 20%);
  background-size: 100%;
  -webkit-background-clip: text;
  -moz-background-clip: text;
  -webkit-text-fill-color: transparent;
  -moz-text-fill-color: transparent;
}
</style>

---
layout: two-cols
---

# 🔑 Nøgledifferentiatorer i Kodnings-LLM'er

<v-clicks>

## 🎯 Instruktionsfølgning vs. kreativ problemløsning
- 📝 **Instruktionsfølgning:** Nøjagtig udførelse af eksplicitte kommandoer
- 💡 **Kreativ Problemløsning:** Evne til at udtænke nye løsninger

## 🧩 Koderæsonneringsevner
- 🔍 Forståelse af logik, struktur og hensigt bag kode
- 🐛 Fejlfinding og omstrukturering
- ✨ Generering af funktionelt korrekte løsninger

</v-clicks>

::right::

<div class="ml-4">

<v-clicks>

## 🛠️ Værktøjsbrugende kapaciteter
- 🔌 Interaktion med eksterne værktøjer
- 📡 API-kald for at indsamle information
- 🤖 Udførelse af handlinger ud over tekstgenerering

## 📊 Struktureret outputgenerering
- 📋 Produktion af JSON, XML eller CSV
- 🔄 Problemfri integration med automatiserede systemer
- 📏 Konsistente, analyserbare outputs

</v-clicks>

</div>

<style>
h1 {
  background-color: #2B90B6;
  background-image: linear-gradient(45deg, #4EC5D4 10%, #146b8c 20%);
  background-size: 100%;
  -webkit-background-clip: text;
  -moz-background-clip: text;
  -webkit-text-fill-color: transparent;
  -moz-text-fill-color: transparent;
}
</style>

---
layout: default
---

# 🔬 Praktisk Sammenligning

<div grid="~ cols-2 gap-4">
<div>

<v-clicks>

## 🔄 Samme prompt, forskellige outputs
- 🎨 Forskellige LLM'er producerer distinkte kodningsstile
- 🛠️ Varierende tilgange til fejlhåndtering
- 🧩 Unikke problemløsningsstrategier

## 🐛 Fejlfindingsstrategier
- 🔧 Specifikke koderettelser
- 📚 Konceptuelle forklaringer
- 🧪 Testmetodologier

</v-clicks>

<div v-click class="mt-4 p-3 bg-blue-500 bg-opacity-10 rounded-lg border border-blue-200">
  <div class="text-blue-400 font-bold">Sammenligning:</div>
  <div class="text-sm mt-1">Forskellige modeller har unikke styrker og svagheder i kodningsscenarier! 🧩</div>
</div>

</div>
<div>

<v-clicks>

## ⚡ Optimering af prompts
- 🎯 Tilpasning til specifikke modelarkitekturer
- 🔍 Fremhævelse af klarhed for Claude
- 📋 Detaljerede eksempler for GPT-4

## 🎬 Live Demo: Sammenligning af LLM-Responser
- 💬 Forskellige responsstile og kapaciteter
- 📊 Opgavespecifikke præstationsvariationer
- 💡 Indsigter i prompt-optimering

</v-clicks>

<div v-click class="mt-4 p-3 bg-green-500 bg-opacity-10 rounded-lg border border-green-200">
  <div class="text-green-400 font-bold">Pro Tip:</div>
  <div class="text-sm mt-1">Vælg den rette model til den specifikke opgave! 🎯</div>
</div>

</div>
</div>

<style>
h1 {
  background-color: #2B90B6;
  background-image: linear-gradient(45deg, #4EC5D4 10%, #146b8c 20%);
  background-size: 100%;
  -webkit-background-clip: text;
  -moz-background-clip: text;
  -webkit-text-fill-color: transparent;
  -moz-text-fill-color: transparent;
}
</style>
