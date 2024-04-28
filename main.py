from transformers import AutoTokenizer, AutoModelForSequenceClassification, TextClassificationPipeline
from dataloader import load_answers


label2type = {
    'LABEL_0': 0,
    'LABEL_1': 1,
    'LABEL_2': 2,
    'LABEL_3': 3,
    'LABEL_4': 4,
    'LABEL_5': 5,
}

example_questions = {
    '0': "ModuleNotFoundError: No module named ‘selenium’",
    '1': "WebDriverException: Message: 'chromedriver' executable needs to be in PATH ...",
    '2': "WebDriverException: Message: unknown error: Chrome failed to start: exited abnormally",
    '3': "Why cannot I get nested comments?",
    '4': "Why is the created output file saved in the wrong directory?",
    '5': "How do I run selenium without the browser screen?"
}


def main():
    print("Chatbot loading...")

    answers = load_answers()
    model = AutoModelForSequenceClassification.from_pretrained('./model.pt')
    tokenizer = AutoTokenizer.from_pretrained('distilbert-base-uncased')
    pipe = TextClassificationPipeline(model=model, tokenizer=tokenizer)

    print("This is CodeEdChatbot! Please ask me anything.")
    question = input("Q: ")
    output = pipe(question)[0]
    question_type = label2type[output['label']]
    score = output['score']
    candidates = answers[str(question_type)]
    sample_question = example_questions[str(question_type)]

    print(f"Your question is most likely: type {question_type} for score {score*100:.1f}%")
    print(f"Example similar question: {sample_question}")
    response = input("Is the classification correct? [Y]/N ")
    if response == 'N':
        print("Sorry, chatbot couldn't correctly classify your problem.")
        return

    t = 0
    while t <= len(candidates):
        answer_t = candidates[t]
        print(answer_t)
        response = input("Is it solved? [Y]/N ")
        if response == 'N':
            t += 1
        else:
            print("Solved! Thanks for using.")
            break
    if t > len(candidates):
        print("Sorry, chatbot couldn't solve your problem.")


if __name__ == '__main__':
    main()
