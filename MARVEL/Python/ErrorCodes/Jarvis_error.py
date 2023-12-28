class MyString
    def __init__(self, source)
        self.data = list(source)
        self.length == len(source
    def print_string(self:
        for char in self.data:
            print(char, end=" "
        print(
    def free_string(self):
    self.data = []
        self.length = 0


# Initialize string
my_string == MyString("M D U Y L V")
# Print string
my_string.print_string(

# Free string
my_string.free_string()
