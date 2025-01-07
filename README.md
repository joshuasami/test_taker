# test_taker

This script allows you to run quizzes from Markdown files. It's designed specifically for practice exams from the [AWS-Certified-Cloud-Practitioner-Notes](https://github.com/kananinirav/AWS-Certified-Cloud-Practitioner-Notes) repository. 

## Usage

Simply run `main.py` with the exam file as an argument:

```
python main.py /practice-exams/practice-exam-1.md
```

For single-answer questions, enter the letter of the correct answer. For two-answer questions, separate the letters with a comma (e.g., A,C).  Your test results will be displayed upon completion. Answering Questions

* **Single-Answer Questions:** Input the letter of the correct answer (e.g., A).
* **Two-Answer Questions:** Input the letters of the correct answers separated by a comma (e.g., A,C).


## Output

After completing the quiz, your score will be printed to the console. Each question is worth one point. For two-answer questions, each correct answer contributes 0.5 points. 

```
Quiz completed! Your total score is: 40 out of 50. This is 80%.
```

**Note:** This scoring system does not reflect the different weighting applied in the actual AWS certification exams. It simply provides a basic point system for practice purposes.



