from data_generation import generate_data
import pandas as pd


def main():
    df = generate_data(10000)  # 生成xxxx条记录。
    # 将生成的数据保存到CSV文件中，不包含索引，使用utf-8-sig编码
    df.to_csv("random_data_weighted.csv", index=False, encoding="utf-8-sig")

    # 设置打印的格式，特别是职业列的宽度
    pd.set_option('display.unicode.east_asian_width', True)  # 正确处理中文字符宽度
    pd.set_option('display.width', 1000)  # 设置打印宽度，以适应更宽的“职业”列
    pd.set_option('display.max_columns', None)  # 不限制显示的最大列数

    # 定义各列的宽度，可以根据需要调整
    column_widths = {
        # 'id': 10,
        '性别': 6,
        '年龄': 6,
        '职业': 25,  # 给“职业”列分配更多的空间
        '学历': 6,
        '兴趣爱好': 25,
    }

    # 使用to_string方法打印DataFrame，并应用自定义的列宽
    print(df.head(50).to_string(index=False, justify='left', col_space=10, formatters={
        # 'id': lambda x: f"{x:<{column_widths['id']}}",
        '性别': lambda x: f"{x:<{column_widths['性别']}}",
        '年龄': lambda x: f"{x:<{column_widths['年龄']}}",
        '职业': lambda x: f"{x:<{column_widths['职业']}}",
        '学历': lambda x: f"{x:<{column_widths['学历']}}",
        '兴趣爱好': lambda x: f"{x:<{column_widths['兴趣爱好']}}",
    }))


# 当此脚本作为主程序运行时，执行main函数
# if __name__ == "__main__":
main()
