class Info2TreeNode:
    def __init__(self,score:int,type:int):
        self.score = score #ポジ+1ネガ-1未確定0
        self.type = type #経験+1評価-1未確定0
        self.dict: dict[str:Info2TreeNode] = {}
    def add(self,str:str,score:int,type:int):
        if str not in self.dict:
            self.dict[str]=Info2TreeNode(score,type)  
        return self.dict[str]

class Info2:
    def __init__(self,dictionary):
        self.dict: dict[str:Info2TreeNode] ={}
        for line in dictionary:
            data = line.split('\t')
            eval = data[0]
            score = 0
            type = 0
            if "ポジ" in eval:
                score = 1
            if "ネガ" in eval:
                score = -1
            if "経験" in eval:
                type = 1
            if "評価" in eval:
                type = -1
            data2 = data[1].split()
            next_node = None
            for i, word in enumerate(data2):
                if i == 0:
                    if word not in self.dict:
                        self.dict[word] = Info2TreeNode(score if i == len(data2)-1 else 0, type if i == len(data2)-1 else 0)
                    next_node = self.dict[word]
                else:
                    next_node = next_node.add(word, score if i == len(data2)-1 else 0, type if i == len(data2)-1 else 0)
        



