# eval_phase2_mtbench.py — 简化 MT-Bench 风格的多轮对话质量评估
# 用法: python eval_phase2_mtbench.py --checkpoint-dir /root/turn_residual_gating/checkpoints/tg_s42 --gate-type threadgate
# 输出: JSON 评分结果

import argparse
import json
import os
import re
import sys

import torch
import torch.nn as nn
import numpy as np
from transformers import AutoTokenizer, AutoModelForCausalLM

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config import MODEL_NAME
from model_loader import load_model_with_gates


TEST_QUESTIONS = [
    {
        "id": 1,
        "category": "writing",
        "turn1": "Draft a professional email requesting a deadline extension for a project. The project is a quarterly financial report, and you need two extra weeks due to delayed data from a partner team.",
        "turn2": "Now rewrite the email to be more concise (under 100 words) and add a specific new deadline of June 15th.",
    },
    {
        "id": 2,
        "category": "reasoning",
        "turn1": "Explain the concept of machine learning to a 10-year-old child.",
        "turn2": "Now explain it to a PhD computer science student, building on your previous explanation and adding technical depth.",
    },
    {
        "id": 3,
        "category": "writing",
        "turn1": "Write a short poem (4-8 lines) about the ocean at sunset.",
        "turn2": "Now rewrite the poem in a completely different style: make it humorous and modern instead of serious and classical.",
    },
    {
        "id": 4,
        "category": "reasoning",
        "turn1": "What are the main causes of climate change? Summarize in 3-4 key points.",
        "turn2": "For each cause you mentioned, propose one realistic solution that could be implemented within 5 years.",
    },
    {
        "id": 5,
        "category": "coding",
        "turn1": "Write a Python function that checks if a string is a valid palindrome, ignoring spaces and punctuation.",
        "turn2": "Now modify the function to also handle Unicode characters and add comprehensive unit tests.",
    },
    {
        "id": 6,
        "category": "reasoning",
        "turn1": "Explain how blockchain technology works in simple terms.",
        "turn2": "Based on your explanation, discuss three specific limitations of blockchain that prevent wider adoption.",
    },
    {
        "id": 7,
        "category": "writing",
        "turn1": "Write a product description for a pair of noise-canceling headphones targeted at music professionals.",
        "turn2": "Now rewrite the description targeting college students on a budget, keeping the same product but changing tone and emphasis.",
    },
    {
        "id": 8,
        "category": "reasoning",
        "turn1": "Compare and contrast democracy and authoritarianism as systems of government.",
        "turn2": "Given your comparison, argue for why a developing nation might temporarily benefit from each system. Be balanced.",
    },
    {
        "id": 9,
        "category": "coding",
        "turn1": "Explain what a binary search tree is and implement one in Python with insert and search operations.",
        "turn2": "Now add a delete operation and an in-order traversal method. Explain the tricky cases in deletion.",
    },
    {
        "id": 10,
        "category": "math",
        "turn1": "A store offers a 20% discount on all items. If you also have a coupon for an additional 15% off the discounted price, what is the total percentage discount?",
        "turn2": "Now generalize: if the first discount is x% and the second is y%, derive a formula for the total discount and prove it.",
    },
]


JUDGE_SYSTEM_PROMPT = """You are a fair and strict judge evaluating AI assistant responses in a multi-turn conversation.

Rate the response quality on a scale of 1-10 based on:
1. Helpfulness: Does it fully address the user's request?
2. Accuracy: Is the information correct?
3. Coherence: Does it properly build on the previous turn's context?
4. Quality: Is it well-organized, clear, and appropriately detailed?

For turn 2, pay special attention to whether the response correctly references and builds upon turn 1.

Output ONLY a JSON object: {"score": <int 1-10>, "reason": "<brief justification>"}"""


def generate_response(model, tokenizer, messages, device, max_new_tokens=512,
                      gate_ctx=None):
    text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    input_ids = tokenizer(text, return_tensors="pt").input_ids.to(device)

    if gate_ctx is not None:
        gate_ctx.prepare_generation(input_ids, tokenizer, max_new_tokens, device)

    with torch.no_grad():
        output = model.generate(
            input_ids,
            max_new_tokens=max_new_tokens,
            do_sample=False,
            temperature=1.0,
        )

    new_tokens = output[0][input_ids.shape[1]:]
    return tokenizer.decode(new_tokens, skip_special_tokens=True).strip()


def judge_response(judge_model, tokenizer, question, response_turn1, response_turn2, device):
    scores = {}

    for turn_label, turn_q, turn_r, context in [
        ("turn1", question["turn1"], response_turn1, ""),
        ("turn2", question["turn2"], response_turn2,
         f"[Previous Turn]\nUser: {question['turn1']}\nAssistant: {response_turn1}\n\n"),
    ]:
        judge_prompt = f"""{context}[Current Turn]
User: {turn_q}
Assistant: {turn_r}

Rate this response (1-10). Output ONLY: {{"score": <int>, "reason": "<brief>"}}"""

        messages = [
            {"role": "system", "content": JUDGE_SYSTEM_PROMPT},
            {"role": "user", "content": judge_prompt},
        ]

        judge_text = generate_response(judge_model, tokenizer, messages, device, max_new_tokens=150)

        score = parse_judge_score(judge_text)
        scores[turn_label] = score

    return scores


def parse_judge_score(text):
    json_match = re.search(r'\{[^}]*"score"\s*:\s*(\d+)[^}]*\}', text)
    if json_match:
        return int(json_match.group(1))
    num_match = re.search(r'\b(\d+)\s*/?\s*10\b', text)
    if num_match:
        return int(num_match.group(1))
    num_match = re.search(r'\b([1-9]|10)\b', text)
    if num_match:
        return int(num_match.group(1))
    return 5


def run_eval(model, tokenizer, device, model_label, gate_ctx=None):
    results = []
    for q in TEST_QUESTIONS:
        print(f"  Q{q['id']} ({q['category']})...", end=" ", flush=True)

        messages_t1 = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": q["turn1"]},
        ]
        resp_t1 = generate_response(model, tokenizer, messages_t1, device,
                                    gate_ctx=gate_ctx)

        messages_t2 = messages_t1 + [
            {"role": "assistant", "content": resp_t1},
            {"role": "user", "content": q["turn2"]},
        ]
        resp_t2 = generate_response(model, tokenizer, messages_t2, device,
                                    gate_ctx=gate_ctx)

        results.append({
            "id": q["id"],
            "category": q["category"],
            "turn1_response": resp_t1,
            "turn2_response": resp_t2,
        })
        print("done")

    return results


def main():
    parser = argparse.ArgumentParser(description="Simplified MT-Bench multi-turn evaluation")
    parser.add_argument("--checkpoint-dir", required=True)
    parser.add_argument("--gate-type", required=True, choices=["threadgate", "uniform"])
    parser.add_argument("--output-dir", default="/root/turn_residual_gating/results/")
    parser.add_argument("--model-name", default=MODEL_NAME)
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Device: {device}")
    print(f"Gate type: {args.gate_type}")

    # --- Phase 1: Generate responses with trained model (LoRA + gates) ---
    print("\nLoading trained model with gates...")
    trained_model, tokenizer, gate_ctx = load_model_with_gates(
        args.checkpoint_dir, args.gate_type, args.model_name,
    )

    print("\nGenerating responses (trained model)...")
    trained_results = run_eval(trained_model, tokenizer, device, "trained",
                               gate_ctx=gate_ctx)

    gate_ctx.cleanup()
    del trained_model
    torch.cuda.empty_cache()

    # --- Phase 2: Generate responses with baseline model ---
    print("\nLoading baseline model...")
    baseline_model = AutoModelForCausalLM.from_pretrained(
        args.model_name,
        torch_dtype=torch.bfloat16,
        device_map="auto",
    )
    baseline_model.eval()

    print("\nGenerating responses (baseline)...")
    baseline_results = run_eval(baseline_model, tokenizer, device, "baseline")

    # --- Phase 3: Judge all responses ---
    print("\nJudging responses...")
    trained_scores = []
    baseline_scores = []

    for tr, br, q in zip(trained_results, baseline_results, TEST_QUESTIONS):
        print(f"  Judging Q{q['id']}...", end=" ", flush=True)

        ts = judge_response(
            baseline_model, tokenizer, q,
            tr["turn1_response"], tr["turn2_response"], device,
        )
        tr["scores"] = ts
        trained_scores.append(ts)

        bs = judge_response(
            baseline_model, tokenizer, q,
            br["turn1_response"], br["turn2_response"], device,
        )
        br["scores"] = bs
        baseline_scores.append(bs)
        print("done")

    del baseline_model
    torch.cuda.empty_cache()

    # --- Compute summary ---
    def avg_scores(score_list):
        t1 = [s["turn1"] for s in score_list]
        t2 = [s["turn2"] for s in score_list]
        return {
            "turn1_avg": float(np.mean(t1)),
            "turn2_avg": float(np.mean(t2)),
            "overall_avg": float(np.mean(t1 + t2)),
            "turn1_scores": t1,
            "turn2_scores": t2,
        }

    trained_summary = avg_scores(trained_scores)
    baseline_summary = avg_scores(baseline_scores)

    improvement = trained_summary["overall_avg"] - baseline_summary["overall_avg"]
    t2_improvement = trained_summary["turn2_avg"] - baseline_summary["turn2_avg"]

    ckpt_name = os.path.basename(args.checkpoint_dir.rstrip("/"))

    output = {
        "checkpoint_dir": args.checkpoint_dir,
        "gate_type": args.gate_type,
        "model": args.model_name,
        "num_questions": len(TEST_QUESTIONS),
        "trained": {
            "summary": trained_summary,
            "responses": trained_results,
        },
        "baseline": {
            "summary": baseline_summary,
            "responses": baseline_results,
        },
        "improvement": {
            "overall_pp": improvement,
            "turn2_pp": t2_improvement,
        },
    }

    output_path = os.path.join(args.output_dir, f"{ckpt_name}_mtbench.json")
    with open(output_path, "w") as f:
        json.dump(output, f, indent=2)

    print(f"\n{'='*50}")
    print(f"MT-Bench Style Evaluation ({args.gate_type})")
    print(f"{'='*50}")
    print(f"                  Trained   Baseline   Diff")
    print(f"Turn 1 avg:       {trained_summary['turn1_avg']:.2f}      {baseline_summary['turn1_avg']:.2f}       {trained_summary['turn1_avg'] - baseline_summary['turn1_avg']:+.2f}")
    print(f"Turn 2 avg:       {trained_summary['turn2_avg']:.2f}      {baseline_summary['turn2_avg']:.2f}       {t2_improvement:+.2f}")
    print(f"Overall avg:      {trained_summary['overall_avg']:.2f}      {baseline_summary['overall_avg']:.2f}       {improvement:+.2f}")
    print(f"\nResults saved to {output_path}")


if __name__ == "__main__":
    main()
