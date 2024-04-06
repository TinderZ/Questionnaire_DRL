import pandas as pd
import random
import numpy as np
from age_distribution import get_age_distribution, age_range
from occupation_distribution import get_occupation_distribution
from hobby_distribution import get_hobby_distribution
from education_distribution import get_education_distribution, education_levels


def generate_data(num_records=1000):
    age_distribution, ages = get_age_distribution()

    occupations = get_occupation_distribution()
    hobbies = get_hobby_distribution()
    education_probs = get_education_distribution()

    # 转换概率分布为累积概率分布
    # occupations_cumulative = np.cumsum([occ['probability'] for occ in occupations])
    hobbies_cumulative = np.cumsum([hob['probability'] for hob in hobbies])

    data = []
    for _ in range(num_records):
        # 使用numpy.random.choice来根据概率分布选择年龄
        chosen_age = np.random.choice(
            [age['age'] for age in ages],
            p=[age['probability'] for age in ages]
        )
        # 控制兴趣爱好的数量
        num_hobbies = random.randint(1, 3)
        # 使用numpy.random.choice一次性选择不重复的兴趣爱好
        hobby_names = [hobby['name'] for hobby in hobbies]
        hobby_probs = [hobby['probability'] for hobby in hobbies]
        chosen_hobbies = np.random.choice(hobby_names, num_hobbies, p=hobby_probs, replace=False).tolist()

        # 根据年龄确定可能的学历及其概率分布
        if 18 <= chosen_age <= 22:
            education_key = '18-22'
        elif 23 <= chosen_age <= 25:
            education_key = '23-25'
        elif 26 <= chosen_age <= 27:
            education_key = '26-27'
        else:
            education_key = '28+'
        # 根据概率分布选择学历
        education_choices = list(education_probs[education_key].keys())
        education_probs_list = list(education_probs[education_key].values())
        education_index = np.random.choice(range(len(education_choices)), p=education_probs_list)
        education = education_choices[education_index]

        # 根据学历过滤职业选择
        valid_occupations = [occ for occ in occupations if
                             education_levels[occ['min_education']] <= education_levels[education] <= education_levels[
                                 occ['max_education']]]

        valid_occupations_cumulative = np.cumsum([occ['probability'] for occ in valid_occupations])
        chosen_occupation = next(
            occ['name'] for occ, cum_prob in zip(valid_occupations, valid_occupations_cumulative)
            if random.random() < cum_prob
        )

        row = \
            {
                # "id": random.randint(100000, 999999),
                "性别": random.choice(["男", "女"]),
                "年龄": chosen_age,
                "职业": chosen_occupation,
                "学历": education,
                "兴趣爱好": ', '.join(chosen_hobbies),  # 将兴趣爱好列表转换为字符串，用逗号分隔
            }
        data.append(row)

    df = pd.DataFrame(data)
    return df
