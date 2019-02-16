"""
The team.py file is where you should write all your code!

Write the __init__ and the step functions. Further explanations
about these functions are detailed in the wiki.

List your Andrew ID's up here!
mscharag
lssong
npipiton
"""
from awap2019 import Tile, Direction, State

class Team(object):
    def __init__(self, initial_board, team_size, company_info):
        """
        The initializer is for you to precompute anything from the
        initial board and the company information! Feel free to create any
        new instance variables to help you out.

        Specific information about initial_board and company_info are
        on the wiki. team_size, although passed to you as a parameter, will
        always be 4.
        """
        self.board = initial_board
        self.team_size = team_size
        self.company_info = company_info
        self.memo = {}
        self.team_name = "The Axioms"
        self.goals = []
        for _ in range(team_size):
            self.goals.append(set())

        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if not self.board[i][j].get_booth()==None:
                    if i>len(self.board)/2:
                        if j>len(self.board[0])/2:
                            self.goals[0].add(self.board[i][j].get_booth())
                        else:
                            self.goals[1].add(self.board[i][j].get_booth())
                    else:
                        if j>len(self.board[0])/2:
                            self.goals[2].add(self.board[i][j].get_booth())
                        else:
                            self.goals[3].add(self.board[i][j].get_booth())
        print(self.goals)


    def getLines(self):
        lines = dict()
        for x in range(len(self.board)):
            for y in range(len(self.board[0])):
                tile = self.board[x][y]
                if tile.get_line() in lines:
                    if tile.is_end_of_line():
                        lines[tile.get_line()] = tile
                lines[tile.get_line()] = tile
        lines.pop(None)
        return lines

    def updateBoard(self,visible_board):
        for tiles in visible_board:
            for t in tiles:
                x,y = t.get_loc()
                self.board[x][y] = t

    def shortestPath(self, fromx, fromy, tox, toy):
        def notWall(d):
            x,y=d.get_loc((fromx,fromy))
            return self.board[x][y].get_booth()==None
        if tox<fromx:
            if notWall(Direction.UP):
                return Direction.UP
        if tox>fromx:
            if notWall(Direction.DOWN):
                return Direction.DOWN
        if toy>fromy:
            return Direction.RIGHT
        if toy<fromy:
            return Direction.LEFT
        return None

    def threshold(self, tile):
        x = tile.get_threshold()
        if x==None:
            return 0
        return x
    
    def shortest_path(self, x, y, a, b):
        if x < 0 or x > len(self.board) or y < 0 or y > len(self.board[0]) or self.board[x][y].get_booth():
            return (float('inf'),Direction.ENTER)
 
        if (x,y) in self.memo:
            return self.memo[(x,y)]
        
        if x==a and y==b:
            return (0,Direction.ENTER)
 
        best = None
        val = float('inf')
        
        for d in [Direction.UP,Direction.DOWN,Direction.LEFT,Direction.RIGHT]:
            newX,newY = d.get_loc((x,y))
            newVal, _ = self.shortest_path(newX,newY,a,b)
            if newVal<val:
                val=newVal
                best=d

        val+=self.threshold(self.board[x][y])
        self.memo[(x,y)] = (val,best)
        return (val,best)

    def moveTowardsLine(self, person):
        lines = self.getLines()
        
        #lines = sorted(lines.values(),key=lambda x: x.get_line())
        #lines = lines[person.id*(len(lines)//4):(person.id+1)*(len(lines)//4)]
        lines = [line for line in lines.values() if line.get_line() in self.goals[person.id]]


        best = None
        points = float('-inf')
            #lowestDist = float('inf')
        for line in lines:
            if points<self.company_info[line.get_line()]:
                best = line
                points = self.company_info[line.get_line()]
#lx,ly = line.get_loc()
#dist = abs(person.y-lx)+abs(person.x-ly)
#if dist<lowestDist:
#    best=line
#    lowestDist=dist

        if best==None:
            return Direction.UP
        
        
        x,y = best.get_loc()
        self.memo = {}
        direction = self.shortest_path(person.x,person.y,x,y)
        if direction[1] == Direction.ENTER:
            self.company_info[best.get_line()]/=2
            return Direction.ENTER
        return direction[1]

    def step(self, visible_board, states, score):
        """
        The step function should return a list of four Directions.

        For more information on what visible_board, states, and score
        are, please look on the wiki.
        """

        self.updateBoard(visible_board)
        
        directions = []
        for bot in states:
            if bot.line_pos==-1:
                directions.append(self.moveTowardsLine(bot))
            else:
                directions.append(Direction.NONE)
        print(directions)
        return directions