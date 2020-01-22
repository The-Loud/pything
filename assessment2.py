# Use for, .split(), and if to create a
# Statement that will print out words that start with 's':

st = 'Print only the words that start with s in this sentence'
for i in st.split():
    if i[0] == 's':
        print(i)

# Use List Comprehension to create a list
# of the first letters of every word in the string below:

st = 'Create a list of the first letters of every word in this string'
[i[0] for i in st.split()]


# Write a program that prints the integers from
# 1 to 100. But for multiples of three print "Fizz"
# instead of the number, and for the multiples
# of five print "Buzz". For numbers which are
# multiples of both three and five print "FizzBuzz".

mylist = [i for i in range(0, 101)]

for i in mylist:
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
