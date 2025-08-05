#!/usr/bin/env python
"""
Script de démarrage pour serveur ASGI sur Render
Utilise Uvicorn pour servir l'application Django avec support WebSocket
"""
import os
import uvicorn

if __name__ == '__main__':
    # Configuration pour Render
    port = int(os.environ.get('PORT', '10000'))
    
    # Lancer Uvicorn avec l'application ASGI
    uvicorn.run(
        "techlearnjess.asgi:application",
        host="0.0.0.0",
        port=port,
        log_level="info"
    )