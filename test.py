import re

def extract_info(lines):
    titles, ytcs, filters = [], [], []

    # Regex patterns to match various parts of the text
    title_pattern = re.compile(r'\bTitle\s*[-:]*\s*(.*)', re.IGNORECASE)
    ytc_pattern = re.compile(r'\bYtc\s*[-:]*\s*(.*)', re.IGNORECASE)
    filter_pattern = re.compile(r'\bFilter\s*[-:]*\s*(.*)', re.IGNORECASE)
    
    current_title = None
    current_ytc = None
    current_filter = None

    for line in lines:
        line = line.strip()
        if line:
            # Check for title
            title_match = title_pattern.search(line)
            if title_match:
                if current_title:  # If there's an existing title, save the previous entry
                    titles.append(current_title)
                    ytcs.append(current_ytc or 'No YTC')
                    filters.append(current_filter or 'No Filter')
                # Update current entry
                current_title = title_match.group(1).strip()
                current_ytc = None
                current_filter = None
                continue  # Skip the rest of the loop for this line
            
            # Check for YTC
            ytc_match = ytc_pattern.search(line)
            if ytc_match:
                current_ytc = ytc_match.group(1).strip()
                continue

            # Check for Filter
            filter_match = filter_pattern.search(line)
            if filter_match:
                current_filter = filter_match.group(1).strip()
                continue

    # Add the last entry to lists
    if current_title:
        titles.append(current_title)
        ytcs.append(current_ytc or 'No YTC')
        filters.append(current_filter or 'No Filter')

    return titles, ytcs, filters

def process_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    titles, ytcs, filters = extract_info(lines)

    # Format and write the result to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        for title, ytc, filter_ in zip(titles, ytcs, filters):
            file.write(f'{title}\n{ytc}\n{filter_}\n\n')

if __name__ == '__main__':
    input_filename = 'input.txt'
    output_filename = 'output.txt'
    process_file(input_filename, output_filename)
