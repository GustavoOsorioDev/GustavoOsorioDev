"""
🚀 KAGGLE SDK FOR CSDD (Spec-Driven Development)
Propósito: Servidor de Inferencia Ollama + Qwen2.5-Coder para uso con VS Code.
Nivel: 0 (Metal / Free Tier)
"""

import os
import subprocess
import time

# --- CONFIGURACIÓN ---
MODEL_NAME = "qwen2.5-coder:32b" # Cambiar a 14b si la GPU es limitada (P100)
NGROK_AUTH_TOKEN = "TU_TOKEN_AQUÍ" # Consíguelo gratis en ngrok.com
PORT = 11434

def run_setup():
    print("📦 [1/4] Instalando Ollama...")
    os.system("curl -fsSL https://ollama.com/install.sh | sh > /dev/null 2>&1")

    print(f"🧠 [2/4] Descargando modelo {MODEL_NAME} (esto tardará unos minutos)...")
    # Levantamos temp server para descargar
    subprocess.Popen(["ollama", "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(5)
    os.system(f"ollama pull {MODEL_NAME}")

    print("🔌 [3/4] Instalando pyngrok para el túnel seguro...")
    os.system("pip install pyngrok --quiet")

    from pyngrok import ngrok
    if NGROK_AUTH_TOKEN != "TU_TOKEN_AQUÍ":
        ngrok.set_auth_token(NGROK_AUTH_TOKEN)
    
    print(f"🌐 [4/4] Abriendo túnel en el puerto {PORT}...")
    public_url = ngrok.connect(PORT).public_url
    
    print("\n" + "="*50)
    print("✅ SERVIDOR LISTO PARA CSDD")
    print(f"🔗 URL PARA VS CODE (Continue.dev): {public_url}")
    print("="*50)
    print("\n💡 Tip: No cierres esta pestaña de Kaggle.")

if __name__ == "__main__":
    try:
        run_setup()
        # Mantenemos el proceso vivo
        while True:
            time.sleep(60)
    except KeyboardInterrupt:
        print("\n🛑 Servidor detenido.")
