def generate_document(characters: str, document: str) -> bool:

    doc_arr = list(document.lower())
    chars_arr = list(characters.lower())
    
    for i in doc_arr:
        if not i in chars_arr:
            return False
        else:
            pos = chars_arr.index(i)
            chars_arr.pop(pos)
    
    return True


print(generate_document("Bste!hetsi ogEAxpelrt x ", "AlgoExpert is the best!"))