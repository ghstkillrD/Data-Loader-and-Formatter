def output_data_from_list(data_table: list):
    print("Displaying data from list...")
    i = 0
    while i < len(data_table):
        col_name = data_table[i].replace("COLUMN ", "")
        print("***********************")
        print(col_name)
        print("***********************")
        i += 1
        while i < len(data_table) and not data_table[i].startswith("COLUMN") and not data_table[i] == "END":
            print(data_table[i])
            i += 1


# Example usage:
data_list_example = ['COLUMN Names', 'Fred', 'John', 'COLUMN Addresses', 'Pontypridd', 'Treforest', 'COLUMN Credit', '10', '20', 'COLUMN Product Names', 'Widget1', 'Widget2', 'COLUMN Suppliers', 'SupplierA', 'SupplierB', 'COLUMN Prices', '10', '20']

if __name__ == '__main__':
    print(output_data_from_list(data_list_example))
