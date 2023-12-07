import sys
from collections import deque

class FlightPlath(object):

    def __init__(self,priceMatrix, indeces) -> None:
        self.rows, self.cols = len(priceMatrix), len(priceMatrix[0])
        if self.rows > 0 and self.cols > 0 and self.rows != self.cols or len(indeces) != self.rows or len(indeces) != self.cols:
            raise Exception('Bad matrix')
        self.priceMatrix = priceMatrix
        self.indeces = indeces
    def validate(self,  source, destination):
        if  source >= destination:
            raise Exception('Bad direction')
    
    def printPath(self, pathData):
        for result in pathData:
            path, price = result
            path = map(lambda x: self.indeces[x], path)
            print(f"{'->'.join(path)}: {price}")
    
    def flightPath(self, source,  destination):
        self.validate(source,destination)
        priceMatrix = self.priceMatrix
        stack = deque([(source, 0,[source])])
        finalPath = []
        while stack:
            source, totalPrice, path = stack.pop()
    
            if source==destination:
                finalPath.append((path, totalPrice))
            connectedDestinations =  priceMatrix[source]
    
            for index in range(source+1, len(connectedDestinations)):
                price = connectedDestinations[index]
                stack.append((index, totalPrice+price, path+[(index)]))
        self.printPath(finalPath)
        return finalPath

if __name__ == '__main__':
    
    arguments = sys.argv[1:]
    print('arguments=>', arguments)
    source = arguments[0] if arguments[0] else 'Castle Black'
    destination =  arguments[1] if arguments[1] else 'Riverrun'

    indeces = ['Castle Black', 'Winterfell', 'Riverrun', 'Kings Landing']
    priceMatrix = [[0,15,80,90],[0,0,40,50],[0,0,0,70],[0,0,0,0]]

    indecesMap = {val:index for index, val in enumerate(indeces)}
    sourceIndex , destinationIndex = indecesMap[source], indecesMap[destination]

    fp = FlightPlath(priceMatrix, indeces)
    allPaths= fp.flightPath(sourceIndex, destinationIndex)
    # print(allPaths)
   
