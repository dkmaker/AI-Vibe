import os
import sys
import subprocess
import time

# Farver til konsoloutput
# (Colors for console output)
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_header(text):
    """
    Udskriver en formateret overskrift til konsollen.
    (Prints a formatted header to the console.)
    """
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'=' * 80}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.BLUE}{text.center(80)}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.BLUE}{'=' * 80}{Colors.ENDC}\n")

def run_script(script_name, description):
    """
    Kører et Python-script og viser en overskrift.
    (Runs a Python script and displays a header.)
    
    Args:
        script_name (str): Navnet på scriptet der skal køres
        description (str): Beskrivelse af scriptet
    """
    print_header(f"KØRER: {script_name} - {description}")
    
    # Få den fulde sti til scriptet
    # (Get the full path to the script)
    script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), script_name)
    
    try:
        # Kør scriptet som en underproces
        # (Run the script as a subprocess)
        subprocess.run([sys.executable, script_path], check=True)
        print(f"\n{Colors.GREEN}✓ {script_name} kørte succesfuldt!{Colors.ENDC}\n")
    except subprocess.CalledProcessError as e:
        print(f"\n{Colors.RED}✗ Fejl ved kørsel af {script_name}: {str(e)}{Colors.ENDC}\n")
    
    # Kort pause mellem scripts
    # (Short pause between scripts)
    time.sleep(2)

def main():
    """
    Hovedfunktion der kører alle sammenligningsscripts i rækkefølge.
    (Main function that runs all comparison scripts in sequence.)
    """
    print_header("LLM SAMMENLIGNINGSTEST")
    print(f"{Colors.YELLOW}Dette script kører alle fire LLM-sammenligninger i rækkefølge.{Colors.ENDC}")
    print(f"{Colors.YELLOW}Hver sammenligning bruger en forskellig prompt for at vise variationen i modellernes svar.{Colors.ENDC}\n")
    
    # Kør hvert script med en beskrivelse
    # (Run each script with a description)
    run_script("main.py", "Generel viden (vedvarende energi)")
    run_script("creative_comparison.py", "Kreativ opgave (digt om AI)")
    run_script("technical_comparison.py", "Teknisk forklaring (prompt-optimering)")
    run_script("web_search_comparison.py", "Web søgning (kvantecomputere i 2025)")
    
    print_header("ALLE SAMMENLIGNINGER GENNEMFØRT")
    print(f"{Colors.GREEN}Alle fire sammenligninger er nu gennemført.{Colors.ENDC}")
    print(f"{Colors.GREEN}Du kan nu sammenligne, hvordan forskellige LLM-modeller reagerer på forskellige typer af prompts.{Colors.ENDC}\n")

if __name__ == "__main__":
    main()
