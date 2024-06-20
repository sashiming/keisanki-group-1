class Info1:
    def __init__(self, s):
        data = s.split()
        self.word = data[0]
        if data[1] == "p":
            self.value = 1
        elif data[1] == "n":
            self.value = -1
        else:
            self.value = 0
        if len(data) == 2:
            data.append("")
        self.isState = True if "状態" in data[2] else False
        self.isPlace = True if "場所" in data[2] else False
        self.isEvent = True if "出来事" in data[2] else False
        self.isAttribute = True if "性質" in data[2] else False
        self.isAction = True if "行為" in data[2] else False
        self.isEmotion = True if "感情" in data[2] else False
        self.isSubjective = True if "主観" in data[2] else False


# list(string) -> dict
def preprocess_dict(dictionary):
    dict1 = {}
    for line in dictionary:
        info = Info1(line)
        dict1[info.word] = info
    return dict1
