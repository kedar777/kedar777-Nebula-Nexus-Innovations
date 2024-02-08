import tkinter as tk
from tkinter import filedialog
import os

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error occurred while reading the file: {e}")
        return None

def write_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        print("File has been successfully updated.")
    except Exception as e:
        print(f"Error occurred while writing to the file: {e}")

def count_words(text):
    words = text.split()
    return len(words)

def count_lines(text):
    lines = text.split('\n')
    return len(lines)

def count_characters(text):
    return len(text)

def replace_words(text, old_word, new_word):
    return text.replace(old_word, new_word)


def main():
    root = tk.Tk()
    root.withdraw() # Hide the root window

    file_path = filedialog.askopenfilename(title="Select Text File", filetypes=[("Text files", "*.txt")])
    if not file_path:
        print("No file selected. Exiting program.")
        return
    
    content = read_file(file_path)
    if content:
        print("Text file content:")
        print(content)

        # Perform text analysis
        num_words = count_words(content)
        num_lines = count_lines(content)
        num_characters = count_characters(content)

        print("\nText analysis:")
        print(f"Number of words: {num_words}")
        print(f"Number of lines: {num_lines}")
        print(f"Number of characters: {num_characters}")

        # Modify content
        old_word = input("\nEnter the word or phrase to replace: ")
        new_word = input("Enter the new word or phrase: ")
        modified_content = replace_words(content, old_word, new_word)

        # Write modified content back to the file
        write_file(file_path, modified_content)

if __name__ == "__main__":
    main()
