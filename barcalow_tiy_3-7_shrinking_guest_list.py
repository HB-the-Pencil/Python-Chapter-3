invitees = ["C.S. Lewis", "J.R.R. Tolkien", "T.S. Eliot"]
print(f"To Mr. {invitees[0]}: You are cordially invited to a dinner party. Please arrive at 6 PM. Book readings to follow.")
print(f"To Mr. {invitees[1]}: You are cordially invited to a dinner party. Please arrive at 6 PM. Book readings to follow.")
print(f"To Mr. {invitees[2]}: You are cordially invited to a dinner party. Please arrive at 6 PM. Book readings to follow. Please have a speech prepared.")

print()

print("To whom it may concern: A larger table has been found, allowing for more space for dinner guests. Please bring a friend if possible.")

print()

invitees.insert(0, "Charles Williams")
invitees.insert(2, "Owen Barfield")
invitees.append("Norton Juster")

print(f"To Mr. {invitees[0]}: You are cordially invited to a dinner party. Please arrive at 6 PM. Book readings to follow.")
print(f"To Mr. {invitees[1]}: You are cordially invited to a dinner party. Please arrive at 6 PM. Book readings to follow.")
print(f"To Mr. {invitees[2]}: You are cordially invited to a dinner party. Please arrive at 6 PM. Book readings to follow.")
print(f"To Mr. {invitees[3]}: You are cordially invited to a dinner party. Please arrive at 6 PM. Book readings to follow.")
print(f"To Mr. {invitees[4]}: You are cordially invited to a dinner party. Please arrive at 6 PM. Book readings to follow.")
print(f"To Mr. {invitees[5]}: You are cordially invited to a dinner party. Please arrive at 6 PM. Book readings to follow.")

# New code is below here.

print()

# Bad news...
print("Unfortunately, we have just learned that the table will not arrive until the day after the dinner party.")

print()

# I don't think Norton Juster will be too torn up about it.
print(f"""To Mr. {invitees.pop()}:
  Our sincerest apologies, but due to shipping delays, the large table will not arrive in time for the dinner party.
  Therefore, we do not have enough room at our table to entertain everyone.
  We hope you are not offended.""")
# Continuing to work backwards...
print(f"""To Mr. {invitees.pop(2)}:
  Our sincerest apologies, but due to shipping delays, the large table will not arrive in time for the dinner party.
  Therefore, we do not have enough room at our table to entertain everyone.
  We hope you are not offended.""")
print(f"""To Mr. {invitees.pop(0)}:
  Our sincerest apologies, but due to shipping delays, the large table will not arrive in time for the dinner party.
  Therefore, we do not have enough room at our table to entertain everyone.
  We hope you are not offended.""")
# And finally, we remove T.S. Eliot:
print(f"""To Mr. {invitees.pop()}:
  Our sincerest apologies, but due to shipping delays, the large table will not arrive in time for the dinner party.
  Therefore, we do not have enough room at our table to entertain everyone.
  We hope you are not offended.""")

print()

# Leaving us with only C.S. Lewis and J.R.R. Tolkien.
print(f"To Mr. {invitees[0]}: The dinner party is still in effect, though with a much-reduced number of attendees. Please arrive at 6 PM.")
print(f"To Mr. {invitees[1]}: The dinner party is still in effect, though with a much-reduced number of attendees. Please arrive at 6 PM.")

# Now that they're invited, we can cross them off of our list.
del invitees[0]
del invitees[0]  # This threw an error because it was "del invitees[1]" and invitees[1] no longer existed.

print(invitees)