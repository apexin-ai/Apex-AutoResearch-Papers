"""Crafter episode runner: random / deterministic / LLM strategies."""
import argparse
import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
from crafter_text_wrapper import CrafterTextWrapper, ACTIONS


def run_random(env, max_steps):
    text_obs, info = env.reset()
    total_reward = 0.0
    died = False
    for step in range(max_steps):
        action = np.random.randint(0, 17)
        text_obs, reward, done, info = env.step(action)
        total_reward += reward
        if done:
            died = info.get("dead", False)
            break
    return {
        "steps": step + 1,
        "reward": total_reward,
        "died": died,
        "health": info["inventory"]["health"],
        "achievements": sum(1 for v in info.get("achievements", {}).values() if v > 0),
    }


def run_deterministic(env, max_steps):
    from crafter_det_agent import CrafterDetAgent
    agent = CrafterDetAgent()
    text_obs, info = env.reset()
    total_reward = 0.0
    died = False
    for step in range(max_steps):
        action = agent.act(info)
        text_obs, reward, done, info = env.step(action)
        total_reward += reward
        if done:
            died = info.get("dead", False)
            break
    return {
        "steps": step + 1,
        "reward": total_reward,
        "died": died,
        "health": info["inventory"]["health"],
        "achievements": sum(1 for v in info.get("achievements", {}).values() if v > 0),
    }


def run_llm(env, max_steps, api_base, model):
    from openai import OpenAI
    client = OpenAI(base_url=api_base, api_key="[REDACTED]")

    action_list = ", ".join(a.lower().replace(" ", "_") for a in ACTIONS)
    system_msg = (
        "You are playing Crafter, a survival game. Manage health, food, drink, "
        "and energy while avoiding monsters. Choose the best action to survive.\n"
        f"Valid actions: {action_list}\n"
        "Reply with ONLY the action name, nothing else."
    )

    text_obs, info = env.reset()
    total_reward = 0.0
    died = False
    parse_ok = 0
    parse_total = 0
    latencies = []

    for step in range(max_steps):
        parse_total += 1
        t0 = time.time()
        try:
            resp = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": system_msg},
                    {"role": "user", "content": text_obs},
                ],
                temperature=0.3,
                max_tokens=20,
            )
            raw = resp.choices[0].message.content.strip()
            latencies.append(time.time() - t0)
        except Exception as e:
            raw = "noop"
            latencies.append(time.time() - t0)

        action_idx = env._parse_action(raw)
        if action_idx > 0 or raw.lower().strip() in ("noop", "no_op"):
            parse_ok += 1

        text_obs, reward, done, info = env.step(action_idx)
        total_reward += reward
        if done:
            died = info.get("dead", False)
            break

    return {
        "steps": step + 1,
        "reward": total_reward,
        "died": died,
        "health": info["inventory"]["health"],
        "achievements": sum(1 for v in info.get("achievements", {}).values() if v > 0),
        "parse_success_rate": parse_ok / max(parse_total, 1),
        "avg_latency_ms": np.mean(latencies) * 1000 if latencies else 0,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--strategy", choices=["random", "deterministic", "llm"], required=True)
    parser.add_argument("--episodes", type=int, default=5)
    parser.add_argument("--max-steps", type=int, default=300)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--output", type=str, default=None)
    parser.add_argument("--api-base", type=str, default="http://localhost:8000/v1")
    parser.add_argument("--model", type=str, default="/root/autodl-tmp/models/Qwen2.5-7B-Instruct/")
    args = parser.parse_args()

    results = []
    for ep in range(args.episodes):
        seed = args.seed + ep
        np.random.seed(seed)
        env = CrafterTextWrapper(seed=seed)

        print(f"[{args.strategy}] Episode {ep+1}/{args.episodes} (seed={seed})...", end=" ", flush=True)

        if args.strategy == "random":
            res = run_random(env, args.max_steps)
        elif args.strategy == "deterministic":
            res = run_deterministic(env, args.max_steps)
        elif args.strategy == "llm":
            res = run_llm(env, args.max_steps, args.api_base, args.model)

        res["seed"] = seed
        res["episode"] = ep + 1
        results.append(res)
        status = "DIED" if res["died"] else "ALIVE"
        print(f"{status} steps={res['steps']} reward={res['reward']:.1f} hp={res['health']} achv={res['achievements']}")

    # Summary
    deaths = sum(1 for r in results if r["died"])
    dr = deaths / len(results) * 100
    avg_steps = np.mean([r["steps"] for r in results])
    avg_reward = np.mean([r["reward"] for r in results])
    avg_achv = np.mean([r["achievements"] for r in results])

    print(f"\n=== {args.strategy.upper()} SUMMARY ({len(results)} episodes) ===")
    print(f"Death Rate: {dr:.0f}% ({deaths}/{len(results)})")
    print(f"Avg Steps: {avg_steps:.1f}")
    print(f"Avg Reward: {avg_reward:.2f}")
    print(f"Avg Achievements: {avg_achv:.1f}")

    if args.strategy == "llm":
        avg_parse = np.mean([r.get("parse_success_rate", 0) for r in results]) * 100
        avg_lat = np.mean([r.get("avg_latency_ms", 0) for r in results])
        print(f"Parse Success Rate: {avg_parse:.0f}%")
        print(f"Avg Latency: {avg_lat:.0f}ms/call")

    print(f"Per-episode: {[('DIED' if r['died'] else 'ALIVE', r['steps'], r['reward']) for r in results]}")

    if args.output:
        os.makedirs(os.path.dirname(args.output), exist_ok=True)
        with open(args.output, "w") as f:
            for r in results:
                f.write(json.dumps(r) + "\n")
        print(f"Results saved to {args.output}")

    return results


if __name__ == "__main__":
    main()
