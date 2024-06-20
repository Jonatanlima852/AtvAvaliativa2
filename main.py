# Decorator all decorators CoffeeShop py
# Coffee example using decorators


class PizzaComponent:
    # Componente
    def getDescription(self):
        return self.__class__.__name__

    def getTotalCost(self):
        return self.__class__.cost

class Massa(PizzaComponent):
    # ComponenteConcreto
    cost = 10.00

class Decorator(PizzaComponent):
    # Decorador
    def __init__(self, pizzaComponent):
        self.component = pizzaComponent

    def getTotalCost(self):
        return self.component.getTotalCost() + self.__class__.cost

    def getDescription(self):
        return self.component.getDescription() + ' ' + self.__class__.__name__


class Queijo(Decorator):
    # DecoradorConcretoE
    cost = 10.00
    def __init__(self, pizzaComponent):
        super().__init__(pizzaComponent)

class Molho(Decorator):
    # DecoradorConcretoE
    cost = 5.00
    def __init__(self, pizzaComponent):
        super().__init__(pizzaComponent)

class Azeitona(Decorator):
    # DecoradorConcretoE
    cost = 2.00
    def __init__(self, pizzaComponent):
        super().__init__(pizzaComponent)

class Presunto(Decorator):
    # DecoradorConcretoE
    cost = 8.00
    def __init__(self, pizzaComponent):
        super().__init__(pizzaComponent)

class Frango(Decorator):
    # DecoradorConcretoE
    cost = 15.00
    def __init__(self, pizzaComponent):
        super().__init__(pizzaComponent)

class Calabresa(Decorator):
    # DecoradorConcretoF
    cost = 12.00
    def __init__(self, pizzaComponent):
        super().__init__(pizzaComponent)


# Exemplo de uso
if __name__ == "__main__":
    # Cria uma pizza de calabresa
    pizzaDeCalabresa = Calabresa(Queijo(Molho(Massa())))
    print(pizzaDeCalabresa.getDescription() + ": $" + str(pizzaDeCalabresa.getTotalCost()))

    # Cria uma pizza de frango
    pizzaDeFrango = Azeitona(Frango(Queijo(Molho(Massa())))) 
    print(pizzaDeFrango.getDescription() + ": $" + str(pizzaDeFrango.getTotalCost()))

