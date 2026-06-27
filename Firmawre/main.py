import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.peg_oled import Oled, OledDisplayMode, OledReactionType

# 1. Inicializar el teclado
keyboard = KMKKeyboard()

# 2. Configurar los pines de tus 3 teclas
keyboard.col_pins = (board.D1, board.D2, board.D3)
keyboard.row_pins = (board.D0,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# 3. Definir tus funciones de "Modo Ninja"
# Tecla 1: Win+D (Minimizar todo)
# Tecla 2: Ctrl+W (Cerrar pestaña)
# Tecla 3: Win+L (Bloquear PC)
keyboard.keymap = [
    [KC.LGUI(KC.D), KC.LCTL(KC.W), KC.LGUI(KC.L)]
]

# 4. Configurar la pantalla OLED
oled_ext = Oled(
    OledDisplayMode.TXT,
    oled_reaction_type=OledReactionType.LAYER,
    width=128,
    height=32,
)
keyboard.extensions.append(oled_ext)

# 5. ¡Arrancar el Keyboardinator!
if __name__ == '__main__':
    keyboard.go()