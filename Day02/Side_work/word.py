def word_count(file):
    with open(file) as f:
        content = f.read()
        count = 0
        for word in content.split():
            count += 1
        return count

print(word_count('text.txt'))

