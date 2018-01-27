def answer(maze):
    h = len(maze)
    w = len(maze[0])
    
    pathLength = GetPathLength(maze,h,w)
    for i in range(0,h):
        for j in range(0,w):
            if maze[i][j] == 1:
                maze[i][j] = 0
                pathTemp = GetPathLength(maze,h,w)
                maze[i][j] = 1
                if pathTemp < pathLength:
                    pathLength = pathTemp
    
    return pathLength
    
    
def GetPathLength(maze,h,w):
    emitters = set()
    colored = set()
    emitters.add("0,0")
    colored.add("0,0")
    pathLength = 1
    
    s = str(h-1)+","+str(w-1)
    while (s not in emitters) & (len(emitters) > 0):
        pathLength += 1
        newEmitters = set()
        for el in emitters:
            colored,newE = Emit(el,maze,emitters,colored,h,w)
            newEmitters = newEmitters|newE
        emitters = newEmitters
    
    if len(emitters) == 0:
        pathLength = float("inf")
    
    return pathLength
    

def GetXY(el):
    for i in range(0,len(el)):
        if el[i] == ",":
            comma = i
    x = int(el[0:comma])
    y = int(el[comma+1:len(el)+1])
    
    return x,y


def Add(x,y,maze,newEmitters,emitters,colored):
    s = str(x)+","+str(y)
    if ((maze[x][y] == 0) & (s not in colored)):
        colored.add(s)
        if s not in emitters:
            newEmitters.add(s)
            
    return colored, newEmitters
        


def Emit(el,maze,emitters,colored,h,w):
    x,y = GetXY(el)
    newEmitters = set()
    
    if x == 0:
        if y == 0:
            colored,newEmitters = Add(x+1,y,maze,newEmitters,emitters,colored)
            colored,newEmitters = Add(x,y+1,maze,newEmitters,emitters,colored)
        elif y == w-1:
            colored,newEmitters = Add(x+1,y,maze,newEmitters,emitters,colored)
            colored,newEmitters = Add(x,y-1,maze,newEmitters,emitters,colored)
        else:
            colored,newEmitters = Add(x+1,y,maze,newEmitters,emitters,colored)
            colored,newEmitters = Add(x,y-1,maze,newEmitters,emitters,colored)
            colored,newEmitters = Add(x,y+1,maze,newEmitters,emitters,colored)
    elif x == h-1:
        if y == 0:
            colored,newEmitters = Add(x-1,y,maze,newEmitters,emitters,colored)
            colored,newEmitters = Add(x,y+1,maze,newEmitters,emitters,colored)
        elif y == w-1:
            colored,newEmitters = Add(x-1,y,maze,newEmitters,emitters,colored)
            colored,newEmitters = Add(x,y-1,maze,newEmitters,emitters,colored)
        else:
            colored,newEmitters = Add(x-1,y,maze,newEmitters,emitters,colored)
            colored,newEmitters = Add(x,y-1,maze,newEmitters,emitters,colored)
            colored,newEmitters = Add(x,y+1,maze,newEmitters,emitters,colored)
    else:
        if y == 0:
            colored,newEmitters = Add(x+1,y,maze,newEmitters,emitters,colored)
            colored,newEmitters = Add(x-1,y,maze,newEmitters,emitters,colored)
            colored,newEmitters = Add(x,y+1,maze,newEmitters,emitters,colored)
        elif y == w-1:
            colored,newEmitters = Add(x+1,y,maze,newEmitters,emitters,colored)
            colored,newEmitters = Add(x-1,y,maze,newEmitters,emitters,colored)
            colored,newEmitters = Add(x,y-1,maze,newEmitters,emitters,colored)
        else:
            colored,newEmitters = Add(x+1,y,maze,newEmitters,emitters,colored)
            colored,newEmitters = Add(x-1,y,maze,newEmitters,emitters,colored)
            colored,newEmitters = Add(x,y-1,maze,newEmitters,emitters,colored)
            colored,newEmitters = Add(x,y+1,maze,newEmitters,emitters,colored)
            
                
    return colored, newEmitters
