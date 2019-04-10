def top_20_words(author):
    # Return a cleaned series of lists of words
    common_words_df = (combined[combined.author == author].text
                       .apply(lambda text: text.translate(None, string.punctuation))
                       .str.lower()
                       .str.split(' '))
    
    # Returns a dictionary where key = words and values = word counts
    dict_of_word_count = {}
    for text in common_words_df:
        for word in text:
            dict_of_word_count[word] = dict_of_word_count.get(word, 0) + 1

    return sorted(dict_of_word_count.iteritems(), key=lambda(v,k): (k,v), reverse=True)[0:20]

def plot_top_20_words(author):
    plt.figure(figsize=(20, 12))
    topwords = top_20_words(author)
    
    words = zip(*topwords)[0]
    freq = zip(*topwords)[1]
    x_pos = np.arange(len(words)) 
    
    sns.barplot(x_pos, freq)
    plt.xticks(x_pos, words)
    plt.title('Top 20 words of: ' + author)
    plt.show()
