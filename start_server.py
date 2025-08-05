#!/usr/bin/env python
"""
Script de démarrage pour serveur ASGI sur Render
Utilise Uvicorn pour servir l'application Django avec support WebSocket
"""
import os
import sys
import django
from django.core.management import execute_from_command_line

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'techlearnjess.settings')

def main():
    """Fonction principale de démarrage"""
    try:
        # Vérifier si on doit faire les migrations
        django.setup()
        
        # Lancer le serveur Uvicorn
        import uvicorn
        port = int(os.environ.get('PORT', '10000'))
        
        print(f"🚀 Démarrage du serveur ASGI sur le port {port}")
        uvicorn.run(
            "techlearnjess.asgi:application",
            host="0.0.0.0",
            port=port,
            log_level="info",
            access_log=True
        )
    except ImportError:
        print("❌ Erreur: Uvicorn n'est pas installé")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Erreur de démarrage: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()