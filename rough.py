file = "/content/Audio_trimmed_wav/Lecture 03: Introduction (Cont'd).wav"
text_data = "aircraft structures i prof anup ghosh department of aerospace engineering indian institute of technology \u2013 kharagpur module \u2013 one lecture \u2013 three introduction continued welcome back"
a = file.split('/')[-1].split('.')[0]
print(a[-1])

b = a[-1].split('.')
print(b[0])
vocabulary = set()
vocabulary.update(text_data.split())
print(vocabulary)

chars = set()
chars.update(file)
print(chars)