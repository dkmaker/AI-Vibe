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

# Definér modeller til sammenligning med web søgning
# (Define models for comparison with web search)
def get_models():
    """
    Returnerer en liste af modeller til sammenligning, alle med web søgning aktiveret.
    (Returns a list of models for comparison, all with web search enabled.)
    """
    return [
        {"id": "openai/gpt-4o:online", "name": "GPT-4o med web søgning"},
        {"id": "anthropic/claude-3-opus", "name": "Claude 3 Opus med web plugin", "use_plugin": True},
        {"id": "perplexity/sonar-pro", "name": "Perplexity Sonar (indbygget søgning)"},
        {"id": "meta-llama/llama-3-70b-instruct", "name": "Llama 3 70B med web plugin", "use_plugin": True}
    ]

# Kald OpenRouter API med web søgning
# (Call OpenRouter API with web search)
async def call_openrouter_api(model_id, prompt, api_key, use_plugin=False):
    """
    Kalder OpenRouter API med den angivne model og prompt, med web søgning aktiveret.
    (Calls the OpenRouter API with the specified model and prompt, with web search enabled.)
    
    Args:
        model_id (str): Model ID til OpenRouter
        prompt (str): Prompten der skal sendes til modellen
        api_key (str): OpenRouter API-nøgle
        use_plugin (bool): Om web plugin skal bruges (for modeller uden indbygget søgning)
        
    Returns:
        dict: Modellens svar med eventuelle web søgningsresultater
    """
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    # Grundlæggende data payload
    # (Basic data payload)
    data = {
        "model": model_id,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 800
    }
    
    # Tilføj web plugin hvis nødvendigt
    # (Add web plugin if necessary)
    if use_plugin:
        data["plugins"] = [
            {
                "id": "web",
                "max_results": 3,  # Begrænser til 3 resultater for at holde omkostningerne nede
                "search_prompt": "Følgende web-søgningsresultater blev fundet. Inkorporer dem i dit svar og citer kilderne med markdown-links."
            }
        ]
    
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=data
        )
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": f"Fejl ved kald til {model_id}: {str(e)}"}

# Vis svar fra modellen med web søgningsresultater
# (Display response from the model with web search results)
def display_response(model_name, response_data):
    """
    Viser modellens svar i konsollen med formatering, inklusive web søgningsresultater hvis tilgængelige.
    (Displays the model's response in the console with formatting, including web search results if available.)
    
    Args:
        model_name (str): Navnet på modellen
        response_data (dict): Modellens svar data
    """
    separator = "=" * 50
    print(f"\n{separator}")
    print(f"MODEL: {model_name}")
    print(f"{separator}")
    
    if "error" in response_data:
        print(response_data["error"])
        return
    
    try:
        # Udpak svar og eventuelle annotationer
        # (Unpack response and any annotations)
        content = response_data["choices"][0]["message"]["content"].strip()
        print(content)
        
        # Vis annotationer (URL citationer) hvis de findes
        # (Display annotations (URL citations) if they exist)
        if "annotations" in response_data["choices"][0]["message"]:
            annotations = response_data["choices"][0]["message"]["annotations"]
            if annotations:
                print("\n--- Kilder fra web søgning ---")
                for i, annotation in enumerate(annotations, 1):
                    if annotation["type"] == "url_citation":
                        url_data = annotation["url_citation"]
                        print(f"{i}. {url_data.get('title', 'Ingen titel')}")
                        print(f"   URL: {url_data.get('url', 'Ingen URL')}")
    except Exception as e:
        print(f"Fejl ved visning af svar: {str(e)}")
    
    print(f"{separator}\n")

# Hovedfunktion til at køre sammenligningen
# (Main function to run the comparison)
async def run_comparison(prompt):
    """
    Kører sammenligningen af forskellige LLM'er med den samme prompt, med web søgning aktiveret.
    (Runs the comparison of different LLMs with the same prompt, with web search enabled.)
    
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
        use_plugin = model.get("use_plugin", False)
        response = await call_openrouter_api(model['id'], prompt, api_key, use_plugin)
        display_response(model['name'], response)
        # Længere pause mellem API-kald for at undgå rate limiting med web søgning
        # (Longer pause between API calls to avoid rate limiting with web search)
        time.sleep(3)

# Hovedprogram
# (Main program)
if __name__ == "__main__":
    # Definer prompten der skal testes - denne gang en prompt der kræver aktuel information
    # (Define the prompt to be tested - this time a prompt that requires current information)
    prompt = "Beskriv kort hvad OrangeMakers laver?"
    
    # Kør sammenligningen
    # (Run the comparison)
    asyncio.run(run_comparison(prompt))
