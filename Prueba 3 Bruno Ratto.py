#Prueba 3

import os.path

def ingresar_libro(title, autor, genero, file):
   
    index = '0'
    libros_lista = crear_lista_libros(file)
    len_libros = len(libros_lista)
    if len_libros>0:
        index = str(int(libros_lista[len_libros-1]['index'])+1)
        
    try:
        with open(file, 'a') as libros:
            line = index + '\t' + title +'\t' + autor +'\t'+ genero + '\n'
            libros.write(line)
            print('texto guardado!')
    except Exception as e:
        print(f"Error : {e}")

def crear_lista_libros(file):   
    ret_value = []
    try:
        with open(file, 'r') as libros:
            output = libros.read()
            lines = output.split(sep='\n')
            libros_list = []
            for line in lines:
                if line == '':
                    break
                
                line_list = line.split('\t')
                
                line_dict = {'index':line_list[0], 'titulo':line_list[1], 'autor':line_list[2], 'genero':line_list[3]}

                libros_list.append(line_dict)
            ret_value = libros_list
            
    except Exception as e:
        print(f'Error: {e}')
    return ret_value
        
def buscar_por_autor(file, autor):
    lista_libros = crear_lista_libros(file)
    return [libro for libro in lista_libros if libro['autor'] == autor]
    
def libro_a_string(libro):
    llaves = libro.keys()
    libro_str = ''
    for i in llaves:
        libro_str += (libro[i] + '\t')
    return libro_str 


        
def print_libros(lista_libros, autor):
    if not autor:
        print("lista de libros en biblioteca \n")
        print("libro   titulo  autor   genero\n")
    
    for i in lista_libros:
        print(libro_a_string(i) + '\n')
   
    

path = 'libreria.csv'

if not os.path.isfile(path):
    file = open(path, 'w')
    file.close()
else:
    print('ya existe')
    pass



while True:
    
    
    print("""Hola ¿Que libro quieres registar?.
                   1.- registrar un libro
                   2.- buscar libro por autor
                   3.- ver libros en biblioteca
                   4.- terminar el registro \n""")
    opcion = input('operacion a realizar: ')
    if opcion == '1':
        print("Ingrese los datos del registro a continuacion: \n")
        titulo = input('titulo:\n')
        autor = input("autor:\n")
        genero = input('genero:\n')
        
        ingresar_libro(titulo, autor , genero, path)

    elif opcion == '2':
        autor = input("Ingresa el autor :")
        print("\n")
        print(f'gastos de categoria {autor}\n')
        print("indice   titulo   autor   genero \n")
        print("------------------------------------------------\n")
        filtrados = buscar_por_autor(path, autor)
        print_libros(filtrados, True)
        
    elif opcion == '3':
        print('\n')
        lista = crear_lista_libros(path)
        print_libros(lista, False)
         
    elif opcion == '4':
        print("Hasta luego")
        break

    else:
        print ("Ingrese una opcin del 1 al 4.")