string = "One inconvenience I sometimes experienced in so small a house, the difficulty of getting to a sufficient distance from my guest when we began to utter the big thoughts in big words."

print([i for i in string.split() if len(i) < 4])