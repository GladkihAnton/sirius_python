from typing import Protocol


class Animal(Protocol):
    def speak(self):
        ...


class Dog:
    def speak(self):
        print("I am a dog")


class Cat:
    def speak(self):
        print("I am a cat")


class Animal1:
    def speak(self):
        raise NotImplementedError


class Dog1(Animal1):
    def speak(self):
        print("I am a dog")


class Cat1(Animal1):
    def speak(self):
        print("I am a cat")


animals: list[Animal] = [Cat(), Dog()]
for animal in animals:
    animal.speak()


animals: list[Animal1] = [Animal1()]
for animal in animals:
    animal.speak()
