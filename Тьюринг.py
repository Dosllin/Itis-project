test_str = "222220"
test_program = {
    'q1': {" ": [' ', 'L', 'q2'],
           '0': ['0', 'R', 'q1'],
           '1': ['1', 'R', 'q1'],
           '2': ['2', 'R', 'q1'] },
    'q2': {" ": ['1', 'N', '!'],
           '0': ['1', 'N', '!'],
           '1': ['2', 'N', '!'],
           '2': ['0', 'L', 'q2'] },
}

def turing(program, string):
    command = 'q1'
    index_str = 0
    list_str = list(string)
    while command != '!':
        letter = list_str[index_str]
        if letter in program[command].keys():
            action = program[command][letter]
            list_str[index_str] = action[0]
            if action[1] == 'R':
                index_str += 1
                if index_str >= len(list_str):
                    list_str.append(' ')
            elif action[1] == 'L':
                index_str -= 1
                if index_str < 0:
                    list_str.insert(0, ' ')
                    index_str = 0
            command = action[2]
        else:
            raise ValueError
        return ''.join(list_str)
print(test_str, turing(test_program, test_str))

