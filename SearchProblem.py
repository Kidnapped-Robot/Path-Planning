
class SearchProblem:
    """
    A search problem associated with finding the optimal path that leads to the goal.
    A search state in this problem is a tuple (x, y) where
    the coordinates specify the position on the grid.
    """
    def __init__(self, startingGameState, goal, obstacles, mapdim, costFn = lambda x: 1):

        self.start = startingGameState
        self.obstacles = obstacles
        self.goal = goal
        self.costFn = costFn
        self.mapdim = mapdim
        self.walls = []
        
        x, y = -1, -1
        x_inc = 1
        y_inc = 0
        x_dec = 0
        y_dec = 0
        self.walls.append((x, y))
        
        for i in range((self.mapdim + 1)**2):
            
            if(x_inc):
                x += 1
                self.walls.append((x, y))
                
                if(x == self.mapdim ):
                    x_inc = 0
                    y_inc = 1
                    
            if(y_inc):
                y += 1
                self.walls.append((x, y))
                
                if(y == self.mapdim):
                    y_inc = 0
                    x_dec = 1
                    
            if(x_dec):
                x -= 1
                self.walls.append((x, y))
                
                if(x == -1):
                    x_dec = 0
                    y_dec = 1
                    
            if(y_dec):
                y -= 1
                self.walls.append((x, y))
                
                if(y == 0):
                    y_dec = 0
                
    def getStartState(self):

        return self.start

    def isGoalState(self, state):

        return (state == self.goal)
    
    def directionToVector(self, action):
        
        return{
                "North": (0, 1),
                "South": (0, -1),
                "East" : (1, 0),
                "West" : (-1, 0),
                "NorthEast": (1, 1),
                "NorthWest": (-1, 1),
                "SouthEast": (1, -1),
                "SouthWest": (-1, -1)}.get(action, (0, 0))

    def getSuccessors(self, state):

        "Returns successor states, the actions they require, and a cost of 1."
        
        successors = []
        x, y = state
          
        for action in ["South", "North", "East", "West", "SouthEast", "SouthWest", "NorthEast", "NorthWest"]:
          
            dx, dy = self.directionToVector(action)
            nextx, nexty = int(x + dx), int(y + dy)
            nextstate = (nextx, nexty)
            
            if( nextstate not in self.obstacles and nextstate not in self.walls):
                cost = self.costFn(nextstate)
                successors.append((nextstate, action, cost))
                
                
        return successors