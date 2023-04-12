import pandas as pd
import numpy as np

from scipy.stats import mannwhitneyu

chat_id = 291445198

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.02
    return mannwhitneyu(x, y).pvalue < alpha
