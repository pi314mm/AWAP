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
        
        self.team_name = "The Axioms"

        self.stepcounter = 0


    def getLines(self):
        lines = dict()
        for tiles in self.board:
            for tile in tiles:
                if tile.is_end_of_line():
                    lines[tile.get_line()] = tile
        return lines

    def updateBoard(self,visible_board):
        for tiles in visible_board:
            for t in tiles:
                x,y = t.loc
                self.board[x][y] = t

    def shortestPath(self, fromx, fromy, tox, toy):
        if tox>fromx:
            return Direction.LEFT
        if tox<fromx:
            return Direction.RIGHT
        if toy>fromy:
            return Direction.UP
        if toy<fromy:
            return Direction.DOWN
        return Direction.ENTER

    def moveTowardsLine(self, person):
        lines = self.getLines()
        closest = None
        lowestDist = float('inf')
        for line in lines.values():
            lx,ly = line.loc
            dist = abs(person.x-lx)+abs(person.y-ly)
            if dist<lowestDist:
                closest=line
                lowestDist=dist
        if closest==None:
            return Direction.UP
        return self.shortestPath(person.x,person.y,closest.loc[0],closest.loc[1])

    def step(self, visible_board, states, score):
        """
        The step function should return a list of four Directions.

        For more information on what visible_board, states, and score
        are, please look on the wiki.
        """
        #print([[t.get_booth() for t in tiles] for tiles in visible_board])
        #print([[t.get_line() for t in tiles] for tiles in visible_board])
        #print([[t.is_end_of_line() for t in tiles] for tiles in visible_board])
        #print([[t.get_num_bots() for t in tiles] for tiles in visible_board])

        self.updateBoard(visible_board)
        print(self.getLines())



        directions = []
        for bot in states:
            if bot.line_pos==-1:
                directions.append(self.moveTowardsLine(bot))
            else:
                directions.append(Direction.NONE)
        return directions