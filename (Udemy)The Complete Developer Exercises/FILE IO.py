# Reading a binary file (e.g., image)
# with open("images.jpeg", "rb") as f:
#     binary_data = f.read()
#     print(binary_data)

# Writing binary data
# with open("copy.jpg", "wb") as f:
#     f.write(binary_data)

# with open("file.txt", "r") as file:
#     data = file.read()  # No need to close manually!
#     print(data)

# with open("file.txt", "r") as f:
#     for line in f:  # Memory-efficient for large files
#         print(line.strip())  # `strip()` removes newline chars

# with open("file.txt", "r+") as f:
#     lines = f.readlines()  # Returns a list of lines
#     second_line = lines[1].split()
#     second_line[1] = "eventuallyEDIT"
#     lines[1]=  " ".join(second_line) + "\n"

#     #Move cursor to the second line
#     f.write(lines[1])
#     print (lines)


# word_to_replace = "eventually"
# replacement_word = "eventuallyEDIT"

# with open("/Users/FRED/Desktop/file.txt", "r+") as f:
#     content = f.read()
#     f.seek(0)  # Reset cursor to start
    
#     # Find all the line start positions
#     lines = content.splitlines(keepends=True)
#     print(lines)
#     if len(lines) < 2:
#         raise ValueError("The file has fewer than 2 lines")

#     # Find where the second line starts in terms of character offset
#     # This will calculate the length of all the characters in first line including \n and \r
#     offset = sum(len(line) for line in lines[:1])
    
#     # Find the position of the word to replace within the second line
#     #find() returns an index position of the first occurrence of the substring, 
#     # only if the substring exists in the input string
#     word_index = lines[1].find(word_to_replace)
#     if word_index == -1:
#         raise ValueError(f"'{word_to_replace}' not found on the second line")

#     absolute_position = offset + word_index

#     # Seek to that position and overwrite the word
#     f.seek(absolute_position) #move cursor to the index of that specific word
#     f.write(replacement_word)



# with open("file.txt", "r") as file:
#     # Get the position after the first line
#     line1 = file.readline()
#     next_line_pos = file.tell()  # Current position (start of next line)
    
#     # Move to the next line explicitly
#     file.seek(next_line_pos)
#     line2 = file.readline()
#     print(line2)


# import mmap

# file_path = "file.txt"
# word_to_replace = b"eventually"
# replacement_word = b"eventual  "

# if len(word_to_replace) != len(replacement_word):
#     raise ValueError("In mmap, replacement word must be the same length as the original.")

# with open(file_path, "r+b") as f:
#     with mmap.mmap(f.fileno(), 0) as mm:
#         # Track line numbers manually
#         line_number = 0
#         line_start = 0

#         for i, byte in enumerate(mm):
#             if byte == ord(b'\n'):  # newline = end of a line
#                 line_number += 1
#                 if line_number == 2:
#                     line_end = i
#                     line_bytes = mm[line_start:line_end]

#                     index = line_bytes.find(word_to_replace)
#                     if index == -1:
#                         raise ValueError(f"'{word_to_replace.decode()}' not found on line 2.")

#                     word_pos = line_start + index
#                     mm[word_pos:word_pos + len(replacement_word)] = replacement_word
#                     break
#                 line_start = i + 1

from translate import Translator

translator = Translator(to_lang="ja")  #japanese
try: 
    with open ("./file.txt", mode= "r+", encoding="utf-8") as my_file:
        text = my_file.read()  # store content in variable after reading
        translation= translator.translate(text)
        print(translation)

        my_file.write("\n" + translation) #writing to the file

        #write to another file - automatically creates file if not exist
        with open ("./file2.txt", mode ="w", encoding="utf-8") as my_file2:
            my_file2.write(translation)

except FileNotFoundError as e:
    print(f" Error: {e}")


