# New Zealand is amazing.
locations = ["New Zealand", "Japan", "Canada", "Brazil", "Germany", "Indonesia", "Fiji"]

print(locations)
# nothing up my sleeves, nothing behind my back... tada! hey presto! a sorted list!
print(sorted(locations))
# and watch as it magically becomes UNSORTED AGAIN!
print(locations)

# but the magic doesn't stop there! Now it's in... REVERSE alphabetical order!
print(sorted(locations, reverse=True))
# and again, the change is undone!
print(locations)

# Now for the extra tricky trick: a list... printed BACKWARDS!
locations.reverse()  # it takes two whole lines of code
print(locations)
# And now for the undoing of the transformation:
locations.reverse()  # shh.... Don't tell anyone it's literally just the same code
print(locations)

# My friends, this next trick is very serious. We will NOT be able to undo the effects of this magic.
locations.sort()
print(locations)
# The list has now permanently become a sorted list.

# We can still print the reverse alphabetical order.
locations.sort(reverse=True)
print(locations)

# thank you, thank you... A magician never reveals his secrets.