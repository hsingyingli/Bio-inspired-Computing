import argparse
from Framework import *


def main(args):
    env = Ackley(dim = args.dim)
    ga  = GA(args)
    ga.evolve()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--mutate_rate'    , type = float   , default = None)
    parser.add_argument('--mutate_mode'    , type = str     , default = 'bit_flip')
    parser.add_argument('--cross_mode'     , type = str     , default = 'two_point')
    parser.add_argument('--population'     , type = int     , default = 100)
    parser.add_argument('--generation'     , type = int     , default = 500)
    parser.add_argument('--dim'            , type = int     , default = 32)
    
    args = parser.parse_args()
    print(args)
    print("-"*100)
    main(args)