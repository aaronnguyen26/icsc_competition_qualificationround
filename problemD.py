import random
import string 


GRID_SIZE = 10 # Initialize a 10x10 grid 

# These are the 8 directions a word can be placed:
# (row_change, col_change)
DIRECTIONS = [
    (0, 1),   # Right (horizontal)
    (0, -1),  # Left (horizontal) 
    (1, 0),   # Down (vertical)
    (-1, 0),  # Up (vertical, also less common but valid)
    (1, 1),   # Down-Right (diagonal)
    (-1, -1), # Up-Left (diagonal)
    (1, -1),  # Down-Left (diagonal)
    (-1, 1)   # Up-Right (diagonal)
]

# --- Helper Functions (these do the heavy lifting for placing words) ---

def _can_place_word(grid: list[list[str]], word: str, r_start: int, c_start: int, dr: int, dc: int) -> bool:
    """
    Checks if a word can be placed in the grid at a given starting position and direction.

    Args:
        grid (list[list[str]]): The current state of the word search grid.
        word (str): The word to try and place.
        r_start (int): The starting row index.
        c_start (int): The starting column index.
        dr (int): The row change for each letter (direction).
        dc (int): The column change for each letter (direction).

    Returns:
        bool: True if the word can be placed without going out of bounds
              or conflicting with existing non-matching letters; False otherwise.
    """
    # Iterate through each character of the word
    for i, char_to_place in enumerate(word):
        r_curr = r_start + i * dr # Calculate current row for this letter
        c_curr = c_start + i * dc # Calculate current column for this letter

        # 1. Check if the current position is within the grid boundaries
        if not (0 <= r_curr < GRID_SIZE and 0 <= c_curr < GRID_SIZE):
            return False # Nope, it goes out of bounds!

        # 2. Check for conflicts with existing letters
        # If the cell is not empty ('.') AND the letter there doesn't match
        # the letter we want to place, then it's a conflict.
        # We convert both to uppercase to ensure case-insensitive matching.
        if grid[r_curr][c_curr] != '.' and grid[r_curr][c_curr] != char_to_place.upper():
            return False # Conflict found! Cannot place here.

    return True # If we made it this far, the word can be placed!


def _place_word(grid: list[list[str]], word: str, r_start: int, c_start: int, dr: int, dc: int):
    """
    Places a word into the grid at a given starting position and direction.
    (Assumes _can_place_word has already confirmed it's a valid spot).

    Args:
        grid (list[list[str]]): The word search grid to modify.
        word (str): The word to place.
        r_start (int): The starting row index.
        c_start (int): The starting column index.
        dr (int): The row change for each letter (direction).
        dc (int): The column change for each letter (direction).
    """
    for i, char_to_place in enumerate(word):
        r_curr = r_start + i * dr
        c_curr = c_start + i * dc
        # Place the letter, ensuring it's uppercase for consistency
        grid[r_curr][c_curr] = char_to_place.upper()


def create_crossword(words: list[str]) -> list[list[str]]:
    """
    Generates a 10x10 word search puzzle grid containing the given words.

    Words can be placed horizontally, vertically, or diagonally.
    Empty spaces in the grid are filled with random uppercase letters.

    Args:
        words (list[str]): A list of words (strings) to hide in the puzzle.

    Returns:
        list[list[str]]: A 2D list (list of lists) of characters
                         representing the completed word search puzzle.
    """
    # Initialize our 10x10 grid with placeholder dots
    grid = [['.' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    # It's a good strategy to try placing longer words first,
    # as they are generally harder to fit into remaining spaces.
    # So, we sort the words by length in descending order.
    words_to_place = sorted(words, key=len, reverse=True)

    # Let's try to place each word from our sorted list
    for word in words_to_place:
        placed_successfully = False
        # Set a limit for attempts to place a single word
        # This prevents infinite loops if a word is impossible to place (e.g., too long)
        MAX_PLACEMENT_ATTEMPTS_PER_WORD = 2000 # Increased attempts for robustness

        for attempt in range(MAX_PLACEMENT_ATTEMPTS_PER_WORD):
            # Pick a random starting point in the grid
            r_start = random.randint(0, GRID_SIZE - 1)
            c_start = random.randint(0, GRID_SIZE - 1)

            # Pick a random direction
            dr, dc = random.choice(DIRECTIONS)

            # Check if this chosen spot and direction works for the current word
            if _can_place_word(grid, word, r_start, c_start, dr, dc):
                # If it does, place the word!
                _place_word(grid, word, r_start, c_start, dr, dc)
                placed_successfully = True
                break # Word placed, move to the next word!

        # (Optional but good for debugging): If we couldn't place a word after many tries
        if not placed_successfully:
            print(f"Warning: Could not place word '{word}' after {MAX_PLACEMENT_ATTEMPTS_PER_WORD} attempts.")
            # In a real application, you might raise an error here or try a different strategy.
            # For this problem, we'll just continue and hope it doesn't happen too often.

    # --- Now, fill in the rest of the empty spots with random letters ---
    # Get all uppercase letters 'A' through 'Z'
    uppercase_letters = string.ascii_uppercase

    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            if grid[r][c] == '.': # If it's still an empty placeholder
                grid[r][c] = random.choice(uppercase_letters) # Fill it with a random letter

    return grid
