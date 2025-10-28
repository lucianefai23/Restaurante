from src.models.restaurant import Restaurant


class IceCreamStand(Restaurant):

    """Um tipo especializado de restaurante."""

    def __init__(self, restaurant_name, cuisine_type, flavors_list):

        """
        Inicialize os atributos da classe pai.
        Em seguida, inicialize os atributos específicos de uma sorveteria.
        """

        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors_list

    def flavors_available(self):
        
        """
        Percorra a lista de sabores disponíveis e imprima.

        :return: "No momento temos os seguintes sabores de sorvete disponíveis" ou "Estamos sem estoque atualmente!"
        """

        if self.flavors:
            sorvet = '\n'.join(self.flavors)
            return f"No momento temos os seguintes sabores de sorvete disponíveis:\n{sorvet}"   
        else:
            return "Estamos sem estoque atualmente!"

    def find_flavor(self, flavor):
    
        """
        Verifica se o sabor informado está disponível.

        :param flavor: sabor do sorvete
        :return: "Temos no momento o sabor flavor", "Não temos no momento o sabor flavor" ou "Estamos sem estoque atualmente!"
        """

        if self.flavors:
            if flavor in self.flavors:
                return f"Temos no momento o sabor {flavor}!"      
            else:
                return f"Não temos no momento o sabor {flavor}!"          
        else:
            return "Estamos sem estoque atualmente!" 

    def add_flavor(self, flavor):
      
        """
        Add o sabor informado ao estoque.

        :param flavor: sabor do sorvete
        :return: "Sabor já disponivel!", flavor adicionado ao estoque! ou "Estamos sem estoque atualmente!"
        """
        if self.flavors:
            if flavor in self.flavors:
                return "Sabor já disponivel!"                   
            else:
                self.flavors.append(flavor)
                return f"{flavor} adicionado ao estoque!"      
        else:
            return "Estamos sem estoque atualmente!"           