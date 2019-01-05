inventor = {
    "gold": 500,
    "pouch": ["flint", "twine", "gemstone"],
    "backpack": ["xylophone", "dagger", "bedroll", "bread loaf" ],
}
print(inventor)

inventor["pocket"] = []
print(inventor)

inventor["pocket"] = ["seashell", "strange", "berry", "lint"]
print(inventor)

inventor["backpack"].remove("dagger")
print(inventor)

inventor["gold"] += 50
print(inventor)