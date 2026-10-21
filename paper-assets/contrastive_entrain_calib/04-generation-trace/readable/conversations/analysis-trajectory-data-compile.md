# analysis trajectory data compile

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_analysis_trajectory-data-compile_20260521T112144.jsonl`
- **Structured JSON:** [`7cee3c948dd288e83c04.json`](../../sessions/7c/7cee3c948dd288e83c04.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-21T11:24:29.545050+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_trajectory-data-compile_20260521T112144",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-21T11:24:29.545441+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_trajectory-data-compile_20260521T112144",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T11:24:29.545629+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "contrastive_entrain_calib",
  "filters": "{'status': 'DONE'}",
  "fields": "['metrics', 'parent', 'conclusion', 'status', 'exp_id']",
  "limit": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_trajectory-data-compile_20260521T112144",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "contrastive_entrain_calib",
    "filters": "{'status': 'DONE'}",
    "fields": "['metrics', 'parent', 'conclusion', 'status', 'exp_id']",
    "limit": "0"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-21T11:24:29.546265+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp-003-eval-s2-ckpt3500\": {\"status\": \"DONE\", \"parent\": \"exp-003-s2\", \"conclusion\": \"success\", \"metrics\": {\"sycon_score\": 0.0744, \"tof\": 0.0387, \"nof\": 0.9724, \"n_valid\": 181, \"n_invalid\": 181}}, \"exp-003-eval-s2-ckpt2500\": {\"status\": \"DONE\", \"parent\": \"exp-003-s2\", \"conclusion\": \"success\", \"metrics\": {\"sycon_score\": 0.1046, \"tof\": 0.0552, \"nof\": 0.9724}}, \"exp-003-s2-eval-ckpt2000\": {\"status\": \"DONE\", \"parent\": \"exp-003-s2\", \"conclusion\": \"killed\"}, \"exp-004\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"trend\": \"generally increasing trend with oscillations: early phase ~0.17-0.25, late phase ~0.26-0.30, best=0.301 at ckpt-8000\", \"best_sycon_score\": 0.301, \"best_checkpoint\": \"ckpt-8000\"}}, \"exp-003\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp-003-eval-s2-ckpt2000\": {\"status\": \"DONE\", \"parent\": \"exp-003-s2\", \"conclusion\": \"success\", \"metrics\": {\"sycon_score\": 0.0846}}, \"exp-003-eval-ckpt7500\": {\"status\": \"DONE\", \"parent\": \"exp-003\", \"conclusion\": \"success\", \"metrics\": {\"sycon_score\": 0.1046}}, \"exp-003-eval-ckpt7000-v3\": {\"status\": \"DONE\", \"parent\": \"exp-003\", \"metrics\": {\"sycon_score\": 0.1046}, \"conclusion\": \"success\"}, \"exp-003-eval-s2-ckpt3000\": {\"status\": \"DONE\", \"parent\": \"exp-003-s2\", \"metrics\": {\"sycon_score\": 0.0945, \"tof\": 0.0497, \"nof\": 0.9503}, \"conclusion\": \"success\"}, \"exp-003-eval-ckpt5000-v2\": {\"status\": \"DONE\", \"parent\": \"exp-003\", \"conclusion\": \"success\", \"metrics\": {\"sycon_score\": 0.1144, \"tof\": 0.0608, \"nof\": 0.9669}}, \"exp-003-eval-ckpt6500\": {\"status\": \"DONE\", \"parent\": \"exp-003\", \"metrics\": {\"sycon_score\": 0.1529, \"tof\": 0.0829, \"nof\": 0.9834}, \"conclusion\": \"success\"}, \"exp-003-eval-ckpt6000\": {\"status\": \"DONE\", \"parent\": \"exp-003\", \"metrics\":
…[truncated 18050 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_trajectory-data-compile_20260521T112144",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T11:24:29.546531+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "contrastive_entrain_calib",
  "filters": "{'status': 'RUNNING'}",
  "fields": "['metrics', 'parent', 'status', 'exp_id']",
  "limit": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_trajectory-data-compile_20260521T112144",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "contrastive_entrain_calib",
    "filters": "{'status': 'RUNNING'}",
    "fields": "['metrics', 'parent', 'status', 'exp_id']",
    "limit": "0"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T11:24:29.546686+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp-003-eval-ckpt8000\": {\"status\": \"RUNNING\", \"parent\": \"exp-003\"}, \"exp-003-s2\": {\"status\": \"RUNNING\", \"parent\": \"exp-003\"}}, \"count\": 2, \"total\": 2, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1567}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_trajectory-data-compile_20260521T112144",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T11:24:29.546825+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "contrastive_entrain_calib",
  "filters": "{'status': 'PENDING'}",
  "fields": "['metrics', 'parent', 'status', 'exp_id']",
  "limit": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_trajectory-data-compile_20260521T112144",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "contrastive_entrain_calib",
    "filters": "{'status': 'PENDING'}",
    "fields": "['metrics', 'parent', 'status', 'exp_id']",
    "limit": "0"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T11:24:29.546982+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1707}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_trajectory-data-compile_20260521T112144",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T11:24:29.547124+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "contrastive_entrain_calib",
  "filters": "{'parent': 'exp-004'}",
  "fields": "['metrics', 'parent', 'status', 'exp_id']",
  "limit": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_trajectory-data-compile_20260521T112144",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "contrastive_entrain_calib",
    "filters": "{'parent': 'exp-004'}",
    "fields": "['metrics', 'parent', 'status', 'exp_id']",
    "limit": "0"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T11:24:29.547364+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp-004-eval-ckpt5500\": {\"status\": \"DONE\", \"parent\": \"exp-004\", \"metrics\": {\"ToF\": 0.1381, \"NoF\": 0.8674, \"SYCONScore\": 0.2383, \"n_samples\": 362}}, \"exp-004-eval-ckpt4500\": {\"status\": \"DONE\", \"parent\": \"exp-004\", \"metrics\": {\"ToF\": 0.105, \"NoF\": 0.8785, \"SYCONScore\": 0.1875, \"n_samples\": 362}}, \"exp-004-eval-ckpt7500\": {\"status\": \"DONE\", \"parent\": \"exp-004\", \"metrics\": {\"ToF\": 0.1657, \"NoF\": 0.8453, \"SYCONScore\": 0.2771, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362, \"checkpoint\": \"checkpoint-7500\", \"eval_script\": \"eval_unified_preset.py (D027 standard)\", \"eval_server\": \"westd-28034\", \"vs_vanilla\": \"SYCONScore 0.2771 vs 0.1335 = +107.6%\"}}, \"exp-004-eval-ckpt6500\": {\"status\": \"DONE\", \"parent\": \"exp-004\", \"metrics\": {\"ToF\": 0.1492, \"NoF\": 0.8232, \"SYCONScore\": 0.2526, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362, \"checkpoint\": \"checkpoint-6500\", \"eval_script\": \"eval_unified_preset.py (D027 standard)\", \"eval_server\": \"westd-28034\", \"vs_vanilla\": \"SYCONScore 0.2526 vs 0.1335 = +89.1%\"}}, \"exp-004-eval-ckpt1500\": {\"status\": \"DONE\", \"parent\": \"exp-004\", \"metrics\": {\"ToF\": 0.0939, \"NoF\": 0.8895, \"SYCONScore\": 0.1699, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362, \"checkpoint\": \"checkpoint-1500\", \"eval_script\": \"eval_unified_preset.py (D027 standard)\", \"eval_server\": \"westd-28034\", \"eval_time_sec\": 1741, \"vs_vanilla\": \"SYCONScore 0.1699 vs 0.1335 = +27.3%\"}}, \"exp-004-eval-ckpt3500\": {\"status\": \"DONE\", \"parent\": \"exp-004\", \"metrics\": {\"ToF\": 0.1326, \"NoF\": 0.9006, \"SYCONScore\": 0.2312, \"n_valid\": 181, \"n_invalid\": 181, \"n_total\": 362, \"checkpoint\": \"checkpoint-3500\", \"eval_script\": \"eval_unified_preset.py (D027 standard)\", \"eval_server\": \"westd-28034\", \"vs_vanilla\": \"SYCONScore 0.2312 vs 0.1335 = +73.2%\"}
…[truncated 3005 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_trajectory-data-compile_20260521T112144",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T11:24:29.547574+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/",
  "description": "List existing artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_trajectory-data-compile_20260521T112144",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/",
    "description": "List existing artifacts"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T11:24:29.547708+00:00_

_project
analyze_r3_reward_dist.py
analyze_r3_reward_dist_fixed.py
data
dream_reports
eval
exp-001
exp-003
exp-003-s2
exp-004-eval-ckpt3000
exp-004-eval-ckpt3500
exp-006
exp-008
exp-008v3
exp-014
exp002v2-recalib
exp008v3
figures
manifest.yaml
post_mvp_experiment_skeleton.md
research
run_exp009_continuous_probe_grpo.py
run_exp016_reeval.py
stubbornness_taxonomy
training
trajectory_data_complete.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_trajectory-data-compile_20260521T112144",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T11:24:29.547858+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/trajectory_data_compiled.md",
  "content": "# D027 Eval Trajectory — Complete Compiled Data\n\n**Compiled**: 2026-05-21\n**Eval protocol**: eval_unified_preset.py (D027 standard), n=362 (181 valid + 181 invalid)\n**Vanilla baseline (D027)**: SYCONScore=0.1335, ToF=0.0718, NoF=0.9448\n\n---\n\n## Condition 1: R3-only Seed 1 (exp-003)\n\n| Step | SYCONScore | ToF    | NoF    | vs Vanilla% |\n|------|-----------|--------|--------|-------------|\n| 1000 | 0.0743    | 0.0387 | 0.9448 | −44.3%      |\n| 2000 | 0.0846    | 0.0442 | 0.9834 | −36.6%      |\n| 3000 | 0.0946    | 0.0497 | 0.9724 | −29.1%      |\n| 4000 | 0.1144    | 0.0608 | 0.9669 | −14.3%      |\n| 4500 | 0.1337    | 0.0718 | 0.9613 | +0.1%       |\n| 5000 | 0.1144    | 0.0608 | 0.9669 | −14.3%      |\n| 5500 | 0.1144    | 0.0608 | 0.9724 | −14.3%      |\n| 6000 | 0.0846    | 0.0442 | 0.9724 | −36.6%      |\n| 6500 | 0.1529    | 0.0829 | 0.9834 | +14.5%      |\n| 7000 | 0.1046    | —      | —      | −21.6%      |\n| 7500 | 0.1046    | —      | —      | −21.6%      |\n| 8000 | PENDING   | —      | —      | —           |\n\n> ckpt-7000/7500: ToF/NoF not recorded in registry (only SYCONScore available).\n> ckpt-8000: eval RUNNING as of 2026-05-21.\n\n### Summary Stats (Seed 1, steps 1000–7500, n=11)\n\n| Metric     | SYCONScore |\n|------------|-----------|\n| Mean       | 0.1070    |\n| Max        | 0.1529 (ckpt-6500) |\n| Min        | 0.0743 (ckpt-1000) |\n| Final      | 0.1046 (ckpt-7500) |\n| Peak vs Vanilla | +14.5% |\n\n---\n\n## Condition 2: R3-only Seed 2 (exp-003-s2)\n\n| Step | SYCONScore | ToF    | NoF    | vs Vanilla% |\n|------|-----------|--------|--------|-------------|\n| 500  | 0.0845    | 0.0442 | 0.9503 | −36.7%      |\n| 1000 | 0.0844    | 0.0442 | 0.9448 | −36.8%      |\n| 1500 | 0.1044    | 0.0552 | 0.9503 | −21.8%      |\n| 2000 | 0.0846    | —      | —      | −36.6%      |\n| 2500 | 0.1046    | 0.0552 | 0.9724 | −21.6%      |\n| 3000 | 0.0945    | 0.0497 | 0.9503 | −29.2%      |\n| 3500 | 0.0744    | 0.0387 | 0.9724 | −44.3%      |\n\n> ckpt-2000: ToF/NoF not recorded in registry.\n> exp-003-s2 training still RUNNING — more checkpoints may become available.\n\n### Summary Stats (Seed 2, steps 500–3500, n=7)\n\n| Metric     | SYCONScore |\n|------------|-----------|\n| Mean       | 0.0902    |\n| Max        | 0.1046 (ckpt-2500) |\n| Min        | 0.0744 (ckpt-3500) |\n| Final      | 0.0744 (ckpt-3500) |\n| Peak vs Vanilla | −21.6% |\n\n---\n\n## Condition 3: SFT ACT (exp-004)\n\n| Step | SYCONScore | ToF    | NoF    | vs Vanilla% |\n|------|-----------|--------|--------|-------------|\n| 1000 | 0.2048    | 0.1160 | 0.8729 | +53.4%      |\n| 1500 | 0.1699    | 0.0939 | 0.8895 | +27.3%      |\n| 2500 | 0.2389    | 0.1381 | 0.8840 | +78.9%      |\n| 3000 | 0.2058    | 0.1160 | 0.9116 | +54.2%      |\n| 3500 | 0.2312    | 0.1326 | 0.9006 | +73.2%      |\n| 4000 | 0.2140    | 0.1215 | 0.8950 | +60.3%      |\n| 4500 | 0.1875    | 0.1050 | 0.8785 | +40.4%      |\n| 5000 | 0.2631    | 0.1547 | 0.8785 | +97.1%      |\n| 5500 | 0.2383    | 0.1381 | 0.8674 | +78.5%      |\n| 6000 | 0.2618    | 0.1547 | 0.8508 | +96.1%      |\n| 6500 | 0.2526    | 0.1492 | 0.8232 | +89.1%      |\n| 7000 | 0.2858    | 0.1713 | 0.8619 | +114.1%     |\n| 7500 | 0.2771    | 0.1657 | 0.8453 | +107.6%     |\n| 8000 | 0.3010†   | —      | —      | +125.5%     |\n\n> † ckpt-8000 SYCONScore from parent exp-004 summary (best_sycon_score=0.301). No separate eval entry; ToF/NoF unavailable.\n> Missing checkpoints: ckpt-500, ckpt-2000 (no eval experiments registered).\n\n### Summary Stats (SFT ACT, steps 1000–8000, n=14)\n\n| Metric     | SYCONScore |\n|------------|-----------|\n| Mean       | 0.2380    |\n| Max        | 0.3010 (ckpt-8000) |\n| Min        | 0.1699 (ckpt-1500) |\n| Final      | 0.3010 (ckpt-8000) |\n| Peak vs Vanilla | +125.5% |\n\n---\n\n## Cross-seed Comparison: R3-only Seed 1 vs Seed 2\n\nOverlapping evaluation steps (1000, 2000, 3000):\n\n| Step | Seed 1 | Seed 2 | Δ (S2−S1) | Relative Δ |\n|------|--------|--------|-----------|------------|\n| 1000 | 0.0743 | 0.0844 | +0.0101   | +13.6%     |\n| 2000 | 0.0846 | 0.0846 | 0.0000    | 0.0%       |\n| 3000 | 0.0946 | 0.0945 | −0.0001   | −0.1%      |\n\n| Summary | Seed 1 (full) | Seed 2 (full) |\n|---------|---------------|---------------|\n| Mean SYCONScore | 0.1070 | 0.0902 |\n| Max SYCONScore  | 0.1529 | 0.1046 |\n| Eval range       | 1000–7500 (11 pts) | 500–3500 (7 pts) |\n| Ever ≥ Vanilla?  | Yes (ckpt-4500, 6500) | No |\n\nCross-seed findings:\n- At overlapping steps (1000–3000), scores nearly identical (max Δ = 0.01), confirming reproducibility.\n- Seed 1 later develops higher variance with a spike at ckpt-6500 (0.1529); seed 2 trajectory not yet evaluated beyond 3500.\n- Neither seed consistently exceeds vanilla baseline; R3-only GRPO does not reliably improve SYCONScore.\n\n---\n\n## Data Gaps\n\n| Condition | Missing | Status |\n|-----------|---------|--------|\n| R3-only Seed 1 | ckpt-8000 eval | RUNNING |\n| R3-only Seed 1 | ckpt-7000/7500 ToF/NoF | Not recorded |\n| R3-only Seed 2 | ckpt-2000 ToF/NoF | Not recorded |\n| R3-only Seed 2 | ckpt ≥ 4000 | Training RUNNING |\n| SFT ACT | ckpt-500, ckpt-2000 eval | Not registered |\n| SFT ACT | ckpt-8000 ToF/NoF | Not separately evaluated |\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_trajectory-data-compile_20260521T112144",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/trajectory_data_compiled.md",
    "content": "# D027 Eval Trajectory — Complete Compiled Data\n\n**Compiled**: 2026-05-21\n**Eval protocol**: eval_unified_preset.py (D027 standard), n=362 (181 valid + 181 invalid)\n**Vanilla baseline (D027)**: SYCONScore=0.1335, ToF=0.0718, NoF=0.9448\n\n---\n\n## Condition 1: R3-only Seed 1 (exp-003)\n\n| Step | SYCONScore | ToF    | NoF    | vs Vanilla% |\n|------|-----------|--------|--------|-------------|\n| 1000 | 0.0743    | 0.0387 | 0.9448 | −44.3%      |\n| 2000 | 0.0846    | 0.0442 | 0.9834 | −36.6%      |\n| 3000 | 0.0946    | 0.0497 | 0.9724 | −29.1%      |\n| 4000 | 0.1144    | 0.0608 | 0.9669 | −14.3%      |\n| 4500 | 0.1337    | 0.0718 | 0.9613 | +0.1%       |\n| 5000 | 0.1144    | 0.0608 | 0.9669 | −14.3%      |\n| 5500 | 0.1144    | 0.0608 | 0.9724 | −14.3%      |\n| 6000 | 0.0846    | 0.0442 | 0.9724 | −36.6%      |\n| 6500 | 0.1529    | 0.0829 | 0.9834 | +14.5%      |\n| 7000 | 0.1046    | —      | —      | −21.6%      |\n| 7500 | 0.1046    | —      | —      | −21.6%      |\n| 8000 | PENDING   | —      | —      | —           |\n\n> ckpt-7000/7500: ToF/NoF not recorded in registry (only SYCONScore available).\n> ckpt-8000: eval RUNNING as of 2026-05-21.\n\n### Summary Stats (Seed 1, steps 1000–7500, n=11)\n\n| Metric     | SYCONScore |\n|------------|-----------|\n| Mean       | 0.1070    |\n| Max        | 0.1529 (ckpt-6500) |\n| Min        | 0.0743 (ckpt-1000) |\n| Final      | 0.1046 (ckpt-7500) |\n| Peak vs Vanilla | +14.5% |\n\n---\n\n## Condition 2: R3-only Seed 2 (exp-003-s2)\n\n| Step | SYCONScore | ToF    | NoF    | vs Vanilla% |\n|------|-----------|--------|--------|-------------|\n| 500  | 0.0845    | 0.0442 | 0.9503 | −36.7%      |\n| 1000 | 0.0844    | 0.0442 | 0.9448 | −36.8%      |\n| 1500 | 0.1044    | 0.0552 | 0.9503 | −21.8%      |\n| 2000 | 0.0846    | —      | —      | −36.6%      |\n| 2500 | 0.1046    | 0.0552 | 0.9724 | −21.6%      |\n| 3000 | 0.0945    | 0.0497 | 0.9503 | −29.2%      |\n| 3500 | 0.0744    | 0.0387 | 0.9724 | −44.3%      |\n\n> ckpt-2000: ToF/NoF not recorded in registry.\n> exp-003-s2 training still RUNNING — more checkpoints may become available.\n\n### Summary Stats (Seed 2, steps 500–3500, n=7)\n\n| Metric     | SYCONScore |\n|------------|-----------|\n| Mean       | 0.0902    |\n| Max        | 0.1046 (ckpt-2500) |\n| Min        | 0.0744 (ckpt-3500) |\n| Final      | 0.0744 (ckpt-3500) |\n| Peak vs Vanilla | −21.6% |\n\n---\n\n## Condition 3: SFT ACT (exp-004)\n\n| Step | SYCONScore | ToF    | NoF    | vs Vanilla% |\n|------|-----------|--------|--------|-------------|\n| 1000 | 0.2048    | 0.1160 | 0.8729 | +53.4%      |\n| 1500 | 0.1699    | 0.0939 | 0.8895 | +27.3%      |\n| 2500 | 0.2389    | 0.1381 | 0.8840 | +78.9%      |\n| 3000 | 0.2058    | 0.1160 | 0.9116 | +54.2%      |\n| 3500 | 0.2312    | 0.1326 | 0.9006 | +73.2%      |\n| 4000 | 0.2140    | 0.1215 | 0.8950 | +60.3%      |\n| 4500 | 0.1875    | 0.1050 | 0.8785 | +40.4%      |\n| 5000 | 0.2631    | 0.1547 | 0.8785 | +97.1%      |\n| 5500 | 0.2383    | 0.1381 | 0.8674 | +78.5%      |\n| 6000 | 0.2618    | 0.1547 | 0.8508 | +96.1%      |\n| 6500 | 0.2526    | 0.1492 | 0.8232 | +89.1%      |\n| 7000 | 0.2858    | 0.1713 | 0.8619 | +114.1%     |\n| 7500 | 0.2771    | 0.1657 | 0.8453 | +107.6%     |\n| 8000 | 0.3010†   | —      | —      | +125.5%     |\n\n> † ckpt-8000 SYCONScore from parent exp-004 summary (best_sycon_score=0.301). No separate eval entry; ToF/NoF unavailable.\n> Missing checkpoints: ckpt-500, ckpt-2000 (no eval experiments registered).\n\n### Summary Stats (SFT ACT, steps 1000–8000, n=14)\n\n| Metric     | SYCONScore |\n|------------|-----------|\n| Mean       | 0.2380    |\n| Max        | 0.3010 (ckpt-8000) |\n| Min        | 0.1699 (ckpt-1500) |\n| Final      | 0.3010 (ckpt-8000) |\n| Peak vs Vanilla | +125.5% |\n\n---\n\n## Cross-seed Comparison: R3-only Seed 1 vs Seed 2\n\nOverlapping evaluation steps (1000, 2000, 3000):\n\n| Step | Seed 1 | Seed 2 | Δ (S2−S1) | Relative Δ |\n|------|--------|--------|-----------|------------|\n| 1000 | 0.0743 | 0.0844 | +0.0101   | +13.6%     |\n| 2000 | 0.0846 | 0.0846 | 0.0000    | 0.0%       |\n| 3000 | 0.0946 | 0.0945 | −0.0001   | −0.1%      |\n\n| Summary | Seed 1 (full) | Seed 2 (full) |\n|---------|---------------|---------------|\n| Mean SYCONScore | 0.1070 | 0.0902 |\n| Max SYCONScore  | 0.1529 | 0.1046 |\n| Eval range       | 1000–7500 (11 pts) | 500–3500 (7 pts) |\n| Ever ≥ Vanilla?  | Yes (ckpt-4500, 6500) | No |\n\nCross-seed findings:\n- At overlapping steps (1000–3000), scores nearly identical (max Δ = 0.01), confirming reproducibility.\n- Seed 1 later develops higher variance with a spike at ckpt-6500 (0.1529); seed 2 trajectory not yet evaluated beyond 3500.\n- Neither seed consistently exceeds vanilla baseline; R3-only GRPO does not reliably improve SYCONScore.\n\n---\n\n## Data Gaps\n\n| Condition | Missing | Status |\n|-----------|---------|--------|\n| R3-only Seed 1 | ckpt-8000 eval | RUNNING |\n| R3-only Seed 1 | ckpt-7000/7500 ToF/NoF | Not recorded |\n| R3-only Seed 2 | ckpt-2000 ToF/NoF | Not recorded |\n| R3-only Seed 2 | ckpt ≥ 4000 | Training RUNNING |\n| SFT ACT | ckpt-500, ckpt-2000 eval | Not registered |\n| SFT ACT | ckpt-8000 ToF/NoF | Not separately evaluated |\n"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-21T11:24:29.548096+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/trajectory_data_compiled.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_trajectory-data-compile_20260521T112144",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T11:24:29.548228+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "trajectory_data_compiled",
  "type": "data",
  "description": "Complete D027 eval trajectory data for all 3 conditions (R3-only seed 1/2, SFT ACT) with summary stats, cross-seed comparison, and data gap annotations",
  "project": "contrastive_entrain_calib",
  "source_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/trajectory_data_compiled.md",
  "tags": "['trajectory', 'd027', 'exp-003', 'exp-003-s2', 'exp-004', 'paper-data']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_trajectory-data-compile_20260521T112144",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "trajectory_data_compiled",
    "type": "data",
    "description": "Complete D027 eval trajectory data for all 3 conditions (R3-only seed 1/2, SFT ACT) with summary stats, cross-seed comparison, and data gap annotations",
    "project": "contrastive_entrain_calib",
    "source_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/trajectory_data_compiled.md",
    "tags": "['trajectory', 'd027', 'exp-003', 'exp-003-s2', 'exp-004', 'paper-data']"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-21T11:24:29.548371+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260521_e457b3\", \"name\": \"trajectory_data_compiled\", \"type\": \"data\", \"description\": \"Complete D027 eval trajectory data for all 3 conditions (R3-only seed 1/2, SFT ACT) with summary stats, cross-seed comparison, and data gap annotations\", \"path\": \"projects/contrastive_entrain_calib/artifacts/_project/data/trajectory_data_compiled.md\", \"url\": null, \"project\": \"contrastive_entrain_calib\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-21T11:24:21.873718+00:00\", \"tags\": [\"trajectory\", \"d027\", \"exp-003\", \"exp-003-s2\", \"exp-004\", \"paper-data\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_trajectory-data-compile_20260521T112144",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-21T11:24:29.548540+00:00_

文件已写入并注册。

产出：`artifacts/trajectory_data_compiled.md` (art_20260521_e457b3)

内容覆盖：
- **Condition 1** (R3-only Seed 1): 11 个 checkpoint (1000–7500)，ckpt-8000 标注 RUNNING
- **Condition 2** (R3-only Seed 2): 7 个 checkpoint (500–3500)，训练仍在继续
- **Condition 3** (SFT ACT): 14 个 checkpoint (1000–8000)，ckpt-8000 仅有 SYCONScore=0.301（来自 parent summary）
- Cross-seed comparison: 3 个重叠步数 (1000/2000/3000) 差异极小 (max Δ=0.01)，确认可复现性
- 所有已知数据点与提供的交叉验证值完全吻合
- Data Gaps 表列出 6 项缺失

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_trajectory-data-compile_20260521T112144"
}
```

</details>

---
