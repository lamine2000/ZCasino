from random import randrange
from math import ceil
from os import system, name


def clear():
    # for windows
    _ = system('cls') if name == 'nt' else system('clear')


if __name__ == '__main__':

    continuer = 'o'
    argent = 1000
    while continuer == 'o':
        print(f'Vous avez {argent}$')

        miseArgent = miseNum = -1

        while not 0 < miseArgent <= argent:
            miseArgent = int(input(f'Combien misez-vous ? [1$;{argent}$]... '))

        while not 0 <= miseNum < 50:
            miseNum = int(input('Sur quel numéro misez-vous ? [0;49]... '))

        numBille = randrange(50)
        print(f'La bille s\'est arrêtée sur le ........ {numBille}')

        if numBille == miseNum:
            gain = miseArgent * 3
            print(f'Quelle chance, vous gagnez {gain}$')
        elif numBille % 2 == miseNum % 2:
            gain = ceil(miseArgent / 2)
            print(f'Bravo, vous gagnez {gain}$')
        else:
            gain = -miseArgent
            print('Dommage, vous perdez votre mise')

        argent += gain
        print(f'Vous avez {argent}$')

        if argent <= 0:
            print('Dommage, vous n\'avez pas assez d\'argent pour miser. À la prochaine !')
            break

        reponse = 'a'
        while reponse[0] not in 'onON':
            reponse = input('Voulez-vous continuer ? O/N... ')

        continuer = reponse[0].lower()

        if continuer == 'o':
            clear()
        else:
            print('Dommage, vous partez déjà. Bye !')
