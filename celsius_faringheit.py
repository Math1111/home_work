class Temperature:
    def __init__(self, celsius=25):
        self.__celsius=celsius

    def celsius_to_faringheit(self, celsius):
        self.__celsius=celsius
        return celsius*1.8+32

    def get_celsius(self):
        return self.__celsius

temp=Temperature(25)
print(temp.celsius_to_faringheit(25))
print(temp.get_celsius())