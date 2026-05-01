# Flashcard revision tool :
Un petit programme qui m'a permis de garder en mémoire les questions de cours que j'avais déjà apprises pendant mes révisions de concours.
Il vous envoie des notifications à intervalles régulières pour éviter d'oublier ce qui a déjà été appris.

# Comment l'adapter à vos besoins :
Dans un premier temps pour pouvoir lancer le programme, il faut:
`pip install plyer`
`pip install apscheduler`
Et puis ensuite, insérer les questions qu'on souhaite réviser directement dans le dictionnaire en haut/ modifier l'intervalle de temps entre chaques notifications suivant les besoins:
`scheduler.add_job(notifs, 'interval', minutes=7)` <- c'est ici qu'il faut modifier l'intervalle

Vous pouvez maintenant exécuter le code!
