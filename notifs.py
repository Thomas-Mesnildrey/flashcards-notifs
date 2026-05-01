from plyer import notification
import random
from apscheduler.schedulers.blocking import BlockingScheduler

global d1 #insert questions in here
d1={1:"Donner l'expression de la température et de la pression thermodynamique",
    2:"Redémontrer les expressions de deltaS pour une phase condensée et pour un gaz parfait",
    3:"Quelle propriété a l'enthalpie standard de réaction? Que peut on en déduire pour une réaction isobare isotherme?",
    4:"Retrouver le critère permettant de déterminer le sens d'évolution d'une réaction isotherme et isobare.",
    5:"Relation de Van't Hoff + en déduire l'effet d'une augmentation de la température sur l'équilibre d'une réaction chimique",
    6:"Etablir le théorème des moments",
    7:"Donner et démontrer l'inégalité de Clausius",
    8:"Etablir le rendement (efficacité) de Carnot",
    9:"Etablire le premier principe industriel de la thermodynamique",
    10:"Etablire le second principe industriel de la thermodynamique",
    11:"Etablir l'équation de la diffusion thermique en 1D cartésienne"}

def notifs():
    c=random.randint(1, len(d1))
    notification.notify(title='Question time!', message=str(d1[c]))


scheduler = BlockingScheduler()
scheduler.add_job(notifs, 'interval', minutes=0.2)
scheduler.start()