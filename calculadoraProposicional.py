class Proposicional:
    # class: define una plantilla para crear objetos de lógica proposicional.

    def __init__(self,valor1,valor2):
        # __init__: método constructor; se ejecuta al crear el objeto.
        # self: referencia al objeto actual.
        # valor1 y valor2: proposiciones booleanas de entrada (True o False).
        self.valor1 = valor1
        # self.valor1: atributo de instancia que guarda la primera proposición.
        self.valor2 = valor2
        # self.valor2: atributo de instancia que guarda la segunda proposición.
    
    def conjuncion(self):
        # conjuncion (AND): solo es True cuando ambas proposiciones son True.
        if self.valor1 == True and self.valor2 == True:
            # if: evalúa la condición lógica.
            return True
            # return: devuelve el resultado de la operación.
        else:
            # else: se ejecuta cuando la condición del if no se cumple.
            return False
    
    def disyuncion(self):
        # disyuncion (OR): solo es False cuando ambas proposiciones son False.
        if self.valor1 == False and self.valor2 == False:
            return False
        else:
            return True
    
    def condicional(self):
        # condicional (p -> q): solo es False cuando p es True y q es False.
        if self.valor1 == True and self.valor2 == False:
            return False
        else:
            return True
        
    def bicondicional(self):
        # bicondicional (p <-> q): es True cuando ambas proposiciones tienen el mismo valor.
        if self.valor1 == self.valor2:
            return True
        else:
            return False
        
    def negacion_p(self):
        # negacion de p (NOT p): invierte el valor de la primera proposición.
        return not self.valor1

    def negacion_q(self):
        # negacion de q (NOT q): invierte el valor de la segunda proposición.
        return not self.valor2


if __name__ == "__main__":
    # Prueba rapida: tabla de verdad para todas las combinaciones de p y q.
    casos = [(True, True), (True, False), (False, True), (False, False)]

    for p, q in casos:
        calc = Proposicional(p, q)
        print(f"p={p}, q={q}")
        print(f"  negacion de p (not p): {calc.negacion_p()}")
        print(f"  negacion de q (not q): {calc.negacion_q()}")
        print(f"  conjuncion (p and q): {calc.conjuncion()}")
        print(f"  disyuncion (p or q): {calc.disyuncion()}")
        print(f"  condicional (p -> q): {calc.condicional()}")
        print(f"  bicondicional (p <-> q): {calc.bicondicional()}")
        print(f"  (not p) and q: {calc.negacion_p() and q}")
        print(f"  p and (not q): {p and calc.negacion_q()}")
        print("-" * 40)



