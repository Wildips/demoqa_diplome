from dataclasses import dataclass, field
from typing import Literal


subject_type = Literal["Maths", "Chemistry", "English", "Biology", "Hindi"]


@dataclass
class User:
    first_name: str = field(repr=False, default="")
    last_name: str = field(repr=False, default="")
    gender: str = field(repr=False, default="")
    mobile: str = field(repr=False, default="")
    email: str = field(repr=False, default="")
    date_of_birth: str = field(repr=False, default="")
    current_address: str = field(repr=False, default="")
    subject: subject_type = field(repr=False, default="")
    hobbies: str = field(repr=False, default="")
    image: str = field(repr=False, default="")
    state: str = field(repr=False, default="")
    city: str = field(repr=False, default="")
