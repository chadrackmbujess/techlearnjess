#!/usr/bin/env python
"""
Script de démarrage pour serveur ASGI sur Render
Utilise Daphne pour servir l'application Django avec support WebSocket
"""
import os
import sys
from daphne.cli import CommandLineInterface

if __name__ == '__main__':
    # Configuration pour Render
    port = os.environ.get('PORT', '10000')
    
    # Arguments pour Daphne
    sys.argv = [
        'daphne',
        '-b', '0.0.0.0',
        '-p', port,
        'techlearnjess.asgi:application'
    ]
    
    # Lancer Daphne
    CommandLineInterface.entrypoint()