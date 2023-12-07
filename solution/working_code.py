source = 'Castle Black'
destination =  'Kings Landing'
indeces = ['Castle Black', 'Winterfell', 'Riverrun', 'Kings Landing']
priceMatrix = [[0,15,80,90],[0,0,40,50],[0,0,0,70],[0,0,0,0]]
def flightPath(priceMatrix,source, destination):
    finalPath = []
    # cache = {}
    def dfs(current, totalPrice, path=[]):
        path.append(current)
        if current == destination:
            finalPath.append((path.copy(),totalPrice))
            return
    
        for j in range(current+1, len(priceMatrix[current])):
            totalPrice += priceMatrix[current][j]
            dfs(j, totalPrice, path)
            lastNode = path.pop()
            totalPrice -= priceMatrix[current][lastNode]
        print(path, totalPrice)
    dfs(source, 0, path=[])
    print(finalPath,"==")

flightPath(priceMatrix,0,3)