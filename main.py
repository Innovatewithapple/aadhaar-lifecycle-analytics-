import pandas as pd
import numpy as np


class Person:
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.getcountofPerson()

    @classmethod
    def getcountofPerson(cls):
        cls.count += 1
