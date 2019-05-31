#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    # this uses a couple of built-in Python functions to reduce the amount of code needed
    # items() gets the keys and values for the recipe dictionary and get() returns the
    # value for the specified key if it's in the dictionary (0 otherwise) and divides it
    # by the amount required by the recipe
    return min(int(ingredients.get(ingredient, 0) / amount) for ingredient, amount in recipe.items())


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
