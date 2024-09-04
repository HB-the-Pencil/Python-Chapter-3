"""  If it weren't for PyCharm's editor yelling at me, I would use single quotes for docstrings.
     I must be weird. Double quotes for everything but the one thing you should use them for.

[X] Ask the students not in your pod group what their favorite candy to get on Halloween.

[X] Compile the list of all the candy. Print the list so that you have everyone's name and corresponding candy

[X] Print the list.

[X] Print each item in the list individually

[X] After you print the list you need to sort the list by name and print it again.

[X] Print each item in the list individually again but skip a line between each item

[X] Add Mr. McKinstry's favorite type of candy to the list.

[X] Print the list in reverse order.

[X] Lastly, find and print the length of your list.

Turn in your Python file.

SHOW ALL YOU CODE SO YOU CAN GET CREDIT FOR EVERYTHING. - AKA don't just use print statements.
"""

# Initialize the list.
favoriteCandies = ["Lemonheads", "Milky Way", "Twix", "Twix", "Reese's", "Airheads"]

# Print the list of who likes what.
print(f"Melody's favorite candy is {favoriteCandies[0]}. (She's indecisive.)")
print(f"Audrina's favorite candy is {favoriteCandies[1]}.")
print(f"Mi's favorite candy is {favoriteCandies[2]}.")
print(f"Marvellous's favorite candy is also {favoriteCandies[3]}.")
print(f"Aden's favorite candy is {favoriteCandies[4]}.")
print(f"Brody's favorite candy is {favoriteCandies[5]}.")

# Print the raw list.
print(favoriteCandies)

# Print each item individually. (Man, I wish we could use for loops.)
print(favoriteCandies[0])
print(favoriteCandies[1])
print(favoriteCandies[2])
print(favoriteCandies[3])
print(favoriteCandies[4])
print(favoriteCandies[5])

# Sort the list by name.
favoriteCandies.sort()
print(favoriteCandies)

# Print each item individually again, but with a line of space as a separator.
print(favoriteCandies[0],end="\n\n")  # Holy smokes, using alt-click to make 6 cursors is amazingly helpful.
print(favoriteCandies[1],end="\n\n")
print(favoriteCandies[2],end="\n\n")
print(favoriteCandies[3],end="\n\n")
print(favoriteCandies[4],end="\n\n")
print(favoriteCandies[5])             # This one actually doesn't need an end tag because it's the last one.

# Thank you for agreeing that almond joys are the best.
favoriteCandies.append("Almond Joy")

# Now print it backwards so that McKinstry is number one. (The list is no longer alphabetical.
favoriteCandies.reverse()
print(favoriteCandies)

# How many people answered the mini-survey?
print(len(favoriteCandies))