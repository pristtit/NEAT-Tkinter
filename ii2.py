from __future__ import print_function
import os
import neat
import visualize
from time import sleep as s
import numpy as np


a = 1
def var(x):
    global a
    a = x

def vvod():
    global xor_inputs, xor_outputs, data
    xor_inputs = np.loadtxt('data.txt', usecols=(0,1,2))
    data = np.loadtxt('data.txt', unpack=True, usecols=3)
    xor_outputs = [[i[1]] for i in enumerate(data)]

def eval_genomes(genomes, config):
    for genome_id, genome in genomes:
        genome.fitness = 1.0
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        for xi, xo in zip(xor_inputs, xor_outputs):
            output = net.activate(xi)
            if a:
                genome.fitness -= ((output[0])/(xo[0])- 1)**2
            else:
                genome.fitness -= (output[0]-xo[0])**2

def run(config_file):
    # Load configuration.
    global config, p, stats
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

def telo(x, cheh):
    if x=='':
        x=1
    winner=p.run(eval_genomes, int(x))
    s ='Fitness = '+ str(winner.fitness)+'\n'
    print('\nBest genome:\n{!s}'.format(winner))
    print('\nOutput:')
    winner_net = neat.nn.FeedForwardNetwork.create(winner, config)
    for xi, xo in zip(xor_inputs, xor_outputs):
        output = winner_net.activate(xi)
        print("input {!r}, expected output {!r}, got {!r}".format(xi, xo, output))
        s +="input {!r}, expected output {!r}, got {!r}\n".format(xi, xo, output)

    node_names = {-1:'A', -2: 'B', 0:'A XOR B'}
    if cheh:
        visualize.draw_net(config, winner, True, node_names=node_names)
    print(cheh)
    return s


run('configinternet.ini')
p = neat.Population(config)
p.add_reporter(neat.StdOutReporter(True))
stats = neat.StatisticsReporter()
p.add_reporter(stats)
vvod()