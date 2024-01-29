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
    if pos_white<=num_black:
        return 1

    value = 1.
    # print(f"num_black = {num_black}, pos_white = {pos_white}")
    for j in range(1, num_black+1):
        # print(f"j = {j} : {float(pos_white - j) / float(N - j)}")
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

    # -------------------- probability --------------------

    plt.clf()
    plt.plot(3,win_chances[2], marker='o', color='red',label='M=10, p='+str(win_chances[2]))
    plt.plot(10,win_chances[9], marker='o', color='red',label='M=100, p='+str(win_chances[9]))
    plt.plot(30,win_chances[29], marker='o', color='red',label='M=1000, p='+str(win_chances[29]))
    plt.legend()
    plt.plot(num_black_array, win_chances, marker='')
    plt.xlabel('Number of black Balls (k)')
    plt.ylabel('Average Win Chance')
    plt.title('Win Chance vs Number of black Balls, N={}'.format(N))
    plt.xlim(1, min(100, max(num_black_array)))
    plt.ylim(0.5, 1)
    plt.grid(True)
    plt.savefig('plot_average__N={}.png'.format(N))

    # -------------------- p_loss/p_win --------------------

    plt.clf()
    loss_chances = [1.0 - x for x in win_chances]
    result = np.copy(win_chances)
    for i in range(len(result)):
        result[i] = loss_chances[i] / win_chances[i] * num_black_array[i]    
    plt.plot(num_black_array, result, marker='')
    plt.xlabel('Number of black Balls (k)')
    plt.ylabel('p_loss / p_win * k')
    plt.title('N={}'.format(N))
    plt.xlim(1, min(100, max(num_black_array)))
    plt.ylim(0, 2)
    plt.grid(True)
    plt.savefig('plot_p_loss_p_win_k__N={}.png'.format(N))

    # -------------------- Relative return --------------------

    plt.clf()
    result = np.copy(win_chances)
    for i in range(len(result)):
        result[i] = win_chances[i] / num_black_array[i]
    plt.plot(num_black_array, result, marker='')
    plt.xlabel('Number of black Balls (k)')
    plt.ylabel('p_win / k')
    plt.title('N={}'.format(N))
    plt.xlim(1, min(100, max(num_black_array)))
    plt.grid(True)
    plt.savefig('plot_p_win_k__N={}.png'.format(N))

    # -------------------- Differentiate p_win --------------------

    plt.clf()
    result = np.copy(win_chances)
    for i in range(1,len(result)):
        result[i] = win_chances[i] - win_chances[i-1]
    plt.plot(num_black_array, result, marker='')
    plt.xlabel('Number of black Balls (k)')
    plt.ylabel('d p_win / dk')
    plt.title('N={}'.format(N))
    plt.xlim(1, min(100, max(num_black_array)))
    plt.yscale('log')
    plt.grid(True)
    plt.savefig('plot_d_p_win_dk__N={}__log.png'.format(N))
    plt.xscale('log')
    plt.savefig('plot_d_p_win_dk__N={}__log_log.png'.format(N))



def plot_win_chance_vs_k_fixed_m(N):
    """
    Plot the win chance against the number of black balls (k). We have several m.
    
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
    plt.xlabel('Number of black Balls (k)')
    plt.ylabel('Average Win Chance')
    plt.title('Win Chance vs Number of black Balls, N={}'.format(N))
    plt.xlim(0, min(100, max(num_black_array)))
    plt.legend(title='pos_white_array')
    plt.grid(True)
    plt.savefig('plot_fixed_m__N={}.png'.format(N))

    

if __name__ == "__main__":
    N = 1000
    plot_win_chance_vs_k(N)
    plot_win_chance_vs_k_fixed_m(N)
