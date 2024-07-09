import requests
from concurrent.futures import ThreadPoolExecutor

# Función para verificar si un directorio existe
def check_directory(url, directory):
    try:
        full_url = f"{url}/{directory}"
        response = requests.get(full_url)
        if response.status_code == 200:
            print(f"Found: {full_url}")
    except requests.RequestException as e:
        print(f"Error accessing {full_url}: {e}")

# Leer el diccionario de directorios
def load_dictionary(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file]

def main():
    url = input("Enter the target URL (e.g., http://example.com): ").strip()
    dictionary_path = input("Enter the path to the dictionary file (e.g., common.txt): ").strip()

    directories = load_dictionary(dictionary_path)

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(check_directory, url, directory) for directory in directories]

    for future in futures:
        future.result()

if __name__ == "__main__":
    main()