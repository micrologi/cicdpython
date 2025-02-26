class Nicolas:
      
    @staticmethod
    def mensagem(nome):
        return f"Olá meu grande mundo, aqui é o {nome}!"

    @staticmethod
    def hipotenusa(ladoa, ladob):
        valor = (ladoa**2 + ladob**2)**0.5
        return f"O valor da hipotenusa é {valor}"

    @staticmethod
    def raizes(a, b, c):
        x1 = ((-1 * b) + (((-4 * a * c) + (b**2))**0.5)) / (2*a)
        x2 = ((-1 * b) - (((-4 * a * c) + (b**2))**0.5)) / (2*a)
        return f"O valor das raízes é {x1} e {x2}"