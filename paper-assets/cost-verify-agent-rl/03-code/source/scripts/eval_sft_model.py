#!/usr/bin/env python3
"""Evaluate SFT model on ALFWorld: action_is_valid, success_rate, format correctness."""

import argparse
import json
import os
import re
import sys
import time
from collections import defaultdict

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "RAGEN"))
from ragen.env.alfworld.env import AlfredTXTEnv
from ragen.env.alfworld.config import AlfredEnvConfig

SYSTEM_PROMPT = (
    "You're a helpful assistant. You are an expert agent in the ALFRED Embodied Environment.\n"
    "Complete household tasks by navigating and interacting with objects.\n\n"
    "Before each action, you MUST first produce a self-guidance assessment:\n"
    "[Assessment: positive/neutral/negative] - evaluate your current progress.\n"
    "[Reasoning: one sentence analyzing what has been accomplished and what remains.]\n"
    "[Suggestion: the best next action from admissible actions.]\n\n"
    "Your reasoning with self-guidance MUST be enclosed within <think> </think> tags.\n"
    "Then choose an admissible action and present it within <answer>...</answer> tags."
)

SIMPLE_CHATML = (
    "{% for message in messages %}"
    "{{'<|im_start|>' + message['role'] + '\\n' + message['content'] + '<|im_end|>' + '\\n'}}"
    "{% endfor %}"
    "{% if add_generation_prompt %}"
    "{{'<|im_start|>assistant\\n'}}"
    "{% endif %}"
)


def parse_action(response: str):
    """Parse action from model response. Returns (action, has_think, has_answer)."""
    has_think = bool(re.search(r"<think>.*?</think>", response, re.DOTALL))

    m = re.search(r"<think>.*?</think>\s*<answer>(.*?)</answer>", response, re.DOTALL)
    if m:
        return m.group(1).strip(), has_think, True

    # Fallback: bare text after </think>
    m = re.search(r"</think>\s*(.*)", response, re.DOTALL)
    if m:
        action = m.group(1).strip().split("\n")[0].strip()
        for tok in ["<|im_end|>", "<|endoftext|>"]:
            action = action.replace(tok, "").strip()
        if action:
            return action, has_think, False

    return "", has_think, False


def run_episode(model, tokenizer, env, max_steps=50, temperature=0.4, max_new_tokens=512):
    """Run a single episode. Returns per-step metrics."""
    obs = env.reset(seed=int(time.time() * 1000) % (2**31), mode="val")
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": obs},
    ]

    steps = []
    done = False

    for step_i in range(max_steps):
        text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        inputs = tokenizer(text, return_tensors="pt").to(model.device)
        input_len = inputs["input_ids"].shape[1]

        with torch.no_grad():
            out = model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                temperature=temperature,
                do_sample=temperature > 0,
                top_p=0.95,
                pad_token_id=tokenizer.pad_token_id or tokenizer.eos_token_id,
            )

        response = tokenizer.decode(out[0][input_len:], skip_special_tokens=False)
        # Strip trailing special tokens for parsing
        clean_response = response.replace("<|im_end|>", "").replace("<|endoftext|>", "").strip()

        action, has_think, has_answer = parse_action(clean_response)
        format_ok = has_think and (has_answer or bool(action))

        action_is_valid = action in env.available_actions if action else False

        step_info = {
            "step": step_i,
            "action": action,
            "has_think": has_think,
            "has_answer": has_answer,
            "format_ok": format_ok,
            "action_is_valid": action_is_valid,
        }

        if not action:
            step_info["success"] = False
            step_info["done"] = True
            steps.append(step_info)
            break

        obs, reward, done, info = env.step(action)
        step_info["reward"] = reward
        step_info["success"] = info.get("success", False)
        step_info["done"] = done
        steps.append(step_info)

        if done:
            break

        messages.append({"role": "assistant", "content": clean_response})
        messages.append({"role": "user", "content": obs})

    return steps


def main():
    parser = argparse.ArgumentParser(description="Evaluate SFT model on ALFWorld")
    parser.add_argument("--model_path", default="/root/autodl-tmp/checkpoints/exp008_sft/final")
    parser.add_argument("--num_episodes", type=int, default=50)
    parser.add_argument("--max_steps", type=int, default=50)
    parser.add_argument("--temperature", type=float, default=0.4)
    parser.add_argument("--output", default=None, help="Save results JSON to this path")
    args = parser.parse_args()

    if not os.path.exists(args.model_path):
        print(f"ERROR: Model path not found: {args.model_path}")
        sys.exit(1)

    print(f"Loading model from {args.model_path} ...")
    tokenizer = AutoTokenizer.from_pretrained(args.model_path)
    tokenizer.chat_template = SIMPLE_CHATML
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(
        args.model_path,
        dtype=torch.bfloat16,
        attn_implementation="sdpa",
        device_map="cuda",
    )
    model.eval()
    print(f"Model loaded on {model.device}")

    os.environ["ALFWORLD_DATA"] = os.path.expanduser("~/.cache/alfworld")
    ragen_root = os.path.join(os.path.dirname(__file__), "..", "RAGEN")
    alfworld_cfg = os.path.join(ragen_root, "ragen", "env", "alfworld", "alfworld_config.yaml")
    env_config = AlfredEnvConfig(config_file=alfworld_cfg, eval_dataset="eval_in_distribution")
    env = AlfredTXTEnv(config=env_config, mode="val")
    print(f"ALFWorld env initialized, {env.num_games} games available")

    ep_results = []
    for ep_i in range(args.num_episodes):
        steps = run_episode(model, tokenizer, env, max_steps=args.max_steps, temperature=args.temperature)

        total_steps = len(steps)
        valid_actions = sum(1 for s in steps if s["action_is_valid"])
        format_ok = sum(1 for s in steps if s["format_ok"])
        success = any(s.get("success", False) for s in steps)

        ep_results.append({
            "episode": ep_i,
            "total_steps": total_steps,
            "valid_actions": valid_actions,
            "format_ok": format_ok,
            "success": success,
            "action_is_valid_rate": valid_actions / total_steps if total_steps > 0 else 0,
            "format_ok_rate": format_ok / total_steps if total_steps > 0 else 0,
        })

        print(
            f"  EP {ep_i:3d}/{args.num_episodes}: "
            f"steps={total_steps:2d}  "
            f"valid={valid_actions}/{total_steps} ({ep_results[-1]['action_is_valid_rate']:.1%})  "
            f"format={format_ok}/{total_steps} ({ep_results[-1]['format_ok_rate']:.1%})  "
            f"success={'Y' if success else 'N'}"
        )

    # Aggregate
    n = len(ep_results)
    avg_valid = sum(r["action_is_valid_rate"] for r in ep_results) / n
    avg_format = sum(r["format_ok_rate"] for r in ep_results) / n
    success_rate = sum(1 for r in ep_results if r["success"]) / n
    avg_steps = sum(r["total_steps"] for r in ep_results) / n

    print("\n" + "=" * 60)
    print(f"RESULTS ({n} episodes)")
    print("=" * 60)
    print(f"  action_is_valid rate : {avg_valid:.1%}")
    print(f"  format_ok rate      : {avg_format:.1%}")
    print(f"  success_rate        : {success_rate:.1%}")
    print(f"  avg_steps/episode   : {avg_steps:.1f}")
    print("=" * 60)

    summary = {
        "model_path": args.model_path,
        "num_episodes": n,
        "temperature": args.temperature,
        "action_is_valid_rate": round(avg_valid, 4),
        "format_ok_rate": round(avg_format, 4),
        "success_rate": round(success_rate, 4),
        "avg_steps": round(avg_steps, 1),
        "episodes": ep_results,
    }

    if args.output:
        os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
        with open(args.output, "w") as f:
            json.dump(summary, f, indent=2)
        print(f"Results saved to {args.output}")

    env.close()


if __name__ == "__main__":
    main()
