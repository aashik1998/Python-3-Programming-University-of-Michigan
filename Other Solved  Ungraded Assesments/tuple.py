#Python has a very powerful tuple assignment feature that allows a tuple of variable names on the left of an assignment statement to be assigned values from a tuple on the right of the assignment. Another way to think of this is that the tuple of values is unpacked into the variable names.
julia = "Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia"

name, surname, birth_year, movie, movie_year, profession, birth_place = julia
print(surname)

#Unpacking Tuples as Arguments to Function Calls
def add(x, y):
    return x + y

print(add(3, 4))
z = (5, 4)
print(add(*z)) # this line will cause the values to be unpacked


