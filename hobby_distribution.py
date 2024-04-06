hobbies = [
    {"name": "短视频", "probability": 0.13},
    {"name": "电子游戏", "probability": 0.15},
    {"name": "阅读", "probability": 0.05},
    {"name": "旅行", "probability": 0.07},
    {"name": "社交活动和聚会", "probability": 0.08},
    {"name": "跑步", "probability": 0.03},
    {"name": "舞蹈", "probability": 0.03},
    {"name": "唱歌", "probability": 0.05},
    {"name": "乐器演奏", "probability": 0.03},
    {"name": "绘画", "probability": 0.03},
    {"name": "摄影", "probability": 0.013},
    {"name": "自行车骑行", "probability": 0.008},
    {"name": "足球", "probability": 0.008},
    {"name": "篮球", "probability": 0.045},
    {"name": "羽毛球", "probability": 0.02},
    {"name": "乒乓球", "probability": 0.02},
    {"name": "游泳", "probability": 0.01},
    {"name": "健身", "probability": 0.03},
    {"name": "看电影", "probability": 0.04},
    {"name": "追剧", "probability": 0.03},
    {"name": "写作", "probability": 0.02},
    {"name": "烹饪", "probability": 0.025},
    {"name": "烘焙", "probability": 0.015},
    {"name": "园艺", "probability": 0.01},
    {"name": "艺术品收藏", "probability": 0.001},
    {"name": "手工艺", "probability": 0.01},
    {"name": "志愿服务", "probability": 0.03},
    {"name": "棋牌类游戏", "probability": 0.01},
    {"name": "剧本杀", "probability": 0.005},
]


total_probability = 0
for hobby in hobbies:
    total_probability += hobby['probability']

print(f"概率总和为: {round(total_probability, 6)}")


def get_hobby_distribution():
    return hobbies
