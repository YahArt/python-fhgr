sentence = "Zählen Sie wie oft in diesem hier geschriebenen Satz der Buchstabe e vorkommt."
print(sentence.count("e"))

sentence = "Ist ein 'ist' in diesem Satz?"
print(sentence.find("ist"))

sentence = "Ich kann keine aes, oes oder ues schreiben. Bitte helfen Sie mir!"
sentence = sentence.replace("ae", "ä").replace("oe", "ö").replace("ue", "ü")
print(sentence)
