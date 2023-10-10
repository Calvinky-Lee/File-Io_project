import csv

def append_file1_info(filename, itemcode_dict):
    with open(filename, encoding='utf-8') as file_in:
        file_in.readline()
        reader = csv.reader(file_in)
        for data in reader:
            product_code = data[0]
            product_name = data[1]
            category_name = decipher_category_name(data[3])

            itemcode_dict[product_code] = [product_name,category_name]

            

def decipher_category_name(value):
    #for some reason i had troubles with the whole string constantly spitting variations of random characters between letters in "Flower/Leaf Vegetables"
    #so i instead did index 0 to check if it was F since "Flower/Leaf Vegetables" is the only cat that starts with F
    if value[0] == "F": 
        value = "Flower/Leaf Vegetables"
    return value


def append_file2_info(filename, itemcode_dict):
    with open(filename, encoding='utf-8') as file_in:
        file_in.readline()
        reader = csv.reader(file_in)
        for data in reader:
            product_code = data[0]
            loss_rate = add_percentage(data[2])
            itemcode_dict[product_code].append(loss_rate)


def add_percentage(value):
    value = "%" + value
    return value

def append_file3_info(filename, itemcode_dict): 
    wholesale_dict = {}
    with open(filename) as file_in:
        file_in.readline()
        reader = csv.reader(file_in)
        for data in reader:
            product_code = data[1]
            wholesale_price = data[2]

            if product_code not in wholesale_dict:
                wholesale_dict[product_code] = [wholesale_price]
            else:
                wholesale_dict[product_code].append(wholesale_price)
    for code in wholesale_dict:
        itemcode_dict[code].append(wholesale_dict[code])

def append_file4_info(filename, itemcode_dict):
    quantity_sold_dict = {}
    selling_price_dict = {}
    
    with open(filename) as file_in:
        file_in.readline()
        reader = csv.reader(file_in)
        for data in reader:
            product_code = data[2]
            quantity_sold = data[3]
            selling_price = data[4]

            if product_code not in quantity_sold_dict:
                quantity_sold_dict[product_code] = [quantity_sold]
            else:
                quantity_sold_dict[product_code].append(quantity_sold)


            if product_code not in selling_price_dict:
                selling_price_dict[product_code] = [selling_price]
            else:
                selling_price_dict[product_code].append(selling_price)
                
    for code in quantity_sold_dict:
        itemcode_dict[code].append(quantity_sold_dict[code])
    for code in selling_price_dict:
        itemcode_dict[code].append(selling_price_dict[code])


def create_data_structure(itemcode_dict):
    Transaction_log = {}
    for data in itemcode_dict:
        data_values = len(itemcode_dict[data]) -1

        itemname = itemcode_dict[data][0]
        category_name = itemcode_dict[data][1]
        loss_rate = itemcode_dict[data][2]

        if data_values >=3:
            wholesale_price = itemcode_dict[data][3]
        else:
            wholesale_price = ""
        if data_values >=4:
            quantity_sold = itemcode_dict[data][4]
        else:
            quantity_sold = ""
        if data_values == 5:
            selling_price = itemcode_dict[data][5]
        else:
            selling_price = ""

        if not category_name in Transaction_log:
            Transaction_log[category_name] = {}
        Transaction_log[category_name][itemname] = {"wholesale_price":wholesale_price \
       ,"loss_rate":loss_rate, "selling_price":selling_price, "quantity_sold":quantity_sold}

    return Transaction_log

def write_data_structure(Transaction_log):
    with open("transaction_log.txt","w") as file_out:
        
        for category in Transaction_log:
            category_print = "Category: "+ category + "\n\n"
            file_out.write(category_print)
            
            for itemname in Transaction_log[category]:
                itemname_print = "\t" + itemname + "\n"
                file_out.write(itemname_print)

                for datakeys in Transaction_log[category][itemname]:
                    values =  Transaction_log[category][itemname][datakeys]
                    data_num = ""
                    for items in values:
                        if not values == "loss_rate":
                            data_num += items + ", "
                        else:
                            data_num = Transaction_log[category][itemname][datakeys][loss_rate]

                    print_data = "\t\t" + datakeys + ": " + data_num + "\n"
                    file_out.write(print_data)

                    
            
    
    

def main():
    itemcode_dict = {}
    append_file1_info("annex1.csv", itemcode_dict)
    append_file2_info("annex2.csv", itemcode_dict)
    append_file3_info("annex3.csv", itemcode_dict)
    append_file4_info("annex4.csv", itemcode_dict)

    Transaction_log = create_data_structure(itemcode_dict)

    write_data_structure(Transaction_log)

main()
