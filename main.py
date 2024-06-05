import qrcode
from qrcode.constants import ERROR_CORRECT_L, ERROR_CORRECT_H
from PIL import Image


def create_simple_qr_code(data: str):
    # Create a QRCode instance
    qr_code_img = qrcode.make(data)
    qr_code_img.save("qr_code.png")


def create_svg_qr_code(data: str):
    import qrcode.image.svg

    # Create a QRCode instance
    qr_code = qrcode.QRCode(version=7, error_correction=ERROR_CORRECT_L, box_size=3, border=2)
    qr_code.add_data(data)
    qr_code.make(fit=True)

    # image_factory : permet de définir le type de l'image générée (par défaut c'est un objet Image de la bibliothèque PIL) mais on peut utiliser un autre type d'image comme SVGImage ou SVGPathImage ou Image de la bibliothèque Pillow ou autre
    qr_code_img = qr_code.make_image(image_factory=qrcode.image.svg.SvgImage)
    qr_code_img.save("qrcode.svg")


def create_png_qr_code(data: str):
    # Create a QRCode instance
    qr_code = qrcode.QRCode(
        # Le paramètre version permet de définir la taille du QR Code
        version=7,
        # Le paramètre error_correction permet de définir le niveau de correction d'erreur, pratiquement c'est le niveau
        # de qualité du QR Code et il peut prendre 4 valeurs : ERROR_CORRECT_L, ERROR_CORRECT_M, ERROR_CORRECT_Q,
        # ERROR_CORRECT_H: on choisit ici le niveau de qualité le plus bas et le plus rapide

        # ERROR_CORRECT_L : 7% de correction d'erreur
        # ERROR_CORRECT_M : 15% de correction d'erreur
        # ERROR_CORRECT_Q : 25% de correction d'erreur
        # ERROR_CORRECT_H : 30% de correction d'erreur
        # il faut savoir que plus le niveau de correction d'erreur est élevé, plus le QR Code est grand et plus il est
        # difficile à scanner et donc il faut prendre le niveau elevé que si on a un QR Code avec beaucoup de données à
        # encoder et
        error_correction=ERROR_CORRECT_L,
        # Le paramètre box_size permet de définir la taille de chaque case du QR Code en pixel et on choisit ici 3 pixels
        box_size=3,
        # Le paramètre border permet de définir la taille de la bordure du QR Code en case et on choisit ici 1 en case
        border=2
    )

    # Ajouter les données à encoder dans le QR Code (ici on a mis "Mon code QR")
    qr_code.add_data(data)
    # On appelle la méthode make pour générer le QR Code et son paramètre fit permet de redimensionner le QR Code pour qu'il s'adapte à la taille des données à encoder sinon il faut définir la taille du QR Code avec le paramètre version et le paramètre box_size
    qr_code.make(fit=True)

    # La méthode make_image permet de générer l'image du QR Code et on peut définir la couleur de remplissage et la couleur de fond du QR Code, ses autres parametres sont : back_color, fill_color, image_factory, module_color, quiet_zone, scale, save_name, save_format
    # fill_color : couleur de remplissage du QR Code
    # back_color : couleur de fond du QR Code
    # image_factory : permet de définir le type de l'image générée (par défaut c'est un objet Image de la bibliothèque
    # PIL) mais on peut utiliser un autre type d'image comme SVGImage ou SVGPathImage ou Image de la bibliothèque Pillow ou autre
    qr_code_img = qr_code.make_image(fill_color="blue", back_color="white")
    qr_code_img.save("qrcode.png")


def create_png_qr_code_with_logo_inside(data: str):
    logo = Image.open('logo.jpeg')
    # base_width est la largeur de l'image du QR Code en pixel et on choisit ici 75 pixels
    base_width = 75
    # logo_width_percent est le pourcentage de la largeur de l'image du QR Code que va occuper le logo et on choisit ici
    # 20% parce que le logo doit être petit pour ne pas gêner la lecture du QR Code et le 20% est une valeur qui a été
    # testée et qui donne un bon résultat et on peut choisir une autre valeur si on veut mais il faut faire des tests
    # pour voir le résultat, logo.size[0] est la largeur du logo en pixel 0 est l'indice de la largeur dans le tuple
    # size qui contient la largeur et la hauteur du logo
    w_percent = (base_width / float(logo.size[0]))
    h_size = int((float(logo.size[1]) * float(w_percent)))
    logo = logo.resize((base_width, h_size))  # Redimensionner le logo
    qr_code = qrcode.QRCode(error_correction=ERROR_CORRECT_H, box_size=10, border=1)  # Créer un objet QRCode
    qr_code.add_data(data)  # Ajouter les données à encoder
    qr_code.make(fit=True)  # Générer le QR Code
    qr_code_img = qr_code.make_image(fill_color="black", back_color="white").convert(
        'RGB')  # Générer l'image du QR Code
    pos = ((qr_code_img.size[0] - logo.size[0]) // 2, (qr_code_img.size[1] - logo.size[1]) // 2)  # Position du logo
    qr_code_img.paste(logo, pos)  # Coller le logo sur l'image du QR Code
    qr_code_img.save("qrcode_with_logo.png")  # Enregistrer l'image du QR Code avec le logo
    # print(float(logo.size[0]))

create_png_qr_code_with_logo_inside("QR Code avec logo")
