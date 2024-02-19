def capslock(random_string):
    '''
    Hallo Welt
    '''
    return(random_string.upper())


def capitalize_first_letters(input_string):
    '''
    merhaba dünya
    '''
    words = input_string.split()
    capitalized_words = [word.capitalize() for word in words]
    result_string = ' '.join(capitalized_words)
    return result_string