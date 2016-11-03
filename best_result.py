# FOR LATER. This is going to use a action-policy evaluator, 
# as well as something that figures reward, and it's going to 
# search all possibilities N moves in advance, and
# then pick the one that ends with the highest reward. 
import time

class StateTree(object):
  def __init__(self, num_branches, state):
    self.reward = reward or 0
    self.state = state
    self.num_branches
    self.branches = [None for i in range(num_branches)]
  def set_reward(self, rew):
    self.reward = rew

  def set_branch(branch_num, self, reward):
    if not self.branches[branch_num]:
      self.branches[branch_num] = stateTree(self.num_branches, 0)
    self.branches[branch_num].set_reward(reward)

  def branches_are_filled(self):
    return all(self.branches)

  def get_branch(self, branch_num):
    return self.branches[branch_num]

  




class BfsAlgo(object):
  def __init__(self, reward_func, num_actions, new_state_from_state_action, state_evaluator, gamma):
    # This takes in a bunch of COMPLEX functions to work.
    # Reward function: Takes in a state, figures out what the most recent
    # reward transition was. So, after you do a move, you figure out what the
    # reward transition is from the return of 'new_state_from_state_action'.
    self.reward_func = reward_func
    # num_actions is the number of possible actions
    self.num_actions = num_actions
    # new_state_from_state_aciton takes in a state and an action, and 
    # figures out what the next state is going to be. 
    # NOTE: It doesn't return the picture, it returns the entire state!
    self.new_state_from_state_action = new_state_from_state_action
    # state_evaluator evaluates a state, probably by using the maximum
    # of state-action values from it.
    self.state_evaluator = state_evaluator
    # Gamma is important for figuring out total reward from any path. You
    # can't just use the end, because that skips interim rewards
    self.gamma = gamma


  def search_from_state(current_state, num_branches, max_depth, max_time):
    if not (max_depth or max_time):
      raise Exception("We don't have infinite time you know.")
    if not max_depth:
      max_depth = float("inf")
    if not max_time:
      max_time = float("inf")

    root = StateTree(num_branches, current_state)
    frontier = [root]
    edge_zone = []
    
    curr_time = time.time()
    curr_depth = 0

    while curr_depth <= max_depth and time.time() < curr_time + max_time:
      print('on to the next one')
      for tree_elem in frontier:
        for branch in tree_elem



    










