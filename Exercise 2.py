def personal_details(name, surname, date_of_birth, place_of_residence, email, phone_number):
    print(str(f'{name} {surname}, {date_of_birth}, {place_of_residence}, {email}, {phone_number}'))

name = input('Write a name: ')
surname = input('Write a surname: ')
date_of_birth = input('Write date_of_birth: ')
place_of_residence = input('Write a place of residence: ')
email = input('Write an email: ')
phone_number = input('Write a phone number: ')

personal_details(name, surname, date_of_birth, place_of_residence, email, phone_number)