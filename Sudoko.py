correct = [[1, 2, 3],
           [2, 3, 1],
           [3, 1, 2]]

incorrect = [[1, 2, 3, 4],
             [2, 3, 1, 3],
             [3, 1, 2, 3],
             [4, 4, 4, 4]]

incorrect2 = [[1, 2, 3, 4],
              [2, 3, 1, 4],
              [4, 1, 2, 3],
              [3, 4, 1, 2]]

incorrect3 = [[1, 2, 3, 4, 5],
              [2, 3, 1, 5, 6],
              [4, 5, 2, 1, 3],
              [3, 4, 5, 2, 1],
              [5, 6, 4, 3, 2]]

incorrect4 = [['a', 'b', 'c'],
              ['b', 'c', 'a'],
              ['c', 'a', 'b']]

incorrect5 = [[1, 1.5],
              [1.5, 1]]


# check_sudoko function
def check_sudoko(square):
    for row in square:
        # create a list of intergers from 1,2...n
        # check for each number in the row whether it is in the list.
        # remove the numbers from the list once they are verified
        # to ensure that each number occurs only once in the list
        check_list = list(range(1, len(square[0]) + 1))

    for i in row:
        if i not in check_list:
            return False
        check_list.remove(i)

        for n in range(len(square[0])):
            # We do the same here for each column in the square.
            check_list = list(range(1,len(square[0])+1))
            for row in square:
                if row[n] not in check_list:
                    return False
                check_list.remove(row[n])

print(check_sudoko(correct))
