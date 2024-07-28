import random

# Define the traditional 54 Loteria cards
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
cards = [f'{name}.png' for name in card_names]

def generate_card():
    return random.sample(cards, 16)  # Assuming each card has a 4x4 grid

def check_win(card, called_cards):
    # Define the win conditions
    win_conditions = [
        # Rows
        [0, 1, 2, 3],
        [4, 5, 6, 7],
        [8, 9, 10, 11],
        [12, 13, 14, 15],
        # Columns
        [0, 4, 8, 12],
        [1, 5, 9, 13],
        [2, 6, 10, 14],
        [3, 7, 11, 15],
        # Diagonals
        [0, 5, 10, 15],
        [3, 6, 9, 12],
        # Corners
        [0, 3, 12, 15]
    ]
    
    # Check each win condition
    for condition in win_conditions:
        if all(card[i] in called_cards for i in condition):
            print(f"Winning condition met: {condition}")  # Add logging
            return True
    return False

