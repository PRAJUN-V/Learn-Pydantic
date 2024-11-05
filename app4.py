from pydantic import BaseModel
from typing import List, Optional

class Student(BaseModel):
    name: str
    age: int
    fav_subject: List[str]
    family_details: Optional[dict[str, str]] = None

student1 = Student(
    name="Prajun V",
    age=23,
    fav_subject=["English"],
    family_details={
        "Father": "Biju V",
        "Mother": "Preeja V",
        "Sister": "Theja Lakshmi V"
    }
)

print(student1)
