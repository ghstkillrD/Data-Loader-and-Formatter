def output_data_from_dictionary(data_table: dict):
    print("Displaying data from dictionary...")
    for col_name, data in data_table.items():
        print("***********************")
        print(col_name)
        print("***********************")
        for value in data:
            print(value)


# Example usage:
data_table_example = {'Names': ['Fred', 'John'], 'Addresses': ['Pontypridd', 'Treforest'], 'Credit': ['10', '20'], 'Product Names': ['Widget1', 'Widget2'], 'Suppliers': ['SupplierA', 'SupplierB'], 'Prices': ['10', '20']}

if __name__ == '__main__':
    print(output_data_from_dictionary(data_table_example))