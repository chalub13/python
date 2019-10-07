#
# Example file for working with loops
#


def main():
    x = 0

    # define a while loop
    print("define a while loop")
    while x < 5:
        print(x)
        x += 1

    # define a for loop
    print("define a for loop")
    for i in range(5, 10, 2):
        print(i)

    # use a for loop over a collection
    print("use a for loop over a collection")
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for x in days:
        print(x)

    # use the break and continue statements
    print("use the break and continue statements")
    for i in range(5, 10):
        # if i == 7:
        #     break
        if i % 2 == 0:
            continue
        print(i)

    # using the enumerate() function to get index
    print("using the enumerate() function to get index")
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for i, d in enumerate(days):
        print(i, d)


if __name__ == "__main__":
    main()
