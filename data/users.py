from dataclasses import dataclass
from enum import Enum
from typing import List


class Subject(Enum):
    maths = "Maths"
    chemistry = "Chemistry"
    english = "English"
    biology = "Biology"
    hindi = "Hindi"


@dataclass
class User:
    first_name: str | None
    last_name: str | None
    gender: str | None
    mobile: str | None
    email: str | None
    date_of_birth: str | None
    # subject: List[Subject] | None
    subject: Subject | None
    hobbies: str | None
    image: str | None
    current_address: str | None
    state: str | None
    city: str | None
