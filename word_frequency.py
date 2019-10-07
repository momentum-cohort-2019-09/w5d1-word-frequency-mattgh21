STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

# def clean_words:
#     for word in my_words


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""

    with open(file) as my_file:
        my_file = my_file.read()
        
        my_file = my_file.split()
        
        my_words =[]
        for word in my_file:
            word = word.lower()

            my_words.append(word)

        # punctuation = my_words.punctuation()
        # if letter in punctuation:
        #     letter.replace(" ")

        #     # .replace
        #     # .strip
        


        # print(my_words)

        


#read in the file -- done
#split the file into words -- done
#clean each word -- use .lower and maybe .punctuation




#remove stop words

#calculate frequency of each word -- needs a dictionary





if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
