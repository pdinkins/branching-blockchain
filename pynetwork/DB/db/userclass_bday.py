import datetime


class User:
    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday  # yyyymmdd

        # extract first and last name
        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]

    def age(self):
        today = datetime.date(2018, 1, 25)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy, mm, dd)   # date of birth
        age_in_days = (today - dob).days
        age_in_years = age_in_days / 365
        return float(age_in_years)


# define the user(s)
user1 = User("first last", "19970902")

print(user1.name)
print(user1.first_name)
print(user1.last_name)
print(user1.birthday)
print(user1.age())





















