def read_words_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            words = [word.strip() for word in file.readlines()]
            return words
    except FileNotFoundError:
        print(f"File {file_name} not found.")
        return []

def get_birth_year():
    while True:
        try:
            birth_year = int(input("Enter your birth year (YYYY): "))
            current_year = datetime.datetime.now().year
            if not (1900 <= birth_year <= current_year):
                raise ValueError(f"Invalid birth year. Please enter a year between 1900 and {current_year}.")
            return birth_year
        except ValueError as e:
            print(e)

def calculate_numeric_sequence(word, birth_year):
    numeric_sequence = []
    letters_sequence = word[:4]
    for char in letters_sequence:
        if char.isalpha():
            char_value = (ord(char.lower()) - ord('a') + 1) * birth_year
            numeric_sequence.append(str(char_value))
    return "-".join(numeric_sequence)

def write_letters_sequence(words_list, output_file, birth_year):
    try:
        with open(output_file, 'w') as file:
            for word in words_list:
                numeric_sequence = calculate_numeric_sequence(word, birth_year)
                file.write(f"{numeric_sequence}\n")
        print(f"Numeric sequences saved to {output_file}.")
    except Exception as e:
        print(f"Error occurred while writing to file: {e}")

if __name__ == "__main__":
    import datetime

    input_file_name = "s.txt"
    output_file_name = "numeric_sequence.txt"

    words_list = read_words_from_file(input_file_name)

    if words_list:
        birth_year = get_birth_year()
        write_letters_sequence(words_list, output_file_name, birth_year)
    else:
        print("No words found in the input file.")
