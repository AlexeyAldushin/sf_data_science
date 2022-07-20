import numpy as np

"""Guess-the-number game
"""

def random_predict(number:int=1) -> int:
    """Predicting the number function

    Args:
        number (int, optional): Picked number. Defaults to 1.

    Returns:
        int: number of guessing attempts
    """
    
    
    count = 0 
    min, max = 1, 101 # range limits at start
    
    while True:
        count += 1
        
        predict_number = (max+min)//2 
        # estimated number in the middle of the range from min to max
        
        if number == predict_number:
            break # stop the cycle if guessed correctly
        
        elif predict_number < number:
            min = predict_number # limiting the range from below
            
        else:
            max = predict_number # limiting the range from above
            
    return(count)


def score_game(random_predict) -> int:
    """Average number of guessing attempts per 1000
    
    Args:
        random_predict ([type]): Predicting the number function

    Returns:
        int: Average number of attempts
    """

    count_ls = [] # list for recording the number of attempts
    np.random.seed(1) # Customizing seed value for reproducibility
    
    random_array = np.random.randint(1, 101, size=(1000))
    # made a list of numbers to guess
    
    for number in random_array:
        count_ls.append(random_predict(number))
                
    score = int(np.mean(count_ls)) # getting average number of attempts

    print(f'Your algorithm guesses the number in: {score} attempts')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(random_predict)