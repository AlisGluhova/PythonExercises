degrees = int(input())
part_of_day = input()
if part_of_day == "Morning":
    if 10 <= degrees <= 18:
        Outfit = "Sweatshirt"
        Shoes = "Sneakers"
        print(f"It's {degrees} degrees, get your {Outfit} and {Shoes}.")
    elif 18 < degrees <= 24:
        Outfit = "Shirt"
        Shoes = "Moccasins"
        print(f"It's {degrees} degrees, get your {Outfit} and {Shoes}.")
    elif degrees >= 25:
        Outfit = "T-Shirt"
        Shoes = "Sandals"
        print(f"It's {degrees} degrees, get your {Outfit} and {Shoes}.")
elif part_of_day == "Afternoon":
    if 10 <= degrees <= 18:
        Outfit = "Shirt"
        Shoes = "Moccasins"
        print(f"It's {degrees} degrees, get your {Outfit} and {Shoes}.")
    elif 18 < degrees <= 24:
        Outfit = "T-Shirt"
        Shoes = "Sandals"
        print(f"It's {degrees} degrees, get your {Outfit} and {Shoes}.")
    elif degrees >= 25:
        Outfit = "Swim Suit"
        Shoes = "Barefoot"
        print(f"It's {degrees} degrees, get your {Outfit} and {Shoes}.")
elif part_of_day == "Evening":
    if 10 <= degrees <= 18:
        Outfit = "Shirt"
        Shoes = "Moccasins"
        print(f"It's {degrees} degrees, get your {Outfit} and {Shoes}.")
    elif 18 < degrees <= 24:
        Outfit = "Shirt"
        Shoes = "Moccasins"
        print(f"It's {degrees} degrees, get your {Outfit} and {Shoes}.")
    elif degrees >= 25:
        Outfit = "Shirt"
        Shoes = "Moccasins"
        print(f"It's {degrees} degrees, get your {Outfit} and {Shoes}.")