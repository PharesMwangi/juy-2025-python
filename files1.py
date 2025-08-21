def modify_file(input_file, output_file):
    try:
        # Read from input_file
        with open(input_file, 'r') as file:
            content = file.read()
            print("Original content:\n", content)

        # Modify content
        upper_case = content.upper()

        # Write to output_file
        with open(output_file, 'w') as file:
            file.write(upper_case)

        print(f"Created {output_file} with modified data successfully.😎")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except IOError:
        print(f"Error: Could not read the file '{input_file}'.")
    finally:
        print("File operations completed.")

if __name__ == "__main__":
    filename = input("Enter the filename to read: ")
    modify_file(filename, "output.txt")