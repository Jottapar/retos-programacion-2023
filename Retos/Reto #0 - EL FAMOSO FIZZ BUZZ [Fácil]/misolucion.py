'''
*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */
 '''

num = 1
print(f'{num}\n')

while num <= 100:
            if num % 3 == 0:
                tex_num = 'fizz'
                print(f'{tex_num}\n')
            elif num % 5 == 0:
                tex_num = 'buzz'
                print(f'{tex_num}\n')
            elif num % 5 == 0 and num % 3 == 0:
                tex_num = 'fizzbuzz'
                print(f'{tex_num}\n')
            else:
                print(f'{num}\n')
            num += 1
