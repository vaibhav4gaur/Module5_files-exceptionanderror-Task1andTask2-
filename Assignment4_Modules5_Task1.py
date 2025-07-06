try:
    with open("hex.txt","r") as f:
         text_file = f.read()
         print(text_file)

except FileNotFoundError:
    print("Error: File 'hex.txt' not found.")
