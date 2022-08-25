import numpy as np

class NothingAgent:
    '''
    Does nothing
    '''

    def register_reset(*args):
        pass

    def update(*args):
        pass

    def compute_action(self, obs):
        return [[0] for x in range(len(obs))]

    def save(*args):
        pass

    def load(*args):
        pass