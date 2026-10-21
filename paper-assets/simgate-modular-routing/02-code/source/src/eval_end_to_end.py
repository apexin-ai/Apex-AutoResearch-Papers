# Plan-003: End-to-end simulated evaluation of SimGate routing strategies.
#
# Uses existing plan-001b counterfactual data (both always-internal and
# always-deterministic trajectories per episode) to evaluate routing conditions.
# For trained-router, loads the Qwen3-1.7B LoRA classification adapter and
# predicts per-episode routing decisions via majority vote on step-level predictions.
#
# Inputs:
#   --data_dir:  plan_c results directory with per-task {episodes.jsonl, episode_summary.jsonl, labeled_steps.jsonl}
#   --router_checkpoint: path to trained LoRA adapter (for trained-router condition)
#
# Outputs (--output_dir):
#   overall_results.json   — per-condition aggregated metrics with bootstrap 90% CI
#   per_task_results.csv   — per-task × per-condition breakdown
#   episode_details.jsonl  — per-episode routing decisions and scores
#
# 5 conditions:
#   always-internal, always-deterministic, oracle, random, trained-router
#
# Dependencies: torch, transformers, peft, numpy, sklearn (for trained-router only)

import argparse
import csv
import json
import os
import sys
from collections import Counter, defaultdict
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

LABEL2ID = {"internal": 0, "deterministic": 1}
ID2LABEL = {0: "internal", 1: "deterministic"}

RAW_LABEL_MAP = {
    "internal-preferred": "internal",
    "det-preferred": "deterministic",
    "no-preference": None,
}

SYSTEM_PROMPT = (
    "You are a routing classifier. Given the current observation and action history, "
    "predict which reasoning modality will lead to a better outcome."
)

DEATH_SCORE = -100.0

CONDITIONS = [
    "always-internal",
    "always-deterministic",
    "oracle",
    "random",
    "trained-router",
]


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_episodes(data_dir: str) -> List[Dict[str, Any]]:
    """Load all episodes from plan_c data directory.

    Each episode dict contains:
      task_type, episode_idx, variation_idx,
      internal_final, det_final, internal_steps, det_steps,
      label (oracle label from episode_summary)
    """
    episodes = []
    if not os.path.isdir(data_dir):
        raise FileNotFoundError(f"Data directory not found: {data_dir}")

    for task_dir_name in sorted(os.listdir(data_dir)):
        task_path = os.path.join(data_dir, task_dir_name)
        if not os.path.isdir(task_path):
            continue

        summary_path = os.path.join(task_path, "episode_summary.jsonl")
        episodes_path = os.path.join(task_path, "episodes.jsonl")

        if not os.path.exists(summary_path) and not os.path.exists(episodes_path):
            continue

        # Prefer episode_summary.jsonl (compact) with episodes.jsonl as fallback
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
                        "signal_source": rec.get("signal_source", ""),
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
                        "signal_source": "",
                    })

    return episodes


def load_labeled_steps(data_dir: str) -> Dict[str, List[Dict]]:
    """Load per-step labeled data keyed by (task_type, episode_id, variation).

    Returns dict: "task:episode:variation" → list of step dicts
    """
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


# ---------------------------------------------------------------------------
# Router model loading & inference
# ---------------------------------------------------------------------------

def summarize_action_history(action_history: List[str], max_actions: int = 5) -> str:
    recent = action_history[-max_actions:] if action_history else []
    if not recent:
        return "(none)"
    return " → ".join(recent)


def build_router_prompt(observation: str, action_history: List[str]) -> str:
    history_summary = summarize_action_history(action_history)
    return (
        f"<|im_start|>system\n{SYSTEM_PROMPT}<|im_end|>\n"
        f"<|im_start|>user\n"
        f"Observation: {observation}\n"
        f"Action history: {history_summary}<|im_end|>"
    )


class TrainedRouter:
    """Wraps the Qwen3-1.7B LoRA classification adapter for routing inference."""

    def __init__(self, adapter_dir: str, base_model: Optional[str] = None,
                 max_seq_len: int = 2048, gpu_id: int = 0, batch_size: int = 32):
        import torch
        from transformers import AutoTokenizer, AutoModelForSequenceClassification
        from peft import PeftModel

        self.device = torch.device(f"cuda:{gpu_id}" if torch.cuda.is_available() else "cpu")
        self.max_seq_len = max_seq_len
        self.batch_size = batch_size

        print(f"Loading router from {adapter_dir}")
        # Try loading tokenizer from adapter dir first, fall back to base model
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(adapter_dir, trust_remote_code=True)
        except Exception:
            self.tokenizer = None

        if base_model is None:
            config_path = os.path.join(adapter_dir, "adapter_config.json")
            with open(config_path) as f:
                cfg = json.load(f)
            base_model = cfg.get("base_model_name_or_path", "")
            if not base_model:
                raise ValueError("Cannot infer base model. Use --base_model.")
        print(f"Base model: {base_model}")

        if self.tokenizer is None:
            self.tokenizer = AutoTokenizer.from_pretrained(base_model, trust_remote_code=True)
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token

        base = AutoModelForSequenceClassification.from_pretrained(
            base_model, num_labels=2, id2label=ID2LABEL, label2id=LABEL2ID,
            trust_remote_code=True, torch_dtype=torch.bfloat16,
        )
        base.config.pad_token_id = self.tokenizer.pad_token_id
        self.model = PeftModel.from_pretrained(base, adapter_dir)
        self.model = self.model.to(self.device)
        self.model.eval()

    def predict_batch(self, texts: List[str]) -> np.ndarray:
        """Return (N, 2) logits array for a batch of prompt strings."""
        import torch
        enc = self.tokenizer(
            texts, return_tensors="pt", padding=True,
            truncation=True, max_length=self.max_seq_len,
        ).to(self.device)
        with torch.no_grad():
            logits = self.model(**enc).logits
        return logits.cpu().float().numpy()

    def predict_episode(self, steps: List[Dict]) -> Tuple[str, float, Dict]:
        """Predict routing for an episode by majority vote over step-level predictions.

        Returns (decision, confidence, detail_dict).
        """
        if not steps:
            return "deterministic", 0.5, {"n_steps": 0, "votes": {}}

        texts = []
        for s in steps:
            texts.append(build_router_prompt(
                s.get("observation", ""),
                s.get("action_history", []),
            ))

        all_preds = []
        for i in range(0, len(texts), self.batch_size):
            batch = texts[i:i + self.batch_size]
            logits = self.predict_batch(batch)
            preds = np.argmax(logits, axis=-1)
            all_preds.extend(preds.tolist())

        votes = Counter(ID2LABEL[p] for p in all_preds)
        decision = votes.most_common(1)[0][0]
        total = sum(votes.values())
        confidence = votes[decision] / total if total > 0 else 0.5

        return decision, confidence, {
            "n_steps": len(all_preds),
            "votes": dict(votes),
            "confidence": confidence,
        }


# ---------------------------------------------------------------------------
# Routing conditions
# ---------------------------------------------------------------------------

def route_always_internal(ep: Dict) -> Tuple[str, float]:
    return "internal", ep["internal_final"]


def route_always_deterministic(ep: Dict) -> Tuple[str, float]:
    return "deterministic", ep["det_final"]


def route_oracle(ep: Dict) -> Tuple[str, float]:
    label = ep["label"]
    mapped = RAW_LABEL_MAP.get(label, label)
    if mapped == "deterministic":
        return "deterministic", ep["det_final"]
    elif mapped == "internal":
        return "internal", ep["internal_final"]
    else:
        # no-preference: pick the better one
        if ep["det_final"] >= ep["internal_final"]:
            return "deterministic", ep["det_final"]
        return "internal", ep["internal_final"]


def route_random(ep: Dict, rng: np.random.RandomState) -> Tuple[str, float]:
    if rng.random() < 0.5:
        return "internal", ep["internal_final"]
    return "deterministic", ep["det_final"]


# ---------------------------------------------------------------------------
# Metrics computation
# ---------------------------------------------------------------------------

def bootstrap_ci(values: np.ndarray, stat_fn, n_boot: int = 1000,
                 ci: float = 0.90, rng: np.random.RandomState = None) -> Dict:
    """Compute bootstrap confidence interval for a statistic."""
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
    ci_low = float(np.percentile(boot_stats, 100 * alpha))
    ci_high = float(np.percentile(boot_stats, 100 * (1 - alpha)))
    return {"mean": observed, "ci_low": ci_low, "ci_high": ci_high, "n": len(values)}


def compute_metrics(scores: List[float], decisions: List[str],
                    internal_steps: List[int], det_steps: List[int],
                    seed: int = 42) -> Dict[str, Any]:
    """Compute all evaluation metrics for one condition."""
    rng = np.random.RandomState(seed)
    arr = np.array(scores, dtype=float)

    # Continuous score
    score_stats = bootstrap_ci(arr, np.mean, rng=rng)

    # Success rate (score > 0)
    success = (arr > 0).astype(float)
    success_stats = bootstrap_ci(success, np.mean, rng=rng)

    # Catastrophic failure rate (score == -100)
    death = (arr <= DEATH_SCORE).astype(float)
    death_stats = bootstrap_ci(death, np.mean, rng=rng)

    # Simulator invocation ratio
    total_det_steps = 0
    total_all_steps = 0
    for dec, i_steps, d_steps in zip(decisions, internal_steps, det_steps):
        if dec == "deterministic":
            total_det_steps += d_steps
            total_all_steps += d_steps
        else:
            total_all_steps += i_steps
    sim_ratio = total_det_steps / total_all_steps if total_all_steps > 0 else 0.0

    # Estimated LLM tokens (rough: ~500 tokens per step for internal, ~200 for deterministic candidate gen)
    est_tokens = 0
    for dec, i_steps, d_steps in zip(decisions, internal_steps, det_steps):
        if dec == "internal":
            est_tokens += i_steps * 500
        else:
            est_tokens += d_steps * 200

    return {
        "continuous_score": score_stats,
        "success_rate": success_stats,
        "catastrophic_failure_rate": death_stats,
        "simulator_invocation_ratio": sim_ratio,
        "estimated_llm_tokens": est_tokens,
        "n_episodes": len(scores),
    }


# ---------------------------------------------------------------------------
# Main evaluation loop
# ---------------------------------------------------------------------------

def evaluate_condition(
    condition: str,
    episodes: List[Dict],
    step_map: Optional[Dict[str, List[Dict]]] = None,
    router: Optional["TrainedRouter"] = None,
    seed: int = 42,
) -> Tuple[List[Dict], Dict[str, Any]]:
    """Evaluate one routing condition across all episodes.

    Returns (episode_details, aggregated_metrics).
    """
    rng = np.random.RandomState(seed)
    details = []
    scores = []
    decisions = []
    internal_steps_list = []
    det_steps_list = []

    for ep in episodes:
        if condition == "always-internal":
            dec, score = route_always_internal(ep)
        elif condition == "always-deterministic":
            dec, score = route_always_deterministic(ep)
        elif condition == "oracle":
            dec, score = route_oracle(ep)
        elif condition == "random":
            dec, score = route_random(ep, rng)
        elif condition == "trained-router":
            if router is None:
                raise ValueError("trained-router requires --router_checkpoint")
            key = f"{ep['task_type']}:{ep['episode_idx']}:{ep['variation_idx']}"
            steps = step_map.get(key, []) if step_map else []
            if not steps:
                # Fallback: try without task_type normalization
                for k, v in (step_map or {}).items():
                    parts = k.split(":")
                    if (parts[0].replace("-", "_") == ep["task_type"].replace("-", "_")
                            and parts[1] == str(ep["episode_idx"])
                            and parts[2] == str(ep["variation_idx"])):
                        steps = v
                        break
            if steps:
                dec, conf, detail = router.predict_episode(steps)
            else:
                dec, conf, detail = "deterministic", 0.5, {"n_steps": 0, "votes": {}}

            score = ep["det_final"] if dec == "deterministic" else ep["internal_final"]
        else:
            raise ValueError(f"Unknown condition: {condition}")

        scores.append(score)
        decisions.append(dec)
        internal_steps_list.append(ep["internal_steps"])
        det_steps_list.append(ep["det_steps"])

        ep_detail = {
            "condition": condition,
            "task_type": ep["task_type"],
            "episode_idx": ep["episode_idx"],
            "variation_idx": ep["variation_idx"],
            "decision": dec,
            "score": score,
            "internal_final": ep["internal_final"],
            "det_final": ep["det_final"],
            "oracle_label": ep["label"],
        }
        if condition == "trained-router" and router is not None:
            ep_detail["router_detail"] = detail if steps else None
        details.append(ep_detail)

    metrics = compute_metrics(scores, decisions, internal_steps_list, det_steps_list, seed)
    return details, metrics


def compute_per_task_metrics(
    details: List[Dict], seed: int = 42
) -> Dict[str, Dict[str, Any]]:
    """Break down metrics by task type."""
    by_task: Dict[str, List[Dict]] = defaultdict(list)
    for d in details:
        by_task[d["task_type"]].append(d)

    results = {}
    rng = np.random.RandomState(seed)
    for task, task_details in sorted(by_task.items()):
        scores = np.array([d["score"] for d in task_details], dtype=float)
        success = (scores > 0).astype(float)
        death = (scores <= DEATH_SCORE).astype(float)

        dec_counts = Counter(d["decision"] for d in task_details)
        total = sum(dec_counts.values())

        results[task] = {
            "n_episodes": len(task_details),
            "mean_score": float(np.mean(scores)),
            "score_std": float(np.std(scores)),
            "success_rate": float(np.mean(success)),
            "death_rate": float(np.mean(death)),
            "sim_ratio": dec_counts.get("deterministic", 0) / total if total > 0 else 0,
            "score_ci": bootstrap_ci(scores, np.mean, rng=rng),
        }
    return results


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

def write_results(
    output_dir: str,
    all_metrics: Dict[str, Dict],
    all_details: Dict[str, List[Dict]],
    all_per_task: Dict[str, Dict[str, Dict]],
):
    """Write evaluation results to output_dir."""
    os.makedirs(output_dir, exist_ok=True)

    # 1. Overall results JSON
    overall_path = os.path.join(output_dir, "overall_results.json")
    with open(overall_path, "w") as f:
        json.dump(all_metrics, f, indent=2)
    print(f"Overall results: {overall_path}")

    # 2. Per-task results CSV
    csv_path = os.path.join(output_dir, "per_task_results.csv")
    rows = []
    for cond, task_metrics in sorted(all_per_task.items()):
        for task, m in sorted(task_metrics.items()):
            rows.append({
                "condition": cond,
                "task_type": task,
                "n_episodes": m["n_episodes"],
                "mean_score": round(m["mean_score"], 2),
                "score_std": round(m["score_std"], 2),
                "score_ci_low": round(m["score_ci"]["ci_low"], 2),
                "score_ci_high": round(m["score_ci"]["ci_high"], 2),
                "success_rate": round(m["success_rate"], 4),
                "death_rate": round(m["death_rate"], 4),
                "sim_ratio": round(m["sim_ratio"], 4),
            })
    if rows:
        with open(csv_path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=rows[0].keys())
            writer.writeheader()
            writer.writerows(rows)
        print(f"Per-task CSV: {csv_path}")

    # 3. Episode details JSONL
    details_path = os.path.join(output_dir, "episode_details.jsonl")
    with open(details_path, "w") as f:
        for cond in sorted(all_details.keys()):
            for d in all_details[cond]:
                f.write(json.dumps(d, default=str) + "\n")
    print(f"Episode details: {details_path}")

    # 4. Per-task JSON (machine-readable)
    per_task_json_path = os.path.join(output_dir, "per_task_results.json")
    with open(per_task_json_path, "w") as f:
        json.dump(all_per_task, f, indent=2)
    print(f"Per-task JSON: {per_task_json_path}")


def print_summary(all_metrics: Dict[str, Dict]):
    """Print a human-readable summary table."""
    print(f"\n{'='*80}")
    print("PLAN-003 END-TO-END EVALUATION SUMMARY")
    print(f"{'='*80}")
    header = f"{'Condition':<25} {'Score':>10} {'90% CI':>20} {'Success':>10} {'Death':>10} {'SimRatio':>10}"
    print(header)
    print("-" * 85)
    for cond in CONDITIONS:
        if cond not in all_metrics:
            continue
        m = all_metrics[cond]
        sc = m["continuous_score"]
        sr = m["success_rate"]
        dr = m["catastrophic_failure_rate"]
        sim = m["simulator_invocation_ratio"]
        print(
            f"{cond:<25} "
            f"{sc['mean']:>10.2f} "
            f"[{sc['ci_low']:>8.2f}, {sc['ci_high']:>7.2f}] "
            f"{sr['mean']:>10.4f} "
            f"{dr['mean']:>10.4f} "
            f"{sim:>10.4f}"
        )
    print(f"{'='*80}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args():
    p = argparse.ArgumentParser(
        description="Plan-003: End-to-end simulated evaluation of SimGate routing"
    )
    p.add_argument("--conditions", type=str,
                   default="always-internal,always-deterministic,oracle,random,trained-router",
                   help="Comma-separated list of conditions to evaluate")
    p.add_argument("--router_checkpoint", type=str, default=None,
                   help="Path to trained LoRA adapter directory (for trained-router)")
    p.add_argument("--base_model", type=str, default=None,
                   help="Base model path (inferred from adapter config if omitted)")
    p.add_argument("--data_dir", type=str, default="results/plan_c",
                   help="Directory with plan-001b episode data")
    p.add_argument("--output_dir", type=str, default="results/plan_003_eval",
                   help="Output directory for results")
    p.add_argument("--episodes_per_task", type=int, default=None,
                   help="Limit episodes per task (None = use all)")
    p.add_argument("--max_seq_len", type=int, default=2048,
                   help="Max sequence length for router inference")
    p.add_argument("--batch_size", type=int, default=32,
                   help="Batch size for router inference")
    p.add_argument("--gpu_id", type=int, default=0)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--n_bootstrap", type=int, default=1000,
                   help="Number of bootstrap resamples for CI")
    return p.parse_args()


def main():
    args = parse_args()
    conditions = [c.strip() for c in args.conditions.split(",") if c.strip()]

    print(f"=== PLAN-003 END-TO-END EVAL ===")
    print(f"Data dir: {args.data_dir}")
    print(f"Conditions: {conditions}")
    print(f"Output dir: {args.output_dir}")
    print(f"Seed: {args.seed}")

    # Load episode data
    episodes = load_episodes(args.data_dir)
    if not episodes:
        print("ERROR: No episodes found. Check --data_dir.")
        sys.exit(1)

    task_counts = Counter(ep["task_type"] for ep in episodes)
    print(f"\nLoaded {len(episodes)} episodes across {len(task_counts)} tasks:")
    for t, c in sorted(task_counts.items()):
        print(f"  {t}: {c} episodes")

    # Limit episodes per task if requested
    if args.episodes_per_task is not None:
        limited = []
        task_seen = Counter()
        for ep in episodes:
            if task_seen[ep["task_type"]] < args.episodes_per_task:
                limited.append(ep)
                task_seen[ep["task_type"]] += 1
        print(f"\nLimited to {args.episodes_per_task}/task → {len(limited)} episodes")
        episodes = limited

    # Load step-level data (needed for trained-router)
    step_map = None
    if "trained-router" in conditions:
        step_map = load_labeled_steps(args.data_dir)
        print(f"Loaded step data for {len(step_map)} episode keys")

    # Load router model if needed
    router = None
    if "trained-router" in conditions:
        if args.router_checkpoint is None:
            print("WARNING: trained-router requires --router_checkpoint. Skipping.")
            conditions = [c for c in conditions if c != "trained-router"]
        elif not os.path.isdir(args.router_checkpoint):
            print(f"WARNING: checkpoint not found: {args.router_checkpoint}. Skipping trained-router.")
            conditions = [c for c in conditions if c != "trained-router"]
        else:
            router = TrainedRouter(
                adapter_dir=args.router_checkpoint,
                base_model=args.base_model,
                max_seq_len=args.max_seq_len,
                gpu_id=args.gpu_id,
                batch_size=args.batch_size,
            )

    # Evaluate each condition
    all_metrics = {}
    all_details = {}
    all_per_task = {}

    for cond in conditions:
        print(f"\n--- Evaluating: {cond} ---")
        details, metrics = evaluate_condition(
            cond, episodes, step_map, router, seed=args.seed,
        )
        per_task = compute_per_task_metrics(details, seed=args.seed)

        all_metrics[cond] = metrics
        all_details[cond] = details
        all_per_task[cond] = per_task

        sc = metrics["continuous_score"]
        dr = metrics["catastrophic_failure_rate"]
        print(f"  Score: {sc['mean']:.2f} [{sc['ci_low']:.2f}, {sc['ci_high']:.2f}]")
        print(f"  Death rate: {dr['mean']:.4f}")
        print(f"  Sim ratio: {metrics['simulator_invocation_ratio']:.4f}")

    # Write outputs
    write_results(args.output_dir, all_metrics, all_details, all_per_task)
    print_summary(all_metrics)

    print(f"\nDone. Results in {args.output_dir}/")


if __name__ == "__main__":
    main()
