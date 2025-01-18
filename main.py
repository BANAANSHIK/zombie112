class Person:
    name="никто"
    weight=0
    height=0
    def __init__(self, newName, newHeight, newWeight):
        self.name = newName
        self.height = newHeight
        self.weight = newWeight

    def walk(self,where='парке'):
        print(self.name, "гуляет в", where)
    # Создать метод (функция, которая находится внутри класса)
    # который будет выводить сообщение от персонажа
    def say(self, text=""):
        print(self.name, "говорит:", text)
        
    def personInfo(self):
        print("Имя", self.name)
        print("Рост", self.height, "см")
        print("Вес", self.weight, "кг")

person_1 = Person("Петя", 220, 500)
person_2 = Person("Зелебоба", 100, 500)

person_1.personInfo()

person_1.walk("пруду")
person_2.walk()
person_1.say("какой хороший день, чтобы пойти куда-нибудь")
person_2.say("Ты че, дурак, штоле?")



# TODO Создать класс СОБАКА, добавить ей характеристики: кличка, порода, вес, злоба, доброта, дрожь
# TODO Добавить методы (функции) бега (должно выводиться "Собака КЛИЧКА бежит") и вывода информации о собаке
# Кличка: Пуська, порода: Доберман, вес: 100 кг, злоба: 70%, доброта: 30%, дрожь: 0%

# TODO Создать класс КОТ, у него должны быть такие же функции.
# TODO ДОбавить обоим классам функцию погони за другим животным. Например: Собака Лайка бежит за Мурзиком.
# функция должна принимать второе животное в качестве аргумента и выводить его имя
class Dog:
    def __init__(self, newName, newBreed, newWeight, newEvil, newGood, newShake):
        self.name = newName
        self.breed = newBreed
        self.weight = newWeight
        self.evil = newEvil
        self.good = newGood
        self.shake = newShake
    def info(self):
        print("Кликуха:", self.name)
        print("Порода:", self.breed)
        print("Вес:", self.weight)
        print("Процент злобы:", self.evil)
        print("Процент доброты:", self.good)
        print("Процент дрожи:", self.shake)
    def run(self):
        print(self.name,"бежит")

dog1 = Dog("Пуська", "чихуахуа", 5, 50, 5, 45)
dog1.run()
dog1.info()
dog2 = Dog("Марс", "Блохастая", 15, 10, 90,0)
dog2.info()