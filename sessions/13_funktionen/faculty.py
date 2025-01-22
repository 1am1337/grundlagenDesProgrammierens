
def faculty(n):

    if n <= 1:
        return 1

    return n * faculty(n - 1)

print(faculty(5000))
