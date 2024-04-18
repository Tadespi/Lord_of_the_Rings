import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

characters_of_the_ring = pd.read_csv("lotr_characters.csv")
script_of_the_ring = pd.read_csv("lotr_scripts.csv")

print(characters_of_the_ring.head())