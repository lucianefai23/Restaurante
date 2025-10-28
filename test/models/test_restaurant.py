from src.models.restaurant import Restaurant


class TestRestaurant:

    def test_describe_restaurant(self):
        restaurante = Restaurant("Glacial", "Sorvete")
        expected = "Esse restaurante se chama Glacial e serve Sorvete." \
               f"Esse restaurante está servindo 0 consumidores desde que está aberto."

        result = restaurante.describe_restaurant()

        assert expected == result