# Plan-003 trained-router eval using ablation-b implicit router (generative SFT).
#
# Replaces the classification-head TrainedRouter with ablation-b's generative
# Qwen3-1.7B + LoRA. For each step, generates text; if output starts with
# [SIMULATE] → route=deterministic, else → route=internal. Episode-level
# decision via majority vote over step predictions.
#
# Inputs:
#   --data_dir:  plan_c results directory (same as eval_end_to_end.py)
#   --adapter_dir: path to ablation-b LoRA adapter (checkpoints/plan-004-implicit/final_adapter)
#   --base_model: Qwen3-1.7B local path
#
# Outputs (--output_dir):
#   implicit_router_results.json — metrics with bootstrap 90% CI
#   implicit_router_episodes.jsonl — per-episode routing decisions
#   implicit_router_steps.jsonl — per-step generation details
#
# Dependencies: torch, transformers, peft, numpy

import argparse
import json
import os
import re
import sys
import time
from collections import Counter, defaultdict
from typing import Any, Dict, List, Optional, Tuple

import numpy as np
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

DEATH_SCORE = -100.0

IMPLICIT_SYSTEM_PROMPT = (
    "You are an agent in a ScienceWorld text environment. "
    "Given the current observation and action history, choose the next action. "
    "If you believe a deterministic simulation would produce a better outcome, "
    "prefix your action with [SIMULATE]. Otherwise, output the action directly."
)

RAW_LABEL_MAP = {
    "internal-preferred": "internal",
    "det-preferred": "deterministic",
    "no-preference": None,
}


def load_episodes(data_dir: str) -> List[Dict[str, Any]]:
    episodes = []
    for task_dir_name in sorted(os.listdir(data_dir)):
        task_path = os.path.join(data_dir, task_dir_name)
        if not os.path.isdir(task_path):
            continue
        summary_path = os.path.join(task_path, "episode_summary.jsonl")
        episodes_path = os.path.join(task_path, "episodes.jsonl")
        if not os.path.exists(summary_path) and not os.path.exists(episodes_path):
            continue
        if os.path.exists(summary_path):
            with open(summary_path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    rec = json.loads(line)
                    episodes.append({
                        "task_type": task_dir_name,
                        "episode_idx": rec.get("episode", rec.get("episode_idx", 0)),
                        "variation_idx": rec.get("variation", rec.get("variation_idx", 0)),
                        "internal_final": float(rec.get("internal_final", 0)),
                        "det_final": float(rec.get("det_final", 0)),
                        "internal_steps": int(rec.get("internal_steps", 0)),
                        "det_steps": int(rec.get("det_steps", 0)),
                        "label": rec.get("label", "no-preference"),
                    })
        elif os.path.exists(episodes_path):
            with open(episodes_path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    rec = json.loads(line)
                    ai = rec.get("always_internal", {})
                    ad = rec.get("always_deterministic", {})
                    episodes.append({
                        "task_type": task_dir_name,
                        "episode_idx": rec.get("episode_idx", 0),
                        "variation_idx": rec.get("variation_idx", 0),
                        "internal_final": float(ai.get("final_score", 0)),
                        "det_final": float(ad.get("final_score", 0)),
                        "internal_steps": int(ai.get("num_steps", 0)),
                        "det_steps": int(ad.get("num_steps", 0)),
                        "label": "no-preference",
                    })
    return episodes


def load_labeled_steps(data_dir: str) -> Dict[str, List[Dict]]:
    step_map: Dict[str, List[Dict]] = defaultdict(list)
    for task_dir_name in sorted(os.listdir(data_dir)):
        task_path = os.path.join(data_dir, task_dir_name)
        steps_path = os.path.join(task_path, "labeled_steps.jsonl")
        if not os.path.exists(steps_path):
            continue
        with open(steps_path) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                rec = json.loads(line)
                key = f"{rec.get('task_type', task_dir_name)}:{rec.get('episode_id', 0)}:{rec.get('variation', 0)}"
                step_map[key].append(rec)
    return dict(step_map)


def bootstrap_ci(values: np.ndarray, stat_fn, n_boot: int = 1000,
                 ci: float = 0.90, rng: np.random.RandomState = None) -> Dict:
    if rng is None:
        rng = np.random.RandomState(42)
    if len(values) == 0:
        return {"mean": 0.0, "ci_low": 0.0, "ci_high": 0.0, "n": 0}
    observed = float(stat_fn(values))
    boot_stats = []
    for _ in range(n_boot):
        sample = rng.choice(values, size=len(values), replace=True)
        boot_stats.append(float(stat_fn(sample)))
    alpha = (1 - ci) / 2
    return {
        "mean": observed,
        "ci_low": float(np.percentile(boot_stats, 100 * alpha)),
        "ci_high": float(np.percentile(boot_stats, 100 * (1 - alpha))),
        "n": len(values),
    }


def compute_metrics(scores: List[float], decisions: List[str],
                    internal_steps: List[int], det_steps: List[int],
                    seed: int = 42) -> Dict[str, Any]:
    rng = np.random.RandomState(seed)
    arr = np.array(scores, dtype=float)
    score_stats = bootstrap_ci(arr, np.mean, rng=rng)
    success = (arr > 0).astype(float)
    success_stats = bootstrap_ci(success, np.mean, rng=rng)
    death = (arr <= DEATH_SCORE).astype(float)
    death_stats = bootstrap_ci(death, np.mean, rng=rng)

    total_det_steps = 0
    total_all_steps = 0
    for dec, i_steps, d_steps in zip(decisions, internal_steps, det_steps):
        if dec == "deterministic":
            total_det_steps += d_steps
            total_all_steps += d_steps
        else:
            total_all_steps += i_steps
    sim_ratio = total_det_steps / total_all_steps if total_all_steps > 0 else 0.0

    return {
        "continuous_score": score_stats,
        "success_rate": success_stats,
        "catastrophic_failure_rate": death_stats,
        "simulator_invocation_ratio": sim_ratio,
        "n_episodes": len(scores),
    }


class ImplicitRouter:
    """Ablation-b implicit router: generative Qwen3-1.7B + LoRA."""

    def __init__(self, adapter_dir: str, base_model: str,
                 max_new_tokens: int = 60, gpu_id: int = 0):
        self.device = torch.device(f"cuda:{gpu_id}" if torch.cuda.is_available() else "cpu")
        self.max_new_tokens = max_new_tokens

        print(f"Loading tokenizer from {base_model}")
        self.tokenizer = AutoTokenizer.from_pretrained(base_model, trust_remote_code=True)

        print(f"Loading base model from {base_model}")
        base = AutoModelForCausalLM.from_pretrained(
            base_model, torch_dtype=torch.bfloat16, device_map=f"cuda:{gpu_id}",
            trust_remote_code=True,
        )
        print(f"Loading adapter from {adapter_dir}")
        self.model = PeftModel.from_pretrained(base, adapter_dir)
        self.model.eval()
        print("ImplicitRouter ready.")

    def _build_prompt(self, observation: str, action_history: List[str]) -> str:
        if action_history:
            hist_str = " → ".join(action_history[-5:])
        else:
            hist_str = "(none)"
        messages = [
            {"role": "system", "content": IMPLICIT_SYSTEM_PROMPT},
            {"role": "user", "content": f"Observation: {observation}\nAction history: {hist_str}"},
        ]
        return self.tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True,
            enable_thinking=False,
        )

    def predict_step(self, observation: str, action_history: List[str]) -> Tuple[str, str]:
        """Generate for one step. Returns (route_decision, raw_output)."""
        prompt_text = self._build_prompt(observation, action_history)
        inputs = self.tokenizer(prompt_text, return_tensors="pt").to(self.device)
        input_len = inputs["input_ids"].shape[1]

        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=self.max_new_tokens,
                do_sample=False,
                temperature=1.0,
            )

        generated_ids = outputs[0][input_len:]
        generated = self.tokenizer.decode(generated_ids, skip_special_tokens=True)
        clean = re.sub(r'<think>.*?</think>\s*', '', generated, flags=re.DOTALL).strip()

        route = "deterministic" if clean.startswith("[SIMULATE]") else "internal"
        return route, clean

    def predict_episode(self, steps: List[Dict]) -> Tuple[str, float, Dict]:
        """Majority vote over step-level generation predictions."""
        if not steps:
            return "deterministic", 0.5, {"n_steps": 0, "votes": {}, "step_details": []}

        step_details = []
        votes = Counter()

        for s in steps:
            route, raw_output = self.predict_step(
                s.get("observation", ""),
                s.get("action_history", []),
            )
            votes[route] += 1
            step_details.append({
                "step_idx": s.get("step_idx", -1),
                "route": route,
                "raw_output": raw_output[:200],
                "oracle_label": RAW_LABEL_MAP.get(s.get("label", ""), s.get("label", "")),
            })

        decision = votes.most_common(1)[0][0]
        total = sum(votes.values())
        confidence = votes[decision] / total if total > 0 else 0.5

        return decision, confidence, {
            "n_steps": total,
            "votes": dict(votes),
            "confidence": confidence,
            "step_details": step_details,
        }


def find_steps_for_episode(ep: Dict, step_map: Dict[str, List[Dict]]) -> List[Dict]:
    """Look up step data for an episode, with fuzzy key matching."""
    key = f"{ep['task_type']}:{ep['episode_idx']}:{ep['variation_idx']}"
    steps = step_map.get(key, [])
    if steps:
        return steps
    for k, v in step_map.items():
        parts = k.split(":")
        if (parts[0].replace("-", "_") == ep["task_type"].replace("-", "_")
                and parts[1] == str(ep["episode_idx"])
                and parts[2] == str(ep["variation_idx"])):
            return v
    return []


def main():
    parser = argparse.ArgumentParser(
        description="Plan-003 eval: ablation-b implicit router (trained-router condition)"
    )
    parser.add_argument("--data_dir", type=str, default="results/plan_c")
    parser.add_argument("--adapter_dir", type=str,
                        default="checkpoints/plan-004-implicit/final_adapter")
    parser.add_argument("--base_model", type=str,
                        default="/root/autodl-tmp/models/Qwen/Qwen3-1.7B")
    parser.add_argument("--output_dir", type=str, default="results/plan_003_eval")
    parser.add_argument("--max_new_tokens", type=int, default=60)
    parser.add_argument("--gpu_id", type=int, default=0)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--dry_run", action="store_true",
                        help="Process only first 3 episodes for validation")
    args = parser.parse_args()

    print("=== PLAN-003 EVAL: IMPLICIT ROUTER (ABLATION-B) ===")
    print(f"Data: {args.data_dir}")
    print(f"Adapter: {args.adapter_dir}")
    print(f"Base model: {args.base_model}")
    print(f"Output: {args.output_dir}")

    episodes = load_episodes(args.data_dir)
    if not episodes:
        print("ERROR: No episodes found.")
        sys.exit(1)

    step_map = load_labeled_steps(args.data_dir)
    task_counts = Counter(ep["task_type"] for ep in episodes)
    total_steps = sum(len(v) for v in step_map.values())
    print(f"\nLoaded {len(episodes)} episodes, {total_steps} steps across {len(task_counts)} tasks")

    if args.dry_run:
        episodes = episodes[:3]
        print(f"DRY RUN: limiting to {len(episodes)} episodes")

    router = ImplicitRouter(
        adapter_dir=args.adapter_dir,
        base_model=args.base_model,
        max_new_tokens=args.max_new_tokens,
        gpu_id=args.gpu_id,
    )

    scores = []
    decisions = []
    internal_steps_list = []
    det_steps_list = []
    episode_details = []
    all_step_details = []

    t0 = time.time()
    steps_done = 0

    for i, ep in enumerate(episodes):
        steps = find_steps_for_episode(ep, step_map)
        dec, conf, detail = router.predict_episode(steps)

        score = ep["det_final"] if dec == "deterministic" else ep["internal_final"]
        scores.append(score)
        decisions.append(dec)
        internal_steps_list.append(ep["internal_steps"])
        det_steps_list.append(ep["det_steps"])

        ep_detail = {
            "condition": "trained-router-implicit",
            "task_type": ep["task_type"],
            "episode_idx": ep["episode_idx"],
            "variation_idx": ep["variation_idx"],
            "decision": dec,
            "confidence": conf,
            "score": score,
            "internal_final": ep["internal_final"],
            "det_final": ep["det_final"],
            "oracle_label": ep["label"],
            "n_steps_routed": detail["n_steps"],
            "votes": detail["votes"],
        }
        episode_details.append(ep_detail)

        for sd in detail.get("step_details", []):
            sd["task_type"] = ep["task_type"]
            sd["episode_idx"] = ep["episode_idx"]
            sd["variation_idx"] = ep["variation_idx"]
            all_step_details.append(sd)

        steps_done += detail["n_steps"]
        elapsed = time.time() - t0
        eps = steps_done / elapsed if elapsed > 0 else 0
        print(f"  [{i+1}/{len(episodes)}] {ep['task_type']} ep{ep['episode_idx']}: "
              f"route={dec} (conf={conf:.2f}), score={score:.1f} "
              f"[{steps_done} steps, {eps:.1f} steps/s]")

    elapsed_total = time.time() - t0
    print(f"\nInference done: {steps_done} steps in {elapsed_total:.1f}s")

    metrics = compute_metrics(scores, decisions, internal_steps_list, det_steps_list, args.seed)

    # Step-level routing accuracy vs oracle
    correct = 0
    total_labeled = 0
    for sd in all_step_details:
        oracle = sd.get("oracle_label")
        if oracle in ("internal", "deterministic"):
            total_labeled += 1
            if sd["route"] == oracle:
                correct += 1
    step_accuracy = correct / total_labeled if total_labeled > 0 else 0.0
    metrics["step_routing_accuracy"] = {
        "accuracy": round(step_accuracy, 4),
        "correct": correct,
        "total_labeled": total_labeled,
    }

    # Episode-level routing accuracy
    ep_correct = 0
    ep_total = 0
    for ed in episode_details:
        oracle = RAW_LABEL_MAP.get(ed["oracle_label"], ed["oracle_label"])
        if oracle in ("internal", "deterministic"):
            ep_total += 1
            if ed["decision"] == oracle:
                ep_correct += 1
    ep_accuracy = ep_correct / ep_total if ep_total > 0 else 0.0
    metrics["episode_routing_accuracy"] = {
        "accuracy": round(ep_accuracy, 4),
        "correct": ep_correct,
        "total_labeled": ep_total,
    }

    vote_dist = Counter(decisions)
    metrics["routing_distribution"] = dict(vote_dist)

    os.makedirs(args.output_dir, exist_ok=True)
    results_path = os.path.join(args.output_dir, "implicit_router_results.json")
    with open(results_path, "w") as f:
        json.dump(metrics, f, indent=2)
    print(f"Metrics: {results_path}")

    episodes_path = os.path.join(args.output_dir, "implicit_router_episodes.jsonl")
    with open(episodes_path, "w") as f:
        for ed in episode_details:
            f.write(json.dumps(ed, default=str) + "\n")
    print(f"Episodes: {episodes_path}")

    steps_path = os.path.join(args.output_dir, "implicit_router_steps.jsonl")
    with open(steps_path, "w") as f:
        for sd in all_step_details:
            f.write(json.dumps(sd, default=str) + "\n")
    print(f"Steps: {steps_path}")

    sc = metrics["continuous_score"]
    dr = metrics["catastrophic_failure_rate"]
    sr = metrics["success_rate"]
    sim = metrics["simulator_invocation_ratio"]
    print(f"\n{'='*60}")
    print("IMPLICIT ROUTER (ABLATION-B) RESULTS")
    print(f"{'='*60}")
    print(f"Score:      {sc['mean']:>8.2f}  [{sc['ci_low']:.2f}, {sc['ci_high']:.2f}]")
    print(f"Success:    {sr['mean']:>8.4f}")
    print(f"Death rate: {dr['mean']:>8.4f}")
    print(f"Sim ratio:  {sim:>8.4f}")
    print(f"Step acc:   {step_accuracy:>8.4f} ({correct}/{total_labeled})")
    print(f"Episode acc:{ep_accuracy:>8.4f} ({ep_correct}/{ep_total})")
    print(f"Routing:    {dict(vote_dist)}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
