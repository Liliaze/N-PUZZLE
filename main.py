import sys
import parser
from solver import Solver

if __name__ == "__main__":
    solver = Solver(parser.parser)
    if len(sys.argv) == 3 and sys.argv[2] == "-i":
            solver.start(True)
    else:
        solver.start(False)