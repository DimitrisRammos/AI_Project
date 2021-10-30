# search.py
# ---------
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


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

from os import PRIO_USER
import util
import math

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def expand(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (child,
        action, stepCost), where 'child' is a child to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that child.
        """
        util.raiseNotDefined()

    def getActions(self, state):
        """
          state: Search state

        For a given state, this should return a list of possible actions.
        """
        util.raiseNotDefined()

    def getActionCost(self, state, action, next_state):
        """
          state: Search state
          action: action taken at state.
          next_state: next Search state after taking action.

        For a given state, this should return the cost of the (s, a, s') transition.
        """
        util.raiseNotDefined()

    def getNextState(self, state, action):
        """
          state: Search state
          action: action taken at state

        For a given state, this should return the next state after taking action from state.
        """
        util.raiseNotDefined()

    def getCostOfActionSequence(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    """

    # print("Start:", problem.getStartState())
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))

    start = problem.getStartState()
    List = []
    visited = {}

    #Stack
    stack = util.Stack()

    #for the start
    visited[start] = True
    stack.push((start,"NULL"))
    exp = {}
    while stack.isEmpty() == False:
        st,ac = stack.pop()
        
        List.append((st,ac))

        
        visited[st] = True
        
        if problem.isGoalState(st) == True:
            break

        li = problem.expand( st)
        exp[st] = li
        
        for state,action,co in li:
            if state in visited:
                if visited[state] == True:
                    continue

            visited[state] = False
            stack.push( (state,action))

    #reverse the list
    List.reverse()

    i = 0
    Li = []
    while i < len(List):
        
        state,action = List[i]

        #if it is the goal
        if problem.isGoalState(state) == True:

            previous_state = state
            previous_action = action
            i +=1
            continue
        
        #we have reverse the list, if we find the start than STOP
        if state == start:
            Li.append(previous_action)
            break
        

        list_with_child = exp[state]
        result = False
        for state_n,action_n,cost_n in list_with_child:
            if state_n == previous_state and previous_action == action_n:
                result = True

        if result == True:

            Li.append(previous_action)
            previous_state = state
            previous_action = action
        
        i = i + 1

    Li.reverse()
    
    return Li
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    start = problem.getStartState()
    List = []
    visited = {}

    #Stack
    queue = util.Queue()

    #for the start
    visited[start] = True
    queue.push((start,"NULL"))
    exp = {}

    while queue.isEmpty() == False:
        st,ac = queue.pop()

        List.append((st,ac))

        if problem.isGoalState(st) == True:
            List.append((st,ac))
            break
        
        visited[st] = True
    
        li = problem.expand( st)
        exp[st] = li
        
        for state,action,co in li:
            if state in visited:
                    continue

            visited[state] = False
            queue.push( (state,action))

    #reverse the list from bfs
    List.reverse()

    i = 0
    Li = []
    while i < len(List):
        
        state,action = List[i]

        if problem.isGoalState(state) == True:
            previous_state = state
            previous_action = action
            i +=1
            continue


        if state == start:
            Li.append(previous_action)
            break


        list_with_child = exp[state]
        result = False
        for state_n,action_n,cost_n in list_with_child:
            if state_n == previous_state and previous_action == action_n:
                result = True

        if result == True:
            Li.append(previous_action)
            previous_state = state
            previous_action = action
        
        i = i + 1

    Li.reverse()
    
    return Li
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    
    start = problem.getStartState()
    visited = {}

    #Stack
    queue = util.Queue()

    #for the start
    visited[start] = True
    #from_start is dictionaries with distance from start state and this state( withn't)
    from_start = {}
    from_start[start] = 0
    
    list_close = {}
    list_open = {}
    list_open[start] = (0 + heuristic(start,problem), None, None)
    min_num = math.inf
    min_element = start

    #from the node where is expand(not double expand in one node)
    exp = {}
    Goal = None

    while len(list_open) != 0:

        state_parent = min_element
        tup = list_open[state_parent]

        if problem.isGoalState(state_parent) == True:
            Goal = state_parent
            list_close[state_parent] = tup 
            break
        
        li = problem.expand( state_parent)
        exp[state_parent] = li

        for state,action,cost in li:
            if state in visited:

                if from_start[state_parent] + cost < from_start[state]:
                    from_start[state] = from_start[state] + cost
                    list_close[state] = (from_start[state] + heuristic(state,problem), state_parent,action)
                continue
            
            if state in list_open:

                if from_start[state_parent] + cost < from_start[state]:
                    from_start[state] = from_start[state_parent] + cost
                    list_open[state] = (from_start[state] + heuristic(state,problem), state_parent,action)
            else:
                from_start[state] = from_start[state_parent] + cost
                list_open[state] = (from_start[state] + heuristic(state,problem),state_parent,action)


            if cost < min_num:
                min_num = cost
                min_element = state

        #delete state from open list and transfer ---> in close List
        del list_open[state_parent]
        list_close[state_parent] = tup
        visited[state_parent] = True

        if min_element == state_parent:
            min_num = math.inf


            for st in list_open:
            
            
                tu = list_open[st]
                cost, before_state,ac = tu
            
            
                if cost < min_num:
                    min_num = cost
                    min_element = st

    state = Goal
    Li = []
    while state != start:
        cost, state_parent, action = tup = list_close[state]
        state = state_parent
        Li.append(action)


    Li.reverse()
    return Li

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
