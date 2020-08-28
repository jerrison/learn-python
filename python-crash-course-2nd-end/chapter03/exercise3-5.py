guests = ["Thierry Henry", "Bill Gates", "Elon Musk", "Lesie"]

print(f"Unfortunately {guests.pop()} can't make it.")

guests.append("buenona")

print(f"{guests[-1].title()} will take his place instead.")

for i, guest in enumerate(guests):
    print(f"Guest {i} is {guest.title()}.")
