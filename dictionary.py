# File: dictionary.py
# Assignment 9.1
# Eric Vargas
# DESC: This program will generate a text file from the output rather than printing to the screen.


def process_line(line, word_count_dict):
    # Removes punctuation and splits words.
    characters_remove = ['!', ',', '-', '.']
    for character in characters_remove:
        line = line.lower().replace(character, "")
    for word in line.split():
        add_word(word, word_count_dict)


# Add each word to the dictionary
def add_word(word, word_count_dict):
    if word in word_count_dict:
        word_count_dict[word] += 1
    else:
        word_count_dict[word] = 1


# formats dictionary
def process_file(word_count_dict, new_file):

    # opens and test new .txt file with print statement.
    gba_file = open(new_file, 'w')
    print("This needs to save gettysburg text to new_file", file=gba_file)
    num_words = 0
    for count in word_count_dict.values():
        num_words += count
    sorted_dict = {word: count for word, count in
                   sorted(word_count_dict.items(), key=lambda item: item[1], reverse=True)}
    print("Length of the Dictionary: " + str(num_words), file=gba_file)
    print("Word                   Count", file=gba_file)
    print("-----------------------------", file=gba_file)
    for word in sorted_dict:
        print("{:20}   -  {:3}".format(word, str(sorted_dict[word])), file=gba_file)
    gba_file.close()


def main():
    # Main function opens the file and calls process_line and process_file
    gba_file = open('gettysburg.txt', 'r')
    # prompts the user to enter a new file name.
    new_file = input("Please name your file:\n")

    word_count_dict = {}
    for line in gba_file:
        process_line(line, word_count_dict)
    # closes file
    gba_file.close()
    process_file(word_count_dict, new_file)


if __name__ == "__main__":
    main()
