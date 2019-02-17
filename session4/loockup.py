teen_code = {
    "pt": "Phat trien",
    "eny": "Em nguoi yeu",
    "any": "Anh nguoi yeu",
    "stt": "Status"
}

while True:
    k = input("Enter code : ")
    print(teen_code[k])
    if k =="exit":
        break
    if k in teen_code:
        print(teen_code[k])
    else:
        print("Not found")
        contrib = input("Do you want to contribute (Y/N)").upper()
        if contrib == "Y":
            trans = input("Your translation?")
            teen_code[k] = trans 



        