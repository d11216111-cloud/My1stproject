# 分數功能計算設計
def calculate_total_score(scores):
    """計算總分數"""
    return sum(scores)
def calculate_average_score(scores):
    """計算平均分數"""
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)
def find_highest_score(scores):
    """找出最高分數"""
    if len(scores) == 0:
        return None
    return max(scores)
def find_lowest_score(scores):
    """找出最低分數"""
    if len(scores) == 0:
        return None
    return min(scores)
def main():
    scores = []
    print("請輸入學生的分數（輸入 'done' 結束）：")
    while True:
        user_input = input("分數: ")
        if user_input.lower() == 'done':
            break
        try:
            score = float(user_input)
            scores.append(score)
        except ValueError:
            print("請輸入有效的數字或 'done' 結束。")
    
    total_score = calculate_total_score(scores)
    average_score = calculate_average_score(scores)
    highest_score = find_highest_score(scores)
    lowest_score = find_lowest_score(scores)
    
    print(f"總分數: {total_score}")
    print(f"平均分數: {average_score}")
    print(f"最高分數: {highest_score}")
    print(f"最低分數: {lowest_score}")
if __name__ == "__main__":
    main()
# scorecod.py end