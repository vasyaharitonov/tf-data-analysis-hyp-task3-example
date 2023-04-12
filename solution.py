import pandas as pd
import numpy as np

from scipy.stats import ttest_ind

chat_id = 291445198

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.02
    return ttest_ind(x, y, equal_var=False).pvalue < alpha
