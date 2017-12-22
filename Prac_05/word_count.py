Dict = {"a": 0, "collection": 0, "fun": 0, "is": 0, "it": 0, "nice": 0, "of": 0, "thing": 0, "this": 0, "words": 0}
Dict_count = 0
sentence = input("Please provide a sentence: ").lower()
for word in sentence.split():
    Dict_count = 1
    Dict[word] = Dict_count
print(Dict)

