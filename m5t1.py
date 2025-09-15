file_name = input("Enter the file name (with extension): ")
try:
    with open(file_name, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(file_name ," was not found. Please check the file path.")

