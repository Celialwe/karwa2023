


class Line :
    def __init__(self, nom, ag) : 
        self.start , self.end = nom.split()
        ag.add(self.start)
        ag.add(self.end)

class AllGare:
    def __init__(self):
        self.allGare = {}
        
    def add(self, gare : str) : 
        if gare not in self.allGare:
            self.allGare[gare] = len(self.allGare)

n = int(input())

ag = AllGare()
depart = ag.add(input())
l = [Line(input(), ag) for _ in range(n)]
nbrGare = len(ag.allGare)

lines = [[0 for _ in range(nbrGare)] for _ in range(nbrGare)]
for line in l:
    startId = ag.allGare.get(line.start)
    endId = ag.allGare.get(line.end)
    lines[startId][endId] = 1
    lines[endId][startId] = 1

depId = ag.allGare.get(depart)

AllSet = {}
ok = {}
for i in range(nbrGare):
    if lines[depId][i] == 1:
        AllSet[i] = set()
        ok[i] = True

for i in range(nbrGare):
    if lines[i][j] == 1 and j not in AllSet[i]:
        AllSet[i].add(j)
