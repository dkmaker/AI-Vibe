import os
import requests
import json
import asyncio
import time
from dotenv import load_dotenv

# Indlæs miljøvariabler fra .env filen
# (Load environment variables from .env file)
def load_api_key():
    """
    Indlæser OpenRouter API-nøglen fra .env filen.
    (Loads the OpenRouter API key from the .env file.)
    """
    load_dotenv()
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise ValueError("OPENROUTER_API_KEY ikke fundet i .env filen. Opret venligst en .env fil med din API-nøgle.")
    return api_key

# Definér modeller til sammenligning
# (Define models for comparison)
def get_models():
    """
    Returnerer en liste af modeller til sammenligning, fra SOTA til mindre kapable.
    (Returns a list of models for comparison, from SOTA to less capable.)
    """
    return [
        {"id": "openai/gpt-4o", "name": "GPT-4o (SOTA)"},
        {"id": "anthropic/claude-3-opus", "name": "Claude 3 Opus (SOTA)"},
        {"id": "meta-llama/llama-3-70b-instruct", "name": "Llama 3 70B (Mellem)"},
        {"id": "mistralai/mistral-7b-instruct", "name": "Mistral 7B (Mindre)"}
    ]

# Kald OpenRouter API
# (Call OpenRouter API)
async def call_openrouter_api(model_id, prompt, api_key):
    """
    Kalder OpenRouter API med den angivne model og prompt.
    (Calls the OpenRouter API with the specified model and prompt.)
    
    Args:
        model_id (str): Model ID til OpenRouter
        prompt (str): Prompten der skal sendes til modellen
        api_key (str): OpenRouter API-nøgle
        
    Returns:
        str: Modellens svar
    """
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": model_id,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 500
    }
    
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=data
        )
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Fejl ved kald til {model_id}: {str(e)}"

# Vis svar fra modellen
# (Display response from the model)
def display_response(model_name, response_text):
    """
    Viser modellens svar i konsollen med formatering.
    (Displays the model's response in the console with formatting.)
    
    Args:
        model_name (str): Navnet på modellen
        response_text (str): Modellens svar
    """
    separator = "=" * 50
    print(f"\n{separator}")
    print(f"MODEL: {model_name}")
    print(f"{separator}")
    print(response_text.strip())
    print(f"{separator}\n")

# Hovedfunktion til at køre sammenligningen
# (Main function to run the comparison)
async def run_comparison(prompt):
    """
    Kører sammenligningen af forskellige LLM'er med den samme prompt.
    (Runs the comparison of different LLMs with the same prompt.)
    
    Args:
        prompt (str): Prompten der skal sendes til alle modeller
    """
    api_key = load_api_key()
    models = get_models()
    
    print(f"\n{'*' * 70}")
    print(f"PROMPT: {prompt}")
    print(f"{'*' * 70}\n")
    
    for model in models:
        print(f"Henter svar fra {model['name']}...")
        response = await call_openrouter_api(model['id'], prompt, api_key)
        display_response(model['name'], response)
        # Kort pause mellem API-kald for at undgå rate limiting
        # (Short pause between API calls to avoid rate limiting)
        time.sleep(1)

# Hovedprogram
# (Main program)
if __name__ == "__main__":
    # Definer prompten der skal testes - denne gang en kreativ opgave
    # (Define the prompt to be tested - this time a creative task)
    prompt = "Skriv et kort digt på 4 linjer om kunstig intelligens og menneskehedens fremtid."
    
    # Kør sammenligningen
    # (Run the comparison)
    asyncio.run(run_comparison(prompt))
