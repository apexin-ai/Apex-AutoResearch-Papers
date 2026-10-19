# code failure mode analysis

**error diag dpo recovery** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/chats/worker_code_failure-mode-analysis_20260513T044723.jsonl`
- **Structured JSON:** [`279b19caafcb27977a37.json`](../../sessions/27/279b19caafcb27977a37.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

13 recorded events

### Tool call

_source line 1 · 2026-05-13T04:49:58.948664+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/src/build_dpo_pairs.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_failure-mode-analysis_20260513T044723",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/src/build_dpo_pairs.py"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-13T04:49:58.949140+00:00_

1	"""Build DPO preference pairs from classified failures and expert trajectories.
2	
3	Fix [2026-05-12]: Use true divergence point instead of LLM-reported failure_step.
4	Old logic used failure_step as split point, but expert and failure trajectories
5	may already differ before that step → prompt-chosen state inconsistency.
6	New logic compares action sequences step-by-step to find the real divergence.
7	
8	For each classified failure:
9	  1. Match expert trajectory by game_file
10	  2. Compare actions step-by-step to find divergence point
11	  3. Shared prefix = prompt, expert continuation = chosen, failure continuation = rejected
12	
13	Input:
14	  - classified_errors.jsonl (error_type, failure_step, conversations)
15	  - alfworld_sft.json (expert trajectories)
16	  - (optional) trajectory_dir with failure JSONL files
17	
18	Output per line:
19	  {prompt, chosen, rejected, error_type, gamma_e, correction_span,
20	   task_id, task_type, game_file, failure_step, divergence_step, metadata}
21	
22	Usage:
23	  python src/build_dpo_pairs.py \
24	    --classified outputs/classify_compare_with_hint_20.jsonl \
25	    --expert data/alfworld_sft.json \
26	    --output data/dpo_pairs_v2.jsonl \
27	    --gamma action=0.85,verification=0.92,planning=0.97
28	
29	Dependencies: (stdlib only)
30	"""
31	
32	import argparse
33	import json
34	import logging
35	from collections import Counter, defaultdict
36	from pathlib import Path
37	
38	logger = logging.getLogger("build_dpo")
39	
40	DEFAULT_GAMMA_MAP = {
41	    "action": 0.85,
42	    "verification": 0.92,
43	    "planning": 0.97,
44	}
45	
46	
47	def parse_gamma_arg(s: str) -> dict[str, float]:
48	    """Parse 'action=0.85,verification=0.92,planning=0.97' → dict."""
49	    gamma_map = dict(DEFAULT_GAMMA_MAP)
50	    for item in s.split(","):
51	        k, v = item.strip().split("=")
52	        gamma_map[k.strip()] = float(v.strip())
53	    return gamma_map
54	
55	
56	# ------------------------------------------------------------------
…[truncated 14869 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_failure-mode-analysis_20260513T044723",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-13T04:49:58.949351+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/collect_trajectories_icl.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_failure-mode-analysis_20260513T044723",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/artifacts/collect_trajectories_icl.py"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-13T04:49:58.949610+00:00_

1	"""ALFWorld trajectory collection with ICL few-shot from expert data.
2	
3	Uses Qwen3-14B-AWQ with task-type-aware ICL demonstrations sampled from
4	expert (SFT) trajectories. Supports dual-GPU collection via --part_num/--part_idx.
5	
6	Usage:
7	  CUDA_VISIBLE_DEVICES=0 python src/collect_trajectories_icl.py \
8	    --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-14B-AWQ \
9	    --gpu 0 --num_tasks 300 --seed 42 \
10	    --part_num 2 --part_idx 0 \
11	    --output_dir data/trajectories_v7_icl_cuda0
12	"""
13	
14	import os
15	import re
16	import json
17	import time
18	import random
19	import logging
20	import argparse
21	from pathlib import Path
22	from collections import defaultdict
23	
24	import yaml
25	import torch
26	import alfworld
27	from alfworld.agents.environment import get_environment
28	from transformers import AutoModelForCausalLM, AutoTokenizer
29	
30	logger = logging.getLogger("collect_traj_icl")
31	
32	PREFIXES = {
33	    "pick_and_place": "put",
34	    "pick_clean_then_place": "clean",
35	    "pick_heat_then_place": "heat",
36	    "pick_cool_then_place": "cool",
37	    "look_at_obj": "examine",
38	    "pick_two_obj": "puttwo",
39	}
40	
41	ALFWORLD_INSTRUCTION = (
42	    "Interact with a household to solve a task. Imagine you are an intelligent "
43	    "agent in a household environment and your target is to perform actions to "
44	    "complete the task goal. At the beginning of your interactions, you will be "
45	    "given the detailed description of the current environment and your goal to "
46	    "accomplish. \nFor each of your turn, you will be given the observation of "
47	    'the last turn. You should first think about the current condition and plan '
48	    'for your future actions, and then output your action in this turn. Your '
49	    'output must strictly follow this format:"Thought: your thoughts.\n'
50	    'Action: your next action".\n\n'
51	    "The available actions are:\n"
52	    "1. go to {recep}\n"
53	    "2. take {obj} from 
…[truncated 13952 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_failure-mode-analysis_20260513T044723",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-13T04:49:58.949811+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/src/etadn_discount.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_failure-mode-analysis_20260513T044723",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/src/etadn_discount.py"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-13T04:49:58.950054+00:00_

1	#!/usr/bin/env python3
2	"""ETADN error-type-aware temporal discount for DMPO.
3	
4	Core formula:
5	    φ(t, T) = γ^t · (1 - γ^(T-t)) / (1 - γ^T)
6	
7	Where:
8	    t = current timestep (0-indexed)
9	    T = total trajectory length
10	    γ = gamma_e (error-type-specific discount factor)
11	
12	γ_e mapping:
13	    action errors      → γ_a = 0.85 (short correction span, concentrated credit)
14	    verification errors → γ_v = 0.92 (medium span, moderate spread)
15	    planning errors     → γ_p = 0.97 (long span, near-uniform credit)
16	
17	Integration with DPO/DMPO:
18	    Standard DPO loss: L = -log σ(β · (log π(y_w|x) - log π(y_l|x)))
19	    DMPO adds per-step weighting: replace uniform sum with φ-weighted sum
20	    ETADN: γ in φ varies by error_type of the (chosen, rejected) pair
21	
22	Dependencies: torch only
23	"""
24	import torch
25	import torch.nn.functional as F
26	from dataclasses import dataclass
27	
28	
29	@dataclass
30	class ETADNConfig:
31	    gamma_action: float = 0.85
32	    gamma_verification: float = 0.92
33	    gamma_planning: float = 0.97
34	    beta: float = 0.1
35	    label_smoothing: float = 0.0
36	
37	
38	def phi(t: int, T: int, gamma: float) -> float:
39	    """DMPO credit assignment weight for timestep t of T.
40	
41	    φ(t, T) = γ^t · (1 - γ^(T-t)) / (1 - γ^T)
42	
43	    Sums to 1 over t ∈ [0, T-1] for any γ ∈ (0, 1).
44	    """
45	    if T <= 0:
46	        return 0.0
47	    if abs(gamma - 1.0) < 1e-8:
48	        return 1.0 / T
49	    if abs(gamma) < 1e-12:
50	        return 1.0 if t == 0 else 0.0
51	    numerator = (gamma ** t) * (1.0 - gamma ** (T - t))
52	    denominator = 1.0 - gamma ** T
53	    return numerator / denominator
54	
55	
56	def compute_discount_weights(T: int, gamma: float) -> torch.Tensor:
57	    """φ weight vector of length T. Returns shape (T,) float32 tensor."""
58	    if T <= 0:
59	        return torch.tensor([], dtype=torch.float32)
60	    if abs(gamma - 1.0) < 1e-8:
61	        return torch.full((T,), 1.0 / T, dtype
…[truncated 11188 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_failure-mode-analysis_20260513T044723",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-13T04:49:58.950354+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/src/analyze_failure_modes.py",
  "content": "\"\"\"Failure mode descriptive analysis for ETADN paper.\n\nAnalyzes divergence patterns between failure trajectories and expert trajectories.\nProduces structured JSON and Markdown report for paper's failure mode characterization.\n\nInput: v7 trajectory JSONL files + expert alfworld_sft.json\nOutput: failure_mode_summary.json + failure_mode_report.md\n\nUsage:\n  python src/analyze_failure_modes.py \\\n    --failure_dir data/trajectories_v7_icl \\\n    --expert_file data/alfworld_sft.json \\\n    --output_dir outputs/failure_analysis\n\"\"\"\n\nimport argparse\nimport json\nimport math\nimport statistics\nfrom collections import Counter, defaultdict\nfrom pathlib import Path\n\n\n# ---------------------------------------------------------------------------\n# Task type mapping\n# ---------------------------------------------------------------------------\n\nTASK_TYPE_FROM_PATH = {\n    \"pick_and_place\": \"pick_and_place\",\n    \"pick_clean_then_place\": \"clean\",\n    \"pick_heat_then_place\": \"heat\",\n    \"pick_cool_then_place\": \"cool\",\n    \"look_at_obj\": \"examine\",\n    \"pick_two_obj\": \"pick_two\",\n}\n\nCANONICAL_TASK_TYPES = [\"pick_and_place\", \"clean\", \"heat\", \"cool\", \"examine\", \"pick_two\"]\n\n\ndef get_task_type(game_file: str) -> str:\n    \"\"\"Infer canonical task type from game_file path.\"\"\"\n    for key, canonical in TASK_TYPE_FROM_PATH.items():\n        if f\"/{key}\" in game_file or game_file.startswith(key):\n            return canonical\n    return \"unknown\"\n\n\ndef normalize_game_file(game_file: str) -> str:\n    \"\"\"Extract &lt;task_dir>/&lt;trial_dir> as matching key.\"\"\"\n    gf = game_file.rstrip(\"/\")\n    if gf.endswith(\"/game.tw-pddl\"):\n        gf = gf[: -len(\"/game.tw-pddl\")]\n    parts = gf.split(\"/\")\n    return \"/\".join(parts[-2:]) if len(parts) >= 2 else gf\n\n\n# ---------------------------------------------------------------------------\n# Message helpers (handle both formats)\n# ---------------------------------------------------------------------------\n\ndef _role(msg: dict) -> str:\n    return msg.get(\"role\") or {\"human\": \"user\", \"gpt\": \"assistant\"}.get(msg.get(\"from\", \"\"), \"\")\n\n\ndef _content(msg: dict) -> str:\n    return msg.get(\"content\") or msg.get(\"value\", \"\")\n\n\ndef find_task_start(conversations: list) -> int:\n    \"\"\"Index of first action step after the last 'Your task is to:' message.\"\"\"\n    task_desc_idx = -1\n    for i, msg in enumerate(conversations):\n        if _role(msg) in (\"user\", \"human\") and \"Your task is to:\" in _content(msg):\n            task_desc_idx = i\n\n    search_from = task_desc_idx + 1 if task_desc_idx >= 0 else 0\n    for i in range(search_from, len(conversations)):\n        if _role(conversations[i]) in (\"assistant\", \"gpt\") and \"Action:\" in _content(conversations[i]):\n            return i\n    return len(conversations)\n\n\ndef extract_steps(conversations: list, start_idx: int) -> list[tuple[dict, dict | None]]:\n    \"\"\"Extract (action_msg, obs_msg|None) pairs from start_idx onward.\"\"\"\n    steps = []\n    i = start_idx\n    while i < len(conversations):\n        if _role(conversations[i]) in (\"assistant\", \"gpt\"):\n            action = conversations[i]\n            obs = None\n            if i + 1 < len(conversations) and _role(conversations[i + 1]) in (\"user\", \"human\"):\n                obs = conversations[i + 1]\n                i += 2\n            else:\n                i += 1\n            steps.append((action, obs))\n        else:\n            i += 1\n    return steps\n\n\ndef extract_action_text(content: str) -> str:\n    \"\"\"Extract and normalize 'Action: ...' from a step message.\"\"\"\n    for line in content.split(\"\\n\"):\n        stripped = line.strip()\n        if stripped.lower().startswith(\"action:\"):\n            return \" \".join(stripped[len(\"action:\"):].split()).lower()\n    return \" \".join(content.split()).lower()\n\n\n# ---------------------------------------------------------------------------\n# Divergence computation\n# ---------------------------------------------------------------------------\n\ndef find_divergence_point(expert_steps, fail_steps) -> int:\n    \"\"\"First step index where expert and failure take different actions.\"\"\"\n    min_len = min(len(expert_steps), len(fail_steps))\n    for i in range(min_len):\n        ea = extract_action_text(_content(expert_steps[i][0]))\n        fa = extract_action_text(_content(fail_steps[i][0]))\n        if ea != fa:\n            return i\n    return min_len\n\n\ndef compute_divergence(fail_traj: dict, expert: dict) -> dict | None:\n    \"\"\"Compute divergence metrics for a failure trajectory matched to an expert.\n\n    Returns dict with divergence_point, expert_length, d, correction_span,\n    or None if computation fails.\n    \"\"\"\n    fail_convs = fail_traj.get(\"conversations\", [])\n    expert_convs = expert.get(\"conversations\", [])\n    if not fail_convs or not expert_convs:\n        return None\n\n    fail_start = find_task_start(fail_convs)\n    expert_start = find_task_start(expert_convs)\n\n    fail_steps = extract_steps(fail_convs, fail_start)\n    expert_steps = extract_steps(expert_convs, expert_start)\n\n    if not fail_steps or not expert_steps:\n        return None\n\n    div_point = find_divergence_point(expert_steps, fail_steps)\n    expert_len = len(expert_steps)\n    d = div_point / expert_len if expert_len > 0 else 0.0\n    correction_span = expert_len - div_point\n\n    return {\n        \"divergence_point\": div_point,\n        \"expert_length\": expert_len,\n        \"failure_length\": len(fail_steps),\n        \"d\": d,\n        \"correction_span\": correction_span,\n    }\n\n\n# ---------------------------------------------------------------------------\n# γ(d) mapping\n# ---------------------------------------------------------------------------\n\ndef gamma_from_d(d: float, gamma_min: float = 0.85, gamma_max: float = 0.97) -> float:\n    \"\"\"Map divergence position d ∈ [0,1] to γ via linear interpolation.\n\n    Early divergence (d→0) → γ_min (action-error-like, concentrated credit).\n    Late divergence (d→1) → γ_max (planning-error-like, spread credit).\n    \"\"\"\n    return gamma_min + d * (gamma_max - gamma_min)\n\n\n# ---------------------------------------------------------------------------\n# Data loading\n# ---------------------------------------------------------------------------\n\ndef load_trajectories(failure_dir: str) -> list[dict]:\n    \"\"\"Load all trajectory JSONL files from a directory.\"\"\"\n    records = []\n    p = Path(failure_dir)\n    for jsonl_file in sorted(p.glob(\"*.jsonl\")):\n        with open(jsonl_file) as f:\n            for line in f:\n                if line.strip():\n                    records.append(json.loads(line))\n    return records\n\n\ndef load_expert_index(expert_file: str) -> dict[str, dict]:\n    \"\"\"Load expert trajectories indexed by normalized game_file.\"\"\"\n    with open(expert_file) as f:\n        experts = json.load(f)\n    return {normalize_game_file(ex[\"game_file\"]): ex for ex in experts}\n\n\n# ---------------------------------------------------------------------------\n# Analysis\n# ---------------------------------------------------------------------------\n\ndef analyze(trajectories: list[dict], expert_index: dict[str, dict],\n            gamma_min: float = 0.85, gamma_max: float = 0.97) -> dict:\n    \"\"\"Run all failure mode analyses. Returns structured results dict.\"\"\"\n\n    # -- 1. Basic statistics --\n    total = len(trajectories)\n    successes = [t for t in trajectories if t.get(\"reward\")]\n    failures = [t for t in trajectories if not t.get(\"reward\")]\n    n_success = len(successes)\n    n_failure = len(failures)\n    success_rate = n_success / total if total > 0 else 0.0\n\n    # Per-task-type success rate\n    type_total = Counter()\n    type_success = Counter()\n    for t in trajectories:\n        tt = t.get(\"task_type\") or get_task_type(t.get(\"game_file\", \"\"))\n        type_total[tt] += 1\n        if t.get(\"reward\"):\n            type_success[tt] += 1\n\n    per_type_sr = {}\n    for tt in CANONICAL_TASK_TYPES:\n        tot = type_total.get(tt, 0)\n        suc = type_success.get(tt, 0)\n        per_type_sr[tt] = {\n            \"total\": tot,\n            \"success\": suc,\n            \"failure\": tot - suc,\n            \"success_rate\": suc / tot if tot > 0 else None,\n        }\n\n    basic_stats = {\n        \"total_tasks\": total,\n        \"success\": n_success,\n        \"failure\": n_failure,\n        \"success_rate\": success_rate,\n        \"per_task_type\": per_type_sr,\n    }\n\n    # -- 4. Expert/Failure matching --\n    exact_match = 0\n    template_match = 0\n    unmatched = 0\n    matched_failures = []\n\n    for t in failures:\n        gf = t.get(\"game_file\", \"\")\n        key = normalize_game_file(gf)\n        expert = expert_index.get(key)\n\n        if expert is not None:\n            exact_match += 1\n            div_info = compute_divergence(t, expert)\n            if div_info is not None:\n                tt = t.get(\"task_type\") or get_task_type(gf)\n                matched_failures.append({\n                    \"task_type\": tt,\n                    \"game_file\": gf,\n                    **div_info,\n                })\n        else:\n            tt = t.get(\"task_type\") or get_task_type(gf)\n            found_template = False\n            for ek, ev in expert_index.items():\n                expert_tt = get_task_type(ev.get(\"game_file\", \"\"))\n                if expert_tt == tt:\n                    found_template = True\n                    break\n            if found_template:\n                template_match += 1\n            else:\n                unmatched += 1\n\n    match_stats = {\n        \"exact_match\": exact_match,\n        \"exact_match_rate\": exact_match / n_failure if n_failure > 0 else 0.0,\n        \"template_match_only\": template_match,\n        \"template_match_rate\": (exact_match + template_match) / n_failure if n_failure > 0 else 0.0,\n        \"unmatched\": unmatched,\n        \"divergence_computed\": len(matched_failures),\n    }\n\n    # -- 2. Divergence analysis --\n    d_values = [m[\"d\"] for m in matched_failures]\n    d_by_type = defaultdict(list)\n    for m in matched_failures:\n        d_by_type[m[\"task_type\"]].append(m[\"d\"])\n\n    bins = [(i / 10, (i + 1) / 10) for i in range(10)]\n    bin_labels = [f\"{lo:.1f}-{hi:.1f}\" for lo, hi in bins]\n    histogram = {label: 0 for label in bin_labels}\n    for d in d_values:\n        idx = min(int(d * 10), 9)\n        histogram[bin_labels[idx]] += 1\n\n    early = [d for d in d_values if d < 0.33]\n    mid = [d for d in d_values if 0.33 <= d < 0.67]\n    late = [d for d in d_values if d >= 0.67]\n\n    def _dist_stats(vals):\n        if not vals:\n            return None\n        return {\n            \"n\": len(vals),\n            \"mean\": statistics.mean(vals),\n            \"median\": statistics.median(vals),\n            \"std\": statistics.stdev(vals) if len(vals) > 1 else 0.0,\n            \"min\": min(vals),\n            \"max\": max(vals),\n            \"q1\": statistics.quantiles(vals, n=4)[0] if len(vals) >= 2 else vals[0],\n            \"q3\": statistics.quantiles(vals, n=4)[2] if len(vals) >= 2 else vals[0],\n        }\n\n    per_type_d = {}\n    for tt in CANONICAL_TASK_TYPES:\n        per_type_d[tt] = _dist_stats(d_by_type.get(tt, []))\n\n    divergence_analysis = {\n        \"overall\": _dist_stats(d_values),\n        \"histogram\": histogram,\n        \"temporal_groups\": {\n            \"early_d_lt_0.33\": {\"n\": len(early), \"mean_d\": statistics.mean(early) if early else None},\n            \"mid_0.33_le_d_lt_0.67\": {\"n\": len(mid), \"mean_d\": statistics.mean(mid) if mid else None},\n            \"late_d_ge_0.67\": {\"n\": len(late), \"mean_d\": statistics.mean(late) if late else None},\n        },\n        \"per_task_type\": per_type_d,\n    }\n\n    # -- 3. γ(d) mapping preview --\n    gamma_values = [gamma_from_d(d, gamma_min, gamma_max) for d in d_values]\n    gamma_analysis = {\n        \"gamma_min\": gamma_min,\n        \"gamma_max\": gamma_max,\n        \"distribution\": _dist_stats(gamma_values) if gamma_values else None,\n        \"temporal_group_gamma\": {\n            \"early\": statistics.mean([gamma_from_d(d, gamma_min, gamma_max) for d in early]) if early else None,\n            \"mid\": statistics.mean([gamma_from_d(d, gamma_min, gamma_max) for d in mid]) if mid else None,\n            \"late\": statistics.mean([gamma_from_d(d, gamma_min, gamma_max) for d in late]) if late else None,\n        },\n    }\n\n    # -- 5. Trajectory length analysis --\n    fail_lengths = [m[\"failure_length\"] for m in matched_failures]\n    expert_lengths = [m[\"expert_length\"] for m in matched_failures]\n    correction_spans = [m[\"correction_span\"] for m in matched_failures]\n\n    length_analysis = {\n        \"failure_trajectory_length\": _dist_stats(fail_lengths),\n        \"expert_trajectory_length\": _dist_stats(expert_lengths),\n        \"correction_span\": _dist_stats(correction_spans),\n    }\n\n    return {\n        \"basic_stats\": basic_stats,\n        \"divergence_analysis\": divergence_analysis,\n        \"gamma_mapping_preview\": gamma_analysis,\n        \"match_stats\": match_stats,\n        \"length_analysis\": length_analysis,\n    }\n\n\n# ---------------------------------------------------------------------------\n# Report generation\n# ---------------------------------------------------------------------------\n\ndef _fmt(val, decimals=3):\n    if val is None:\n        return \"-\"\n    if isinstance(val, float):\n        return f\"{val:.{decimals}f}\"\n    return str(val)\n\n\ndef generate_markdown(results: dict) -> str:\n    \"\"\"Generate Markdown report from analysis results.\"\"\"\n    lines = []\n    bs = results[\"basic_stats\"]\n    da = results[\"divergence_analysis\"]\n    gm = results[\"gamma_mapping_preview\"]\n    ms = results[\"match_stats\"]\n    la = results[\"length_analysis\"]\n\n    # -- Section 1 --\n    lines.append(\"# Failure Mode Analysis Report\\n\")\n    lines.append(\"## 1. Basic Statistics\\n\")\n    lines.append(f\"| Metric | Value |\")\n    lines.append(f\"|--------|-------|\")\n    lines.append(f\"| Total tasks | {bs['total_tasks']} |\")\n    lines.append(f\"| Success | {bs['success']} |\")\n    lines.append(f\"| Failure | {bs['failure']} |\")\n    lines.append(f\"| Success rate | {_fmt(bs['success_rate'])} |\")\n    lines.append(\"\")\n\n    lines.append(\"### Per-task-type Success Rate\\n\")\n    lines.append(\"| Task Type | Total | Success | Failure | Success Rate |\")\n    lines.append(\"|-----------|-------|---------|---------|--------------|\")\n    for tt in CANONICAL_TASK_TYPES:\n        info = bs[\"per_task_type\"].get(tt, {})\n        lines.append(\n            f\"| {tt} | {info.get('total', 0)} | {info.get('success', 0)} \"\n            f\"| {info.get('failure', 0)} | {_fmt(info.get('success_rate'))} |\"\n        )\n    lines.append(\"\")\n\n    # -- Section 2 --\n    lines.append(\"## 2. Divergence Analysis\\n\")\n    ov = da.get(\"overall\")\n    if ov:\n        lines.append(f\"Divergence position d = divergence_point / expert_length\\n\")\n        lines.append(\"| Statistic | Value |\")\n        lines.append(\"|-----------|-------|\")\n        for k in (\"n\", \"mean\", \"median\", \"std\", \"min\", \"max\", \"q1\", \"q3\"):\n            lines.append(f\"| {k} | {_fmt(ov[k])} |\")\n        lines.append(\"\")\n\n    lines.append(\"### d-value Histogram\\n\")\n    lines.append(\"| Bin | Count |\")\n    lines.append(\"|-----|-------|\")\n    for bin_label, count in da[\"histogram\"].items():\n        lines.append(f\"| {bin_label} | {count} |\")\n    lines.append(\"\")\n\n    lines.append(\"### Temporal Groups\\n\")\n    lines.append(\"| Group | n | Mean d |\")\n    lines.append(\"|-------|---|--------|\")\n    tg = da[\"temporal_groups\"]\n    for label, key in [(\"Early (d<0.33)\", \"early_d_lt_0.33\"),\n                        (\"Mid (0.33≤d<0.67)\", \"mid_0.33_le_d_lt_0.67\"),\n                        (\"Late (d≥0.67)\", \"late_d_ge_0.67\")]:\n        g = tg[key]\n        lines.append(f\"| {label} | {g['n']} | {_fmt(g.get('mean_d'))} |\")\n    lines.append(\"\")\n\n    lines.append(\"### Per-task-type d Distribution\\n\")\n    lines.append(\"| Task Type | n | Mean | Median | Std |\")\n    lines.append(\"|-----------|---|------|--------|-----|\")\n    for tt in CANONICAL_TASK_TYPES:\n        info = da[\"per_task_type\"].get(tt)\n        if info:\n            lines.append(\n                f\"| {tt} | {info['n']} | {_fmt(info['mean'])} \"\n                f\"| {_fmt(info['median'])} | {_fmt(info['std'])} |\"\n            )\n        else:\n            lines.append(f\"| {tt} | 0 | - | - | - |\")\n    lines.append(\"\")\n\n    # -- Section 3 --\n    lines.append(\"## 3. γ(d) Mapping Preview\\n\")\n    lines.append(f\"γ(d) = γ_min + d·(γ_max - γ_min), γ_min={gm['gamma_min']}, γ_max={gm['gamma_max']}\\n\")\n    gd = gm.get(\"distribution\")\n    if gd:\n        lines.append(\"| Statistic | γ value |\")\n        lines.append(\"|-----------|---------|\")\n        for k in (\"mean\", \"median\", \"std\", \"min\", \"max\"):\n            lines.append(f\"| {k} | {_fmt(gd[k], 4)} |\")\n        lines.append(\"\")\n\n    lines.append(\"### Mean γ by Temporal Group\\n\")\n    lines.append(\"| Group | Mean γ |\")\n    lines.append(\"|-------|--------|\")\n    tgg = gm[\"temporal_group_gamma\"]\n    for label, key in [(\"Early\", \"early\"), (\"Mid\", \"mid\"), (\"Late\", \"late\")]:\n        lines.append(f\"| {label} | {_fmt(tgg.get(key), 4)} |\")\n    lines.append(\"\")\n\n    # -- Section 4 --\n    lines.append(\"## 4. Expert/Failure Matching\\n\")\n    lines.append(\"| Metric | Value |\")\n    lines.append(\"|--------|-------|\")\n    lines.append(f\"| Exact match (game_file) | {ms['exact_match']} ({_fmt(ms['exact_match_rate'])}) |\")\n    lines.append(f\"| Template match (same task type) | {ms['template_match_only']} |\")\n    lines.append(f\"| Combined match rate | {_fmt(ms['template_match_rate'])} |\")\n    lines.append(f\"| Unmatched failures | {ms['unmatched']} |\")\n    lines.append(f\"| Divergence computed | {ms['divergence_computed']} |\")\n    lines.append(\"\")\n\n    # -- Section 5 --\n    lines.append(\"## 5. Trajectory Length Analysis\\n\")\n    lines.append(\"| Metric | Failure | Expert | Correction Span |\")\n    lines.append(\"|--------|---------|--------|-----------------|\")\n    fl = la.get(\"failure_trajectory_length\")\n    el = la.get(\"expert_trajectory_length\")\n    cs = la.get(\"correction_span\")\n    for stat in (\"n\", \"mean\", \"median\", \"std\", \"min\", \"max\"):\n        lines.append(\n            f\"| {stat} | {_fmt(fl.get(stat) if fl else None)} \"\n            f\"| {_fmt(el.get(stat) if el else None)} \"\n            f\"| {_fmt(cs.get(stat) if cs else None)} |\"\n        )\n    lines.append(\"\")\n\n    return \"\\n\".join(lines)\n\n\ndef print_summary(results: dict):\n    \"\"\"Print concise summary to stdout.\"\"\"\n    bs = results[\"basic_stats\"]\n    da = results[\"divergence_analysis\"]\n    ms = results[\"match_stats\"]\n\n    print(f\"\\n{'=' * 55}\")\n    print(\"FAILURE MODE ANALYSIS SUMMARY\")\n    print(f\"{'=' * 55}\")\n    print(f\"Tasks: {bs['total_tasks']}  Success: {bs['success']}  \"\n          f\"Failure: {bs['failure']}  SR: {bs['success_rate']:.3f}\")\n\n    print(f\"\\nPer-type SR:\")\n    for tt in CANONICAL_TASK_TYPES:\n        info = bs[\"per_task_type\"].get(tt, {})\n        sr = info.get(\"success_rate\")\n        sr_str = f\"{sr:.3f}\" if sr is not None else \"-\"\n        print(f\"  {tt:<16} {info.get('total', 0):>4} tasks  SR={sr_str}\")\n\n    print(f\"\\nMatching: exact={ms['exact_match']}  \"\n          f\"template_only={ms['template_match_only']}  \"\n          f\"unmatched={ms['unmatched']}  \"\n          f\"divergence_computed={ms['divergence_computed']}\")\n\n    ov = da.get(\"overall\")\n    if ov:\n        print(f\"\\nDivergence d (n={ov['n']}):\")\n        print(f\"  mean={ov['mean']:.3f}  median={ov['median']:.3f}  \"\n              f\"std={ov['std']:.3f}  [{ov['min']:.3f}, {ov['max']:.3f}]\")\n\n    tg = da[\"temporal_groups\"]\n    print(f\"\\nTemporal groups:\")\n    for label, key in [(\"Early  d<0.33 \", \"early_d_lt_0.33\"),\n                        (\"Mid    0.33-0.67\", \"mid_0.33_le_d_lt_0.67\"),\n                        (\"Late   d≥0.67 \", \"late_d_ge_0.67\")]:\n        g = tg[key]\n        print(f\"  {label}  n={g['n']}\")\n\n    print(f\"{'=' * 55}\")\n\n\n# ---------------------------------------------------------------------------\n# CLI\n# ---------------------------------------------------------------------------\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Failure mode descriptive analysis for ETADN paper\"\n    )\n    parser.add_argument(\"--failure_dir\", type=str, required=True,\n                        help=\"Directory with trajectory JSONL files\")\n    parser.add_argument(\"--expert_file\", type=str, required=True,\n                        help=\"Expert trajectories JSON (alfworld_sft.json)\")\n    parser.add_argument(\"--output_dir\", type=str, required=True,\n                        help=\"Output directory for results\")\n    parser.add_argument(\"--gamma_min\", type=float, default=0.85,\n                        help=\"γ_min for γ(d) mapping (default: 0.85)\")\n    parser.add_argument(\"--gamma_max\", type=float, default=0.97,\n                        help=\"γ_max for γ(d) mapping (default: 0.97)\")\n    args = parser.parse_args()\n\n    trajectories = load_trajectories(args.failure_dir)\n    if not trajectories:\n        print(f\"ERROR: No trajectories found in {args.failure_dir}\")\n        return\n\n    expert_index = load_expert_index(args.expert_file)\n    print(f\"Loaded {len(trajectories)} trajectories, {len(expert_index)} experts\")\n\n    results = analyze(trajectories, expert_index, args.gamma_min, args.gamma_max)\n\n    out = Path(args.output_dir)\n    out.mkdir(parents=True, exist_ok=True)\n\n    json_path = out / \"failure_mode_summary.json\"\n    with open(json_path, \"w\") as f:\n        json.dump(results, f, indent=2, ensure_ascii=False)\n\n    md_path = out / \"failure_mode_report.md\"\n    report = generate_markdown(results)\n    with open(md_path, \"w\") as f:\n        f.write(report)\n\n    print_summary(results)\n    print(f\"\\nOutput: {json_path}\")\n    print(f\"        {md_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_failure-mode-analysis_20260513T044723",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/src/analyze_failure_modes.py",
    "content": "\"\"\"Failure mode descriptive analysis for ETADN paper.\n\nAnalyzes divergence patterns between failure trajectories and expert trajectories.\nProduces structured JSON and Markdown report for paper's failure mode characterization.\n\nInput: v7 trajectory JSONL files + expert alfworld_sft.json\nOutput: failure_mode_summary.json + failure_mode_report.md\n\nUsage:\n  python src/analyze_failure_modes.py \\\n    --failure_dir data/trajectories_v7_icl \\\n    --expert_file data/alfworld_sft.json \\\n    --output_dir outputs/failure_analysis\n\"\"\"\n\nimport argparse\nimport json\nimport math\nimport statistics\nfrom collections import Counter, defaultdict\nfrom pathlib import Path\n\n\n# ---------------------------------------------------------------------------\n# Task type mapping\n# ---------------------------------------------------------------------------\n\nTASK_TYPE_FROM_PATH = {\n    \"pick_and_place\": \"pick_and_place\",\n    \"pick_clean_then_place\": \"clean\",\n    \"pick_heat_then_place\": \"heat\",\n    \"pick_cool_then_place\": \"cool\",\n    \"look_at_obj\": \"examine\",\n    \"pick_two_obj\": \"pick_two\",\n}\n\nCANONICAL_TASK_TYPES = [\"pick_and_place\", \"clean\", \"heat\", \"cool\", \"examine\", \"pick_two\"]\n\n\ndef get_task_type(game_file: str) -> str:\n    \"\"\"Infer canonical task type from game_file path.\"\"\"\n    for key, canonical in TASK_TYPE_FROM_PATH.items():\n        if f\"/{key}\" in game_file or game_file.startswith(key):\n            return canonical\n    return \"unknown\"\n\n\ndef normalize_game_file(game_file: str) -> str:\n    \"\"\"Extract &lt;task_dir>/&lt;trial_dir> as matching key.\"\"\"\n    gf = game_file.rstrip(\"/\")\n    if gf.endswith(\"/game.tw-pddl\"):\n        gf = gf[: -len(\"/game.tw-pddl\")]\n    parts = gf.split(\"/\")\n    return \"/\".join(parts[-2:]) if len(parts) >= 2 else gf\n\n\n# ---------------------------------------------------------------------------\n# Message helpers (handle both formats)\n# ---------------------------------------------------------------------------\n\ndef _role(msg: dict) -> str:\n    return msg.get(\"role\") or {\"human\": \"user\", \"gpt\": \"assistant\"}.get(msg.get(\"from\", \"\"), \"\")\n\n\ndef _content(msg: dict) -> str:\n    return msg.get(\"content\") or msg.get(\"value\", \"\")\n\n\ndef find_task_start(conversations: list) -> int:\n    \"\"\"Index of first action step after the last 'Your task is to:' message.\"\"\"\n    task_desc_idx = -1\n    for i, msg in enumerate(conversations):\n        if _role(msg) in (\"user\", \"human\") and \"Your task is to:\" in _content(msg):\n            task_desc_idx = i\n\n    search_from = task_desc_idx + 1 if task_desc_idx >= 0 else 0\n    for i in range(search_from, len(conversations)):\n        if _role(conversations[i]) in (\"assistant\", \"gpt\") and \"Action:\" in _content(conversations[i]):\n            return i\n    return len(conversations)\n\n\ndef extract_steps(conversations: list, start_idx: int) -> list[tuple[dict, dict | None]]:\n    \"\"\"Extract (action_msg, obs_msg|None) pairs from start_idx onward.\"\"\"\n    steps = []\n    i = start_idx\n    while i < len(conversations):\n        if _role(conversations[i]) in (\"assistant\", \"gpt\"):\n            action = conversations[i]\n            obs = None\n            if i + 1 < len(conversations) and _role(conversations[i + 1]) in (\"user\", \"human\"):\n                obs = conversations[i + 1]\n                i += 2\n            else:\n                i += 1\n            steps.append((action, obs))\n        else:\n            i += 1\n    return steps\n\n\ndef extract_action_text(content: str) -> str:\n    \"\"\"Extract and normalize 'Action: ...' from a step message.\"\"\"\n    for line in content.split(\"\\n\"):\n        stripped = line.strip()\n        if stripped.lower().startswith(\"action:\"):\n            return \" \".join(stripped[len(\"action:\"):].split()).lower()\n    return \" \".join(content.split()).lower()\n\n\n# ---------------------------------------------------------------------------\n# Divergence computation\n# ---------------------------------------------------------------------------\n\ndef find_divergence_point(expert_steps, fail_steps) -> int:\n    \"\"\"First step index where expert and failure take different actions.\"\"\"\n    min_len = min(len(expert_steps), len(fail_steps))\n    for i in range(min_len):\n        ea = extract_action_text(_content(expert_steps[i][0]))\n        fa = extract_action_text(_content(fail_steps[i][0]))\n        if ea != fa:\n            return i\n    return min_len\n\n\ndef compute_divergence(fail_traj: dict, expert: dict) -> dict | None:\n    \"\"\"Compute divergence metrics for a failure trajectory matched to an expert.\n\n    Returns dict with divergence_point, expert_length, d, correction_span,\n    or None if computation fails.\n    \"\"\"\n    fail_convs = fail_traj.get(\"conversations\", [])\n    expert_convs = expert.get(\"conversations\", [])\n    if not fail_convs or not expert_convs:\n        return None\n\n    fail_start = find_task_start(fail_convs)\n    expert_start = find_task_start(expert_convs)\n\n    fail_steps = extract_steps(fail_convs, fail_start)\n    expert_steps = extract_steps(expert_convs, expert_start)\n\n    if not fail_steps or not expert_steps:\n        return None\n\n    div_point = find_divergence_point(expert_steps, fail_steps)\n    expert_len = len(expert_steps)\n    d = div_point / expert_len if expert_len > 0 else 0.0\n    correction_span = expert_len - div_point\n\n    return {\n        \"divergence_point\": div_point,\n        \"expert_length\": expert_len,\n        \"failure_length\": len(fail_steps),\n        \"d\": d,\n        \"correction_span\": correction_span,\n    }\n\n\n# ---------------------------------------------------------------------------\n# γ(d) mapping\n# ---------------------------------------------------------------------------\n\ndef gamma_from_d(d: float, gamma_min: float = 0.85, gamma_max: float = 0.97) -> float:\n    \"\"\"Map divergence position d ∈ [0,1] to γ via linear interpolation.\n\n    Early divergence (d→0) → γ_min (action-error-like, concentrated credit).\n    Late divergence (d→1) → γ_max (planning-error-like, spread credit).\n    \"\"\"\n    return gamma_min + d * (gamma_max - gamma_min)\n\n\n# ---------------------------------------------------------------------------\n# Data loading\n# ---------------------------------------------------------------------------\n\ndef load_trajectories(failure_dir: str) -> list[dict]:\n    \"\"\"Load all trajectory JSONL files from a directory.\"\"\"\n    records = []\n    p = Path(failure_dir)\n    for jsonl_file in sorted(p.glob(\"*.jsonl\")):\n        with open(jsonl_file) as f:\n            for line in f:\n                if line.strip():\n                    records.append(json.loads(line))\n    return records\n\n\ndef load_expert_index(expert_file: str) -> dict[str, dict]:\n    \"\"\"Load expert trajectories indexed by normalized game_file.\"\"\"\n    with open(expert_file) as f:\n        experts = json.load(f)\n    return {normalize_game_file(ex[\"game_file\"]): ex for ex in experts}\n\n\n# ---------------------------------------------------------------------------\n# Analysis\n# ---------------------------------------------------------------------------\n\ndef analyze(trajectories: list[dict], expert_index: dict[str, dict],\n            gamma_min: float = 0.85, gamma_max: float = 0.97) -> dict:\n    \"\"\"Run all failure mode analyses. Returns structured results dict.\"\"\"\n\n    # -- 1. Basic statistics --\n    total = len(trajectories)\n    successes = [t for t in trajectories if t.get(\"reward\")]\n    failures = [t for t in trajectories if not t.get(\"reward\")]\n    n_success = len(successes)\n    n_failure = len(failures)\n    success_rate = n_success / total if total > 0 else 0.0\n\n    # Per-task-type success rate\n    type_total = Counter()\n    type_success = Counter()\n    for t in trajectories:\n        tt = t.get(\"task_type\") or get_task_type(t.get(\"game_file\", \"\"))\n        type_total[tt] += 1\n        if t.get(\"reward\"):\n            type_success[tt] += 1\n\n    per_type_sr = {}\n    for tt in CANONICAL_TASK_TYPES:\n        tot = type_total.get(tt, 0)\n        suc = type_success.get(tt, 0)\n        per_type_sr[tt] = {\n            \"total\": tot,\n            \"success\": suc,\n            \"failure\": tot - suc,\n            \"success_rate\": suc / tot if tot > 0 else None,\n        }\n\n    basic_stats = {\n        \"total_tasks\": total,\n        \"success\": n_success,\n        \"failure\": n_failure,\n        \"success_rate\": success_rate,\n        \"per_task_type\": per_type_sr,\n    }\n\n    # -- 4. Expert/Failure matching --\n    exact_match = 0\n    template_match = 0\n    unmatched = 0\n    matched_failures = []\n\n    for t in failures:\n        gf = t.get(\"game_file\", \"\")\n        key = normalize_game_file(gf)\n        expert = expert_index.get(key)\n\n        if expert is not None:\n            exact_match += 1\n            div_info = compute_divergence(t, expert)\n            if div_info is not None:\n                tt = t.get(\"task_type\") or get_task_type(gf)\n                matched_failures.append({\n                    \"task_type\": tt,\n                    \"game_file\": gf,\n                    **div_info,\n                })\n        else:\n            tt = t.get(\"task_type\") or get_task_type(gf)\n            found_template = False\n            for ek, ev in expert_index.items():\n                expert_tt = get_task_type(ev.get(\"game_file\", \"\"))\n                if expert_tt == tt:\n                    found_template = True\n                    break\n            if found_template:\n                template_match += 1\n            else:\n                unmatched += 1\n\n    match_stats = {\n        \"exact_match\": exact_match,\n        \"exact_match_rate\": exact_match / n_failure if n_failure > 0 else 0.0,\n        \"template_match_only\": template_match,\n        \"template_match_rate\": (exact_match + template_match) / n_failure if n_failure > 0 else 0.0,\n        \"unmatched\": unmatched,\n        \"divergence_computed\": len(matched_failures),\n    }\n\n    # -- 2. Divergence analysis --\n    d_values = [m[\"d\"] for m in matched_failures]\n    d_by_type = defaultdict(list)\n    for m in matched_failures:\n        d_by_type[m[\"task_type\"]].append(m[\"d\"])\n\n    bins = [(i / 10, (i + 1) / 10) for i in range(10)]\n    bin_labels = [f\"{lo:.1f}-{hi:.1f}\" for lo, hi in bins]\n    histogram = {label: 0 for label in bin_labels}\n    for d in d_values:\n        idx = min(int(d * 10), 9)\n        histogram[bin_labels[idx]] += 1\n\n    early = [d for d in d_values if d < 0.33]\n    mid = [d for d in d_values if 0.33 <= d < 0.67]\n    late = [d for d in d_values if d >= 0.67]\n\n    def _dist_stats(vals):\n        if not vals:\n            return None\n        return {\n            \"n\": len(vals),\n            \"mean\": statistics.mean(vals),\n            \"median\": statistics.median(vals),\n            \"std\": statistics.stdev(vals) if len(vals) > 1 else 0.0,\n            \"min\": min(vals),\n            \"max\": max(vals),\n            \"q1\": statistics.quantiles(vals, n=4)[0] if len(vals) >= 2 else vals[0],\n            \"q3\": statistics.quantiles(vals, n=4)[2] if len(vals) >= 2 else vals[0],\n        }\n\n    per_type_d = {}\n    for tt in CANONICAL_TASK_TYPES:\n        per_type_d[tt] = _dist_stats(d_by_type.get(tt, []))\n\n    divergence_analysis = {\n        \"overall\": _dist_stats(d_values),\n        \"histogram\": histogram,\n        \"temporal_groups\": {\n            \"early_d_lt_0.33\": {\"n\": len(early), \"mean_d\": statistics.mean(early) if early else None},\n            \"mid_0.33_le_d_lt_0.67\": {\"n\": len(mid), \"mean_d\": statistics.mean(mid) if mid else None},\n            \"late_d_ge_0.67\": {\"n\": len(late), \"mean_d\": statistics.mean(late) if late else None},\n        },\n        \"per_task_type\": per_type_d,\n    }\n\n    # -- 3. γ(d) mapping preview --\n    gamma_values = [gamma_from_d(d, gamma_min, gamma_max) for d in d_values]\n    gamma_analysis = {\n        \"gamma_min\": gamma_min,\n        \"gamma_max\": gamma_max,\n        \"distribution\": _dist_stats(gamma_values) if gamma_values else None,\n        \"temporal_group_gamma\": {\n            \"early\": statistics.mean([gamma_from_d(d, gamma_min, gamma_max) for d in early]) if early else None,\n            \"mid\": statistics.mean([gamma_from_d(d, gamma_min, gamma_max) for d in mid]) if mid else None,\n            \"late\": statistics.mean([gamma_from_d(d, gamma_min, gamma_max) for d in late]) if late else None,\n        },\n    }\n\n    # -- 5. Trajectory length analysis --\n    fail_lengths = [m[\"failure_length\"] for m in matched_failures]\n    expert_lengths = [m[\"expert_length\"] for m in matched_failures]\n    correction_spans = [m[\"correction_span\"] for m in matched_failures]\n\n    length_analysis = {\n        \"failure_trajectory_length\": _dist_stats(fail_lengths),\n        \"expert_trajectory_length\": _dist_stats(expert_lengths),\n        \"correction_span\": _dist_stats(correction_spans),\n    }\n\n    return {\n        \"basic_stats\": basic_stats,\n        \"divergence_analysis\": divergence_analysis,\n        \"gamma_mapping_preview\": gamma_analysis,\n        \"match_stats\": match_stats,\n        \"length_analysis\": length_analysis,\n    }\n\n\n# ---------------------------------------------------------------------------\n# Report generation\n# ---------------------------------------------------------------------------\n\ndef _fmt(val, decimals=3):\n    if val is None:\n        return \"-\"\n    if isinstance(val, float):\n        return f\"{val:.{decimals}f}\"\n    return str(val)\n\n\ndef generate_markdown(results: dict) -> str:\n    \"\"\"Generate Markdown report from analysis results.\"\"\"\n    lines = []\n    bs = results[\"basic_stats\"]\n    da = results[\"divergence_analysis\"]\n    gm = results[\"gamma_mapping_preview\"]\n    ms = results[\"match_stats\"]\n    la = results[\"length_analysis\"]\n\n    # -- Section 1 --\n    lines.append(\"# Failure Mode Analysis Report\\n\")\n    lines.append(\"## 1. Basic Statistics\\n\")\n    lines.append(f\"| Metric | Value |\")\n    lines.append(f\"|--------|-------|\")\n    lines.append(f\"| Total tasks | {bs['total_tasks']} |\")\n    lines.append(f\"| Success | {bs['success']} |\")\n    lines.append(f\"| Failure | {bs['failure']} |\")\n    lines.append(f\"| Success rate | {_fmt(bs['success_rate'])} |\")\n    lines.append(\"\")\n\n    lines.append(\"### Per-task-type Success Rate\\n\")\n    lines.append(\"| Task Type | Total | Success | Failure | Success Rate |\")\n    lines.append(\"|-----------|-------|---------|---------|--------------|\")\n    for tt in CANONICAL_TASK_TYPES:\n        info = bs[\"per_task_type\"].get(tt, {})\n        lines.append(\n            f\"| {tt} | {info.get('total', 0)} | {info.get('success', 0)} \"\n            f\"| {info.get('failure', 0)} | {_fmt(info.get('success_rate'))} |\"\n        )\n    lines.append(\"\")\n\n    # -- Section 2 --\n    lines.append(\"## 2. Divergence Analysis\\n\")\n    ov = da.get(\"overall\")\n    if ov:\n        lines.append(f\"Divergence position d = divergence_point / expert_length\\n\")\n        lines.append(\"| Statistic | Value |\")\n        lines.append(\"|-----------|-------|\")\n        for k in (\"n\", \"mean\", \"median\", \"std\", \"min\", \"max\", \"q1\", \"q3\"):\n            lines.append(f\"| {k} | {_fmt(ov[k])} |\")\n        lines.append(\"\")\n\n    lines.append(\"### d-value Histogram\\n\")\n    lines.append(\"| Bin | Count |\")\n    lines.append(\"|-----|-------|\")\n    for bin_label, count in da[\"histogram\"].items():\n        lines.append(f\"| {bin_label} | {count} |\")\n    lines.append(\"\")\n\n    lines.append(\"### Temporal Groups\\n\")\n    lines.append(\"| Group | n | Mean d |\")\n    lines.append(\"|-------|---|--------|\")\n    tg = da[\"temporal_groups\"]\n    for label, key in [(\"Early (d<0.33)\", \"early_d_lt_0.33\"),\n                        (\"Mid (0.33≤d<0.67)\", \"mid_0.33_le_d_lt_0.67\"),\n                        (\"Late (d≥0.67)\", \"late_d_ge_0.67\")]:\n        g = tg[key]\n        lines.append(f\"| {label} | {g['n']} | {_fmt(g.get('mean_d'))} |\")\n    lines.append(\"\")\n\n    lines.append(\"### Per-task-type d Distribution\\n\")\n    lines.append(\"| Task Type | n | Mean | Median | Std |\")\n    lines.append(\"|-----------|---|------|--------|-----|\")\n    for tt in CANONICAL_TASK_TYPES:\n        info = da[\"per_task_type\"].get(tt)\n        if info:\n            lines.append(\n                f\"| {tt} | {info['n']} | {_fmt(info['mean'])} \"\n                f\"| {_fmt(info['median'])} | {_fmt(info['std'])} |\"\n            )\n        else:\n            lines.append(f\"| {tt} | 0 | - | - | - |\")\n    lines.append(\"\")\n\n    # -- Section 3 --\n    lines.append(\"## 3. γ(d) Mapping Preview\\n\")\n    lines.append(f\"γ(d) = γ_min + d·(γ_max - γ_min), γ_min={gm['gamma_min']}, γ_max={gm['gamma_max']}\\n\")\n    gd = gm.get(\"distribution\")\n    if gd:\n        lines.append(\"| Statistic | γ value |\")\n        lines.append(\"|-----------|---------|\")\n        for k in (\"mean\", \"median\", \"std\", \"min\", \"max\"):\n            lines.append(f\"| {k} | {_fmt(gd[k], 4)} |\")\n        lines.append(\"\")\n\n    lines.append(\"### Mean γ by Temporal Group\\n\")\n    lines.append(\"| Group | Mean γ |\")\n    lines.append(\"|-------|--------|\")\n    tgg = gm[\"temporal_group_gamma\"]\n    for label, key in [(\"Early\", \"early\"), (\"Mid\", \"mid\"), (\"Late\", \"late\")]:\n        lines.append(f\"| {label} | {_fmt(tgg.get(key), 4)} |\")\n    lines.append(\"\")\n\n    # -- Section 4 --\n    lines.append(\"## 4. Expert/Failure Matching\\n\")\n    lines.append(\"| Metric | Value |\")\n    lines.append(\"|--------|-------|\")\n    lines.append(f\"| Exact match (game_file) | {ms['exact_match']} ({_fmt(ms['exact_match_rate'])}) |\")\n    lines.append(f\"| Template match (same task type) | {ms['template_match_only']} |\")\n    lines.append(f\"| Combined match rate | {_fmt(ms['template_match_rate'])} |\")\n    lines.append(f\"| Unmatched failures | {ms['unmatched']} |\")\n    lines.append(f\"| Divergence computed | {ms['divergence_computed']} |\")\n    lines.append(\"\")\n\n    # -- Section 5 --\n    lines.append(\"## 5. Trajectory Length Analysis\\n\")\n    lines.append(\"| Metric | Failure | Expert | Correction Span |\")\n    lines.append(\"|--------|---------|--------|-----------------|\")\n    fl = la.get(\"failure_trajectory_length\")\n    el = la.get(\"expert_trajectory_length\")\n    cs = la.get(\"correction_span\")\n    for stat in (\"n\", \"mean\", \"median\", \"std\", \"min\", \"max\"):\n        lines.append(\n            f\"| {stat} | {_fmt(fl.get(stat) if fl else None)} \"\n            f\"| {_fmt(el.get(stat) if el else None)} \"\n            f\"| {_fmt(cs.get(stat) if cs else None)} |\"\n        )\n    lines.append(\"\")\n\n    return \"\\n\".join(lines)\n\n\ndef print_summary(results: dict):\n    \"\"\"Print concise summary to stdout.\"\"\"\n    bs = results[\"basic_stats\"]\n    da = results[\"divergence_analysis\"]\n    ms = results[\"match_stats\"]\n\n    print(f\"\\n{'=' * 55}\")\n    print(\"FAILURE MODE ANALYSIS SUMMARY\")\n    print(f\"{'=' * 55}\")\n    print(f\"Tasks: {bs['total_tasks']}  Success: {bs['success']}  \"\n          f\"Failure: {bs['failure']}  SR: {bs['success_rate']:.3f}\")\n\n    print(f\"\\nPer-type SR:\")\n    for tt in CANONICAL_TASK_TYPES:\n        info = bs[\"per_task_type\"].get(tt, {})\n        sr = info.get(\"success_rate\")\n        sr_str = f\"{sr:.3f}\" if sr is not None else \"-\"\n        print(f\"  {tt:<16} {info.get('total', 0):>4} tasks  SR={sr_str}\")\n\n    print(f\"\\nMatching: exact={ms['exact_match']}  \"\n          f\"template_only={ms['template_match_only']}  \"\n          f\"unmatched={ms['unmatched']}  \"\n          f\"divergence_computed={ms['divergence_computed']}\")\n\n    ov = da.get(\"overall\")\n    if ov:\n        print(f\"\\nDivergence d (n={ov['n']}):\")\n        print(f\"  mean={ov['mean']:.3f}  median={ov['median']:.3f}  \"\n              f\"std={ov['std']:.3f}  [{ov['min']:.3f}, {ov['max']:.3f}]\")\n\n    tg = da[\"temporal_groups\"]\n    print(f\"\\nTemporal groups:\")\n    for label, key in [(\"Early  d<0.33 \", \"early_d_lt_0.33\"),\n                        (\"Mid    0.33-0.67\", \"mid_0.33_le_d_lt_0.67\"),\n                        (\"Late   d≥0.67 \", \"late_d_ge_0.67\")]:\n        g = tg[key]\n        print(f\"  {label}  n={g['n']}\")\n\n    print(f\"{'=' * 55}\")\n\n\n# ---------------------------------------------------------------------------\n# CLI\n# ---------------------------------------------------------------------------\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Failure mode descriptive analysis for ETADN paper\"\n    )\n    parser.add_argument(\"--failure_dir\", type=str, required=True,\n                        help=\"Directory with trajectory JSONL files\")\n    parser.add_argument(\"--expert_file\", type=str, required=True,\n                        help=\"Expert trajectories JSON (alfworld_sft.json)\")\n    parser.add_argument(\"--output_dir\", type=str, required=True,\n                        help=\"Output directory for results\")\n    parser.add_argument(\"--gamma_min\", type=float, default=0.85,\n                        help=\"γ_min for γ(d) mapping (default: 0.85)\")\n    parser.add_argument(\"--gamma_max\", type=float, default=0.97,\n                        help=\"γ_max for γ(d) mapping (default: 0.97)\")\n    args = parser.parse_args()\n\n    trajectories = load_trajectories(args.failure_dir)\n    if not trajectories:\n        print(f\"ERROR: No trajectories found in {args.failure_dir}\")\n        return\n\n    expert_index = load_expert_index(args.expert_file)\n    print(f\"Loaded {len(trajectories)} trajectories, {len(expert_index)} experts\")\n\n    results = analyze(trajectories, expert_index, args.gamma_min, args.gamma_max)\n\n    out = Path(args.output_dir)\n    out.mkdir(parents=True, exist_ok=True)\n\n    json_path = out / \"failure_mode_summary.json\"\n    with open(json_path, \"w\") as f:\n        json.dump(results, f, indent=2, ensure_ascii=False)\n\n    md_path = out / \"failure_mode_report.md\"\n    report = generate_markdown(results)\n    with open(md_path, \"w\") as f:\n        f.write(report)\n\n    print_summary(results)\n    print(f\"\\nOutput: {json_path}\")\n    print(f\"        {md_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-13T04:49:58.951044+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/rl-active-probe-fl/src/analyze_failure_modes.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_failure-mode-analysis_20260513T044723",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-13T04:49:58.951233+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python -m py_compile src/analyze_failure_modes.py && echo \"OK\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_failure-mode-analysis_20260513T044723",
  "tool": "Bash",
  "tool_args": {
    "command": "python -m py_compile src/analyze_failure_modes.py && echo \"OK\""
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-13T04:49:58.951363+00:00_

Exit code 127
/bin/bash: line 1: python: command not found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_failure-mode-analysis_20260513T044723",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-13T04:49:58.951486+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -m py_compile src/analyze_failure_modes.py && echo \"OK\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_failure-mode-analysis_20260513T044723",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -m py_compile src/analyze_failure_modes.py && echo \"OK\""
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-13T04:49:58.951604+00:00_

OK

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_failure-mode-analysis_20260513T044723",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-13T04:49:58.951781+00:00_

语法验证通过。脚本写入 `src/analyze_failure_modes.py`，覆盖全部 5 类分析：

1. **基本统计** — 总体成功率 + 6 种 task type 分别统计
2. **Divergence 分析** — d 分布统计、10-bin 直方图、early/mid/late 三组、per-type d 分布
3. **γ(d) 映射预览** — 线性插值 γ(d)=γ_min+d·(γ_max-γ_min)，各组均值 γ
4. **Expert/Failure 匹配** — exact match / template match / unmatched 统计
5. **轨迹长度** — failure vs expert 长度分布 + correction span

输出 `failure_mode_summary.json` + `failure_mode_report.md`，纯 CPU，无 GPU 依赖。divergence 计算逻辑直接复用 `build_dpo_pairs.py` 的 action 对比方式。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_failure-mode-analysis_20260513T044723"
}
```

</details>

---
