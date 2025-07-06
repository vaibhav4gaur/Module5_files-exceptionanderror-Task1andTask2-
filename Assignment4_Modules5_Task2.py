user_input = input("Enter text to write to the file: ")
with open("result.txt","a") as f:
    f.write(user_input + "\n")
    print("Data successfully written to result.txt.")

user_input1 = input("Enter additional text to append: ")
with open("result.txt","a") as f:
    f.write(user_input1 + "\n")
    print("Data successfully appended to result.txt.")

print("Final Performance of result.txt: ")
with open("result.txt","r") as f:
    perform_file = f.read()
    print(perform_file)