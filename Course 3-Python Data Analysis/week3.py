
import csv

# Problem 1: Reading the field names from a CSV file
def read_csv_fieldnames(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      A list of strings corresponding to the field names in 
      the given CSV file.
    """
    fieldnames = []
    with open(filename, "r") as csvfile:                # don't need to explicitly close the file now
        csvreader = csv.reader(csvfile,
                               delimiter=separator,
                               quotechar=quote)
        for row in csvreader:
            fieldnames.extend(row[:])
            return fieldnames
#Test
#read_csv_fieldnames("/Users/dongdongdongdong/Desktop/hightemp.csv", ',', '“')



# Problem 2: Reading a CSV file into a list of dictionaries
def read_csv_as_list_dict(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a list of dictionaries where each item in the list
      corresponds to a row in the CSV file.  The dictionaries in the
      list map the field names to the field values for that row.
    """
    list_table = []
    with open(filename, "r") as csvfile:
        csvreader = csv.DictReader(csvfile,
                                   delimiter=separator,
                                   quotechar=quote)
        for row in csvreader:
            list_table.append(row)
    print(list_table)
    return list_table
#Test
#read_csv_as_list_dict("/Users/dongdongdongdong/Desktop/hightemp.csv", ',', '“')



# Problem 3: Reading a CSV file into a dictionary of dictionaries
def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      keyfield  - field to use as key for rows
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a dictionary of dictionaries where the outer dictionary
      maps the value in the key_field to the corresponding row in the
      CSV file.  The inner dictionaries map the field names to the 
      field values for that row.
    """
    dict_table = {}
    with open(filename, "rt", newline='') as csvfile:  
        csvreader = csv.DictReader(csvfile,
                                   delimiter=separator,
                                   quotechar=quote)
        for row in csvreader:
            dict_table[row[keyfield]] = row
#    print(dict_table)
    return dict_table
#Test
#read_csv_as_nested_dict("/Users/dongdongdongdong/Desktop/hightemp.csv", 'City', ',', '“')



# Problem 4: Writing a list of dictionaries to a CSV file
def write_csv_from_list_dict(filename, table, fieldnames, separator, quote):
    """
    Inputs:
      filename   - name of CSV file
      table      - list of dictionaries containing the table to write
      fieldnames - list of strings corresponding to the field names in order
      separator  - character that separates fields
      quote      - character used to optionally quote fields
    Output:
      Writes the table to a CSV file with the name filename, using the
      given fieldnames.  The CSV file should use the given separator and
      quote characters.  All non-numeric fields will be quoted.
    """
    with open(filename, 'w', newline='') as csvfile:
#        fieldnames = read_csv_fieldnames(filename, separator, quote)
        writer = csv.DictWriter(csvfile, 
                                fieldnames=fieldnames,
                                delimiter=separator,
                                quotechar=quote,
                                quoting=csv.QUOTE_NONNUMERIC)
        writer.writeheader()
        for row in table:
            writer.writerow(row)
