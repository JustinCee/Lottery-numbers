import rsaidnumber
from datetime import date, datetime

id_number = rsaidnumber.parse('9610055082082')
print(id_number.date_of_birth)


def age():
    sub = (id_number - date)
    return sub


print(age)
