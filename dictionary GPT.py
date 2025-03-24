def wordcount(s):
    word_count = {}  # Dictionary to store word counts
    words = s.split(' ')  # Split the string into words

    # Count occurrences of each word
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1  # Add new word with count 1

    # Print the results
    for key, value in word_count.items():
        print(f"{key} {value}") 
