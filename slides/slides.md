---
theme: seriph
#theme: default
background: https://source.unsplash.com/collection/94734566/1920x1080
title: AI-Vibe - Moderne AI-udviklingsværktøjer 🚀
info: |
  ## AI-Vibe Præsentation
  Moderne AI-udviklingsværktøjer og deres indvirkning på softwareudvikling.
class: text-center
drawings:
  persist: false
transition: fade-out
mdc: true
---

# ✨ AI-Vibe ✨

## Moderne AI-udviklingsværktøjer 🤖

<div @click="$slidev.nav.next" class="mt-12 py-1 px-4 rounded-lg" hover:bg="white op-20">
  Tryk på mellemrum for næste side <carbon:arrow-right class="animate-pulse"/>
</div>

<div class="abs-br m-6 text-xl flex gap-2">
  <button @click="$slidev.nav.openInEditor()" title="Åbn i Editor" class="slidev-icon-btn opacity-70 !border-none !hover:text-white">
    <carbon:edit />
  </button>
  <a href="https://github.com/slidevjs/slidev" target="_blank" class="slidev-icon-btn opacity-70 !border-none !hover:text-white">
    <carbon:logo-github />
  </a>
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
h2 {
  font-weight: 500;
  font-size: 1.5rem !important;
}
</style>

<!--
Velkommen til denne præsentation om moderne AI-udviklingsværktøjer og deres indvirkning på softwareudvikling.
-->

---
src: ./pages/01-agenda.md
---

---
src: ./pages/02-evolution.md
---

---
src: ./pages/03-llm-landscape.md
---

---
src: ./pages/04-modern-ai-tools.md
---

---
src: ./pages/05-live-demo.md
---
