import csv

def append_file1_info(filename, itemcode_dict):
    with open(filename) as file_in:
        file_in.readline()
        reader = csv.reader(file_in)
        for data in reader:
            item_code = data[0]
            item_name = data[1]
            category_name = decipher_category_name(data[3])
            print(category_name)
            input()
            

def decipher_category_name(value):
    if value == "Flower/LeafÂ Vegetables":
        value = "Flower/Leaf Vegetables"
    return value

def append_file2_info(filename, itemcode_dict):
    pass
def append_file3_info(filename, itemcode_dict):
    pass
def append_file4_info(filename, itemcode_dict):
    pass


def main():
    itemcode_dict = {}
    append_file1_info("annex1.csv", itemcode_dict)


main()
