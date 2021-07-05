RESULT_LIST = []

def read_dictionary():
    words_file = open('words_alpha.txt', 'r')
    word_lines = words_file.readlines()
    cleaned_lines = []
    for item in word_lines:
        if len(item) > 3:
            cleaned_lines.append(item[:-1])
    cleaned_lines.sort()
    index_dictionary = {'a': 0}
    for i in range(1, len(cleaned_lines)):
        if cleaned_lines[i][0] != cleaned_lines[i-1][0]:
            index_dictionary[cleaned_lines[i][0]] = i
    return cleaned_lines, index_dictionary


def read_board():
    board_size = int(input("Please input the size of the board: "))
    board_list = []
    line_num = 1
    for line in range(board_size):
        input_prompt = "Please input line " + str(line_num) \
                       + " of the board, no spaces, use Q for qu, otherwise lowercase: "
        board_line = input(input_prompt)
        line_list = []
        for letter in board_line:
            if letter == "Q":
                line_list.append("qu")
            else:
                line_list.append(letter)
        board_list.append(line_list)
        line_num += 1
    return board_list


def word_finder(board_list, word_list, index_dictionary):
    """Takes in a game state, and returns a list of words that can be formed
    in descending order of length"""
    for y in range(len(board_list)):
        for x in range(len(board_list[y])):
            current_prefix = board_list[y][x]
            trace = []
            recursive_parser(board_list, trace, current_prefix, (x, y), word_list, index_dictionary)


def recursive_parser(board_list, current_trace, current_prefix, current_coords, word_list, index_dictionary):
    global RESULT_LIST
    if not prefix_in_dict(current_prefix, word_list, index_dictionary):
        return
    current_trace.append(current_coords)
    queue = []
    neighbors = find_neighbors(current_coords, board_list)
    for coord in neighbors:
        if coord not in current_trace:
            queue.append(coord)
    #print(current_prefix, current_coords, queue, current_trace)  #####DEBUG#####
    if prefix_is_word(current_prefix, word_list, index_dictionary) and current_prefix not in RESULT_LIST:
        RESULT_LIST.append(current_prefix)
    while queue:
        succ_coord = queue.pop()
        x, y = succ_coord
        next_prefix = current_prefix + board_list[y][x]
        recursive_parser(board_list, current_trace, next_prefix, succ_coord, word_list, index_dictionary)
    current_trace.remove(current_coords)
    return


def find_neighbors(current_position, board_list):
    neighbor_list = []
    board_size = len(board_list)
    x, y = current_position
    if x + 1 < board_size:
        neighbor_list.append((x+1, y))
    if x - 1 >= 0:
        neighbor_list.append((x-1, y))
    if x + 1 < board_size and y + 1 < board_size:
        neighbor_list.append((x+1, y+1))
    if x + 1 < board_size and y - 1 >= 0:
        neighbor_list.append((x+1, y-1))
    if x - 1 >= 0 and y + 1 < board_size:
        neighbor_list.append((x-1, y+1))
    if x - 1 >= 0 and y - 1 >= 0:
        neighbor_list.append((x-1, y-1))
    if y + 1 < board_size:
        neighbor_list.append((x, y+1))
    if y - 1 >= 0:
        neighbor_list.append((x, y-1))
    return neighbor_list


def prefix_in_dict(prefix, word_list, index_dictionary):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if prefix[0] != 'z':
        next_letter = alphabet[alphabet.index(prefix[0]) + 1]
        relevant_words = word_list[index_dictionary[prefix[0]]:index_dictionary[next_letter]]
    else:
        relevant_words = word_list[index_dictionary['z']:]
    for word in relevant_words:
        if word.startswith(prefix):
            return True
    return False


def prefix_is_word(prefix, word_list, index_dictionary):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if prefix[0] != 'z':
        next_letter = alphabet[alphabet.index(prefix[0]) + 1]
        relevant_words = word_list[index_dictionary[prefix[0]]:index_dictionary[next_letter]]
    else:
        relevant_words = word_list[index_dictionary['z']:]
    if prefix in relevant_words:
        return True
    else:
        return False


if __name__ == "__main__":
    word_list, index_dictionary = read_dictionary()
    board_list = read_board()
    word_finder(board_list, word_list, index_dictionary)
    RESULT_LIST.sort(key=lambda x: len(x), reverse=True)
    print(RESULT_LIST[:40])
