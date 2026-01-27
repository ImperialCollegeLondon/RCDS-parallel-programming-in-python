import string

def count_word_occurrences_in_file(file_path):
    '''
    Count the occurrences of each word in a file.
    
    Args:
        file_path (str): The path to the file to analyze.
        
    Returns:
        dict: A dictionary where the keys are the words in the file and the values are the number of times each word appears.
    '''
    with open(file_path, 'r') as file:
        # Get the text from the file as a string
        text = file.read()

    # Convert the text to lowercase and remove punctuation
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Split the text into a list of words
    words = text.split()    

    # Create a dictionary to store the word occurrences
    word_occurrences = {}
    for word in words:
        # Add the word to the dictionary if it doesn't exist, otherwise increment the count
        if word in word_occurrences:
            word_occurrences[word] += 1
        else:
            word_occurrences[word] = 1

    return sort_dict_by_value(word_occurrences)

def sort_dict_by_value(d):
    '''
    Sort a dictionary by its values in descending order.

    Args:
        d (dict): The dictionary to sort.

    Returns:
        dict: The sorted dictionary.
    '''
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

def form_filepath(i):
    '''
    Form the file path for the essay with index i.

    Args:
        i (int): The index of the essay.

    Returns:
        str: The file path for the essay
    '''
    return f'data/07_essays/essay_{str(i).zfill(3)}.txt'


def add_dictionaries(d1, d2):
    '''
    Add two dictionaries together.

    Args:
        d1 (dict): The first dictionary.
        d2 (dict): The second dictionary.

    Returns:
        dict: The combined dictionary.
    '''
    # Initialize the combined dictionary
    combined_dict = d1.copy()

    # Add the values from the second dictionary to the first dictionary
    for key, value in d2.items():
        if key in combined_dict:
            combined_dict[key] += value
        else:
            combined_dict[key] = value

    return combined_dict

# A sample usage of the functions on the first two essays (essay_000.txt)
# Get the filepath
file_path = form_filepath(0)
# Count the occurrences of each word in the file
word_occurrences_0 = count_word_occurrences_in_file(file_path)

# Repeat for the second file
file_path = form_filepath(1)
word_occurrences_1 = count_word_occurrences_in_file(file_path)

# Add the two dictionaries together
combined_word_occurrences = add_dictionaries(word_occurrences_0, word_occurrences_1)

# Sort the combined dictionary by value
sorted_word_occurrences = sort_dict_by_value(combined_word_occurrences)

# Print the sorted dictionary
print(sorted_word_occurrences)
    