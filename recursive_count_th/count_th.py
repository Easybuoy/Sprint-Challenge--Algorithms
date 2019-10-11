'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word, count=0, index=0):
    count = 0
    index = 0

    def countWord(word, count, index):
        # Convert word to array
        splitWord = list(word)
        if (index < len(list(word)) - 1):
            # Check if combined word at index and index+1 is equal to th
            if (splitWord[index] + splitWord[index+1] == 'th'):
                count += 1
                index += 1
                return countWord(word, count, index)
            else:
                index += 1
                return countWord(word, count, index)
        else:
            return count

    return countWord(word, count, index)


print(count_th('wothath'))
