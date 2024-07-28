import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: str
    day_of_birth: str
    month_of_birth: str
    year_of_birth: str
    subjects: str
    hobby: str
    picture: str
    address: str
    state: str
    city: str


user = User(first_name='Roman',
            last_name='Tropin',
            email='tropetcia967@gmail.com',
            gender='Male',
            phone_number='8900900555',
            day_of_birth='11',
            month_of_birth='February',
            year_of_birth='1998',
            subjects='Physics',
            hobby='Sports',
            picture='homework.png',
            address='116 N 2nd St, Cave City, KY 42127, USA',
            state='Uttar Pradesh',
            city='Merrut'
            )
