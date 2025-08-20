def cake_calculator(flour: int, sugar: int) -> list[int]:
    """
    Calculates how many cakes can be made and the remaining flour and sugar.

    This function takes the available amounts of flour and sugar, and
    based on a specific cake recipe (100 flour per cake, 50 sugar per cake), determines the maximum number of cakes
    that can be baked. It also calculates the quantities of flour and sugar
    that will be left over after baking.

    The recipe requires:
    - 100 units of flour per cake
    - 50 units of sugar per cake

    Args:
        flour (int): The total amount of flour available (must be larger than 0).
        sugar (int): The total amount of sugar available (must be larger than 0).

    Returns:
        list[int]: A list containing three integers: 
                   [0] - The total number of cakes that can be made.
                   [1] - The amount of flour remaining after making all cakes.
                   [2] - The amount of sugar remaining after making all cakes.
    """ 

     # Define the recipe's ingredient requirements.
    flour_needed_per_cake = 100
    sugar_needed_per_cake = 50
    cakes_made = 0

    # Condition to keep making cakes as long as there is enough flour and sugar.
    while flour >= flour_needed_per_cake and sugar >= sugar_needed_per_cake:
        # Subtract the ingredients needed for one cake.
        flour -= flour_needed_per_cake
        sugar -= sugar_needed_per_cake
        cakes_made += 1 # Increase the number of cake made. 

    # Return the final counts of cakes made and remaining ingredients (flour, sugar)
    return [cakes_made, flour, sugar]
