#!/usr/bin/python3
if __name__ == "__main__":

    import hidden_4

    AllNames = dir(hidden_4)
    for names in AllNames:
        if (names[:2] != "__"):
            print(names)
