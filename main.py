import re
import sys

def parse_markdown(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    # split content into questions, split based on question numbers
    questions_raw = re.split(r'\n\d+\.\s', content)[1:]

    questions = []
    for q in questions_raw:

        # extract question text and options
        q_parts = q.strip().split('\n\n')
        q_text_and_options = q_parts[0].strip().split('\n')
        q_text = q_text_and_options[0].strip()

        # extract options
        options = []
        for line in q_text_and_options[1:]:
            opt_match = re.search(r'-\s+([A-Z])\.\s+(.+)', line)
            if opt_match:
                options.append(f"{opt_match.group(1)}. {opt_match.group(2)}")
            else:
                continue

        # extract correct answers
        answer_match = re.search(
            r'<details markdown=1><summary markdown=\'span\'>Answer</summary>\s*Correct answer:\s*(.*?)\s*</details>',
            q, re.DOTALL)
        if answer_match:
            correct = [ans.strip() for ans in re.split(r',\s*', answer_match.group(1))]
        else:
            correct = []

        questions.append({
            'question': q_text,
            'options': options,
            'correct': correct
        })

    return questions

def run_quiz(questions):
    score = 0
    print("Welcome to the interactive quiz! Let's get started.\n")

    for idx, q in enumerate(questions, 1):
        print(f"Question {idx}: {q['question']}\n")
        for opt in q['options']:
            print(f"{opt}")
        print()

        # get user answer
        user_answer = input("Your answer (e.g., A or A,B): ").upper()
        user_answers = [ans.strip().lower() for ans in user_answer.split(',')]
        q['correct'] = [ans.lower() for ans in q['correct']]

        # scoring logic
        if len(q['correct']) > 1:
            # multiple correct answers
            correct_set = set(q['correct'])
            user_set = set(user_answers)
            correct_choices = correct_set.intersection(user_set)
            points = 0.5 * len(correct_choices)
            score += points
        else:
            # single correct answer
            if user_answers[0] == q['correct'][0]:
                score += 1

        print(f"Correct answer(s): {', '.join(q['correct'])}\n")

    print(f"Quiz completed! Your total score is: {score} out of {len(questions)}. This is {score/len(questions)*100:.2f}%.")

if __name__ == "__main__":
    
    # load the markdown filename
    filename = sys.argv[1]
    if type(filename) != str:
        print("Please provide a valid markdown file.")
        sys.exit(1)

    # parse the markdown file
    questions = parse_markdown(filename)
    if not questions:
        print("No questions were found in the markdown file.")
    else:
        run_quiz(questions)
