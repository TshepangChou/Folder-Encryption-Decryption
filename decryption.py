import pyzipper

def decrypt_zip(input_file, output_folder, password):
    with pyzipper.AESZipFile(input_file) as zf:
        zf.setpassword(password.encode('utf-8'))
        zf.extractall(path=output_folder)

if __name__ == "__main__":
    input_file = 'encrypted_folder.zip'
    output_folder = 'decrypted_folder'
    password = 'OcIuSk8dGjHEzNYtmo4pqZDQBFsP3rlU'

    decrypt_zip(input_file, output_folder, password)
    print(f"{input_file} has been decrypted into folder '{output_folder}'")