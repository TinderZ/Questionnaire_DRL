import numpy as np
import matplotlib.pyplot as plt

# 限定年龄范围
age_range = np.arange(18, 51)


def original_probability_density(age):
    return -0.0025 * age ** 2 + 0.125 * age + 1


def piecewise_probability_density(age):
    probability_at_20 = original_probability_density(20)  # 计算20岁处的概率
    if age < 20:
        return probability_at_20  # 20岁以下都用20岁处的概率
    else:
        return original_probability_density(age)  # 20岁以上使用原函数的概率


# 计算每个年龄的概率
probabilities = np.array([piecewise_probability_density(age) for age in age_range])
# 归一化概率，以确保总概率为1
probabilities /= np.sum(probabilities)


def get_age_distribution():
    # 将年龄和对应的概率放入字典中
    age_distribution = {age: prob for age, prob in zip(age_range, probabilities)}
    # 定义年龄及其概率的配对列表
    ages = [{'age': age, 'probability': age_distribution[age]} for age in age_range]
    # 返回年龄分布字典
    # return age_distribution
    return age_distribution, [{'age': age, 'probability': prob} for age, prob in age_distribution.items()]


# ages_cumulative = np.cumsum([occ['probability'] for occ in ages])
# 可视化图片

plt.figure(figsize=(10, 6))
plt.bar(age_range, probabilities, color='blue', edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Probability')
plt.title('Age Distribution with Piecewise Function')
plt.grid(True)
plt.show()
