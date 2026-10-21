# Plan C episode-level labeling data collection for router SFT training.
#
# For each task variation, runs 2 complete episodes (always-internal + always-deterministic),
# compares final episode scores to label each step's modality preference.
# Reuses run_episode_internal / run_episode_deterministic from signal_prescreening.py.
#
# Outputs:
#   {output_dir}/{task_type}/labeled_steps.jsonl  — one labeled step per line (training data)
#   {output_dir}/{task_type}/episode_summary.jsonl — one episode summary per line
#
# Usage:
#   python src/episode_level_collection.py --task_types "boil,melt" --episodes 20 --gpu_id 0

import argparse
import json
import os
import random
import sys
import time
from typing import List, Dict, Any

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scienceworld_utils import (
    create_env, reset_env, get_valid_actions, get_score,
    step_env, close_env, fork_and_lookahead, get_task_types,
    get_max_variations,
)
from llm_agent import LLMAgent, find_model_path

DEATH_THRESHOLD = -100


def resolve_task_type(name: str) -> str:
    try:
        available = get_task_types()
    except Exception:
        return name
    if name in available:
        return name
    matches = [t for t in available if name.lower() in t.lower()]
    if matches:
        return matches[0]
    return name


def is_lethal(fr: Dict[str, Any]) -> bool:
    if fr["done"] and fr["score"] < 0:
        return True
    if fr["score"] <= -100:
        return True
    return False


def scan_reuse_episodes(reuse_dirs: List[str], task_name: str) -> Dict[str, Any]:
    """Scan reuse directories for existing episodes of a given task.

    Returns dict with 'total' count and 'sources' list of {dir, count, path}.
    """
    task_name_normalized = task_name.replace(" ", "_")
    candidates = [task_name, task_name_normalized]
    if "-" in task_name:
        candidates.append(task_name.replace("-", "_"))
    if "_" in task_name:
        candidates.append(task_name.replace("_", "-"))

    sources = []
    total = 0

    for reuse_dir in reuse_dirs:
        reuse_dir = reuse_dir.rstrip("/")
        if not os.path.isdir(reuse_dir):
            continue

        found_path = None
        for cand_name in candidates:
            ep_path = os.path.join(reuse_dir, cand_name, "episodes.jsonl")
            if os.path.isfile(ep_path):
                found_path = ep_path
                break

        if not found_path:
            subdirs = os.listdir(reuse_dir)
            for sd in subdirs:
                if sd.lower() == task_name_normalized.lower():
                    ep_path = os.path.join(reuse_dir, sd, "episodes.jsonl")
                    if os.path.isfile(ep_path):
                        found_path = ep_path
                        break

        if found_path:
            count = 0
            with open(found_path) as f:
                for line in f:
                    line = line.strip()
                    if line:
                        count += 1
            sources.append({
                "dir": reuse_dir,
                "path": found_path,
                "count": count,
            })
            total += count

    return {"total": total, "sources": sources}


def run_episode_internal(
    agent: LLMAgent,
    task_name: str,
    variation_idx: int,
    max_steps: int,
) -> Dict[str, Any]:
    """Always-internal: pure LLM ReAct, no death filter."""
    env = create_env(task_name, variation_idx)
    obs, _ = reset_env(env)
    initial_score = get_score(env)

    steps = []
    action_history = []
    history_dicts = []
    t0 = time.time()

    for step_idx in range(max_steps):
        valid_actions = get_valid_actions(env)
        if not valid_actions:
            break

        action, raw_output = agent.select_action_react(obs, valid_actions, history_dicts)

        score_before = get_score(env)
        obs_new, reward, done, info = step_env(env, action)
        score_after = get_score(env)

        steps.append({
            "step": step_idx,
            "action": action,
            "modality": "internal",
            "score_before": score_before,
            "score_after": score_after,
            "score_delta": score_after - score_before,
            "observation": obs_new[:500],
            "llm_output": raw_output[:300],
            "action_history": list(action_history),
            "is_dead": score_after <= DEATH_THRESHOLD,
        })
        action_history.append(action)
        history_dicts.append({"action": action, "observation": obs_new[:200], "score": score_after})
        obs = obs_new

        if done:
            break

    final_score = get_score(env)
    close_env(env)

    return {
        "mode": "always-internal",
        "task_name": task_name,
        "variation_idx": variation_idx,
        "final_score": final_score,
        "initial_score": initial_score,
        "num_steps": len(steps),
        "total_time_s": time.time() - t0,
        "steps": steps,
        "action_history": action_history,
    }


def run_episode_deterministic(
    agent: LLMAgent,
    task_name: str,
    variation_idx: int,
    max_steps: int,
    n_candidates: int = 3,
) -> Dict[str, Any]:
    """Always-deterministic: LLM candidates + fork evaluation + death filter."""
    env = create_env(task_name, variation_idx)
    obs, _ = reset_env(env)
    initial_score = get_score(env)

    steps = []
    action_history = []
    history_dicts = []
    t0 = time.time()

    for step_idx in range(max_steps):
        valid_actions = get_valid_actions(env)
        if not valid_actions:
            break

        candidates, raw_output = agent.generate_candidate_actions(
            obs, valid_actions, history_dicts, n=n_candidates
        )

        best_action = None
        best_delta = float("-inf")
        best_action_fallback = None
        best_delta_fallback = float("-inf")
        fork_results = []
        for cand in candidates:
            fr = fork_and_lookahead(task_name, variation_idx, action_history, cand)
            lethal = is_lethal(fr)
            fork_results.append({
                "action": cand,
                "score_delta": fr["score_delta"],
                "score": fr["score"],
                "lethal": lethal,
            })
            if fr["score_delta"] > best_delta_fallback:
                best_delta_fallback = fr["score_delta"]
                best_action_fallback = cand
            if not lethal and fr["score_delta"] > best_delta:
                best_delta = fr["score_delta"]
                best_action = cand

        if best_action is None:
            best_action = best_action_fallback if best_action_fallback else valid_actions[0]

        score_before = get_score(env)
        obs_new, reward, done, info = step_env(env, best_action)
        score_after = get_score(env)

        steps.append({
            "step": step_idx,
            "action": best_action,
            "modality": "deterministic",
            "score_before": score_before,
            "score_after": score_after,
            "score_delta": score_after - score_before,
            "candidates": fork_results,
            "observation": obs_new[:500],
            "llm_output": raw_output[:300],
            "action_history": list(action_history),
            "is_dead": score_after <= DEATH_THRESHOLD,
        })
        action_history.append(best_action)
        history_dicts.append({"action": best_action, "observation": obs_new[:200], "score": score_after})
        obs = obs_new

        if done:
            break

    final_score = get_score(env)
    close_env(env)

    return {
        "mode": "always-deterministic",
        "task_name": task_name,
        "variation_idx": variation_idx,
        "final_score": final_score,
        "initial_score": initial_score,
        "num_steps": len(steps),
        "total_time_s": time.time() - t0,
        "steps": steps,
        "action_history": action_history,
    }


def label_episode(internal_final: float, det_final: float) -> str:
    internal_death = internal_final <= DEATH_THRESHOLD
    det_death = det_final <= DEATH_THRESHOLD

    if internal_death and det_death:
        return "tie"
    if internal_death:
        return "deterministic"
    if det_death:
        return "internal"

    if det_final > internal_final:
        return "deterministic"
    elif internal_final > det_final:
        return "internal"
    else:
        return "tie"


def run_task_collection(
    agent: LLMAgent,
    task_name: str,
    n_episodes: int,
    start_episode: int,
    max_steps: int,
    output_dir: str,
    n_candidates: int = 3,
) -> Dict[str, Any]:
    task_dir = os.path.join(output_dir, task_name.replace(" ", "_"))
    os.makedirs(task_dir, exist_ok=True)

    steps_file = os.path.join(task_dir, "labeled_steps.jsonl")
    summary_file = os.path.join(task_dir, "episode_summary.jsonl")

    max_var = get_max_variations(task_name)
    end_episode = start_episode + n_episodes

    print(f"\n{'='*60}")
    print(f"EPISODE-LEVEL COLLECTION: {task_name}")
    print(f"Episodes: {start_episode}..{end_episode-1} ({n_episodes} total) | Max steps: {max_steps}")
    print(f"Max variations: {max_var}")
    print(f"{'='*60}")

    label_counts = {"deterministic": 0, "internal": 0, "tie": 0}
    total_labeled_steps = 0
    death_counts = {"internal": 0, "det": 0, "both": 0}
    score_gaps = []

    for ep_idx in range(start_episode, end_episode):
        variation_idx = ep_idx % max_var
        print(f"\n--- Episode {ep_idx} (variation={variation_idx}) ---")

        print(f"  [I] always-internal...", end=" ", flush=True)
        t = time.time()
        r_int = run_episode_internal(agent, task_name, variation_idx, max_steps)
        print(f"score={r_int['final_score']:.1f} ({time.time()-t:.0f}s)")

        print(f"  [D] always-deterministic...", end=" ", flush=True)
        t = time.time()
        r_det = run_episode_deterministic(
            agent, task_name, variation_idx, max_steps, n_candidates
        )
        print(f"score={r_det['final_score']:.1f} ({time.time()-t:.0f}s)")

        internal_final = r_int["final_score"]
        det_final = r_det["final_score"]
        ep_label = label_episode(internal_final, det_final)
        score_gap = det_final - internal_final

        # Track deaths
        int_death = internal_final <= DEATH_THRESHOLD
        det_death = det_final <= DEATH_THRESHOLD
        if int_death and det_death:
            death_counts["both"] += 1
        elif int_death:
            death_counts["internal"] += 1
        elif det_death:
            death_counts["det"] += 1

        label_counts[ep_label] += 1
        if ep_label != "tie":
            score_gaps.append(abs(score_gap))

        # Write episode summary
        ep_summary = {
            "episode": ep_idx,
            "variation": variation_idx,
            "internal_final": internal_final,
            "det_final": det_final,
            "label": ep_label,
            "score_gap": score_gap,
            "internal_steps": r_int["num_steps"],
            "det_steps": r_det["num_steps"],
        }
        with open(summary_file, "a") as f:
            f.write(json.dumps(ep_summary) + "\n")

        print(f"  Label: {ep_label} (gap={score_gap:+.1f})")

        # Write labeled steps from winning episode (skip ties)
        if ep_label == "tie":
            continue

        winning_result = r_det if ep_label == "deterministic" else r_int
        for step in winning_result["steps"]:
            record = {
                "task_type": task_name,
                "episode_id": ep_idx,
                "variation": variation_idx,
                "step_idx": step["step"],
                "observation": step["observation"],
                "action": step["action"],
                "action_history": step["action_history"],
                "score_before": step["score_before"],
                "score_after": step["score_after"],
                "label": ep_label,
                "episode_score_internal": internal_final,
                "episode_score_det": det_final,
                "score_gap": score_gap,
            }
            with open(steps_file, "a") as f:
                f.write(json.dumps(record) + "\n")
            total_labeled_steps += 1

    avg_gap = sum(score_gaps) / len(score_gaps) if score_gaps else 0.0

    print(f"\n=== EPISODE-LEVEL COLLECTION: {task_name} ===")
    print(f"Episodes: {n_episodes} (start={start_episode})")
    print(f"Label distribution: det={label_counts['deterministic']}, int={label_counts['internal']}, tie={label_counts['tie']}")
    print(f"Avg score gap (non-tie): {avg_gap:.2f}")
    print(f"Total labeled steps: {total_labeled_steps}")
    print(f"Death episodes: internal={death_counts['internal']}, det={death_counts['det']}, both={death_counts['both']}")

    return {
        "task_name": task_name,
        "n_episodes": n_episodes,
        "start_episode": start_episode,
        "label_counts": label_counts,
        "total_labeled_steps": total_labeled_steps,
        "avg_score_gap": avg_gap,
        "death_counts": death_counts,
    }


def copy_reused_episodes(sources: List[Dict], task_dir: str) -> int:
    """Copy episodes from reuse sources into the output episodes.jsonl."""
    episodes_file = os.path.join(task_dir, "episodes.jsonl")
    copied = 0
    for src in sources:
        with open(src["path"]) as fin:
            with open(episodes_file, "a") as fout:
                for line in fin:
                    line = line.strip()
                    if line:
                        fout.write(line + "\n")
                        copied += 1
    return copied


def main():
    parser = argparse.ArgumentParser(
        description="Plan C episode-level labeling: collect SFT training data by comparing always-internal vs always-deterministic episodes"
    )
    parser.add_argument("--task_types", type=str, default=None,
                        help="Comma-separated task type names")
    parser.add_argument("--task_list", type=str, default=None,
                        help="Comma-separated task type names (alias for --task_types)")
    parser.add_argument("--episodes", type=int, default=20,
                        help="Number of episodes per task type (default: 20)")
    parser.add_argument("--start_episode", type=int, default=0,
                        help="Starting episode index for incremental runs (default: 0)")
    parser.add_argument("--gpu_id", type=int, default=0)
    parser.add_argument("--max_steps", type=int, default=30)
    parser.add_argument("--output_dir", type=str, default="results/plan_c/")
    parser.add_argument("--model_path", type=str, default=None)
    parser.add_argument("--use_vllm", action="store_true", default=True)
    parser.add_argument("--no_vllm", action="store_true", default=False,
                        help="Use HF transformers instead of vLLM")
    parser.add_argument("--n_candidates", type=int, default=3,
                        help="Number of candidate actions for deterministic mode")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--reuse_dirs", type=str, default=None,
                        help="Comma-separated directories to scan for existing episode data")
    parser.add_argument("--dry_run", action="store_true", default=False,
                        help="Only scan reuse dirs and report what would be collected, no GPU inference")
    args = parser.parse_args()

    task_types_str = args.task_types or args.task_list
    if not task_types_str:
        parser.error("--task_types or --task_list is required")

    if args.no_vllm:
        args.use_vllm = False

    random.seed(args.seed)

    task_names_raw = [t.strip() for t in task_types_str.split(",") if t.strip()]
    task_names = [resolve_task_type(t) for t in task_names_raw]

    reuse_dirs = []
    if args.reuse_dirs:
        reuse_dirs = [d.strip() for d in args.reuse_dirs.split(",") if d.strip()]

    if args.dry_run:
        print(f"=== DRY RUN: scanning reuse dirs for {len(task_names)} tasks ===")
        print(f"Reuse dirs: {reuse_dirs}")
        print(f"Target episodes per task: {args.episodes}\n")

        for task_name in task_names:
            reuse_info = scan_reuse_episodes(reuse_dirs, task_name) if reuse_dirs else {"total": 0, "sources": []}
            existing = reuse_info["total"]
            needed = max(0, args.episodes - existing)

            if needed == 0:
                print(f"SKIP: {task_name} — already have {existing} episodes (target={args.episodes})")
            else:
                print(f"COLLECT: {task_name} — have {existing}, need {needed} more (target={args.episodes})")

            for src in reuse_info["sources"]:
                print(f"  reuse: {src['path']} ({src['count']} episodes)")

        print("\n=== DRY RUN complete, no data collected ===")
        return

    print(f"Task types: {task_names}")
    print(f"Episodes: {args.episodes} (start={args.start_episode}), Max steps: {args.max_steps}")
    print(f"GPU: {args.gpu_id}, vLLM: {args.use_vllm}, Seed: {args.seed}")
    if reuse_dirs:
        print(f"Reuse dirs: {reuse_dirs}")

    # Scan reuse data before initializing agent (may skip all tasks)
    task_plans = {}
    for task_name in task_names:
        reuse_info = scan_reuse_episodes(reuse_dirs, task_name) if reuse_dirs else {"total": 0, "sources": []}
        existing = reuse_info["total"]
        needed = max(0, args.episodes - existing)
        task_plans[task_name] = {
            "reuse_info": reuse_info,
            "existing": existing,
            "needed": needed,
        }
        if needed == 0:
            print(f"SKIP: {task_name} — already have {existing} episodes (target={args.episodes})")
        else:
            print(f"PLAN: {task_name} — reuse {existing}, collect {needed} new episodes")
            for src in reuse_info["sources"]:
                print(f"  reuse: {src['path']} ({src['count']} episodes)")

    tasks_needing_collection = [t for t in task_names if task_plans[t]["needed"] > 0]

    if not tasks_needing_collection:
        print("\nAll tasks already have sufficient episodes. Writing collection_meta.json files.")
        for task_name in task_names:
            plan = task_plans[task_name]
            task_dir = os.path.join(args.output_dir, task_name.replace(" ", "_"))
            os.makedirs(task_dir, exist_ok=True)
            copy_reused_episodes(plan["reuse_info"]["sources"], task_dir)
            meta = {
                "task_name": task_name,
                "target_episodes": args.episodes,
                "reused_episodes": plan["existing"],
                "new_episodes": 0,
                "reuse_sources": [{"dir": s["dir"], "count": s["count"]} for s in plan["reuse_info"]["sources"]],
            }
            with open(os.path.join(task_dir, "collection_meta.json"), "w") as f:
                json.dump(meta, f, indent=2)
        return

    agent = LLMAgent(
        model_path=args.model_path,
        use_vllm=args.use_vllm,
        gpu_id=args.gpu_id,
    )

    os.makedirs(args.output_dir, exist_ok=True)
    all_results = {}

    for task_name in task_names:
        plan = task_plans[task_name]
        task_dir = os.path.join(args.output_dir, task_name.replace(" ", "_"))
        os.makedirs(task_dir, exist_ok=True)

        if plan["reuse_info"]["sources"]:
            copied = copy_reused_episodes(plan["reuse_info"]["sources"], task_dir)
            print(f"Copied {copied} reused episodes for {task_name}")

        if plan["needed"] > 0:
            effective_start = plan["existing"] if reuse_dirs else args.start_episode
            result = run_task_collection(
                agent, task_name, plan["needed"], effective_start,
                args.max_steps, args.output_dir, args.n_candidates,
            )
            all_results[task_name] = result
        else:
            all_results[task_name] = {
                "task_name": task_name,
                "n_episodes": 0,
                "start_episode": 0,
                "label_counts": {"deterministic": 0, "internal": 0, "tie": 0},
                "total_labeled_steps": 0,
                "avg_score_gap": 0.0,
                "death_counts": {"internal": 0, "det": 0, "both": 0},
                "skipped": True,
            }

        meta = {
            "task_name": task_name,
            "target_episodes": args.episodes,
            "reused_episodes": plan["existing"],
            "new_episodes": plan["needed"],
            "reuse_sources": [{"dir": s["dir"], "count": s["count"]} for s in plan["reuse_info"]["sources"]],
        }
        with open(os.path.join(task_dir, "collection_meta.json"), "w") as f:
            json.dump(meta, f, indent=2)

    if len(task_names) > 1:
        print(f"\n{'='*60}")
        print("GLOBAL SUMMARY")
        print(f"{'='*60}")
        for tn, r in all_results.items():
            if r.get("skipped"):
                print(f"  {tn}: SKIPPED (reused {task_plans[tn]['existing']} episodes)")
            else:
                lc = r["label_counts"]
                reused = task_plans[tn]["existing"]
                print(f"  {tn}: det={lc['deterministic']} int={lc['internal']} tie={lc['tie']} | steps={r['total_labeled_steps']} | reused={reused}")


if __name__ == "__main__":
    main()
