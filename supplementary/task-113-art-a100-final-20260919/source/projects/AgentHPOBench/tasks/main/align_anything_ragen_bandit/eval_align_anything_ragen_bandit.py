#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
import time
from pathlib import Path

import torch
import torch.nn.functional as F


ARM_PROBS = torch.tensor([0.08, 0.16, 0.29, 0.48, 0.72, 0.91], dtype=torch.float32)
OPTIMAL_ARM = int(torch.argmax(ARM_PROBS).item())


def run_bandit(config: dict, steps: int, seed: int) -> dict:
    gen = torch.Generator().manual_seed(seed)
    logits = torch.zeros(len(ARM_PROBS), dtype=torch.float32, requires_grad=True)
    opt_name = str(config.get("optimizer", "adam")).lower()
    lr = float(config.get("learning_rate", 0.03))
    if opt_name == "sgd":
        optimizer = torch.optim.SGD([logits], lr=lr)
    else:
        optimizer = torch.optim.Adam([logits], lr=lr)

    batch_size = int(config.get("batch_size", 32))
    entropy_coef = float(config.get("entropy_coef", 0.01))
    temperature = max(float(config.get("temperature", 1.0)), 1e-4)
    baseline_mode = str(config.get("reward_baseline", "ema")).lower()
    ema = 0.0
    history = []

    for step in range(int(steps)):
        dist = torch.distributions.Categorical(logits=logits / temperature)
        actions = dist.sample((batch_size,))
        probs = ARM_PROBS[actions]
        rewards = torch.bernoulli(probs, generator=gen)
        if baseline_mode == "mean":
            baseline = rewards.mean()
        elif baseline_mode == "ema":
            batch_mean = float(rewards.mean().item())
            ema = 0.9 * ema + 0.1 * batch_mean if step else batch_mean
            baseline = torch.tensor(ema)
        else:
            baseline = torch.tensor(0.0)
        advantage = rewards - baseline
        log_prob = dist.log_prob(actions)
        entropy = dist.entropy()
        loss = -(advantage.detach() * log_prob).mean() - entropy_coef * entropy
        optimizer.zero_grad(set_to_none=True)
        loss.backward()
        optimizer.step()
        with torch.no_grad():
            policy = F.softmax(logits / temperature, dim=0)
            history.append(
                {
                    "step": step + 1,
                    "train_reward": float(rewards.mean().item()),
                    "optimal_prob": float(policy[OPTIMAL_ARM].item()),
                    "chosen_arm": int(torch.argmax(policy).item()),
                    "loss": float(loss.detach().item()),
                }
            )

    with torch.no_grad():
        policy = F.softmax(logits / temperature, dim=0)
        chosen_arm = int(torch.argmax(policy).item())
        # Interpret success rate as the probability that a rollout selects the
        # optimal arm, matching stochastic bandit evaluation rather than greedy
        # argmax, which can saturate on tiny logit differences.
        success_rate = float(policy[OPTIMAL_ARM].item())
        expected_reward = float((policy * ARM_PROBS).sum().item())
        optimal_prob = float(policy[OPTIMAL_ARM].item())

    return {
        "success_rate": success_rate,
        "optimal_arm_probability": optimal_prob,
        "expected_reward": expected_reward,
        "chosen_arm": chosen_arm,
        "optimal_arm": OPTIMAL_ARM,
        "policy": [float(x) for x in policy.tolist()],
        "history": history,
        "config": config,
        "steps": int(steps),
        "seed": int(seed),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--results-dir", required=True)
    parser.add_argument("--learning-rate", type=float, default=0.03)
    parser.add_argument("--batch-size", type=int, default=32)
    parser.add_argument("--entropy-coef", type=float, default=0.01)
    parser.add_argument("--temperature", type=float, default=1.0)
    parser.add_argument("--reward-baseline", choices=["none", "mean", "ema"], default="ema")
    parser.add_argument("--optimizer", choices=["adam", "sgd"], default="adam")
    parser.add_argument("--steps", type=int, default=20)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    config = {
        "learning_rate": args.learning_rate,
        "batch_size": args.batch_size,
        "entropy_coef": args.entropy_coef,
        "temperature": args.temperature,
        "reward_baseline": args.reward_baseline,
        "optimizer": args.optimizer,
    }
    started = time.time()
    result = run_bandit(config, args.steps, args.seed)
    result["seconds"] = round(time.time() - started, 3)
    out_dir = Path(args.results_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "results.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print("RESULT_JSON " + json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
