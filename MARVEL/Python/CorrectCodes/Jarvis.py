class MyString:
    def __init__(self, source):
        self.data = ""
        self.length = 0
        self.initialize_string(source)

    def initialize_string(self, source):
        self.length = len(source)
        self.data = source

    def print_string(self):
        for i in range(self.length):
            print(chr(ord(self.data[i]) - 1), end="")
        print()

    def free_string(self):
        self.data = ""
        self.length = 0


def main():
    my_string = MyString("NEVZMW")
    my_string.print_string()
    my_string.free_string()


if __name__ == "__main__":
    main()
