print("Welcome, House1's price is 500K L.E")
Q1 = int(input("How much do you have? #In L.E #No Decimals-> for example:500000  "))
if Q1 < 500000:
    print("sorry, there isn't any house with this price but if i find one, i will message you")
elif Q1 > 500000:
    print(f"Perfect! You can buy this house, but in my opinion there is a better house for {Q1}L.E . You have the choice")
else:
    print("Exactly, you afford this house, let's check the house so you can make your decision.")


