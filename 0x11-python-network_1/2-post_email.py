#!/usr/bin/python3
"""Displays the body of the response of a POST request to a given URL with an email.

Usage: ./2-post_email.py <URL> <email>
"""
import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    # Récupération des arguments de la ligne de commande
    url = sys.argv[1]
    email = sys.argv[2]
    
    # Préparation des données à envoyer dans la requête POST
    val = {'email': email}
    data = urllib.parse.urlencode(val).encode("ascii")
    
    # Création de la requête POST
    req = urllib.request.Request(url, data=data)
    
    # Envoi de la requête et récupération de la réponse
    with urllib.request.urlopen(req) as response:
        # Lecture et affichage du corps de la réponse décodé en UTF-8
        print(response.read().decode('utf-8'))
