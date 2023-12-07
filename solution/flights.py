
source = 'Castle Black'
destination =  'Kings Landing'
indeces = ['Castle Black', 'Winterfell', 'Riverrun', 'Kings Landing']
priceMatrix = [[0,15,80,90],[0,0,40,50],[0,0,0,70],[0,0,0,0]]
# def flightPath(priceMatrix,source, destination):
    # finalPath = []
    # cache = {}
    # def dfs(current, totalPrice, path=[]):
    #     path.append(current)
    #     if current == destination:
    #         finalPath.append((path.copy(),totalPrice))
    #         return
    
    #     for j in range(current+1, len(priceMatrix[current])):
    #         totalPrice += priceMatrix[current][j]
    #         dfs(j, totalPrice, path)
    #         lastNode = path.pop()
    #         totalPrice -= priceMatrix[current][lastNode]
    #     print(path, totalPrice)
    # dfs(source, 0, path=[])
    # print(finalPath,"==")


    # def bfs(current, totalPrice, path=[]):
    #     for j in range(len(priceMatrix[current]), current+1, -1):
    #         totalPrice += priceMatrix[current][j]
    #         bfs(j, totalPrice, path)
     
    #     if current == destination:
    #         finalPath.append((path.copy(),totalPrice))
    #         lastNode = path.pop()
    #         totalPrice -= priceMatrix[current][lastNode]
    #         return
    # bfs(source, 0, path=[])
    # print(finalPath,"===")

from collections import deque
def flightPath(priceMatrix, source,  destination):
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
    return finalPath





    
# x=flightPath(priceMatrix,0,  2)
# print(x)