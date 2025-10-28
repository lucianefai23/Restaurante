class Restaurant:
    """Model de restaurante simples."""

    def __init__(self, restaurant_name, cuisine_type):
        ### Adicionando docstring
        """
        Inicialize os atributos do restaurante.
        """

        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.open = False

    def describe_restaurant(self):
        return f"Esse restaurante se chama {self.restaurant_name} e serve {self.cuisine_type}." \
               f"Esse restaurante está servindo {self.number_served} consumidores desde que está aberto."

    def open_restaurant(self):
       
        if not self.open:
            self.open = True                                        
            self.number_served = 0                                 
            return f"{self.restaurant_name} agora está aberto!"     
        else:
            return f"{self.restaurant_name} já está aberto!"        

    def close_restaurant(self):
        
        if self.open:
            self.open = False
            self.number_served = 0
            return f"{self.restaurant_name} agora está fechado!"    
              

    def set_number_served(self, total_customers):
       
        if self.open:
            self.number_served = total_customers
            return self.number_served                           
        else:
            return f"{self.restaurant_name} está fechado!"      

    def increment_number_served(self, more_customers):
        
        if self.open:
            self.number_served += more_customers                
            return self.number_served                           
        else:
            return f"{self.restaurant_name} está fechado!"  