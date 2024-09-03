invitees = ["C.S. Lewis", "J.R.R. Tolkien", "Norton Juster"]
print(f"To Mr. {invitees[0]}: You are cordially invited to a dinner party. Please arrive at 6 PM. Book readings to follow.")
print(f"To Mr. {invitees[1]}: You are cordially invited to a dinner party. Please arrive at 6 PM. Book readings to follow.")
print(f"To Mr. {invitees[2]}: You are cordially invited to a dinner party. Please arrive at 6 PM. Book readings to follow. Please have a speech prepared.")

print()

# oh dear~ Norton Juster can't make it.
print(f"{invitees[2]} has declined to attend, saying he is uncomfortable with making a speech in front of {invitees[0]} and {invitees[1]}.")

print()

# Maybe T.S. Eliot would better enjoy the company of the others.
invitees[2] = "T.S. Eliot"
print(f"To Mr. {invitees[0]}: You are cordially invited to a dinner party. Please arrive at 6 PM. Book readings to follow.")
print(f"To Mr. {invitees[1]}: You are cordially invited to a dinner party. Please arrive at 6 PM. Book readings to follow.")
print(f"To Mr. {invitees[2]}: You are cordially invited to a dinner party. Please arrive at 6 PM. Book readings to follow. Please have a speech prepared.")