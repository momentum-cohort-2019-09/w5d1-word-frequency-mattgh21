STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""

    with open(file) as my_file:
        my_file = my_file.read().lower()
        
        my_file = my_file.split()
        
        my_words =[]
        for word in my_file:
            word = word.lower()

            my_words.append(word)


        
        # print(my_words)
        
        def clean_text(text):
            all_letters = "abcdefghijklmnopqrstuvwxyz"
            keep_text = ""
            for char in text:
                if char in all_letters:
                    keep_text += char
            return keep_text

        clean_words = []

        for word in my_words:
            clean_words.append(clean_text(word))



        # remove stop words

        good_words = [word for word in clean_words if word not in STOP_WORDS]

        # words_final = {}

        # for good_word in good_words:
        #     words_final.update({good_word: good_words.count(good_word)})


        print(good_words)
        # print(clean_words)


        



#read in the file -- done
#split the file into words -- done
#clean each word -- use .lower and maybe .punctuation

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
