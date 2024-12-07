import os
from datetime import datetime
import ntpath
import math
from pathlib import Path
from exif import Image



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


class autoId():
    def __init__(self):
        self.id = 0
    def nextId(self):
        id= self.id
        self.id+=1
        return id


class monImage():
    def __init__(self, path, nextId):
        self.nextId = nextId
        self.path = path

    def extractInfo(self):
        with open(self.path, 'rb') as src:
            img = Image(src)
            try:
                x = img.get('exposure_time')
                if x < 1:
                    x = 1 / x
                    app = '1/{}'.format(math.floor(x))
                else:
                    app = math.floor(x)
                exifDict = {}
                exifDict["id"] = self.nextId
                exifDict["fichier"] = ntpath.basename(self.path)
                exifDict["nom"] = Path(self.path).stem
                exifDict["focale"] = "{} mm".format(img.get('focal_length'))
                exifDict["Vitesse"] = "{} sec.".format(app)
                exifDict["ouverture"] = "F/{}".format(img.get('f_number'))
                exifDict["iso"] = "{} iso".format(img.get('photographic_sensitivity'))
                exifDict["comment"] = ""
            except:
                with open(self.path, 'rb') as src1:
                    img = Image(src1)
                    exifDict = {}
                    exifDict["id"] = self.nextId
                    exifDict["fichier"] = ntpath.basename(self.path)
                    exifDict["nom"] = Path(self.path).stem
                    exifDict["comment"] = ""
            finally:
                return exifDict

