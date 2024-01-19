def output_total_mean_median(data_table, total_col_name: str):
    if isinstance(data_table, dict):
        print(f"Displaying total from column {total_col_name} from dictionary...")
        if total_col_name not in data_table:
            print(f"Column: {total_col_name} could not be found")
            return
        col_data = data_table[total_col_name]
    else:
        print(f"Displaying total from column {total_col_name} from list...")
        i = 0
        while i < len(data_table) and not data_table[i].replace("COLUMN ", "") == total_col_name:
            i += 1
        if i == len(data_table):
            print(f"Column: {total_col_name} could not be found")
            return
        col_data = data_table[i + 1:]

    numerical_data = []
    for value in col_data:
        try:
            numerical_data.append(int(value))
        except ValueError:
            print(f"One or more values in {total_col_name} could not be converted into numerical values")

    total = sum(numerical_data)
    mean = total / len(numerical_data) if len(numerical_data) > 0 else 0
    median = sorted(numerical_data)[len(numerical_data) // 2] if len(numerical_data) > 0 else 0

    print(f"Total from column {total_col_name} = {total}")
    print(f"The mean of column {total_col_name} = {mean}")
    print(f"The median of column {total_col_name} = {median}")

#Example
data_list_example = [
    "COLUMN Prices",
    "10",
    "20"
]

data_dict_example = {
    "Prices": [10, 20]
}

if __name__ == '__main__':
    print(output_total_mean_median(data_list_example, "Prices"))