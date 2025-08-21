def modify_file(input_file, output_file):
    try:
        # Write to input_file
        with open(input_file, 'w') as file:
            file.write("I have been written with precision\n")
            file.write("I love the content in me")

        # Read from input_file
        with open(input_file, 'r') as file:
            content = file.read()
            print(content)

        # Modify content
        upper_case = content.upper()

        # Write to output_file
        with open(output_file, 'w') as file:
            file.write(upper_case)

        print(f"created {output_file}, with modified data successfully.😎")

    except FileNotFoundError:
        print("File Not Found")
    finally:
        print("Files operations completed successfully!")

# Example usage
if __name__ == "__main__":
    modify_file("input.txt", "output.txt")