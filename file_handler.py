# File Read & Write + Error Handling Challenge

def main():
    try:
        # Ask user for filename
        input_file = input("Enter the name of the file to read: ")

        # Open and read content
        with open(input_file, "r") as file:
            content = file.read()

        # Modify content (example: make everything uppercase)
        modified_content = content.upper()

        # Write to a new file
        output_file = "modified_" + input_file
        with open(output_file, "w") as file:
            file.write(modified_content)

        print(f"✅ File has been read and modified successfully!")
        print(f"New file created: {output_file}")

    except FileNotFoundError:
        print("❌ Error: The file does not exist. Please check the filename.")
    except PermissionError:
        print("❌ Error: Permission denied. Cannot read the file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
