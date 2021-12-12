# multiAgents.py
# --------------
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


from pacman import GameState
from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

import math

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and child states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed child
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        
        
        
        
    
        # Useful information you can extract from a GameState (pacman.py)
        childGameState = currentGameState.getPacmanNextState(action)
        newPos = childGameState.getPacmanPosition()
        newFood = childGameState.getFood()
        newGhostStates = childGameState.getGhostStates()
        # newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        
        #if action is stop or the new state(new state is newPos) is hear one ghost(from table newGhostStates)
        for Ghost in newGhostStates:
            if Ghost.getPosition() == newPos:
                return -math.inf
        
        if action == Directions.STOP:
            return -math.inf
        
        #now all it's ok from ghost and action != STOP
        #now will return th min distance from one food and new pos(but the min is the best)
        foodList = newFood.asList()
        mindistance = math.inf
        
        for food in foodList:
            distance = util.manhattanDistance(food, newPos)
            if distance <  mindistance:
                mindistance = distance
        
        return childGameState.getScore() + (1.0/mindistance)

def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.getNextState(agentIndex, action):
        Returns the child game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"
        # gamestate = (gameState.getPacmanState()).getPosition()
        agent_index = 0
        depth = 0
        price = self.MinimaxDecision(gameState, depth, agent_index)

        return price
        
        util.raiseNotDefined()
        
    
    def Min_Value( self, gamestate, depth, agent_index):

        min = math.inf
        actions = gamestate.getLegalActions(agent_index)        

        for a in actions:
            
            #if action is wall
            if a == Directions.STOP:
                continue
            
            #next state continue the game
            state_next = gamestate.getNextState( agent_index, a)
            price = self.MinimaxDecision( state_next, depth, agent_index+1)
            if price < min:
                min = price
        
        return min
    
    
        
    def Max_Value( self, gamestate, depth,agent_index):
    
        max = -math.inf
        max_action = None

        actions = gamestate.getLegalActions(agent_index)        
        for a in actions:
            
            #if action is wall
            if a == Directions.STOP:
                continue
            
            #next state continue the game
            state_next = gamestate.getNextState( agent_index, a)
            
            price = self.MinimaxDecision(state_next,depth, agent_index+1)
            if price > max:
                max = price
                max_action = a
                
        #if depth is zero return the max_action       
        if depth == 0:
            return max_action

        return max
    
    
    def MinimaxDecision(self,gamestate,depth, agent_index):


        max_action = None
        max = -math.inf

        #if agent_index is the max agent
        if agent_index == gamestate.getNumAgents():
            agent_index = 0
            depth = depth + 1
            
        if depth == self.depth:
            return self.evaluationFunction( gamestate)
            
        if gamestate.isWin() or gamestate.isLose():
            return self.evaluationFunction(gamestate)        

        if agent_index == self.index:
            return self.Max_Value( gamestate, depth,agent_index)
        else:
            return self.Min_Value( gamestate, depth,agent_index)
            
class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        
        
        agent_index = 0
        depth = 0
        a = -math.inf
        b = math.inf
        action = self.A_B_SEARCH(gameState, a, b, depth, agent_index)
        return action
                
    
    def Min_Value( self, gamestate, a, b, depth, agent_index):

        min = math.inf

        price = math.inf
        actions = gamestate.getLegalActions(agent_index)        
        
        
        for ac in actions:
            
            #if action is wall
            if ac == Directions.STOP:
                continue
            
            #next state continue the game
            state_next = gamestate.getNextState( agent_index, ac)
                
            u = self.A_B_SEARCH( state_next, a, b, depth, agent_index+1)
        
            if u < price:
                price = u
            
            if price < a:
                return price
            
            if price < b:
                b = price
                    
        return price
    
    
        
    def Max_Value( self, gamestate, a, b, depth,agent_index):
    
        price = -math.inf
        price_action = None

        actions = gamestate.getLegalActions(agent_index)   
             
        for ac in actions:
            
            #if action is wall
            if ac == Directions.STOP:
                continue
            
            #next state continue the game
                       
            state_next = gamestate.getNextState( agent_index, ac)
            
            u = self.A_B_SEARCH( state_next, a, b, depth, agent_index +1)

            if u > price:
                price = u
                price_action = ac
            
        
            if price > b:
                return price
            
            if price > a:
                a = price
                
        if depth == 0:
            return price_action 

        return price
    
    
    
    def A_B_SEARCH(self,gamestate, a, b, depth, agent_index):

        #if agent_index is the max agent
        if agent_index == gamestate.getNumAgents():
            agent_index = 0
            depth = depth + 1
        
    
        if depth == self.depth:
            return self.evaluationFunction( gamestate)
            
        if gamestate.isWin() or gamestate.isLose():
            return self.evaluationFunction(gamestate)        

        
        if agent_index == self.index:
            return self.Max_Value( gamestate,  a, b, depth, agent_index)
        else:
            return self.Min_Value( gamestate,  a, b, depth, agent_index)

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"

        agent_index = 0
        depth = 0
        action = self.ExepticMax(gameState, depth, agent_index)

        return action
        
        
    
    def Change( self, gamestate, depth, agent_index):
        
        sum = 0
        actions = gamestate.getLegalActions( agent_index)
        num = 0
        for a in actions:
            
            #if action is wall
            if a == Directions.STOP:
                continue
            
            #state next continue the game
            state_next = gamestate.getNextState( agent_index, a)
            price = self.ExepticMax( state_next, depth, agent_index +1)
            sum = sum + price
            num = num + 1
        
        All = sum/num
        return All
    
        
    def Max( self, gamestate, depth,agent_index):
    
        max = -math.inf
        max_action = None

        actions = gamestate.getLegalActions(agent_index)        
        for a in actions:
            
            #if action is wall
            if a == Directions.STOP:
                continue
            
            #next state continue the game
            state_next = gamestate.getNextState( agent_index, a)
            
            price = self.ExepticMax( state_next,depth, agent_index+1)
            if price > max:
                max = price
                max_action = a
                
        #if depth is zero return the max_action       
        if depth == 0:
            return max_action

        return max
    
    
    def ExepticMax(self,gamestate,depth, agent_index):


        #if agent_index is the max agent
        if agent_index == gamestate.getNumAgents():
            agent_index = 0
            depth = depth + 1
            
        if depth == self.depth:
            return self.evaluationFunction( gamestate)
            
        if gamestate.isWin() or gamestate.isLose():
            return self.evaluationFunction(gamestate)        

        if agent_index == self.index:
            return self.Max( gamestate, depth,agent_index)
        else:
            return self.Change( gamestate, depth,agent_index)

def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    gamestate = currentGameState.getPacmanPosition()
        
    #Win
    win = currentGameState.isWin()
    if win == True:
        return math.inf
    
    #lose
    lose = currentGameState.isLose()
    if lose == True:
        return -math.inf
    
 
    foodList = currentGameState.getFood().asList()
    best_food = 0
    for food in foodList:
        distance = manhattanDistance( gamestate, food)
        distance = (1.0/distance)
        best_food = max( best_food, distance)

    
    #cap
    best_cap = 0
    CapList = currentGameState.getCapsules()
    for cap in CapList:
        distance = manhattanDistance( gamestate, cap)
        distance = (1.0/distance)
        best_cap = max( best_cap, distance)

    #Ghosts
    for ghost in currentGameState.getGhostStates():
        distane = manhattanDistance(currentGameState.getPacmanPosition(), ghost.getPosition())

        if ghost.scaredTimer > 0:
            if( distance > 8):
                score = 0
            else:
                score = pow(8 - distane, 2)
        else:
            if( distance > 7):
                score = pow(7 - distane, 2)
            else:
                score = 0
    
    best_g = score   
    return (currentGameState.getScore() + best_cap + best_food + best_g )
    util.raiseNotDefined()    

    
    def _scoreFromGhost(gameState):
      score = 0
      for ghost in gameState.getGhostStates():
        disGhost = manhattanDistance(gameState.getPacmanPosition(), ghost.getPosition())
        if ghost.scaredTimer > 0:
          score += pow(max(8 - disGhost, 0), 2)
        else:
          score -= pow(max(7 - disGhost, 0), 2)
      return score



    score = currentGameState.getScore()
    scoreGhosts = _scoreFromGhost(currentGameState)
    scoreFood = _scoreFromFood(currentGameState)
    scoreCapsules = _scoreFromCapsules(currentGameState)

    return score + scoreGhosts + scoreFood + scoreCapsules

# Abbreviation
better = betterEvaluationFunction
