import os
import calc_score
import format_string
import load_file
import morphological_analysis
import preprocess_dict
import preprocess_dict2

data_str, dict1_str, dict2_str = load_file.func_read_data()
sentences = data_str.splitlines()
data = [morphological_analysis.analyze_single_sentence(s) for s in sentences]
dict1 = preprocess_dict.preprocess_dict(dict1_str.splitlines())
dict2 = preprocess_dict2.Info2(dict2_str.splitlines())
scores = calc_score.calc_score(data, dict1, dict2)

set_sentences = set()
score_sentences = []
for (s, p) in zip(sentences, scores):
    if s not in set_sentences:
        set_sentences.add(s)
        score_sentences.append((p, s))
score_sentences.sort()
max_len = max(format_string.calc_length(s) for s in sentences)

root_dir = os.path.dirname(os.path.dirname(__file__))
result_path = os.path.join(root_dir, 'data', 'result.txt')
with open(result_path, 'w') as file:
    for (p, s) in score_sentences:
        file.write(f"{format_string.align_text(s, max_len)} | {p:10.4f}\n")
