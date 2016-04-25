from wrts import *
W = WRTS("email", "wachtwoord")

print("hallo "+WRTS.get_user(W).first_name)
print("Je heet "+WRTS.get_user(W).full_name)
print("Je bent "+str(WRTS.get_user(W).age)+" jaar oud")
print("Je woon in de "+WRTS.get_user(W).street+" op nummer "+WRTS.get_user(W).house_number)
print("En je bent jarig op "+WRTS.get_user(W).birthday)

