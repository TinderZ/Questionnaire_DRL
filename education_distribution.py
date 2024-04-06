import pandas as pd
import random
import numpy as np


education_levels = {
    '高中': 1,
    '大专': 2,
    '本科': 3,
    '硕士': 4,
    '博士': 5
}

# 学历及其在不同年龄段的概率分布
education_distribution = \
    {
        '18-22': {'高中': 1.0},  # 18-22岁只有高中
        '23-25': {'大专': 0.7, '本科': 0.3},  # 23-25岁大专和本科的概率分布
        '26-27': {'大专': 0.7, '本科': 0.25, '硕士': 0.05},  # 26-27岁的概率分布
        '28+': {'大专': 0.7, '本科': 0.2, '硕士': 0.07, '博士': 0.03}  # 28岁及以上的概率分布
    }


def get_education_distribution():
    return education_distribution
