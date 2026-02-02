import csv
import re
from collections import Counter

def get_tokens(text):
    if not text:
        return []
    return re.findall(r'\w+', text.lower())

def calculate_rouge_one_f1(reference, hypothesis):
    if not hypothesis or not hypothesis.strip():
        return 0.0
    
    ref_tokens = get_tokens(reference)
    hyp_tokens = get_tokens(hypothesis)
    
    if not hyp_tokens:
        return 0.0
        
    ref_counts = Counter(ref_tokens)
    hyp_counts = Counter(hyp_tokens)
    
    overlap = 0
    for token in hyp_counts:
        overlap += min(hyp_counts[token], ref_counts[token])
        
    precision = overlap / len(hyp_tokens)
    recall = overlap / len(ref_tokens)
    
    if precision + recall == 0:
        return 0.0
        
    f1 = 2 * (precision * recall) / (precision + recall)
    
    return round(f1, 3)

def solve():
    sum_f1_ver1 = 0.0
    sum_f1_ver2 = 0.0
    count = 0
    
    try:
        with open('corpus.csv', mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                count += 1
                translation = row['translation']
                ver1 = row.get('ver1', '') 
                ver2 = row.get('ver2', '')
                
                f1_v1 = calculate_rouge_one_f1(translation, ver1)
                f1_v2 = calculate_rouge_one_f1(translation, ver2)
                
                sum_f1_ver1 += f1_v1
                sum_f1_ver2 += f1_v2
                
    except FileNotFoundError:
        print(0.0)
        return

    if count == 0:
        print(0.0)
        return

    result = (sum_f1_ver1 - sum_f1_ver2) / count
    
    print(round(result, 3))

if __name__ == '__main__':
    solve()