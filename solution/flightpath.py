from collections import deque
class FlightPlath(object):

    def __init__(self,priceMatrix, indeces) -> None:
        self.rows, self.cols = len(priceMatrix), len(priceMatrix[0])
        if self.rows > 0 and self.cols > 0 and self.rows != self.cols or len(indeces) != self.rows or len(indeces) != self.cols:
            raise Exception('Bad matrix')
        
        self.graph =  self.graph = {i: [(j, priceMatrix[i][j]) for j in range(self.cols) if priceMatrix[i][j] != 0] for i in range(self.rows)}
        self.indeces = indeces
    def validate(self,  source, destination):
        if  source >= destination:
            raise Exception('Bad direction')
    
    def printPath(self, pathData):
        for result in pathData:
            toatalPrice = 0
            p = []
            for path in result:
                node, price = path
                toatalPrice += price
                p.append(f'{self.indeces[node]}')
            print(f"{'->'.join(p)}: {toatalPrice}")
        return
    
    def findPathAndPrice(self, source, destination):
        self.validate(source, destination)
        allPaths = []

        def dfs(node, temp=[]):
            n = node[0]
            temp.append(node)
            for nextNode in self.graph[n]:
                dfs(nextNode, temp)
                temp.pop()
            if n == destination:
                allPaths.append(temp.copy())
                return
        dfs((source,0))
        self.printPath(allPaths)
        return allPaths
    
    def findPrice(self, source, destination):
        self.validate(source, destination)
        allPaths = []

        def dfs(node, price):
            n,p = node # node: [node, price]
            price +=p
            for node in self.graph[n]:
                dfs(node, p)
            if n == destination:
                allPaths.append(price)
                return
        dfs((source,0),0)
        return allPaths
     







    


print(__name__,"===")
if __name__ == '__main__':
    source = 'Castle Black'
    destination =  'Kings Landing'
    indeces = ['Castle Black', 'Winterfell', 'Riverrun', 'Kings Landing']
    priceMatrix = [[0,15,80,90],[0,0,40,50],[0,0,0,70],[0,0,0,0]]


    indecesMap = {val:index for index, val in enumerate(indeces)}
    sourceIndex , destinationIndex = indecesMap[source], indecesMap[destination]


    fp = FlightPlath(priceMatrix, indeces)
    fp.findPathAndPrice(sourceIndex, destinationIndex)
    fp.findPrice(sourceIndex, destinationIndex)


'''
./bin/list-flight-paths "Castle Black" "Winterfell"
Castle Black -> Winterfell: 15

./bin/list-flight-paths "Castle Black" "Riverrun"
Castle Black -> Winterfell -> Riverrun: 55
Castle Black -> Riverrun: 80
'''