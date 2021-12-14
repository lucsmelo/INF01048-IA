# analysis.py
# -----------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


######################
# ANALYSIS QUESTIONS #
######################

# Set the given parameters to obtain the specified policies through
# value iteration.

def question2():
    answerDiscount = 0.9
    answerNoise = 0.0
    return answerDiscount, answerNoise

def question3a():
    # Close exit, risk the cliff
    answerDiscount = 0.9
    answerNoise = 0.2
    answerLivingReward = -2.5  # MAN, this place is disgusting let's get the heck out of here ASAP I dont care about cliffs just wanna get out
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3b():
    # Close exit, avoiding the cliff
    answerDiscount = 0.3  # Make future less desirable so agent chooses closest exit
    answerNoise = 0.2  # Make it possible for the agent to fall on the cliff so it will avoid this area
    answerLivingReward = -1.0  # Make staying on the grid not all that tasty
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3c():
    # Distant exit, risk the cliff
    answerDiscount = 0.9
    answerNoise = 0.0  # Make it IMpossible for the agent to fall on the cliff
    answerLivingReward = 0.0
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3d():
    # Distant exit, avoid the cliff
    answerDiscount = 0.9
    answerNoise = 0.2  # Make it possible for the agent to fall on the cliff
    answerLivingReward = 0.0
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3e():
    # Avoid both exits and the cliff
    answerDiscount = 0.9
    answerNoise = 0.0
    answerLivingReward = 10.0  # Make those damn cells so tasty the agent never wants to leave
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question6():
    answerEpsilon = None
    answerLearningRate = None
    return 'NOT POSSIBLE'
    # If not possible, return 'NOT POSSIBLE'

if __name__ == '__main__':
    print('Answers to analysis questions:')
    import analysis
    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        print('  Question %s:\t%s' % (q, str(response)))
