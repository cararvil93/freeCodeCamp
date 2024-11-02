import copy
import random


class Hat:
    def __init__(self, **kwargs):
        # Check that there is at least one ball
        n_balls = 0
        for _, value in kwargs.items():
            n_balls += value
        if n_balls == 0:
            raise (f"There must be at least one ball in the hat")

        # Load kwargs into a list
        self.contents = []
        for key, value in kwargs.items():
            for _ in range(value):
                self.contents.append(key)

    def draw(self, n_draws):

        if n_draws > len(self.contents):
            drawn_balls = copy.deepcopy(self.contents)
            self.contents = []
            return drawn_balls

        drawn_balls = random.sample(self.contents, n_draws)
        for ball in drawn_balls:
            self.contents.remove(ball)

        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_success = 0
    for _ in range(num_experiments):

        # Make a temporal copy of hats for each iteration
        hat_copy = copy.deepcopy(hat)
        # Draw the balls
        balls_drawn = hat_copy.draw(num_balls_drawn)

        # Save results in dictionary
        balls_drawn_dict = {}
        for color in balls_drawn:
            if color in balls_drawn_dict.keys():
                continue
            balls_drawn_dict[color] = balls_drawn.count(color)
        # Compare results with expectation
        results = [
            (
                True
                if key in balls_drawn_dict.keys()
                and expected_balls[key] <= balls_drawn_dict[key]
                else False
            )
            for key in expected_balls.keys()
        ]
        if all(results):
            num_success += 1

    # Return probability
    return num_success / num_experiments


# Test all
hat = Hat(black=6, red=4, green=3)


probability = experiment(hat=copy.copy(hat),
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000)
