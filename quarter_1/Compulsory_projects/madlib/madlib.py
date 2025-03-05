print("Welcome to Madlib Game")

adjective : str = input("Enter an adjective: ")
noun :str = input("Enter a noun: ")
verb :str = input("Enter a verb: ")
adjective1 :str = input("Enter another adjective: ")
noun1 :str = input("Enter another noun: ")
verb1 :str = input("Enter another verb: ")

story = f" Once upon a time, there was a very {adjective} {noun} who loved to {verb} every day. \
one day, it met a {adjective1} {noun1} who was always {verb1} in the forest. They became best friend!"
    
print(story)