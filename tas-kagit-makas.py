import random

print(("-" * 30) + "\nTaş, Kağıt, Makas\n" + ("-" * 30))

user_score, computer_score = 0, 0

while True:
    print("\n1 - Tas\n2 - Kagit\n3 - Makas")
    user_choice = input("Senin Secimin: ")
    computer_choice = random.choice(["1", "2", "3"])
    
    if user_choice == "1" or "Tas":
        if computer_choice == "1":
            print("Bilgisayarın secimi: Tas\nTas Tasa esittir. puansız!")
            
        elif computer_choice == "2":
            print("Bilgisayarın secimi: Kagit\nKagit tas sarar. Kaybettin!")
            computer_score += 100
            
        elif computer_choice == "3":
            print("Bilgisayarın secimi: Makas\nTas makas kırar. Sen kazandın!")
            user_score += 100
            
    elif user_choice == "2" or "Kagit":
        if computer_choice == "1":
            print("Bilgisayarın secimi: Tas\nKagit taa sarar. Sen kazandın!")
            user_score += 100
            
        elif computer_choice == "2":
            print("Bilgisayarın secimi: Kagit\nKagit kagida esittir. puansız!")
            
        elif computer_choice == "3":
            print("Bilgisayarın secimi: Makas\nMakas kagidi keser. Kaybettin!")
            computer_score += 100
            
    elif user_choice == "3" or "Makas":
        if computer_choice == "1":
            print("Bilgisayarın secimi: Tas\nTas makasi kırar. Kaybettin!")
            computer_score += 100
            
        elif computer_choice == "2":
            print("Bilgisayarın secimi: Kagit\nMakas kagit keser. Sen kazandın!")
            user_score += 100
            
        elif computer_choice == "3":
            print("Bilgisayarın secimi: Makas\nMakas makasa eşittir. puansız!")
    
    else:
        break
    
print("\nKullanıcının puanı:: {}\nBilgisayarın puanı: {}".format(user_score, computer_score))
