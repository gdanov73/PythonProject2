calls=0
def count_calls() :
    global calls
    calls = calls + 1
def string_info(string:str) :
    len(string)
    string.upper()
    string.lower()
    b = (len(string), string.upper(), string.lower())
    count_calls()
    return b
def is_contains(string: str,list_to_search: list) :
    count_calls()
    for i in list_to_search :
        if string.lower() == i.lower() :
           return  True
    return False
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
