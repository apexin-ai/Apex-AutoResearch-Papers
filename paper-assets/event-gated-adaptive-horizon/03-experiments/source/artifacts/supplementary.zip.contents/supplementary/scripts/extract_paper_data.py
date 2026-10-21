import json
import os
from datetime import datetime

LOGDIR = "/root/autodl-tmp/event-gated-adaptive-horizon/logdir"

EXPERIMENTS = {
    "exp_001_baseline": {
        "dir": "baseline_s1",
        "config": {"task": "walker_walk", "seed": 1, "dt_embed": "none", "subsample": False, "H": 15, "dt": 1}
    },
    "exp_008d_subsample_on_h8": {
        "dir": "exp_008d_subsample_on_h8",
        "config": {"task": "walker_walk", "seed": 1, "dt_embed": "trained", "subsample": True, "H": 8}
    },
    "exp_008f_no_dt_embed_subsample_on_h8": {
        "dir": "exp_008f_no_dt_embed_subsample_on_h8",
        "config": {"task": "walker_walk", "seed": 1, "dt_embed": "none", "subsample": True, "H": 8}
    },
    "exp_009c_008f_walker_s2": {
        "dir": "exp_009c_008f_walker_s2",
        "config": {"task": "walker_walk", "seed": 2, "dt_embed": "none", "subsample": True, "H": 8}
    },
    "exp_009b_008d_walker_s2": {
        "dir": "exp_009b_008d_walker_s2",
        "config": {"task": "walker_walk", "seed": 2, "dt_embed": "trained", "subsample": True, "H": 8}
    },
    "exp_008e_v3_subsample_on_dt1_h15": {
        "dir": "exp_008e_v3_subsample_on_dt1_h15",
        "config": {"task": "walker_walk", "seed": 1, "dt_embed": "trained", "subsample": True, "H": 15, "dt": 1}
    },
    "exp_008a_no_subsample_dt2": {
        "dir": "exp_008a_fixed_dt2_no_subsample",
        "config": {"task": "walker_walk", "seed": 1, "dt_embed": "untrained", "subsample": False, "H": 15, "dt": 2}
    },
    "exp_006_fixed_dt2": {
        "dir": "fixed_dt2_v1_s1",
        "config": {"task": "walker_walk", "seed": 1, "dt_embed": "trained", "subsample": True, "H": 15, "dt": 2}
    },
}

def extract_experiment(exp_id, info):
    metrics_path = os.path.join(LOGDIR, info["dir"], "metrics.jsonl")
    if not os.path.exists(metrics_path):
        print(f"  WARNING: {metrics_path} not found")
        return None

    # Parse all lines
    step_data = {}  # step -> merged dict
    with open(metrics_path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            step = row.get("step")
            if step is None:
                continue
            step = int(step)
            if step not in step_data:
                step_data[step] = {}
            step_data[step].update(row)

    # Extract checkpoints (steps that have eval_return)
    checkpoints = []
    for step in sorted(step_data.keys()):
        d = step_data[step]
        if "eval_return" not in d:
            continue
        
        eval_return = d.get("eval_return")
        value_mean = d.get("value_mean")
        actor_entropy = d.get("actor_entropy")
        model_loss = d.get("model_loss")
        reward_loss = d.get("reward_loss")
        value_loss = d.get("value_loss")
        
        ve_ratio = None
        if value_mean is not None and eval_return is not None and eval_return != 0:
            ve_ratio = value_mean / eval_return
        
        cp = {
            "step": step,
            "eval_return": eval_return,
            "value_mean": value_mean,
            "ve_ratio": ve_ratio,
            "actor_entropy": actor_entropy,
            "model_loss": model_loss,
            "reward_loss": reward_loss,
            "value_loss": value_loss,
        }
        # Also grab train_return if available
        if "train_return" in d:
            cp["train_return"] = d["train_return"]
        
        checkpoints.append(cp)
    
    return {
        "config": info["config"],
        "logdir": info["dir"],
        "num_checkpoints": len(checkpoints),
        "checkpoints": checkpoints
    }

result = {"experiments": {}, "metadata": {"extracted_at": datetime.now().isoformat(), "server": "bjb1-45299"}}

for exp_id, info in EXPERIMENTS.items():
    print(f"Processing {exp_id} ({info['dir']})...")
    data = extract_experiment(exp_id, info)
    if data:
        result["experiments"][exp_id] = data
        last_cp = data["checkpoints"][-1] if data["checkpoints"] else {}
        print(f"  {data['num_checkpoints']} checkpoints, last: step={last_cp.get('step')}, eval_return={last_cp.get('eval_return'):.2f}, value_mean={last_cp.get('value_mean'):.4f}, ve_ratio={last_cp.get('ve_ratio'):.4f}, actor_entropy={last_cp.get('actor_entropy'):.4f}")

out_path = os.path.join(LOGDIR, "paper_figure_data.json")
with open(out_path, "w") as f:
    json.dump(result, f, indent=2)

print(f"\nSaved to {out_path}")
print(f"Total experiments: {len(result['experiments'])}")
