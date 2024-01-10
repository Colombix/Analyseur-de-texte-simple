import re

def compter_mots_phrases(texte):
    
    # Compter le nombre de mots
    nombre_mots = len(texte.split())

    # Compter le nombre de phrases
    phrases = re.split(r'[.!?]', texte)

    # Filtrer les éléments vides 
    phrases = [phrase for phrase in phrases if phrase.strip()]

    nombre_phrases = len(phrases)

    return nombre_mots, nombre_phrases

while True:
    # Demander à l'utilisateur de saisir un texte
    texte_utilisateur = input("Veuillez saisir le texte que vous souhaitez analyser (ou 'stop' pour arrêter) : ")

    # Vérifier si l'utilisateur veut arrêter
    if texte_utilisateur.lower() == 'stop':
        print("Arrêt de l'analyse.")
        break

    # Appeler la fonction d'analyse avec le texte de l'utilisateur
    mots, phrases = compter_mots_phrases(texte_utilisateur)

    # Afficher les résultats
    print(f"Nombre de mots: {mots}")
    print(f"Nombre de phrases: {phrases}")
