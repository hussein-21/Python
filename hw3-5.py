# Name: Hussein Alsaidi
# Date: 02/27/2023
# Description: This is part 5 of the  Decisions and Boolean Logic.

pain= input("Enter 'S' if pain is short, sharp and/or shooting or\n'D' if pain dull, throbbing and persistent:")
if pain == "S":
    trigger = input("Enter 'H' if pain triggered by hot or cold drinks or sweets or \n'B' if triggered by biting:")
    if trigger == "H":
        print("Investigate for exposed dentine from gingival, a lost filling or caries.")
    if trigger == "B":
        print("Investigate for Cracked cusp, Loose filling, and/or Fractured tooth")
if pain == "D":
    trigger = input("Enter 'T' if localized, tooth tender to percussion \n or 'I' if local inflammation \n or 'G' if generalized inflammation and necrosis \n or 'D' if local/diffuse pain:")
    if trigger == "T":
        print("Investigate periapical infection, and/or sinusitis ")
    if trigger == "I":
        print("Investigate impacted food, and/or pericoronitis ")
    if trigger == "G":
        print("Check for acute necrotizing ulcerative gingivitis")
    if trigger == "D":
        print("Investigate for dry socket or temporomandibular joint disorder.")