import matplotlib.pyplot as plt
# -------------------------------------------------
def txt_a_lista(opc):
    if opc < 7:
        if opc == 1:
            txt = 'resultados\_resultadosPythonBubble.txt'
        elif opc == 2:
            txt = 'resultados\_resultadosPythonMerge.txt'
        elif opc == 3:
            txt = 'resultados\_resultadosC++Bubble.txt'
        elif opc == 4:
            txt = 'resultados\_resultadosC++Merge.txt'
        elif opc == 5:
            txt = 'resultados\_resultadosGoBubble.txt'
        elif opc == 6:
            txt = 'resultados\_resultadosGoMerge.txt'
    else:
        print("Opc no valida:",opc)
        return None
    lista_flotante = []
    archivo = open(txt, "r")
    lista_lineas_str = archivo.readlines()
    archivo.close()
    for i in lista_lineas_str:
        lista_flotante.append(float(i))
    return lista_flotante
def generarGrafico(lista, py_b,py_m,cpp_b,cpp_m,go_b,gop_m):
    #lista          tamanios
    x = lista
    fx1 = py_b
    fx2 = py_m 
    gx1 = cpp_b
    gx2 = cpp_m
    hx1 = go_b
    hx2 = gop_m
    
    plt.plot(x, fx1)
    plt.plot(x, fx2)
    plt.plot(x, gx1)
    plt.plot(x, gx2)
    plt.plot(x, hx1)
    plt.plot(x, hx2)

    plt.plot(x, fx1, label = "python bubble")
    plt.plot(x, fx2, label = "python merge")
    plt.plot(x, gx1, label = "c++ bubble")
    plt.plot(x, gx2, label = "c++ merge")
    plt.plot(x, hx1, label = "go bubble")
    plt.plot(x, hx2, label = "go merge")
    plt.legend(loc = "upper left")

    plt.xlabel("Tamanios", )
    plt.ylabel("Tiempo en microsegundos (ms)")

    plt.savefig('diagrama.png')
    plt.show()
# -------------------------------------------------
def main():
    #tamanios = [100, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000, 50000]
    #tamanios = [1000,1500,2000,2500,3000,3500,4000,6000]
    tamanios = [1,1000,1500,2000,2000,3000,3500]
    # listas donde se almacenaran los resultados finales
    list_python_bubble = txt_a_lista(1)
    list_python_merge = txt_a_lista(2)
    list_cpp_bubble = txt_a_lista(3)
    list_cpp_merge = txt_a_lista(4)
    list_go_bubble = txt_a_lista(5)
    list_go_merge = txt_a_lista(6)
    generarGrafico(tamanios,list_python_bubble,list_python_merge,list_cpp_bubble,list_cpp_merge,list_go_bubble,list_go_merge)

# -------------------------------------------------
main()