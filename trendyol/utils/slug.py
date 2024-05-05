def slugify(title: str):
    slug = ""
    AZ_TO_EN_LETTERS = {
        "ə": "e",
        "ç": "c",
        "ş": "s",
        "ğ": "g",
        "ö": "o",
        "ü": "u",
        "ı": "i",
    }   
    for char in title.lower():
        if char in AZ_TO_EN_LETTERS.keys():
            slug += AZ_TO_EN_LETTERS[char]
        elif char.isalnum():
            slug += char
        elif char == ' ':
            if slug and slug[-1] != '-':
                slug += '-'
    return slug


