#pragma once

// Definimos que el cerebro es tu RP2040
#define MATRIX_ROWS 1
#define MATRIX_COLS 3

// Tus 3 pines dorados del circuito directo
#define DIRECT_PINS { \
    { GP1, GP2, GP3 } \
}

// Esto le dice a la computadora que es el Keyboardinator
#define DEVICE_VER 0x0001
#define PRODUCT Keyboardinator