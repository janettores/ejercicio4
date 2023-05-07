class Ventana:
    __titulo= ""
    __valor_x_sup_izq = 0
    __valor_y_sup_izq = 0
    __valor_x_inf_der = 0
    __valor_y_inf_der = 0
    def __init__(self, titulo, valor_x_sup_izq=0, valor_y_sup_izq=0, valor_x_inf_der= 500, valor_y_inf_der=500):
        self.__titulo = titulo
        self.__valor_x_sup_izq = valor_x_sup_izq
        self.__valor_y_sup_izq = valor_y_sup_izq
        self.__valor_x_inf_der = valor_x_inf_der
        self.__valor_y_inf_der = valor_y_inf_der
        if valor_x_sup_izq < 0 or valor_y_sup_izq < 0 or valor_x_inf_der > 500 or valor_y_inf_der > 500 or valor_x_sup_izq < valor_x_inf_der or valor_y_sup_izq < valor_y_inf_der:
            print("Error en el Ingreso de las Coordenadas \n")
    def getTitulo(self):
        return self.__titulo
    def alto(self):
        return self.__valor_y_inf_der - self.__valor_y_sup_izq
    def ancho(self):
        return self.__valor_y_inf_der - self.__valor_y_sup_izq
    def mostrar(self):
        return print("Titulo: {}, Xsuperior_izquierdo: {}, Xinferior_derecho: {}, Ysuperior_izquierdo: {}, Yinferior_derecho: {} " .format(self.getTitulo(), self.__valor_x_sup_izq, self.__valor_x_inf_der, self.__valor_y_sup_izq, self.__valor_y_inf_der))
    def moverDerecha(self, posiciones =1):
        if self.__valor_x_sup_izq + posiciones>= 0:
            self.__valor_x_sup_izq += posiciones
        if self.__valor_x_inf_der + posiciones <=500:
            self.__valor_x_inf_der += posiciones
    def moverIzquierda(self, posiciones =1):
        if self.__valor_x_sup_izq -posiciones >=0:
            self.__valor_x_sup_izq += posiciones
        if self.__valor_x_inf_der - posiciones <=500:
            self.__valor_y_inf_der +=posiciones
    def subir(self,posiciones=1):
        if self.__valor_y_sup_izq + posiciones >=0:
            self.__valor_y_sup_izq +=posiciones
        if self.__valor_y_inf_der + posiciones <=500:
            self.__valor_y_inf_der +=posiciones
    def bajar(self, posiciones=1):
        if self.__valor_y_sup_izq - posiciones >=0:
            self.__valor_y_sup_izq +=posiciones
        if self.__valor_y_inf_der - posiciones <=500:
            self.__valor_y_inf_der += posiciones