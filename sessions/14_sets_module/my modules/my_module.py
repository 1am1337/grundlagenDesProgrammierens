
def print_something(something_else=""):

    print("something", str(something_else))

# den namen des aktuellen namespaces ausgeben
# print(__name__)

# main program / Hauptprogramm (wird nur ausgeführt, wenn das Script als
# Haptprogramm ausgeführt wird)
if __name__ == "__main__":
    print_something()
    print_something('12345')
