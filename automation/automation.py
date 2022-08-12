import re

# Regex solution from top comment at https://stackoverflow.com/questions/3868753/find-usa-phone-numbers-in-python-script
regex_phone = r"(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})"
# Regex solution from https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/
regex_email = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

def find_valid_email(text):
    addresses = re.findall(regex_email, text)
    single_emails = [*set(addresses)]
    single_emails.sort()
    return single_emails

def find_valid_phone(text):
    phones = re.findall(regex_phone, text)
    single_phones = [*set(phones)]
    return single_phones

def standardize_phones(phones):
    nums = ["1","2","3","4","5","6","7","8","9","0"]
    new_phones = []
    standard_phones = []

    for phone in phones:
        new = ""
        for char in phone:
            if char in nums:
                new += char
        new_phones.append(new)

    for phone in new_phones:
        if len(phone) == 7:
            new_phone = "206" + phone
            standard_phones.append(new_phone)
        else:
            standard_phones.append(phone)

    return standard_phones

def sort_phones(phones):
    num_phones = []
    for phone in phones:
        num_phones.append(int(phone))
    num_phones.sort()

    sorted_phones = []
    for nums in num_phones:
        str_phone = str(nums)
        if len(str_phone) == 9:
            full_phone = "0" + str_phone
            sorted_phones.append(full_phone)
        else:
            sorted_phones.append(str_phone)

    return sorted_phones

def add_dash(phones):
    new_phones = []

    for phone in phones:
        new_phone = ""
        count = 0
        dash = 0
        for char in phone:
            count += 1
            new_phone += char
            if count % 3 == 0 and dash < 2:
                new_phone += "-"
                dash += 1
        new_phones.append(new_phone)

    return new_phones

# open and read potential_contacts.txt
with open("./potential_contacts.txt") as f:
    potential_contacts = f.read()

emails = find_valid_email(potential_contacts)
phone_nums = add_dash(sort_phones(standardize_phones(find_valid_phone(potential_contacts))))

f = open("emails.txt", "w")
for email in emails:
    f.write(email + "\n")
f.close()

f = open("phone_numbers.txt", "w")
for num in phone_nums:
    f.write(num + "\n")
f.close()