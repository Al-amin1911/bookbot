class bookbot:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_content = ""
        self.char_map = {}
        self.char_sort = []

    def get_book(self):
        with open(self.file_path) as f:
            self.file_content = f.read()

        return self.file_content

    def word_count(self):
        word_list = self.file_content.split()
        return len(word_list)

    def char_count(self):
        file_content = self.file_content.lower()
        for char in file_content:
            if char not in self.char_map:
                self.char_map[char] = 1
            else:
                self.char_map[char] += 1

    
    def sorted_char(self):
        def helper(dictionary):
            return dictionary["num"]
        for char,count in self.char_map.items():
            z = {}
            z["char"] = char
            z["num"] = count
            self.char_sort.append(z)
        
        self.char_sort.sort(reverse=True, key = helper)

        return self.char_sort






    
      