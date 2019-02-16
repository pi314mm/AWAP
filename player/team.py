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
    self.companyInfo = {} # 2D array of {"score": int, "avgLineLen": float}

    self.memo = {}
    def shortest_path(self, x, y):
        if self.memo[x*10000+y]:
            return self.memo[x*10000+y]

    def save_info(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if ( self.board[i][j] != NONE)
                    boardInfo[i][j].avgPopulation = self.board[i][j]

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

        self.rows = len(self.board)
        self.cols = len(self.board[0])

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
