string_to_number = {
    'NO': 0,
    'SI': 1,
    'SOY YO': 2
}

def process_data(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    lines = lines[1:]
    
    cleaned_data = []
    for line in lines:
        columns = line.strip().split(',')
        columns = columns[2:]
        new_columns = [string_to_number.get(col, col) for col in columns]
        cleaned_line = ','.join(map(str, new_columns))
        cleaned_data.append(cleaned_line)
    
    with open(output_file, 'w') as file:
        file.write('\n'.join(cleaned_data))


input_file = 'raw-data.csv'
output_file = 'data.csv'

process_data(input_file, output_file)

print("Data cleaning completed successfully.")
