class Animal:
    def speak(self):
        print("Животное говорит")


class Dog(Animal):
    def speak(self):
        print("�� пес: гав! гав!")


class Big_dog(Animal):
    def speak(self):
        print("Большой пёс: гав! гав! гав!")


class Small_dog(Animal):
    def speak(self):
        print("Маленький пёс:тяф!тяф!")

class Toy_dog(Dog):
    def speak(self):
        pass

class Robot_dog(Toy_dog):
    def speak(self):
        print("Робочn пёс: тяф!тяф! тяф!тяф!")


class BigAngryDog(Big_dog):
    def speak(self):
        print('Взгляд злой')
        Big_dog.speak(self)
        print('Хмурится')

class Cat(Animal):
    def _meow(self):
        print("Мяу!")
    def speak(self):
        self._meow()

class NewCat(Cat):
    def _meow(self):
        print("пуфф")

cat=Cat()
cat.speak()

new_cat=NewCat()
new_cat.speak()

angry=BigAngryDog()
angry.speak()

animal=Animal()
animal.speak()

dog=Dog()
dog.speak()

small_dog=Small_dog()
small_dog.speak()

big_dog=Big_dog()
big_dog.speak()

robot_dog=Robot_dog()
robot_dog.speak()

def say_n_times(animal, times):
    for _ in range(times):
        animal.speak()
dryzok=BigAngryDog()
say_n_times(dryzok, 3)
print('---------')

cat=Cat()
say_n_times(cat, 2)

print('------')
list_of_animals=[Cat(),Dog(),NewCat(), BigAngryDog()]
for animal in list_of_animals:
    animal.speak()
