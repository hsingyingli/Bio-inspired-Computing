import argparse
from ga import *


def main(args):
    GA = Genetic_Algorithm(args)
    GA.init_popuation()
    GA.train()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--representation'    , type = str     , default = 'real_value')
    parser.add_argument('--crossover_mode'    , type = str     , default = 'whole')
    parser.add_argument('--mutation_mode'     , type = str     , default = 'random_reset')
    parser.add_argument('--popuation_size'    , type = int     , default = 100)
    parser.add_argument('--generation'        , type = int     , default = 500)
    parser.add_argument('--dim'               , type = int     , default = 10)
    parser.add_argument('--bound'             , type = int     , default = 32)
    parser.add_argument('--k'                 , type = int     , default = 2)
    parser.add_argument('--dna_size'          , type = float   , default = 10)
    parser.add_argument('--pc'                , type = float   , default = 0.9)
    
    args = parser.parse_args()
    print(args)
    print("-"*100)
    main(args)