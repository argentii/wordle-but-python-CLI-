words_five_letters = [
    "apple", "grape", "beach", "chair", "dance", "early", "fence", "ghost", "happy", "arrow",
    "blink", "cabin", "dream", "eagle", "frost", "lemon", "magic", "novel", "ocean", "paint",
    "queen", "river", "score", "track", "unity", "zebra", "amber", "brick", "crane", "daisy",
    "eager", "flame", "glide", "honey", "ivory", "jolly", "knack", "latch", "melon", "noble",
    "oasis", "pearl", "quilt", "raven", "sheep", "tiger", "urban", "vivid", "wheat", "xenon",
    "yield", "zonal", "acorn", "bride", "charm", "delve", "embed", "fable", "grasp", "hatch",
    "inlet", "joint", "karma", "lumen", "mirth", "niche", "orbit", "petal", "quark", "realm",
    "smile", "thorn", "utter", "vigor", "whale", "youth", "azure", "banjo", "coral", "dealt",
    "event", "frost", "giant", "haste", "input", "jazzy", "koala", "ledge", "manor", "ninth",
]   #add more words here if you want^^

with open("five_letter_words.txt", "w") as file: #shane, my cmsc 201 prof, showed us how to use file i/o in python and i finally used it lmao thanks shane
    for word in words_five_letters:
        file.write(word + "\n")

print("words.txt created!")
