import unicodedata

def calc_length(text):
    count = 0
    for c in text:
        if unicodedata.east_asian_width(c) in 'FWA':
            count += 2
        else:
            count += 1
    return count

def align_text(text, width):
    fill_count = width - calc_length(text)
    if fill_count <= 0: 
        return text
    return text + '　' * ((fill_count + 1) // 2)