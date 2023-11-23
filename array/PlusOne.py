#  66. Plus One

# Input: digits = [9]
# Output: [1,0]

# Input: digits = [1,2,3]
# Output: [1,2,4]

# Input: digits = [4,3,9,9]
# Output: [4,4,0,0]

def plusOne(digits):
    # convert the list of digits to a number
    # ! map() returns a list of the results after applying the given function to each item of a given iterable (list, tuple etc.)
    # ? map() takes two parameters: function and iterable (list, tuple etc.) 
    # ? ''.join() returns a string concatenated with the elements of an iterable
    temp = map(str, digits)
    num = int(''.join(temp))
    print(num)
    # add 1 to the number
    num += 1
    
    # convert the number back to a list of digits
    return [int(i) for i in str(num)]


if __name__ == '__main__':
    # print(plusOne([9]))
    # print(plusOne([1,2,3]))
    print(plusOne([4,3,9,9]))