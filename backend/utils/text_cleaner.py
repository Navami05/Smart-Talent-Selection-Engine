import re


def clean_text(text: str) -> str:
    # Replace multiple spaces with a single space
    text = re.sub(r"[ \t]+", " ", text)

    # Remove spaces at the beginning and end of each line
    lines = [line.strip() for line in text.splitlines()]

    # Remove empty lines
    lines = [line for line in lines if line]

    # Join the cleaned lines
    text = "\n".join(lines)

    return text

import re


def clean_text(text: str) -> str:
    # Replace multiple spaces with a single space
    text = re.sub(r"[ \t]+", " ", text)

    # Remove spaces at the beginning and end of each line
    lines = [line.strip() for line in text.splitlines()]

    # Remove empty lines
    lines = [line for line in lines if line]

    # Join the cleaned lines
    text = "\n".join(lines)

    return text


