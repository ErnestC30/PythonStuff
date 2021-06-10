"""
A sentence is a list of words that are separated by a single space with no leading or trailing spaces. 
Each word consists of lowercase and uppercase English letters.
A sentence can be shuffled by appending the 1-indexed word position to each word then rearranging the words in the sentence.
Given a shuffled sentence s containing no more than 9 words, reconstruct and return the original sentence.
"""
def sortSentence(s):
    words = s.split()
    rearranged = ['']*len(words)

    for word in words:
        ind, word = int(word[len(word)-1]), word[:len(word)-1]
        rearranged[ind-1] = word

    return ' '.join(rearranged)


s = "is2 sentence4 This1 a3"
print(sortSentence(s))