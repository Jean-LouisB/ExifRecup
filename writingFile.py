import json


class fichierJson():
    def __init__(self):
        self.fileContent = []

    def addFileContent(self, objet):
        self.fileContent.append(objet)

    def getFile(self):
        return self.fileContent

    def writeFile(self):
        tab = json.dumps(self.fileContent)
        f = open("dataImages.JSON", "w")  # ecrase le contenu précédent
        f.write(tab)
        f.close()


class writeLog():
    def __init__(self, title='log.txt'):
        self.title = title
        self.write('\n##########################   Nouvelle session  ########################## \n\n', 'a')

    def write(self, line, method):
        with open('logs/'+self.title, method, encoding="utf-8") as f:
            f.write(line+"\n")
            f.close()

