def load_data_from_file_into_list(filename: str):
    data_list = []
    file = open(filename, "r")
    for line in file:
        if line.startswith("COLUMN"):
            data_list.append(line.strip())
        elif not line.strip() == "END":
            data_list.append(line.strip())
    file.close()
    return data_list

if __name__ == '__main__':
    print(load_data_from_file_into_list("file.txt"))