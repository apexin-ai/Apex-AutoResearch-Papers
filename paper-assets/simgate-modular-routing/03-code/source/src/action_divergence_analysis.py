"""Action divergence analysis between internal and deterministic modalities in MVP data."""
import json
import os
import glob
from collections import defaultdict

RESULTS_DIR = "/root/autodl-tmp/simgate-modular-routing/results/mvp"

def load_episodes(task_dir):
    episodes = []
    path = os.path.join(task_dir, "episodes.jsonl")
    with open(path) as f:
        for line in f:
            episodes.append(json.loads(line))
    return episodes

def analyze_task(task_name, task_dir):
    episodes = load_episodes(task_dir)

    total_steps = 0
    diverge_steps = 0
    phase_stats = defaultdict(lambda: {"total": 0, "diverge": 0})

    ep_count = 0

    for ep in episodes:
        oracle = ep.get("oracle_routing") or ep.get("oracle")
        if oracle is None:
            continue

        steps = oracle.get("steps", [])
        ep_count += 1

        for s in steps:
            ia = s.get("internal_action")
            da = s.get("det_action")
            if ia is None or da is None:
                continue

            step_idx = s["step"]
            total_steps += 1

            if step_idx < 10:
                phase = "steps_01_10"
            elif step_idx < 20:
                phase = "steps_11_20"
            else:
                phase = "steps_21_30"

            phase_stats[phase]["total"] += 1

            if ia != da:
                diverge_steps += 1
                phase_stats[phase]["diverge"] += 1

    return {
        "task": task_name,
        "episodes": ep_count,
        "total_steps": total_steps,
        "diverge_steps": diverge_steps,
        "divergence_rate": diverge_steps / total_steps if total_steps > 0 else 0,
        "phases": dict(phase_stats),
    }

def gpu_cost_estimate(global_div_rate):
    print("\n" + "=" * 60)
    print("GPU COST ESTIMATE (plan-001b episode-terminal labeling)")
    print("=" * 60)

    task_types = 15
    episodes_per_task = 20
    steps_per_episode = 30
    total_steps = task_types * episodes_per_task * steps_per_episode

    fork_count = total_steps * global_div_rate
    fork_continuation_steps = 10
    fork_modalities = 2
    steps_per_fork = fork_continuation_steps * fork_modalities
    sec_per_step = 4
    num_gpus = 2

    base_time_s = total_steps * sec_per_step
    fork_time_s = fork_count * steps_per_fork * sec_per_step
    total_time_s = (base_time_s + fork_time_s) / num_gpus

    print(f"\nParameters:")
    print(f"  {task_types} tasks × {episodes_per_task} eps × {steps_per_episode} steps = {total_steps} total steps")
    print(f"  Divergence rate: {global_div_rate:.1%}")
    print(f"  Fork count: {fork_count:.0f}")
    print(f"  Steps per fork: {steps_per_fork} (K={fork_continuation_steps} × 2 modalities)")
    print(f"  Inference speed: {sec_per_step}s/step")
    print(f"  GPUs: {num_gpus}")

    print(f"\nTime breakdown:")
    print(f"  Base episode collection: {base_time_s:,.0f}s = {base_time_s/3600:.1f}h")
    print(f"  Fork continuations:      {fork_time_s:,.0f}s = {fork_time_s/3600:.1f}h")
    print(f"  Total (single GPU):      {base_time_s + fork_time_s:,.0f}s = {(base_time_s + fork_time_s)/3600:.1f}h")
    print(f"  Total ({num_gpus}-GPU parallel):   {total_time_s:,.0f}s = {total_time_s/3600:.1f}h")

    autodl_rate_per_hour = 2.58  # A6000 ¥/h
    cost = (total_time_s / 3600) * autodl_rate_per_hour * num_gpus
    print(f"\n  Estimated cost (2×A6000 @ ¥{autodl_rate_per_hour}/GPU·h): ¥{cost:.0f}")

def main():
    task_dirs = sorted(glob.glob(os.path.join(RESULTS_DIR, "*")))

    print("=" * 60)
    print("ACTION DIVERGENCE ANALYSIS")
    print("=" * 60)

    results = []
    global_total = 0
    global_diverge = 0

    for td in task_dirs:
        if not os.path.isdir(td):
            continue
        task_name = os.path.basename(td)
        r = analyze_task(task_name, td)
        results.append(r)
        global_total += r["total_steps"]
        global_diverge += r["diverge_steps"]

    for r in results:
        print(f"\nTask: {r['task']} ({r['episodes']} episodes, {r['total_steps']} steps)")
        print(f"  Divergence rate: {r['divergence_rate']:.1%} ({r['diverge_steps']} diverge / {r['total_steps']} total)")
        print(f"  By phase:")
        for phase_key in ["steps_01_10", "steps_11_20", "steps_21_30"]:
            p = r["phases"].get(phase_key, {"total": 0, "diverge": 0})
            rate = p["diverge"] / p["total"] if p["total"] > 0 else 0
            label = phase_key.replace("steps_", "Steps ").replace("_", "-")
            print(f"    {label}:  {rate:.1%} ({p['diverge']}/{p['total']})")

    global_rate = global_diverge / global_total if global_total > 0 else 0
    print(f"\n{'=' * 60}")
    print(f"OVERALL")
    print(f"{'=' * 60}")
    print(f"Global divergence rate: {global_rate:.1%} ({global_diverge}/{global_total})")
    print(f"Tasks analyzed: {len(results)}")
    print(f"Total episodes (oracle): {sum(r['episodes'] for r in results)}")

    gpu_cost_estimate(global_rate)

if __name__ == "__main__":
    main()
