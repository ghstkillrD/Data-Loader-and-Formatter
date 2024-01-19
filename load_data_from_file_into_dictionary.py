def load_data_from_file_into_dictionary(filename: str):
    data_dictionary = {}
    current_column = None
    file = open(filename, "r")
    for line in file:
        if line.startswith("COLUMN"):
            current_column = line.strip().replace("COLUMN ", "")
            data_dictionary[current_column] = []
        elif not line.strip() == "END":
            data_dictionary[current_column].append(line.strip())
    file.close()
    return data_dictionary

if __name__ == '__main__':
    print(load_data_from_file_into_dictionary("file.txt"))