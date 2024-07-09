import hashlib

def get_hash_function(algorithm):
    if algorithm == "md5":
        return hashlib.md5
    elif algorithm == "sha1":
        return hashlib.sha1
    elif algorithm == "sha256":
        return hashlib.sha256
    elif algorithm == "sha512":
        return hashlib.sha512
    else:
        raise ValueError("Unsupported hash algorithm")

def compute_hash(string, algorithm):
    hash_function = get_hash_function(algorithm)
    return hash_function(string.encode()).hexdigest()

def load_dictionary(file_path):
    with open(file_path, "r", encoding="latin-1") as file:
        return [line.strip() for line in file.readlines()]

def main():
    hash_to_crack = input("Enter the hash to crack: ")
    dictionary_file = input("Enter the dictionary file path: ")
    algorithm = input("Enter the hash algorithm (md5, sha1, sha256, sha512): ").lower()

    dictionary = load_dictionary(dictionary_file)
    
    for word in dictionary:
        if compute_hash(word, algorithm) == hash_to_crack:
            print(f"Cracked: {word} --> {hash_to_crack}")
            break
    else:
        print("No match found.")

if __name__ == "__main__":
    main()