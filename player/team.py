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
    self.boardInfo = [] # 2D array of {"tile": tile, "avgPopulation": float}
    self.companyInfo = {} # Map from company to {"score": int, "avgLineLen": float}
    self.avgDensity = 0

    def threshold(x):
        if x == -1:
            return avgDensity
        if x < 10:
            return x / 3
        else:
            return 5

    self.memo = {}
    def shortest_path(self, x, y):
        if x < 0 or x > len(boardInfo[0]) or y < 0 or y > len(boardInfo):
            return {"pts", 0, "dist", 1000000000000}

        if self.memo[x*10000+y]:
            return self.memo[x*10000+y]

        if self.boardInfo[x][y].get_booth():
            return {"pts", self.boardInfo[x][y].get_booth()

        up = {**shortest_path(self, x, y-1), "dir": "up"}
        if up.dist < 1000000000000:
            up.dist = up.dist + threshold(self.boardInfo[x][y-1].avgPopulation)
        right = {**shortest_path(self, x+1, y), "dir": "right"}
        if right.dist < 1000000000000:
            right.dist = right.dist + threshold(self.boardInfo[x+1][y].avgPopulation)
        left = {**shortest_path(self, x-1, y), "dir": "left"}
        if left.dist < 1000000000000:
            left.dist = left.dist + threshold(self.boardInfo[x-1][y].avgPopulation)
        down = {**shortest_path(self, x, y+1), "dir": "down"}
        if down.dist < 1000000000000:
            down.dist = down.dist + threshold(self.boardInfo[x][y+1].avgPopulation)

        best = None
        for dir in [up, right, left, down]:
            score = dir.pts / (dir.dist ** 1.1)
            if !best or best.score < score:
                best = {dir, "score": score}

        self.memo[x*10000 + y] = best
        return best

    def save_info(self, state):


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
        print("init: ", initial_board, team_size, company_info)

        for company in self.company_info:
            self.companyInfo[company] = {}
            self.companyInfo[company].score = self.company_info[company]
            self.companyInfo[company].avgLineLen = None

        self.boardInfo = []
        for row in self.board:
            myRow = []
            for col in row:
                myRow.append({"tile": col, "avgPopulation": None})
            self.boardInfo.append(myRow)

        self.team_name = "The Axioms"

    def step(self, visible_board, states, score):
        """
        The step function should return a list of four Directions.

        For more information on what visible_board, states, and score
        are, please look on the wiki.
        """
        for state in states`:
            print(state)
        return [Direction.UP,Direction.UP,Direction.UP,Direction.UP]
