from re import X


class Enzot:

    @staticmethod
    def mensagem(nome):
        return f"Olá mundo doido, aqui é o {nome}!"


    @staticmethod
    def hipotenusa(cateto1, cateto2):
        valor = (cateto1**2 + cateto2**2)**0.5
        return f"O valor da hipotenusa é {valor}"

    @staticmethod
    def raizes(a, b, c):
        x1 = ((-1*b) + (((-4 * a * c) + (b**2))**0.5)) / (2*a)
        x2 = ((-1*b) - (((-4 * a * c) + (b**2))**0.5)) / (2*a)
        return f"O resultado das contas são x1: {x1}, x2: {x2}"