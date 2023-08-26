import ntpath
import math
from pathlib import Path
from exif import Image

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

