def sortSentence(s):
    words = s.split()
    rearranged = ['']*len(words)

    for word in words:
        ind, word = int(word[len(word)-1]), word[:len(word)-1]
        rearranged[ind-1] = word

    return ' '.join(rearranged)


s = "is2 sentence4 This1 a3"
print(sortSentence(s))