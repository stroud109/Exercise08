#!/usr/bin/env python
# starting key should begin with a capital letter
# last string added should end with a ., ! or ?


import sys, random, twitter

def make_chains(corpus, len_gram):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    markov_dict = {}

    #for line in corpus:
    words = corpus.split() # words refers to words in a line

    for i in range(len(words)-len_gram):
        next_word = words[i+len_gram]
        key = tuple(words[i:i+len_gram])

        # val = []
        if markov_dict.get(key):
            markov_dict[key].append(next_word)
        else:
            markov_dict[key] = [next_word]

        # val = markov_dict.get(key, [])
        # val.append(next_word) # modifies the original list

        # if (words[i], words[i+1]) not in markov_dict:
        #     markov_dict[(words[i], words[i+1])] = [words[i+2]]
        # else:
        #     markov_dict[(words[i], words[i+1])].append(words[i+2])
        
    return markov_dict

def make_text(chains, len_gram): # chains is a dictionary
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""

    capitalized_key_list = []

    for key in chains.keys(): # chains.keys() results in in a list
        if key[0].istitle():
            capitalized_key_list.append(key)
    
    random_key = random.choice(capitalized_key_list) # this key needs to be a random CAPPED key
    random_value = random.choice(chains[random_key])

    new_text = []

    for i in random_key:
        new_text.append(i)

    new_text.append(random_value)

    while True:
        new_key = tuple(new_text[-len_gram:])

        if new_key in chains:
            new_value = random.choice(chains[new_key])

            if len(" ".join(new_text)) + len(new_value) < 140:
                new_text.append(new_value)
            else:
                break
        else:
            break

    # starting key should begin with a capital letter
    # last string added should end with a . ! or ?
    # no punctuation should occur until the final character 


    return " ".join(new_text) 

def main():
    # constant variable
    LEN_GRAM = 2

    filename = sys.argv[1]
    f = open(filename)

    # Change this to read input_text from a file
    input_text = f.read()
    
    chain_dict = make_chains(input_text, LEN_GRAM)
    random_text = make_text(chain_dict, LEN_GRAM)
    # print random_text

    api = twitter.Api(consumer_key='x',
                      consumer_secret='x', 
                      access_token_key='x', 
                      access_token_secret='x')

    status = api.PostUpdate(random_text)
    print status.text

    return input_text

if __name__ == "__main__":
    main()