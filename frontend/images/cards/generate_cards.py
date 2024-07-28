from PIL import Image, ImageDraw, ImageFont

card_names = [
    "el_gallo", "el_diablito", "la_dama", "el_catrin", "el_paraguas",
    "la_sirena", "la_escalera", "la_bottle", "el_barril", "el_arbol",
    "el_melon", "el_valiente", "el_gorrito", "la_muerte", "la_pera",
    "la_bandera", "el_bandolon", "el_violoncello", "la_garza", "el_pajaro",
    "la_mano", "la_bota", "la_luna", "el_cotorro", "el_borracho",
    "el_negrito", "el_corazon", "la_sandia", "el_tambor", "el_camaron",
    "las_jaras", "el_musico", "la_araña", "el_soldado", "la_estrella",
    "el_cazo", "el_mundo", "el_apache", "el_nopal", "el_alacran",
    "la_rosa", "la_calavera", "la_campana", "el_cantarito", "el_venado",
    "el_sol", "la_corona", "la_chalupa", "el_pino", "el_pescado",
    "la_palma", "la_maceta", "el_arpa", "la_rana"
]

def generate_card_images():
    for name in card_names:
        img = Image.new('RGB', (200, 300), color = (73, 109, 137))
        d = ImageDraw.Draw(img)
        try:
            fnt = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 20)
        except IOError:
            fnt = ImageFont.load_default()
        text = name.replace("_", " ").title()
        textbbox = d.textbbox((0, 0), text, font=fnt)
        textwidth, textheight = textbbox[2] - textbbox[0], textbbox[3] - textbbox[1]
        width, height = img.size
        x = (width - textwidth) / 2
        y = (height - textheight) / 2
        d.text((x, y), text, font=fnt, fill=(255, 255, 255))
        img.save(f'{name}.png')

if __name__ == "__main__":
    generate_card_images()

