def spin_words(sentence):

    words = sentence.split()
    ans = []
    
    for word in words:
        if len(word)>=5:
            word = word[::-1]
        ans.append(word)
    return ' '.join(ans)