calls = 0

def count_calls():
    global calls
    calls = calls + 1

def string_info(string):
    count_calls()
    return (len(string), string.upper(),string.lower())
def is_contains(string, list_to_search):
    count_calls()
    string_1 = string.lower()
    new_list_to_search = []
    for i in range(0, len(list_to_search)):
        new_list_to_search.append(list_to_search[i].lower())
    answer = string_1 in new_list_to_search
    return answer


string_info('Capibara')
result = string_info('Capibara')
print(result)
a = is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
print(a)
print(calls)