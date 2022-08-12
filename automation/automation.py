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




test = """One world we cold public trip. Tonight stock two short financial million. Cost some animal great course next eye. danielletaylor@hotmail.com Less or information clear century guess somebody. Sister follow wide report land find.861-26-5898Especially can south wall need.+1-178-383-0937x54779He final hour painting nature people never rise. Home decide ever kind together dinner. danielletaylor@hotmail.com +1-178-383-0937x54779Thank appear test call in key set. Approach agree land him gas alone reach. Agent region book whose military traditional quite.
My evidence little those minute pick approach crime. Compare reflect measure by kind risk boy recently. deleonchristopher@christian-wilson.com Tv career but foot foot actually rise. Type once hot answer.766-91-8057Difference them son born cup probably.001-048-736-2919Much across whether soldier minute. Enough able expect edge these training hit.
Method local same. Event rise ground such. During must view Congress cold seven. Interview special right better. megan54@kramer-solis.com Tonight miss party fill card school personal. Watch letter great worry company why prepare always. More central others learn full.760-45-3403Customer glass here none fight probably use.5599662227Various research deal team security give senior final. Heart career world write policy everything month spend. Name write share price prepare.
Total make campaign build ground. 246-8320 Dinner newspaper woman shoulder me. Short level term discuss character. hsoto@sharp-king.com See occur or hard management trial. View movie spend film defense rise interview.359-09-7400Involve mouth some minute anything.693-728-3320President course serious star. Poor official they society list field.
Adult have end suffer. Notice real culture in treatment radio. dflores@yahoo.com Someone recognize decade movement example. Ago write his us many unit result. Soon team pretty already black charge.690-10-4368Month challenge contain market population her world.6660833177Skill expect social against material. Leg per few no name next.
Always still occur training. Side work attention establish hard. Glass party trade color. Cultural environmental great. aguilarjoseph@hinton-hardin.org According reason history pull class. Group training common first. Teach day tough sit first.038-03-8511Develop ability call lay democratic anyone level trip.437-807-8509x41110Him through fish present return expert family. Arm produce stage series.
Your million yes senior same table up. Worker against ready method. Nothing want certain go might purpose back deep. rebeccathomas@ortiz.net Eye significant hot hard help recently expert. Value himself identify film. Issue good art hand young mean. Somebody exactly such attention mother.717-15-7870Sound community government child here budget authority.+1-057-270-7914x831Mind oil fall speak never finally foot. Take cultural three mother industry hundred. Either develop huge figure prove. Yard sense customer possible let group officer information.
Short group upon add grow society marriage. Assume animal around measure bad toward. john34@yahoo.com Will arm she form either. Thousand national raise must thing.029-86-1921Total physical put.001-430-040-4181x85048Hair just teach fill approach. Character answer current. Hope collection position whatever north take friend. john34@yahoo.com 
Stay conference season worker. Accept suffer food community while. nicholas74@yahoo.com Attention conference back interesting return. White film imagine energy to arm open.079-65-9359Personal buy design reflect trouble picture his.(896)573-1016x36403Red traditional safe election want cover. Father use should hour international affect miss with. Mean she thus hand."""

# find_valid_phone(test)
# standardize_phones(find_valid_phone(test))
# sort_phones(standardize_phones(find_valid_phone(test)))
# add_dash(sort_phones(standardize_phones(find_valid_phone(test))))