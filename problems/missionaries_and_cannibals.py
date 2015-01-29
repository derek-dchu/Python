from data_structure.stack import Stack


class State:
    def __init__(self, m, c, b):
        """
        m: number of missionaries on left bank
        c: number of cannibals on left bank
        b: indicator of boat on left bank
        """
        self.m = m
        self.c = c
        self.b = b
        self.next_states = []

    def __eq__(self, state):
        return (self.m == state.m
            and self.c == state.c
            and self.b == state.b)

    def __add__(self, action):
        return State(self.m + action["m"],
            self.c + action["c"],
            self.b + action["b"])

    def __sub__(self, action):
        return State(self.m - action["m"],
            self.c - action["c"],
            self.b - action["b"])

    def __hash__(self):
        return 31*(self.m+31*(self.c+31*self.b))

    def __str__(self):
        return "<{},{},{}>".format(self.m, self.c, self.b)


def actions():
    actions = [
        {
            "m": 1,
            "c": 0,
            "b": 1
        },
        {
            "m": 0,
            "c": 1,
            "b": 1
        },
        {
            "m": 1,
            "c": 1,
            "b": 1
        },
        {
            "m": 2,
            "c": 0,
            "b": 1
        },
        {
            "m": 0,
            "c": 2,
            "b": 1
        }
    ]

    for action in actions:
        yield action

def is_valid_state(state):
    return not (state.m < 0 or state.c < 0 
        or (state.m > 0 and state.m < state.c) or 
        state.m > 3 or state.c > 3 
        or (state.m < 3 and state.m > state.c))

def solution():
    init_state = State(3, 3, 1)
    goal_state = State(0, 0, 0)
    state_stack = Stack()
    state_stack.push(init_state)
    visited = {
        init_state: True
    }

    while not state_stack.is_empty:
        curr_state = state_stack.pop()

        for action in actions():
            if curr_state.b == 1:
                new_state = curr_state - action
            else:
                new_state = curr_state + action
            if is_valid_state(new_state) and new_state not in visited:
                visited[new_state] = True
                curr_state.next_states.append(new_state)
                state_stack.push(new_state)
            
            if new_state == goal_state:
                return init_state
    return []


def find_solution(init_state):
    steps = []
    helper(init_state, steps)
    return steps

def helper(state, steps=[]):
    steps.append(state)

    if state == State(0, 0, 0):
        return True

    for s in state.next_states:
        if helper(s, steps):
            return True
        else:
            steps.pop()
    return False

def print_solution(steps):
    l_to_r = "{} --- {} --> {}"
    r_to_l = "{} <-- {} --- {}"
    for i in range(0, len(steps)-1):
        curr_state = steps[i]
        next_state = steps[i+1]
        right_bank = State(3 - curr_state.m, 3 - curr_state.c, curr_state.b ^ 1)
        if i % 2 == 0:
            print(l_to_r.format(curr_state, (curr_state.m-next_state.m, curr_state.c-next_state.c), right_bank))
        else:
            print(r_to_l.format(curr_state, (next_state.m-curr_state.m, next_state.c-curr_state.c), right_bank))
    print(State(0, 0, 0))


if __name__ == '__main__':
    print_solution(find_solution(solution()))