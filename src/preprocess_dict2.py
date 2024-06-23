class Info2TreeNode:
    def __init__(self,score:int,type:int):
        self.score = score #ポジ+1ネガ-1未確定0
        self.type = type #経験+1評価-1未確定0
        self.dict: dict[str:Info2TreeNode] = {}
    def add(self,str:str,score:int,type:int):
        if (str in self.dict) and score != 0 and type != 0 and self.dict[str].score == 0 and self.dict[str].type == 0:
            self.dict[str].score = score
            self.dict[str].type = type
        if str not in self.dict:
            self.dict[str]=Info2TreeNode(score,type)  
        return self.dict[str]

class Info2:
    def __init__(self,dictionary):
        self.first = Info2TreeNode(0,0)
        self.current:Info2TreeNode = self.first
        for line in dictionary:
            current = self.first
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
            for i, word in enumerate(data2):
                self.current = self.current.add(word,score if i == len(data2)-1 else 0,type if i == len(data2)-1 else 0)
        self.current = self.first
    def search(self,word):
        if word in self.current.dict:
            self.current = self.current.dict[word]
            return (True,self.current.score,self.current.type)
        else:
            return (False,0,0)
            
    def reset(self,):
        self.current = self.first
        



