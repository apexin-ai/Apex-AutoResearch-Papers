"""从 RSFT candidates (generations.jsonl) 中 random 选 k=1（每个 doc 随机选 1 个），
输出 rsft_trainer 兼容格式。"""
import json
import random
import re
import sys
from collections import defaultdict

random.seed(42)

def extract_user_content(prompt_text):
    """从 chat template prompt 中提取 user message content。"""
    marker = "<|im_start|>user\n"
    start = prompt_text.find(marker)
    if start < 0:
        return prompt_text
    content_start = start + len(marker)
    end = prompt_text.find("<|im_end|>", content_start)
    if end < 0:
        return prompt_text[content_start:]
    return prompt_text[content_start:end]

input_path = sys.argv[1]
output_path = sys.argv[2]

candidates = []
with open(input_path) as f:
    for line in f:
        line = line.strip()
        if line:
            candidates.append(json.loads(line))

by_doc = defaultdict(list)
for c in candidates:
    by_doc[c["doc_id"]].append(c)

selected = [random.choice(v) for v in by_doc.values()]

print(f"Selected {len(selected)} from {len(candidates)} candidates ({len(by_doc)} docs)")

with open(output_path, "w") as f:
    for s in selected:
        item = {
            "input": extract_user_content(s["prompt"]),
            "output": s["output"],
            "ced_score": 1.0,
            "doc_id": s["doc_id"],
            "generation_idx": s["generation_idx"],
            "format_reward": float(s.get("format_ok", False)),
            "f1_reward": 0.0,
            "combined_score": 0.0,
        }
        f.write(json.dumps(item, ensure_ascii=False) + "\n")

print(f"Written to {output_path}")
