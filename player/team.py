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
import random

class Team(object):
    def threshold(self, x):
        if x < 10:
            return x / 3
        else:
            return 5

    def shortest_path(self, x, y):
        if x < 0 or x >= len(self.boardInfo[0]) or y < 0 or y >= len(self.boardInfo):
            return {"pts": 0, "dist": 1000000000000, "dir": "test"}

        if (x*10000+y) in self.memo:
            return self.memo[x*10000+y]

        if self.boardInfo[y][x]["tile"].get_booth():
            return {"pts": 0, "dist": 1000000000000}

        if self.boardInfo[y][x]["tile"].get_line():
            compName = self.boardInfo[y][x]["tile"].get_line()
            compInfo = self.companyInfo[compName]
            ret = {"pts": compInfo["score"], "dist": compInfo["avgLineLen"] + 2, "company": compName}
            if not self.board[y][x].is_end_of_line():
                ret["dist"] += 3
                ret["dir"] = random.choice([Direction.UP, Direction.LEFT, Direction.RIGHT, Direction.DOWN])
            else:
                ret["dir"] = Direction.ENTER
            return ret

        self.memo[x*10000 + y] = {"pts": 0, "dist": 1000000000000}

        up = {**self.shortest_path(x, y-1), "dir": Direction.UP}
        if up["dist"] < 1000000000000:
            up["dist"] = up["dist"] + self.threshold(self.boardInfo[y-1][x]["avgPopulation"])
        right = {**self.shortest_path(x+1, y), "dir": Direction.RIGHT}
        if right["dist"] < 1000000000000:
            right["dist"] = right["dist"] + self.threshold(self.boardInfo[y][x+1]["avgPopulation"])
        left = {**self.shortest_path(x-1, y), "dir": Direction.LEFT}
        if left["dist"] < 1000000000000:
            left["dist"] = left["dist"] + self.threshold(self.boardInfo[y][x-1]["avgPopulation"])
        down = {**self.shortest_path(x, y+1), "dir": Direction.DOWN}
        if down["dist"] < 1000000000000:
            down["dist"] = down["dist"] + self.threshold(self.boardInfo[y+1][x]["avgPopulation"])

        best = None
        for dir in [up, right, left, down]:
            score = dir["pts"] / (dir["dist"] ** 1.1)
            if not best or best["score"] < score:
                best = {**dir, "score": score}

        self.memo[x*10000 + y] = best
        return best

    def save_info(self):
        found = {}
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j].get_num_bots() != None:
                    self.boardInfo[i][j]["avgPopulation"] = self.board[i][j].get_num_bots()
                if self.board[i][j].get_num_bots() and self.board[i][j].get_line():
                    comp = self.board[i][j].get_line()
                    if not comp in found:
                        found[comp] = 0
                    found[comp] += self.board[i][j].get_num_bots()
        for comp in found:
            if self.companyInfo[comp]["avgLineLen"] == 0:
                self.companyInfo[comp]["avgLineLen"] = found[comp]
            else:
                self.companyInfo[comp]["avgLineLen"] = self.companyInfo[comp]["avgLineLen"] * 0.9 + found[comp] * 0.1

    def __init__(self, initial_board, team_size, company_info):
        """
        The initializer is for you to precompute anything from the
        initial board and the company information! Feel free to create any
        new instance variables to help you out.

        Specific information about initial_board and company_info are
        on the wiki. team_size, although passed to you as a parameter, will
        always be 4.
        """
        self.boardInfo = [] # 2D array of {"tile": tile, "avgPopulation": float}
        self.companyInfo = {} # Map from company to {"score": int, "avgLineLen": float, "endLine": float}
        self.memo = {}

        self.board = initial_board
        self.team_size = team_size
        self.company_info = company_info
        #print("init: ", initial_board, team_size, company_info)

        self.rows = len(self.board)
        self.cols = len(self.board[0])

        for company in self.company_info:
            self.companyInfo[company] = {}
            self.companyInfo[company]["score"] = self.company_info[company]
            self.companyInfo[company]["avgLineLen"] = 0

        for row in self.board:
            myRow = []
            for col in row:
                myRow.append({"tile": col, "avgPopulation": 0})
            self.boardInfo.append(myRow)

        self.team_name = "The Axioms"

    def mapdirs(self, dir):
        return {
            "up": Direction.UP,
            "down": Direciton.DOWN,
            "left": Direction.LEFT,
            "right": Direciton.RIGHT
        }[dir]

    def get_decision(self, state):
        paths = [self.shortest_path(state.y, state.x),
            self.shortest_path(state.y - 1, state.x),
            self.shortest_path(state.y, state.x + 1),
            self.shortest_path(state.y, state.x - 1),
            self.shortest_path(state.y + 1, state.x)
        ]

        best = 0
        for i in range(1, 5):
            path = paths[i]
            if path["score"] > paths[best]["score"]:
                best = i

        return paths[best]["dir"]

    def step(self, visible_board, states, score):
        """
        The step function should return a list of four Directions.

        For more information on what visible_board, states, and score
        are, please look on the wiki.
        """
        self.memo = {}

        self.board = visible_board
        self.save_info()
        paths = []
        for state in states:
            if state.line_pos != -1:
                paths.append({"dir": Direction.NONE, "company": self.board[state.x][state.y]})
                print(state.line_pos)
            else:
                path = self.shortest_path(state.y, state.x)
                paths.append(path)
                if path["dir"] == Direction.ENTER:
                    self.companyInfo[path["company"]]["score"] /= 2
        print("START")
        print(paths)
        return [path["dir"] for path in paths]
