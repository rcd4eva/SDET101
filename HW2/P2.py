print("\nSDET101-102 HW2 Part 2, Ricardo DaSilveira, UCID:212-05-998, rcd4@njit.edu\n")


#######=======================#####
#######       Question 4      #####
#######=======================#####
print("\nQuestion 4")
print("a. Combine the two lists into one called numbers.")
print("b. Sort the numbers list in descending order.")
print("c. Remove the number 5 from the list.")
print("d. Print the final list.\n")

odd_numbers = [1, 3, 5, 7, 9]
even_numbers = [2, 4, 6, 8, 10]
numbers = odd_numbers + even_numbers
numbers.sort(reverse=True)
numbers.remove(5)
print(f"Final numbers: {numbers}")

#######=======================#####
#######       Question 5      #####
#######=======================#####
print("\nQuestion 5")
print("a. Create a new list containing the lengths of each word.")
print("b. Find and print the longest word in the list.")
print("c. Create a list of words that start with the letter 'a'.\n")

words = ['python', 'data', 'science', 'machine', 'learning', 'artificial', 'intelligence']
i=0
word_lengths = [len(word) for word in words]
print(f"Word lengths: {word_lengths}")
longest_word = max(words, key=len)
print(f"Longest word: {longest_word}")
a_words = [word for word in words if word.startswith('a')]
print(f"Words starting with 'a': {a_words}")

#######=======================#####
#######       Question 6      #####
#######=======================#####
print("\nQuestion 6")
print("a. Add the two matrices and store the result in a new matrix.")
print("b. Print the resulting matrix.\n")

matrix_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
 
matrix_b = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

#matrix_x is used to verify the list comprehension results
# matrix_x =[
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ] 

matrix_sum = [[matrix_a[col][row] + matrix_b[col][row] for row in range(len(matrix_a[0]))] for col in range(len(matrix_a))]
for row in matrix_sum:
    print(row)