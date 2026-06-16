import re
import os

# CHANGE THESE
USERNAME = "kev-disie"
REPO = "Ctf_challenges"
BRANCH = "main"
FOLDER = "Attachments"

BASE_URL = f"https://raw.githubusercontent.com/{USERNAME}/{REPO}/{BRANCH}/{FOLDER}/"

def convert_obsidian_images(md_text):
    # 1. Convert ![[image.png]]
    pattern_wiki = r'!\[\[(.*?)\]\]'

    def replace_wiki(match):
        img = match.group(1).strip()
        return f"![{os.path.splitext(img)[0]}]({BASE_URL}{img})"

    md_text = re.sub(pattern_wiki, replace_wiki, md_text)

    # 2. Convert ![text](Attachments/image.png)
    pattern_md = r'!\[(.*?)\]\((.*?)\)'

    def replace_md(match):
        alt = match.group(1)
        path = match.group(2)

        if path.startswith("http"):
            return match.group(0)

        filename = os.path.basename(path)
        return f"![{alt}]({BASE_URL}{filename})"

    md_text = re.sub(pattern_md, replace_md, md_text)

    return md_text


def process_file(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    converted = convert_obsidian_images(content)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(converted)

    print("Done ✔ Medium-ready file created:", output_file)


if __name__ == "__main__":
    process_file("input.md", "medium_ready.md")
