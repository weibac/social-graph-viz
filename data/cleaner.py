string_to_number = {
    'NO': 0,
    'SI': 1,
    'SOY YO': 2
}

input_file = 'raw.csv'
output_file = 'clean.csv'
first_nonheader_line = 412

def process_data(input_file, output_file, first_nonheader_line):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    lines = lines[first_nonheader_line - 1:]
    
    cleaned_data = []
    for line in lines:
        if "No doy mi" in line:
            continue
        if '\"SI, NO\"' in line: # Students picking both YES and NO (frontend error on our part) are assumed to be indecisive and counted as having responded NO
            line = line.replace('\"SI, NO\"', "NO")
        columns = line.strip().split(',')
        columns = columns[2:]
        new_columns = [string_to_number.get(col, col) for col in columns]
        cleaned_line = ','.join(map(str, new_columns))
        cleaned_data.append(cleaned_line)
    
    with open(output_file, 'w') as file:
        file.write('\n'.join(cleaned_data))

process_data(input_file, output_file, first_nonheader_line)

print("Data cleaning completed successfully.")
