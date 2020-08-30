rivers = {"nile": "egypt", "han": "china", "delta": "united states of america"}

print(f"The following is a list of rivers and the country they flow through:  ")
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print(f"\nLet's print all the rivers:")
for river in rivers:
    print(river.title())

print(f"\nLet's print all the countries:")
for country in rivers.values():
    print(country.title())
