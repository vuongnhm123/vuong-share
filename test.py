# Hàm hiển thị một câu hỏi và lấy câu trả lời từ người dùng
def ask_question(question, option_a, option_b):
    while True:
        answer = input(f"{question}\n a. {option_a}\n b. {option_b}\nChọn (a/b): ").lower()
        if answer in ['a', 'b']:
            return answer
        else:
            print("Vui lòng chọn 'a' hoặc 'b'.")

# Hàm tính điểm cho một loại tính cách cụ thể dựa trên câu trả lời
def calculate_score(answers):
    score = {
        "E": answers.count("E"),
        "I": answers.count("I"),
        "S": answers.count("S"),
        "N": answers.count("N"),
        "T": answers.count("T"),
        "F": answers.count("F"),
        "J": answers.count("J"),
        "P": answers.count("P"),
    }
    return score

# Hàm xác định loại MBTI dựa trên điểm số
def determine_mbti(score):
    mbti = ""
    mbti += "E" if score["E"] >= score["I"] else "I"
    mbti += "S" if score["S"] >= score["N"] else "N"
    mbti += "T" if score["T"] >= score["F"] else "F"
    mbti += "J" if score["J"] >= score["P"] else "P"
    return mbti

# Hàm xử lý từng câu hỏi và trả về danh sách câu trả lời
def process_questions(questions):
    answers = []
    for q, (option_a, option_b, personality_a, personality_b) in questions.items():
        answer = ask_question(q, option_a, option_b)
        if answer == 'a':
            answers.append(personality_a)
        else:
            answers.append(personality_b)
    return answers

# Hàm chính để chạy chương trình
def main():
    questions = {
        "Bạn cảm thấy thoải mái khi làm quen với người lạ?": ("Có", "Không", "E", "I"),
        "Bạn thường chú trọng đến các chi tiết nhỏ?": ("Có", "Không", "S", "N"),
        "Bạn đưa ra quyết định dựa trên lý trí?": ("Có", "Không", "T", "F"),
        "Bạn thích lên kế hoạch chi tiết trước khi làm?": ("Có", "Không", "J", "P")
    }

    # Xử lý các câu hỏi và lấy câu trả lời
    answers = process_questions(questions)
    
    # Tính điểm dựa trên câu trả lời
    score = calculate_score(answers)

    # Xác định loại MBTI
    mbti_type = determine_mbti(score)
    
    print(f"Loại tính cách MBTI của bạn là: {mbti_type}")

if __name__ == "__main__":
    main()
