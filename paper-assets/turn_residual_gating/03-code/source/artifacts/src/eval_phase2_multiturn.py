# eval_phase2_multiturn.py — 多轮指令遵循评估 (5-10 turn)
# 用法: python eval_phase2_multiturn.py --checkpoint-dir /root/turn_residual_gating/checkpoints/tg_s42 --gate-type threadgate
# 输出: JSON 评分结果，关键指标 instruction_retention_ratio

import argparse
import json
import os
import re
import sys

import torch
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config import MODEL_NAME
from model_loader import load_model_with_gates


SCENARIOS = [
    {
        "name": "format_constraint",
        "system_prompt": "Always respond in exactly 3 bullet points. Never use more or fewer.",
        "turns": [
            "What are the benefits of regular exercise?",
            "How does photosynthesis work?",
            "What makes a good leader?",
            "Describe the water cycle.",
            "Remember your format rules. What is quantum computing?",
            "List the reasons for learning a second language.",
            "What are the causes of inflation?",
            "Explain how vaccines work.",
        ],
        "score_fn": "format_3_bullets",
    },
    {
        "name": "ending_constraint",
        "system_prompt": "Always end your response with 'END OF RESPONSE'",
        "turns": [
            "What is machine learning?",
            "How do solar panels generate electricity?",
            "What causes earthquakes?",
            "Explain the concept of supply and demand.",
            "What is the difference between DNA and RNA?",
            "How does the internet work?",
            "What are black holes?",
            "Explain how airplanes stay in the air.",
        ],
        "score_fn": "ends_with_marker",
    },
    {
        "name": "role_constraint",
        "system_prompt": "You are a pirate. Always talk like a pirate using pirate vocabulary.",
        "turns": [
            "Tell me about yourself.",
            "What's your favorite food?",
            "How do you spend your weekends?",
            "What's the weather like today?",
            "Explain how a computer processor works.",
            "What is the theory of relativity?",
            "How do databases store information?",
            "Explain the concept of machine learning algorithms.",
        ],
        "score_fn": "pirate_keywords",
    },
    {
        "name": "prohibition_constraint",
        "system_prompt": "Never use the word 'however' in your responses.",
        "turns": [
            "Compare cats and dogs as pets.",
            "What are the pros and cons of remote work?",
            "Is renewable energy better than fossil fuels?",
            "Compare democracy and authoritarianism.",
            "What are the advantages and disadvantages of social media?",
            "Compare online and traditional education.",
            "Is artificial intelligence a threat or an opportunity?",
            "Compare urban and rural living.",
        ],
        "score_fn": "no_however",
    },
    {
        "name": "topic_constraint",
        "system_prompt": "When asked about any topic, always mention how it relates to climate change.",
        "turns": [
            "Tell me about ocean acidification.",
            "How do forests affect the atmosphere?",
            "What is the greenhouse effect?",
            "How does transportation affect the environment?",
            "Explain how prime numbers work.",
            "What is the best recipe for chocolate cake?",
            "How does the stock market work?",
            "Tell me about the history of chess.",
        ],
        "score_fn": "mentions_climate",
    },
]


def score_format_3_bullets(response):
    lines = [l.strip() for l in response.strip().split("\n") if l.strip()]
    bullet_lines = [l for l in lines if re.match(r"^[-•*]\s", l)]
    return 1 if len(bullet_lines) == 3 else 0


def score_ends_with_marker(response):
    return 1 if response.strip().endswith("END OF RESPONSE") else 0


def score_pirate_keywords(response):
    keywords = [
        "ahoy", "matey", "arr", "ye ", " ye,", " ye.", "sailor", "ship",
        "sea", "treasure", "captain", "plank", "pirate", "aye", "landlubber",
        "booty", "crew", "sail", "anchor", "yo ho",
    ]
    text = response.lower()
    return 1 if any(kw in text for kw in keywords) else 0


def score_no_however(response):
    return 0 if "however" in response.lower() else 1


def score_mentions_climate(response):
    keywords = [
        "climate", "environment", "carbon", "warming", "emission",
        "greenhouse", "temperature", "fossil", "renewable", "sustainability",
        "pollution", "ecological",
    ]
    text = response.lower()
    return 1 if any(kw in text for kw in keywords) else 0


SCORE_FNS = {
    "format_3_bullets": score_format_3_bullets,
    "ends_with_marker": score_ends_with_marker,
    "pirate_keywords": score_pirate_keywords,
    "no_however": score_no_however,
    "mentions_climate": score_mentions_climate,
}


def generate_response(model, tokenizer, messages, device, gate_ctx=None,
                      max_new_tokens=256):
    text = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True,
    )
    input_ids = tokenizer(text, return_tensors="pt").input_ids.to(device)

    if gate_ctx is not None:
        gate_ctx.prepare_generation(input_ids, tokenizer, max_new_tokens, device)

    with torch.no_grad():
        output = model.generate(
            input_ids,
            max_new_tokens=max_new_tokens,
            do_sample=False,
        )

    new_tokens = output[0][input_ids.shape[1]:]
    return tokenizer.decode(new_tokens, skip_special_tokens=True).strip()


def run_scenario(model, tokenizer, device, scenario, gate_ctx=None):
    score_fn = SCORE_FNS[scenario["score_fn"]]
    system_prompt = scenario["system_prompt"]

    messages = [{"role": "system", "content": system_prompt}]
    scores = []
    turn_responses = []

    for turn_text in scenario["turns"]:
        messages.append({"role": "user", "content": turn_text})
        response = generate_response(
            model, tokenizer, messages, device, gate_ctx=gate_ctx,
        )
        messages.append({"role": "assistant", "content": response})

        score = score_fn(response)
        scores.append(score)
        turn_responses.append({
            "user": turn_text,
            "assistant": response,
            "score": score,
        })

    num_turns = len(scores)
    early_end = min(4, num_turns)
    early_scores = scores[:early_end]
    late_scores = scores[early_end:]

    early_acc = float(np.mean(early_scores)) if early_scores else 0.0
    late_acc = float(np.mean(late_scores)) if late_scores else 0.0

    return {
        "name": scenario["name"],
        "system_prompt": system_prompt,
        "turns": turn_responses,
        "scores_per_turn": scores,
        "early_turn_accuracy": early_acc,
        "late_turn_accuracy": late_acc,
    }


def main():
    parser = argparse.ArgumentParser(
        description="Multi-turn instruction following evaluation",
    )
    parser.add_argument("--checkpoint-dir", required=True)
    parser.add_argument("--gate-type", required=True,
                        choices=["threadgate", "uniform", "baseline"])
    parser.add_argument("--output-dir",
                        default="/root/turn_residual_gating/results/")
    parser.add_argument("--model-name", default=MODEL_NAME)
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Device: {device}")
    print(f"Gate type: {args.gate_type}")

    print("\nLoading model...")
    model, tokenizer, gate_ctx = load_model_with_gates(
        args.checkpoint_dir, args.gate_type, args.model_name,
    )

    print("\nRunning scenarios...")
    scenario_results = []
    for i, scenario in enumerate(SCENARIOS):
        print(f"  Scenario {i+1}/{len(SCENARIOS)}: {scenario['name']}...")
        result = run_scenario(model, tokenizer, device, scenario,
                              gate_ctx=gate_ctx)
        scenario_results.append(result)
        print(f"    early={result['early_turn_accuracy']:.2f}  "
              f"late={result['late_turn_accuracy']:.2f}")

    gate_ctx.cleanup()

    all_early = [s["early_turn_accuracy"] for s in scenario_results]
    all_late = [s["late_turn_accuracy"] for s in scenario_results]
    overall_early = float(np.mean(all_early))
    overall_late = float(np.mean(all_late))
    retention = overall_late / overall_early if overall_early > 0 else 0.0

    ckpt_name = os.path.basename(args.checkpoint_dir.rstrip("/"))
    output = {
        "checkpoint_dir": args.checkpoint_dir,
        "gate_type": args.gate_type,
        "model": args.model_name,
        "scenarios": scenario_results,
        "overall_early_accuracy": overall_early,
        "overall_late_accuracy": overall_late,
        "instruction_retention_ratio": retention,
    }

    output_path = os.path.join(args.output_dir, f"{ckpt_name}_multiturn.json")
    with open(output_path, "w") as f:
        json.dump(output, f, indent=2)

    print(f"\n{'='*50}")
    print(f"Multi-turn Instruction Following ({args.gate_type})")
    print(f"{'='*50}")
    for s in scenario_results:
        print(f"  {s['name']:25s}  early={s['early_turn_accuracy']:.2f}  "
              f"late={s['late_turn_accuracy']:.2f}")
    print(f"\nOverall early accuracy:  {overall_early:.2f}")
    print(f"Overall late accuracy:   {overall_late:.2f}")
    print(f"Retention ratio:         {retention:.2f}")
    print(f"\nResults saved to {output_path}")


if __name__ == "__main__":
    main()
