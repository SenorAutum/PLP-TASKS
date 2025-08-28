import os

# --- Part 1: File Read & Write Challenge ---

def file_read_write_challenge():
    """
    Creates, writes to, reads from, and appends to a file.
    """
    print("--- Running File Read & Write Challenge ---")
    try:
        # Step 1: Create and write to a new file
        # 'w' mode creates a file if it doesn't exist, and overwrites it if it does.
        with open("my_file.txt", "w") as file:
            file.write("This is the first line of the file.\n")
            file.write("Here is line number 2 with some numbers: 12345.\n")
            file.write("And this is the third and final initial line.\n")
        print("✅ Successfully created and wrote to 'my_file.txt'")

        # Step 2: Read the file and display its contents
        print("\n--- Reading from 'my_file.txt' ---")
        with open("my_file.txt", "r") as file:
            content = file.read()
            print(content)
        print("✅ Successfully read the file.")

        # Step 3: Append to the file
        # 'a' mode opens the file for appending, without overwriting existing content.
        with open("my_file.txt", "a") as file:
            file.write("\nAppending a new line here.\n")
            file.write("And another one for good measure.\n")
        print("\n✅ Successfully appended new lines to 'my_file.txt'")
        
        print("\n--- Final content of 'my_file.txt' ---")
        with open("my_file.txt", "r") as file:
            final_content = file.read()
            print(final_content)

    except Exception as e:
        print(f"An unexpected error occurred during the file challenge: {e}")


# --- Part 2: Error Handling Lab ---

def error_handling_lab():
    """
    Asks the user for a filename and handles potential errors.
    """
    print("\n\n--- Running Error Handling Lab ---")
    try:
        # Ask the user for a filename
        filename = input("Please enter the name of the file you want to read: ")
        
        # Try to open and read the file
        with open(filename, "r") as file:
            content = file.read()
            print(f"\n--- Contents of '{filename}' ---")
            print(content)
            print("✅ Successfully read the file.")

    except FileNotFoundError:
        # This block runs if the file does not exist.
        print(f"Error: The file '{filename}' was not found. Please check the name and try again.")
    
    except PermissionError:
        # This block runs if the script doesn't have permission to read the file.
        print(f"Error: You do not have permission to read the file '{filename}'.")

    except Exception as e:
        # A general catch-all for any other unexpected errors.
        print(f"An unexpected error occurred: {e}")
    finally:
        # This block runs no matter what, whether there was an error or not.
        print("\n--- Error handling lab finished. ---")


# --- Main execution ---
if __name__ == "__main__":
    file_read_write_challenge()
    error_handling_lab()
