import matplotlib.pyplot as plt
import numpy as np

max_num_black_ratio = 3./4.

def calculate_win_chance(N, num_black,pos_white):
    """
    Calculate the win chance for black balls in buckets lottery.
    
    Parameters:
    - N: Total number of balls.
    - num_black: Number of black balls.
    - pos_white: Position of the bucket seperator ball.
    
    Returns:
    - Win chance.
    """
    value = 1.
    # print(f"num_black = {num_black}, pos_white = {pos_white}")
    for j in range(1, num_black+1):
        # print(f"j = {j} : {float(pos_white - j) / float(N - j)}")
        if pos_white-j==0:
            return 1
        value *= float(pos_white - j) / float(N - j)    
    return 1-value

def average_win_chance(N, num_black):
    """
    Calculate the average win chance over all possible positions of the white ball i.
    
    Parameters:
    - N: Total number of balls.
    - num_black: Number of black balls.
    
    Returns:
    - Average win chance as a decimal.
    """
    return np.mean([calculate_win_chance(N, num_black, m) for m in range(1, N+1)])

def plot_win_chance_vs_k(N):
    """
    Plot the win chance against the number of black balls.
    
    Parameters:
    - N: Total number of balls.
    """
    num_black_array = list(range(1, int(max_num_black_ratio * N)))
    # print(f"num_black_array = {num_black_array}")
    win_chances = [average_win_chance(N, k) for k in num_black_array]

    plt.clf()
    plt.plot(num_black_array, win_chances, marker='')
    plt.xlabel('Number of Adversary Balls (k)')
    plt.ylabel('Average Win Chance')
    plt.title('Win Chance vs Number of Adversary Balls, N={}'.format(N))
    plt.xlim(0, min(100, max(num_black_array)))
    plt.grid(True)
    # make a string for the filename containing the number of balls
    plt.savefig('plot_average__N={}.png'.format(N))

def plot_win_chance_vs_k_fixed_m(N):
    """
    Plot the win chance against the number of adversary balls (k). We have several m.
    
    Parameters:
    - N: Total number of balls.
    """
    pos_white_array = [.5, .75,  .9, .95]
    pos_white_array = [int(x * N) for x in pos_white_array]
    num_black_array = list(range(1, int(max_num_black_ratio * N)))    
    # print(f"pos_white_array = {pos_white_array}")
    # print(f"num_black_array = {num_black_array}")
    plt.clf()
    for m in pos_white_array:
        win_chances = [calculate_win_chance(N, k, m) for k in num_black_array]
        plt.plot(num_black_array, win_chances, marker='', label=m)
    plt.xlabel('Number of Adversary Balls (k)')
    plt.ylabel('Average Win Chance')
    plt.title('Win Chance vs Number of black Balls, N={}'.format(N))
    plt.xlim(0, min(100, max(num_black_array)))
    plt.legend(title='pos_white_array')
    plt.grid(True)
    plt.savefig('plot_fixed_m__N={}.png'.format(N))

    

if __name__ == "__main__":
    N = 100
    plot_win_chance_vs_k(N)
    plot_win_chance_vs_k_fixed_m(N)
    N = 1000
    plot_win_chance_vs_k(N)
    plot_win_chance_vs_k_fixed_m(N)
