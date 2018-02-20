import random
from matplotlib import pyplot as plt


class Environment:
    ''' c_1 and c_2 is the chance of REWARD of action 1 and 2 '''

    def __init__(self, c_1, c_2):
        self.c_1 = c_1
        self.c_2 = c_2

    def penalty(self, action):
        if action == 1:
            if random.random() <= self.c_1:
                return False
            else:
                return True
        if action == 2:
            if random.random() <= self.c_2:
                return False
            else:
                return True
        print('Invalid action.')
        return False

    def changeActionPenaltyChance(self, c_1, c_2):
        self.c_1 = c_1
        self.c_2 = c_2


class Tsetlin:
    def __init__(self, n):
        self.n = n
        self.state = random.choice([self.n, self.n + 1])

    def reward(self):
        if self.state <= self.n and self.state > 1:
            self.state -= 1
        elif self.state > self.n and self.state < 2 * self.n:
            self.state += 1

    def penalize(self):
        if self.state <= self.n:
            self.state += 1
        else:
            self.state -= 1

    def makeDecision(self):
        if self.state <= self.n:
            return 1
        else:
            return 2

    def printInfo(self, nr, action, penOrRew, debugging=True):
        if debugging:
            print('Voter nr:', nr, ' :', penOrRew, 'for action:', action, ', state:', self.state)


def run_simulation(n_states, target, n_automata):
    sensors = [Tsetlin(n_states) for i in range(n_automata)]

    iterations = 10
    count = 0
    env = Environment(0, 0)
    active = []
    for k in range(100):
        for i in range(iterations):
            actions = [v.makeDecision() for v in sensors]
            #M = sum([1 for i in actions if actions[i] == 1])
            M = sum([1 for i in actions if i == 1])
            rewardChance = 0.0
            if M == target:
                count += 1
                # rewardChance = 1.0

            active.append(M)

            if M <= target:
                rewardChance = M * (1 / n_automata)
            elif M > target:
                rewardChance = target * (1 / n_automata) - (M - target) * (1 / n_automata)
            env.changeActionPenaltyChance(rewardChance, rewardChance)  # TODO: Might have to twark individual % chance
            for j in range(len(sensors)):
                if env.penalty(actions[j]):
                    sensors[j].penalize()
                    # sensors[j].printInfo(j, sensors[j], 'punished')
                else:
                    sensors[j].reward()
                    # sensors[j].printInfo(j, sensors[j], 'rewarded')
                    # print('\n--\n')
    # statistics
    print('States:', n_states)
    print('Iterations: ', iterations * 100)
    print('Correct: ', count)
    print('Accuracy: ', count / (iterations * 100))
    return float(count / (iterations * 100))
    return active


states = [1, 2, 3, 5, 10]
Y = []
for i in states:
    Y.append(run_simulation(i, 7, 10))
    print('\n--\n')

# print(run_simulation(1, 3, 5))



X = states

plt.plot(X, Y, 'ro')
plt.plot(X, Y)
plt.title("Learning Automata")
plt.ylabel("percentage probability")
plt.xlabel("Different states")
# plt.legend()
plt.grid(True, color='g')
plt.show()