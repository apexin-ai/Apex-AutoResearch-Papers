# Phase 1 GAR 诊断：测量 Qwen2.5-7B-Instruct 多轮对话中 GAR 跨 turn 衰减
# 输入：无（内置 5 段 10-turn 多轮对话）
# 输出：phase1_gar_results.json + phase1_gar_curve.png
# 用法：python run_phase1_gar.py [--results-dir /path/to/results]

import argparse
import json
import os
import sys
import torch
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from transformers import AutoModelForCausalLM, AutoTokenizer

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gar import GARMeasurer
from turn_utils import detect_turn_boundaries


SYSTEM_PROMPTS = [
    "You are a knowledgeable science tutor. Always explain concepts step by step. Use analogies when possible. Never give direct answers without explanation. If the student makes an error, gently correct them and guide them to the right answer.",
    "You are a professional code reviewer. Focus on code quality, security, and performance. Point out potential bugs and suggest improvements. Always explain why a change is needed, not just what to change. Be constructive and specific.",
    "You are a creative writing coach. Help users improve their storytelling skills. Focus on character development, plot structure, and vivid descriptions. Give specific feedback with examples. Encourage experimentation with different styles.",
    "You are a math problem solver. Show all steps clearly. Explain the reasoning behind each step. If there are multiple approaches, mention them. Check your work by verifying the answer. Use LaTeX notation for formulas.",
    "You are a debate coach who helps users argue both sides of issues. Present balanced perspectives. Challenge weak arguments constructively. Teach logical reasoning and evidence evaluation. Avoid personal opinions.",
]

CONVERSATIONS = [
    ["Why is the sky blue?", "What about sunsets being red?", "How does a rainbow form?",
     "Why do stars twinkle?", "What causes thunder?", "How do magnets work?",
     "Why is water wet?", "What is gravity?", "How do airplanes fly?", "Why is space dark?"],
    ["Review this: def add(a,b): return a+b", "What about error handling?", "How should I write tests for it?",
     "Is recursion better than iteration?", "When should I use async/await?", "How to handle memory leaks?",
     "Best practices for API design?", "How to optimize database queries?", "When to use microservices?", "How to handle rate limiting?"],
    ["Help me start a mystery story", "How do I create a compelling villain?", "What makes good dialogue?",
     "How to build suspense?", "Should I use first or third person?", "How to write a plot twist?",
     "Tips for describing settings?", "How to end a chapter with a cliffhanger?", "How to avoid cliches?", "How to write an epilogue?"],
    ["Solve: 3x + 7 = 22", "What is the derivative of x^3?", "Explain the Pythagorean theorem",
     "What is a prime number?", "How to calculate compound interest?", "What is the area of a circle?",
     "Explain matrix multiplication", "What is a logarithm?", "How to solve quadratic equations?", "What is calculus used for?"],
    ["Should AI be regulated?", "Is remote work better than office work?", "Should college be free?",
     "Is social media harmful?", "Should voting be mandatory?", "Is nuclear energy safe?",
     "Should animals have legal rights?", "Is space exploration worth the cost?", "Should there be a universal basic income?", "Is genetic engineering ethical?"],
]


def build_conversation(tokenizer, model, system_prompt, user_questions, device, max_new_tokens=100):
    messages = [{"role": "system", "content": system_prompt}]

    for q in user_questions:
        messages.append({"role": "user", "content": q})
        text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        input_ids = tokenizer(text, return_tensors="pt").input_ids.to(device)

        if input_ids.shape[1] > 1800:
            messages.pop()
            break

        with torch.no_grad():
            output = model.generate(input_ids, max_new_tokens=max_new_tokens, do_sample=False)

        new_tokens = output[0][input_ids.shape[1]:]
        response = tokenizer.decode(new_tokens, skip_special_tokens=True).strip()
        messages.append({"role": "assistant", "content": response})

    return messages


def measure_gar_per_turn(model, tokenizer, measurer, messages, device):
    full_text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=False)
    input_ids = tokenizer(full_text, return_tensors="pt").input_ids.squeeze(0)

    if input_ids.shape[0] > 2048:
        input_ids = input_ids[:2048]

    boundaries = detect_turn_boundaries(input_ids, tokenizer)
    goal_positions = boundaries["goal_token_positions"]

    if not goal_positions:
        return None

    assistant_positions = boundaries["assistant_last_token_positions"]
    if not assistant_positions:
        return None

    input_ids_batch = input_ids.unsqueeze(0).to(device)

    with measurer.measure():
        with torch.no_grad():
            model(input_ids_batch, output_attentions=True)

    gar_per_turn = []
    for pos in assistant_positions:
        result = measurer.compute_gar(goal_positions, [pos])
        gar_per_turn.append(result["mean_gar"])

    return gar_per_turn


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--results-dir", default="./results")
    parser.add_argument("--model-name", default="Qwen/Qwen2.5-7B-Instruct")
    args = parser.parse_args()

    os.makedirs(args.results_dir, exist_ok=True)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Device: {device}")

    tokenizer = AutoTokenizer.from_pretrained(args.model_name)
    model = AutoModelForCausalLM.from_pretrained(
        args.model_name,
        torch_dtype=torch.bfloat16,
        device_map="auto",
        attn_implementation="eager",
    )
    model.eval()

    measurer = GARMeasurer(model)

    all_gar_curves = []

    for i, (sys_prompt, user_qs) in enumerate(zip(SYSTEM_PROMPTS, CONVERSATIONS)):
        print(f"\nConversation {i+1}/{len(SYSTEM_PROMPTS)}: {sys_prompt[:50]}...")

        messages = build_conversation(tokenizer, model, sys_prompt, user_qs, device)
        num_turns = sum(1 for m in messages if m["role"] == "assistant")
        print(f"  Generated {num_turns} assistant turns")

        gar_curve = measure_gar_per_turn(model, tokenizer, measurer, messages, device)

        if gar_curve:
            print(f"  GAR per turn: {[f'{g:.4f}' for g in gar_curve]}")
            all_gar_curves.append(gar_curve)
        else:
            print(f"  WARNING: Could not measure GAR for this conversation")

    if not all_gar_curves:
        print("ERROR: No valid GAR measurements")
        return

    min_turns = min(len(c) for c in all_gar_curves)
    aligned = [c[:min_turns] for c in all_gar_curves]
    avg_gar = np.mean(aligned, axis=0).tolist()

    turn1_gar = avg_gar[0]
    mid_turns_gar = np.mean(avg_gar[2:8]) if len(avg_gar) >= 8 else np.mean(avg_gar[2:])
    relative_drop = (turn1_gar - mid_turns_gar) / turn1_gar if turn1_gar > 0 else 0

    passed = relative_drop >= 0.15

    results = {
        "model": args.model_name,
        "num_conversations": len(all_gar_curves),
        "num_turns": min_turns,
        "gar_curves": all_gar_curves,
        "avg_gar_per_turn": avg_gar,
        "turn1_avg_gar": turn1_gar,
        "mid_turns_avg_gar": float(mid_turns_gar),
        "relative_drop": float(relative_drop),
        "pass": passed,
    }

    results_path = os.path.join(args.results_dir, "phase1_gar_results.json")
    with open(results_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {results_path}")

    fig, ax = plt.subplots(figsize=(8, 5))
    turns_x = list(range(1, min_turns + 1))

    for i, curve in enumerate(aligned):
        ax.plot(turns_x, curve, alpha=0.3, linewidth=1, label=f"Conv {i+1}" if i < 5 else None)

    ax.plot(turns_x, avg_gar, "b-o", linewidth=2.5, markersize=6, label="Average", zorder=10)

    ax.axhline(y=turn1_gar, color="green", linestyle="--", alpha=0.5, label=f"Turn 1: {turn1_gar:.3f}")
    ax.axhline(y=float(mid_turns_gar), color="red", linestyle="--", alpha=0.5, label=f"Mid (3-8): {float(mid_turns_gar):.3f}")

    ax.set_xlabel("Turn Index", fontsize=12)
    ax.set_ylabel("GAR (Goal Attention Ratio)", fontsize=12)
    ax.set_title(
        f"GAR vs Turn Index — {args.model_name.split('/')[-1]}\n"
        f"Relative Drop: {relative_drop*100:.1f}% ({'PASS' if passed else 'FAIL'}: threshold 15%)",
        fontsize=11,
    )
    ax.legend(fontsize=9)
    ax.set_xticks(turns_x)
    ax.grid(True, alpha=0.3)

    fig_path = os.path.join(args.results_dir, "phase1_gar_curve.png")
    fig.savefig(fig_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Plot saved to {fig_path}")

    print(f"\n{'='*50}")
    print(f"Phase 1 GAR Diagnostic Results")
    print(f"{'='*50}")
    print(f"Turn 1 avg GAR:        {turn1_gar:.4f}")
    print(f"Mid-turns (3-8) avg:   {float(mid_turns_gar):.4f}")
    print(f"Relative drop:         {relative_drop*100:.1f}%")
    print(f"Pass criteria (>=15%): {'PASS' if passed else 'FAIL'}")


if __name__ == "__main__":
    main()
