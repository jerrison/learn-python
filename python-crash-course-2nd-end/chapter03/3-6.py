guests = ["Thierry Henry", "Bill Gates", "Elon Musk", "Lesie"]

print(f"Unfortunately {guests.pop()} can't make it.")

guests.append("buenona")

print(f"{guests[-1].title()} will take his place instead.")

for i, guest in enumerate(guests):
    print(f"Guest {i} is {guest.title()}.")

print("Good news! We found a bigger table. I will invite new guests.")

guests.insert(0, "Karl Marx")
guests.insert(
    round(len(guests) / 2), "Pele",
)
guests.append("Barbie")

print("printing invitations".title())

for i, guest in enumerate(guests):
    print(
        f"Dear {guest}, I gladly invite you to my special dinner. When you arrive at the table, please seat yourself in position {i}."
    )
