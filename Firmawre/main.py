import board
import busio  # Necesario para el bus I2C
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
keyboard.keymap = [
    [KC.LGUI(KC.D), KC.LCTL(KC.W), KC.LGUI(KC.L)]
]

# 4. Configurar el bus I2C para la pantalla OLED (Pines D4 y D5)
i2c = busio.I2C(board.SCL, board.SDA)

# 5. Configurar la pantalla OLED pasando el bus i2c
oled_ext = Oled(
    OledDisplayMode.TXT,
    oled_reaction_type=OledReactionType.LAYER,
    i2c=i2c,  # Aquí conectamos el bus que definimos arriba
    width=128,
    height=32,
)
keyboard.extensions.append(oled_ext)

# 6. ¡Arrancar el Keyboardinator!
if __name__ == '__main__':
    keyboard.go()