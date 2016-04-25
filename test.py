from wrts import *
W = WRTS("email", "wachtwoord")

"""print("hallo "+WRTS.get_user(W).first_name)
print("Je heet "+WRTS.get_user(W).full_name)
print("Je bent "+str(WRTS.get_user(W).age)+" jaar oud")
print("Je woon in de "+WRTS.get_user(W).street+" op nummer "+WRTS.get_user(W).house_number)
print("En je bent jarig op "+WRTS.get_user(W).birthday)"""
for u in WRTS.get_uitgevers(W):
    for m in u.methods_slug:
        if m == "neue-kontakte":
            for b in WRTS.get_methoden(W, m).covers_id:
                print(WRTS.get_boeken(W, b).lists_list_collection_lists_subject)

