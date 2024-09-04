# Functions to use:
# .append() X
# .insert() X (apparently placing an X will remove it from the list! that's cool
# .remove() X
# .pop() X
# .sort()
# .reverse() X
# sorted() X
# len() X
# del X
# direct replacement (list[x] = "y") X

# This is a list of some of the spells in a tabletop role-playing game that I'm making.
spells = ["cure", "fire", "thunder", "watr", "blizzard", "cura", "fira", "thundara", "watera", "blizzara",
          "curaga", "firaga", "thundaga", "blizzaga"]
print(spells)

# whoops, forgot waterga (I actually did lol). Better add it now.
spells.insert(13, "waterga")
print(spells)

# Let's add the life spell to the end.
spells.append("life")
print(spells)

# On second thought, there wouldn't be any other life spells. Let's pop it and say we removed it.
print(f"Popped {spells.pop()} from spells")

# Just realized there's a typo in water. Let's fix it.
spells[3] = "water"
print(spells)

# Now that it's good, let's sort the spells from the most powerful first (aka backwards order).
spells.reverse()
print(spells)

# Now I want to temporarily see it by type.
spells.reverse()
print(sorted(spells))

# How many spells is that?
print(len(spells))

# Before I order the elemental spells, I'll remove the healing spells.
del spells[0]  # Cure is the first item in the list
spells.remove("cura")
spells.remove("curaga")  # We don't know where these items are, so we use remove. Also, I needed to use it.
print(spells)

# Now sort the elemental spells by type. (They appear mostly in backwards order, except for water.)
spells.sort()
print(spells)

# and we're done!