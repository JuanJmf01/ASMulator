# ASMSimulator

Este es un simulador de una Unidad Aritmética Lógica (ALU) con registros, operaciones y una memoria RAM de 16 bits. El simulador permite realizar operaciones de suma, resta, negación, entre otros, sobre registros y almacenar o leer valores de la memoria RAM.

## Componentes

### ALU

La ALU contiene métodos para realizar diversas operaciones:

- `add(input1, input2)`: Realiza una suma binaria de dos números de 16 bits.
- `subtract(input1, input2)`: Realiza una resta binaria de dos números de 16 bits.
- `negate(input)`: Realiza la negación de un número de 16 bits.
- `plusOne(input)`: Suma uno a un número de 16 bits.

### RegisterA y RegisterD

Estos registros almacenan números binarios de 16 bits.

### InstructionDecoder

El decodificador de instrucciones permite interpretar y ejecutar operaciones sobre los registros utilizando la ALU y accediendo a la RAM.

### RAM

Una memoria RAM de 16 posiciones, cada una capaz de almacenar un número binario de 16 bits.

## Uso del programa

### Ejecución

El programa se inicia ejecutando el archivo `main.py`.

### Interfaz de usuario

- Se muestran los valores actuales en los registros A y D.
- El usuario puede ingresar operaciones como suma, resta, almacenamiento en RAM, lectura de RAM, negación, entre otras.
- Se solicita al usuario ingresar dos números binarios de 16 bits para realizar las operaciones.
- Los resultados de las operaciones se muestran en la consola.

## Contribuciones

Este proyecto es de código abierto. Siéntete libre de colaborar, hacer sugerencias o informar sobre problemas a través de las solicitudes de extracción o problemas en GitHub.

## Autor

[Cambiar aquí con tu nombre] - [Enlace a tu perfil si es necesario]

