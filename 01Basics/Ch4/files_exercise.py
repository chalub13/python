#
# Read and write files using the built-in Python file methods
#


def main():
    # Open a file for writing and create it if it doesn't exist
    # f = open("textfile.txt", "w+")

    # Open the file for appending text to the end
    # f = open("textfile.txt", "a")
    # write some lines of data to the file
    # for i in range(10):
    #  f.write("This is a line #: " + str(i) + "\r\n")

    # close the file when done
    # f.close()

    # Open the file back up and read the contents
    f = open("textfile.txt", "r")
    if f.mode == "r":
        contents = f.read()
        print(contents)

        for i in f.readlines():
            print(i)


if __name__ == "__main__":
    main()

