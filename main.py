meme_dict = {
            "Tbh": "To Be Honest",
            "Ngl": "Not Gonna Lie",
            "Aka": "As Known As",
            "Asap": "As soon as possible",
            "Lol": "Laugh out loud",
            "Istg": "I swear to god",
            "Idk": "I don't know",
            "Idc": "I don't care",
            "wdym": "What do you mean",
            "Wit": "what is it",
            "wayd": "What are you doing",
            "ttyl": "talk to you later",
            "b4": "before",
            "salfok": "salah fokus",
            "brb": "be right back",
            "ytta": "yang tau-tau aja",
            "gg": "good game",
            "nn": "naon",
            "sns": "sorry not sorry",
            }
word = input("Type what word you don't understand/ Ketik kata yang anda tidak mengerti:")
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    ("the word you're looking for isn't here./ Kata yang anda mengetik tidak ada di sini.")
