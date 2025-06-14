from langchain.text_splitter import RecursiveCharacterTextSplitter, Language

text = '''# Sample Python Script: Read, Process, and Write Text

def process_text(text):
    """
    Sample text processing function.
    You can replace this with your own logic.
    """
    return text.upper()  # Example: Convert text to uppercase

def main():
    input_file = 'input.txt'
    output_file = 'output.txt'

    try:
        # Read input text
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Process the text
        processed_content = process_text(content)

        # Write the processed content to output file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(processed_content)

        print(f"Processed content written to '{output_file}'")

    except FileNotFoundError:
        print(f"Error: '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
'''
spliiter = RecursiveCharacterTextSplitter.from_language(
    language = Language.PYTHON,
    chunk_size = 200,
    chunk_overlap = 0,
)

chunk = spliiter.split_text(text)

print(chunk[2])

