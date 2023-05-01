import os
import re
from googletrans import Translator

def split_front_matter(content):
    pattern = r"(?s)(---.*?---)(.*)"
    match = re.match(pattern, content)
    if match:
        return match.groups()
    return None, content

def translate_content(content, src, dest):
    translator = Translator()
    return translator.translate(content, src=src, dest=dest).text

def format_content(text):
    text = re.sub(r'(?<=[.,;:])(?=[^\s])', r' ', text)

    text = re.sub(r'((?<=\*\*)|(?<=\*)|(?<=_)|(?<=`))\s+|\s+((?=\*\*)|(?=\*)|(?=_)|(?=`)|$)', '', text)

    return text

def main():
    content_dir = "content/posts"

    for root, dirs, files in os.walk(content_dir):
        for file in files:
            if file == "index.en.md":
                break
            if file == "index.es.md":
                file_path = os.path.join(root, file)

                with open(file_path, "r") as f:
                    content = f.read()

                front_matter, body = split_front_matter(content)
                translated_body = translate_content(body, "es", "en")
                formated_body = format_content(translated_body)

                translated_file_path = os.path.join(root, "index.en.md")
                with open(translated_file_path, "w") as f:
                    f.write(front_matter)
                    f.write("\n")
                    f.write(formated_body)

                print(f"Translated post: {translated_file_path}")

if __name__ == "__main__":
    main()