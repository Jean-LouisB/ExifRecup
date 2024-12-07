# GET EXIF

### V2.0.0
JPG uniquement

1 - créer un dossier "images" sur le bureau avec les photos

### Utilisation

    from getexif.process import Process


    try:
        process = Process()
        result = process.get_exif()
        print(f"{result} images ont été traités")
    except Exception as e:
        print(f"Erreur de traitement : {str(e)}")
