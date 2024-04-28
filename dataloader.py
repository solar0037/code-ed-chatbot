import json
# import pandas as pd

# def load_qa(path: str='sof_qa.json') -> pd.DataFrame:
#     with open(path, 'r', encoding='utf-8') as f:
#         sof_qa = json.load(f)
#     df = pd.DataFrame(sof_qa)
#     return df


def load_answers(path: str='answers.json') -> dict:
    with open(path, 'r', encoding='utf-8') as f:
        answers = json.load(f)
    return answers
