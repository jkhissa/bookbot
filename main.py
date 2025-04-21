from stats import get_num_words, count_characters, report
import sys
if len(sys.argv) < 2:
    print("Hello there, to use this program effectively you need to pass a path to a book that you would like analysed, Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    def main():
        book_path = sys.argv[1]
        text = get_book_text(book_path)
        num_words = get_num_words(text)
        char_counts = count_characters(text)
        sorted_chars = report(char_counts)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        
        # Print each character count
        for char_dict in sorted_chars:
            char = char_dict["char"]
            count = char_dict["count"]
            if char.isalpha():  # Only print alphabetical characters
                print(f"{char}: {count}")
        
        print("============= END ===============")

    def get_book_text(path):
        with open(path) as f:
            return f.read()

    main()





