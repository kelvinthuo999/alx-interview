#!/usr/bin/python3

def is_winner(player):
    return "Maria" if player == 0 else "Ben"

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def isWinner(x, nums):
    """
    Determine the winner of the prime game.
    
    :param x: Number of rounds
    :param nums: List of numbers for each round
    :return: Name of the player that won the most rounds
    """
    winners = []
    for i in range(x):
        # Copy the current round's numbers for each player's turn
        maria_nums = nums[i].copy()
        ben_nums = nums[i].copy()
        
        # Simulate Maria's turn
        for num in sorted(maria_nums, reverse=True):
            if is_prime(num):
                maria_nums = [n for n in maria_nums if n % num!= 0]
                break
        
        # Simulate Ben's turn
        for num in sorted(ben_nums, reverse=True):
            if is_prime(num):
                ben_nums = [n for n in ben_nums if n % num!= 0]
                break
        
        # Update the winner count
        winners.append(is_winner(i % 2))
    
    # Count the winners
    counts = {player: winners.count(player) for player in ["Maria", "Ben"]}
    
    # Determine the overall winner
    if counts["Maria"] > counts["Ben"]:
        return "Maria"
    elif counts["Ben"] > counts["Maria"]:
        return "Ben"
    else:
        return None
