"""BF16 + enforce_eager disentangling experiment.

Runs bfloat16 with enforce_eager=True (same engine path as float32)
to separate precision effect from engine effect.
"""
import json
import re
import os
import sys

os.environ["CUDA_VISIBLE_DEVICES"] = "0"
os.environ["VLLM_USE_V1"] = "0"

import pandas as pd
from vllm import LLM, SamplingParams

sys.path.insert(0, ".")
from src.data.prompt_templates import ANSWER_MAP, format_prompt

ANSWER_PATTERN = re.compile(r"^\s*([A-Da-d])\b")

def extract_answer(text):
    m = ANSWER_PATTERN.match(text)
    return m.group(1).upper() if m else None

def main():
    with open("data/mmlu_items.json") as f:
        items = json.load(f)
    with open("data/few_shot_examples.json") as f:
        few_shot = json.load(f)

    design = pd.read_csv("design_matrix.csv")
    bf16_design = design[design["precision"] == "bfloat16"].copy()
    print(f"BF16 conditions: {len(bf16_design)}")

    print("Loading bfloat16 + enforce_eager=True (V0 engine)...")
    llm = LLM(
        model="meta-llama/Llama-3.1-8B-Instruct",
        dtype="bfloat16",
        seed=42,
        tensor_parallel_size=1,
        gpu_memory_utilization=0.90,
        trust_remote_code=True,
        max_model_len=4096,
        enforce_eager=True,
    )

    llm.generate(["Warmup prompt."], SamplingParams(temperature=0, max_tokens=5))
    print("Warmup done.")

    results = []
    for _, row in bf16_design.iterrows():
        cond_id = int(row["condition_id"])
        temperature = float(row["temperature"])
        top_p_raw = row["top_p"]
        top_p = float(top_p_raw) if top_p_raw != "" and pd.notna(top_p_raw) else None
        prompt_template = int(row["prompt_template"])
        seed = int(row["seed"])
        ordering = int(row["ordering"])

        prompts = []
        item_meta = []
        for item in items:
            subject = item["subject"]
            examples = few_shot[subject][str(ordering)]
            prompt_text = format_prompt(
                template_id=prompt_template,
                subject=subject,
                question=item["question"],
                choices=item["choices"],
                few_shot_examples=examples,
            )
            prompts.append(prompt_text)
            item_meta.append(item)

        sp = SamplingParams(
            temperature=temperature,
            top_p=top_p if top_p is not None else 1.0,
            max_tokens=20,
            seed=seed,
        )
        outputs = llm.generate(prompts, sp)

        n_correct = 0
        for output, item in zip(outputs, item_meta):
            text = output.outputs[0].text
            predicted = extract_answer(text)
            gold = ANSWER_MAP[item["answer_idx"]]
            correct = int(predicted == gold) if predicted else 0
            n_correct += correct

            results.append({
                "condition_id": cond_id,
                "item_id": item["item_id"],
                "subject": item["subject"],
                "model": "meta-llama/Llama-3.1-8B-Instruct",
                "precision": "bfloat16_eager",
                "temperature": temperature,
                "top_p": top_p,
                "prompt_template": prompt_template,
                "seed": seed,
                "ordering": ordering,
                "generated_text": text,
                "predicted_answer": predicted,
                "gold_answer": gold,
                "correct": correct,
            })

        print(f"  Condition {cond_id:>3d}: {n_correct}/{len(items)} correct")

    with open("results/bf16_eager_results.jsonl", "w") as f:
        for r in results:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    total = len(results)
    correct_total = sum(r["correct"] for r in results)
    print(f"\nBF16+eager: {correct_total}/{total} = {correct_total/total:.4f}")

    from collections import defaultdict
    by_subject = defaultdict(list)
    for r in results:
        by_subject[r["subject"]].append(r["correct"])
    print("\nPer-subject accuracy:")
    for subj, vals in sorted(by_subject.items()):
        print(f"  {subj}: {sum(vals)/len(vals):.4f} ({len(vals)} records)")

    print("\nDone -> results/bf16_eager_results.jsonl")

if __name__ == "__main__":
    main()
