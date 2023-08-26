import os
from datetime import datetime
from writingFile import fichierJson, writeLog
from autoId import autoId
from exifData import monImage


class Process:
    def __init__(self):
        self.nbFile = 0
        self.listErreur = []
        self.listTraitee = []

    def exifImageJason(self):
        jason = fichierJson()  # instancie la création du fichier
        nextId = autoId()  # gère les id
        listImg = os.listdir('images')  # nombre d'images à traiter dans le dossier
        count = 0  # Donne le nombre d'images dans le dossier images/
        for f in listImg:
            count += 1  # compte les images dans le dossier
        for i in range(0, count):
            if os.path.splitext(listImg[i])[1] == '.jpg':
                imagePath = 'images/' + listImg[i]  # nbImg[i] renvoi le nom du fichier.
                imageEnTraitement = monImage(imagePath, nextId.nextId())
                dataExif = imageEnTraitement.extractInfo()
                jason.addFileContent(dataExif)
                dateNow = datetime.now()
                self.listTraitee.append("{} : {} traitée".format(dateNow, listImg[i]))

            else:
                dateNow = datetime.now()
                self.listErreur.append("{} : {} non traité".format(dateNow, listImg[i]))

        jason.writeFile()
        try:
            goodLog = writeLog('goog_log.txt')
            for i in range(len(self.listTraitee)):
                goodLog.write(self.listTraitee[i], 'a')
        except Exception as erreur:
            print("Erreur ici : ")
            print(erreur.__cause__)
        try:
            badLog = writeLog('bad_log.txt')
            for i in range(len(self.listErreur)):
                badLog.write(self.listErreur[i], 'a')
        except Exception as erreur:
            print("Erreur ici : ")
            print(erreur)

