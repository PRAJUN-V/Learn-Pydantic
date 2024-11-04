from pydantic import BaseModel

class Fruit(BaseModel):
    name: str
    number: int

# fruit1 = Fruit(name=1, number="Orange") # This will give error because of pydantic validation.

fruit2 = Fruit(name="Apple", number=2)
print(fruit2)
print(type(fruit2))
