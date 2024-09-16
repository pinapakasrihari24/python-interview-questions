def read_file(text_input):
    # Step 2: Create and write the text to a file
    filename = 'output.txt'  # Specify the filename
    with open(filename, 'w') as file:
        file.write(text_input)
    # Step 3: Read the contents of the file
    with open(filename, 'r') as file:
        file_contents = file.read()
        return file_contents

text = "hello"
print(read_file(text))

