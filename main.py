from stats import bookbot
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

file_path = sys.argv[1]
run = bookbot(file_path)
run.get_book()
print(f"============ BOOKBOT ============\n Analyzing book found at {sys.argv[1]}...")
print(f"----------- Word Count ----------\n Found {run.word_count()} total words")
print(f"--------- Character Count -------")
run.char_count()
sorted_char = run.sorted_char()
for char_dict in sorted_char:
    if char_dict["char"].isalpha():
        print(f"{char_dict['char']}: {char_dict['num']}")

    
      