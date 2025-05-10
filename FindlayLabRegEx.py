import re

def main():
    # Asks the user for the file name
    file_name = input("Enter the name of the file: ")

    try:
        with open(file_name, 'r') as file: #opens the file and reads it
            content = file.read() #the read file is in content

        # Define RegEx patterns
        ssn = r'\d{3}[-.]\d{2}[-.]\d{4}' #stablishes specific numbers and spaces
        phone_number = r'\d{3}-\d{3}-\d{4}'
        postal_code = r'\d{5}(-\d{4})?'

        # Search for patterns in the file, findall scans for the target meaning patterns
        ssn_matches = re.findall(ssn, content)
        phone_number_matches = re.findall(phone_number, content)
        postal_code_matches = re.findall(postal_code, content)

            # Prints the results
        print(f"US National ID's found: {len(ssn_matches)}")
        print(f"US Phone number's found: {len(phone_number_matches)}")
        print(f"US Postal Codes found: {len(postal_code_matches)}")

    except FileNotFoundError:
        print(f"File '{file_name}' not found. Please provide a valid file name.")

if __name__ == "__main__":
    main()
