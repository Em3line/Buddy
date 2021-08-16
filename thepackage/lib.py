from datetime import timedelta, date, datetime
import unicodedata


NAME_LIST = [
    'Émeline', 'Anna', 'Prunelle', 'Thibault', 'Zacharie', 'Alix', 'Kenza',
    'Morgan', 'Selim', 'Stéphane', 'Antoine', 'Jean-Rémi', 'Jean', 'Krystelle',
    'Xavier', 'Bilel', 'Julien'
]


def try_me() :
    ''' Who's your buddy ?'''
    name_in = input("Ton prénom ? ")
    for elem in NAME_LIST:
        if unicodedata.normalize('NFKD', elem.lower()).encode('ASCII','ignore').decode() == \
            unicodedata.normalize('NFKD', name_in.lower()).encode('ASCII','ignore').decode():
            name = elem
    day_origin = date(2021, 7, 5)  # date de la remise à zéro des compteurs
    # nombre de jours ouvrés entre le 05/07 et le jour demandé
    # attention, pour simplifier la boucle le compteur passe à 1 dès premier jour
    nbr_days = 0
    auj = datetime.now()
    day_target = date(auj.year,auj.month,auj.day)
    while True:
        if day_origin.weekday() < 5:
            nbr_days += 1
        if day_origin == day_target:
            break
        day_origin += timedelta(1)
    # recherche du nom du buddy correspondant dans la liste
    i_bud = (len(NAME_LIST) - NAME_LIST.index(name) + 4 + nbr_days) % 17
    print("Ton buddy aujourd'hui est :", NAME_LIST[(i_bud)])
    return NAME_LIST[(i_bud)]
