# GET EXIF

### Instalation
pip:
    pip install export-exif

git:
    https://github.com/Jean-LouisB/ExifRecup.git

## Versions
### V2.0.0
JPG uniquement

Créer un dossier "images" sur le bureau avec les photos
Par défaut il cherche le dossier "images" sur le bureau.

## Utilisation

    from getexif.process import Process


    try:
        process = Process()
        result = process.get_exif()
        print(f"{result} images ont été traités")
    except Exception as e:
        print(f"Erreur de traitement : {str(e)}")
