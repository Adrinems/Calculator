class Calculator:

    def __init__(self, args):
        self.operacion = args[0]
        self.parametros = args[1:]

    def getResult(self):
        operaciones = {'Suma': self.suma(),
                       'Resta': self.resta(),
                       'Multiplicacion': self.mult(),
                       'Division': self.div()}
        return operaciones[self.operacion]

    def suma(self):
        return self.parametros[0] + self.parametros[1]

    def resta(self):
        return self.parametros[0] - self.parametros[1]

    def mult(self):
        return self.parametros[0] * self.parametros[1]

    def div(self):
        return self.parametros[0] / self.parametros[1]
