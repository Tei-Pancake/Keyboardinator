#include QMK_KEYBOARD_H

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    [0] = LAYOUT_directional_3key(
        LGUI(KC_D), // Tecla 1: Minimiza todo (Simulador de Trabajo)
        LCTL(KC_W), // Tecla 2: Cierra pestaña actual (Limpieza rápida)
        LGUI(KC_L)  // Tecla 3: Bloqueo de seguridad
    )
};