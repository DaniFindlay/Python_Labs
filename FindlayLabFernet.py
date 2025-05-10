from cryptography.fernet import Fernet

# generate a Fernet key
def generate_fernet_key():#defines the fuction
    key = Fernet.generate_key()#generates the key
    with open("FindlayKey", "wb") as key_file:#create and opens a file Findlaykey
        key_file.write(key)#writes the key in the file. 
    return key

#encrypts name and student number
def encrypt_name_and_id(name, student_id, key):#defines the function
    f = Fernet(key)#ferney key is defined as f
    plaintext = f"{name} {student_id}".encode()#the plain text is encoded
    ciphertext = f.encrypt(plaintext)#encripts the text
    with open("FindlayFile", "wb") as encrypted_file:#creates the second file and assign the content
        encrypted_file.write(ciphertext)#writes the content which is the ciphertxt. 

# replaces with your last name and student ID with my actual information
your_last_name = "Findlay"  # my last name
your_student_id = "098765"  # my student id

#generates the Fernet key
fernet_key = generate_fernet_key()

#encrypts and savse the name and student ID
encrypt_name_and_id(your_last_name, your_student_id, fernet_key)

#print out the files and content creationg succesfully. 
print("Fernet key saved to FindlayKey")
print(f"Encrypted data saved to FindlayFile")
