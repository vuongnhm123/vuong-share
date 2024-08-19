def ask_question(question):
    while True:
        answer = input(f"{question} (a/b): ").lower()
        if answer in ['a', 'b']:
            return answer
        else:
            print("Vui lòng chọn 'a' hoặc 'b'.")

def calculate_mbti(answers):
    mbti = ""
    mbti += "E" if answers['EI'] > 0 else "I"
    mbti += "S" if answers['SN'] > 0 else "N"
    mbti += "T" if answers['TF'] > 0 else "F"
    mbti += "J" if answers['JP'] > 0 else "P"
    return mbti

def main():
    questions = {
        "EI": [
            ("Bạn thích tham gia các buổi tiệc đông người?", "a. Có", "b. Không"),
            ("Bạn cảm thấy thoải mái khi gặp gỡ người lạ?", "a. Có", "b. Không")
        ],
        "SN": [
            ("Bạn tin tưởng vào trực giác nhiều hơn?", "a. Có", "b. Không"),
            ("Bạn thường chú ý đến chi tiết nhỏ?", "a. Không", "b. Có")
        ],
        "TF": [
            ("Bạn đưa ra quyết định dựa trên lý trí?", "a. Có", "b. Không"),
            ("Bạn chú trọng cảm xúc hơn trong quyết định?", "a. Không", "b. Có")
        ],
        "JP": [
            ("Bạn thích lên kế hoạch chi tiết trước khi làm?", "a. Có", "b. Không"),
            ("Bạn thích để mọi thứ tự nhiên xảy ra?", "a. Không", "b. Có")
        ]
    }

    answers = {
        "EI": 0,
        "SN": 0,
        "TF": 0,
        "JP": 0
    }

    for category, qs in questions.items():
        for q, a, b in qs:
            answer = ask_question(q)
            if answer == "a":
                answers[category] += 1
            else:
                answers[category] -= 1

    mbti_type = calculate_mbti(answers)
    print(f"Loại tính cách của bạn là: {mbti_type}")

if __name__ == "__main__":
    main()
