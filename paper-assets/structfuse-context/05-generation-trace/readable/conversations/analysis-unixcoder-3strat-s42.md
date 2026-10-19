# analysis unixcoder 3strat s42

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/chats/worker_analysis_unixcoder-3strat-s42_20260516T092457.jsonl`
- **Structured JSON:** [`5cfb4016f404cbadd1ac.json`](../../sessions/5c/5cfb4016f404cbadd1ac.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

19 recorded events

### Tool call

_source line 1 · 2026-05-16T09:26:15.452815+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__save_project_file",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_unixcoder-3strat-s42_20260516T092457",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__save_project_file",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T09:26:15.453143+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_unixcoder-3strat-s42_20260516T092457",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T09:26:15.453322+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "tail -200 ~/runs/structfuse-context/unixcoder-3strat-s42.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_unixcoder-3strat-s42_20260516T092457",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "tail -200 ~/runs/structfuse-context/unixcoder-3strat-s42.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-16T09:26:15.453456+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "ls -la /root/autodl-tmp/structfuse/full_m2_unixcoder_outputs/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_unixcoder-3strat-s42_20260516T092457",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "ls -la /root/autodl-tmp/structfuse/full_m2_unixcoder_outputs/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-16T09:26:15.453692+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  [eval@200] {'val_loss': 0.472696835282665, 'recall@1': 0.524496644295302, 'recall@5': 0.9677852348993289, 'recall@10': 1.0}\\n  New best val_loss=0.4727, saved to /root/autodl-tmp/structfuse/full_m2_unixcoder_outputs/random_s42/best_by_val_loss\\n  New best R@1=0.5245, saved to /root/autodl-tmp/structfuse/full_m2_unixcoder_outputs/random_s42/best_by_recall_at_1\\n  step 250  loss=0.4002  lr=1.96e-05\\n  step 300  loss=0.3814  lr=1.92e-05\\n  step 350  loss=0.2443  lr=1.87e-05\\n  step 400  loss=0.3501  lr=1.80e-05\\n  [eval@400] {'val_loss': 0.4512897757075777, 'recall@1': 0.5483221476510067, 'recall@5': 0.9771812080536912, 'recall@10': 1.0}\\n  New best val_loss=0.4513, saved to /root/autodl-tmp/structfuse/full_m2_unixcoder_outputs/random_s42/best_by_val_loss\\n  New best R@1=0.5483, saved to /root/autodl-tmp/structfuse/full_m2_unixcoder_outputs/random_s42/best_by_recall_at_1\\n  step 450  loss=0.4448  lr=1.72e-05\\n  step 500  loss=0.3764  lr=1.63e-05\\n  step 550  loss=0.2912  lr=1.53e-05\\n  step 600  loss=0.3368  lr=1.42e-05\\n  [eval@600] {'val_loss': 0.4517119612069738, 'recall@1': 0.5523489932885906, 'recall@5': 0.9761744966442953, 'recall@10': 1.0}\\n  val_loss not improved (1/3)\\n  New best R@1=0.5523, saved to /root/autodl-tmp/structfuse/full_m2_unixcoder_outputs/random_s42/best_by_recall_at_1\\n  step 650  loss=0.3870  lr=1.31e-05\\n  step 700  loss=0.2998  lr=1.19e-05\\n[Epoch 2] Using pre-mined negatives (random)...\\n  step 750  loss=0.2011  lr=1.07e-05\\n  step 800  loss=0.1731  lr=9.45e-06\\n  [eval@800] {'val_loss': 0.45829284489154815, 'recall@1': 0.552013422818792, 'recall@5': 0.9768456375838926, 'recall@10': 1.0}\\n  val_loss not improved (2/3)\\n  step 850  loss=0.2779  lr=8.22e-06\\n  step 900  loss=0.2265  lr=7.02e-06\\n  step 950  loss=0.3206  lr=5.87e-06\\n  step 1000  loss=0.3183  lr=4.78e-06\\n  [eval@1000] {'val_loss': 0.45922159980607513, 'recall@1': 0.5533557046979866, 'recall@
…[truncated 6453 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_unixcoder-3strat-s42_20260516T092457",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T09:26:15.453874+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 4\\ndrwxr-xr-x  5 root root   96 May 16 16:10 .\\ndrwxr-xr-x 21 root root 4096 May 16 15:12 ..\\ndrwxr-xr-x  5 root root  107 May 16 17:22 dataflow_aware_s42\\ndrwxr-xr-x  5 root root  107 May 16 16:10 embedding_distance_s42\\ndrwxr-xr-x  5 root root  107 May 16 14:54 random_s42\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_unixcoder-3strat-s42_20260516T092457",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T09:26:15.454055+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "grep -A2 \"Early stopping\\|Final eval\\|wandb sync\\|DONE: strategy=embedding\" ~/runs/structfuse-context/unixcoder-3strat-s42.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_unixcoder-3strat-s42_20260516T092457",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "grep -A2 \"Early stopping\\|Final eval\\|wandb sync\\|DONE: strategy=embedding\" ~/runs/structfuse-context/unixcoder-3strat-s42.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T09:26:15.454189+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_unixcoder-3strat-s42_20260516T092457",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T09:26:15.454310+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "ls -la /root/autodl-tmp/structfuse/full_m2_unixcoder_outputs/random_s42/ /root/autodl-tmp/structfuse/full_m2_unixcoder_outputs/embedding_distance_s42/ /root/autodl-tmp/structfuse/full_m2_unixcoder_outputs/dataflow_aware_s42/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_unixcoder-3strat-s42_20260516T092457",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "ls -la /root/autodl-tmp/structfuse/full_m2_unixcoder_outputs/random_s42/ /root/autodl-tmp/structfuse/full_m2_unixcoder_outputs/embedding_distance_s42/ /root/autodl-tmp/structfuse/full_m2_unixcoder_outputs/dataflow_aware_s42/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T09:26:15.454444+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/structfuse/full_m2_unixcoder_outputs/dataflow_aware_s42/:\\ntotal 20\\ndrwxr-xr-x 5 root root  107 May 16 17:22 .\\ndrwxr-xr-x 5 root root   96 May 16 16:10 ..\\ndrwxr-xr-x 2 root root 4096 May 16 17:19 best_by_recall_at_1\\ndrwxr-xr-x 2 root root 4096 May 16 16:38 best_by_val_loss\\ndrwxr-xr-x 2 root root 4096 May 16 17:22 final\\n-rw-r--r-- 1 root root 4595 May 16 17:22 train.log\\n\\n/root/autodl-tmp/structfuse/full_m2_unixcoder_outputs/embedding_distance_s42/:\\ntotal 20\\ndrwxr-xr-x 5 root root  107 May 16 16:10 .\\ndrwxr-xr-x 5 root root   96 May 16 16:10 ..\\ndrwxr-xr-x 2 root root 4096 May 16 15:25 best_by_recall_at_1\\ndrwxr-xr-x 2 root root 4096 May 16 15:25 best_by_val_loss\\ndrwxr-xr-x 2 root root 4096 May 16 16:10 final\\n-rw-r--r-- 1 root root 4883 May 16 16:10 train.log\\n\\n/root/autodl-tmp/structfuse/full_m2_unixcoder_outputs/random_s42/:\\ntotal 20\\ndrwxr-xr-x 5 root root  107 May 16 14:54 .\\ndrwxr-xr-x 5 root root   96 May 16 16:10 ..\\ndrwxr-xr-x 2 root root 4096 May 16 14:52 best_by_recall_at_1\\ndrwxr-xr-x 2 root root 4096 May 16 14:23 best_by_val_loss\\ndrwxr-xr-x 2 root root 4096 May 16 14:54 final\\n-rw-r--r-- 1 root root 4381 May 16 14:54 train.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_unixcoder-3strat-s42_20260516T092457",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T09:26:15.454584+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "cat /root/autodl-tmp/structfuse/full_m2_unixcoder_outputs/embedding_distance_s42/train.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_unixcoder-3strat-s42_20260516T092457",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "cat /root/autodl-tmp/structfuse/full_m2_unixcoder_outputs/embedding_distance_s42/train.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T09:26:15.454788+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[2026-05-16 14:54:03] START: python -u /root/structfuse/training/train.py --model-name microsoft/unixcoder-base --train-file /root/autodl-tmp/structfuse/full_m2_training_data/train_embedding_distance_s42.jsonl --val-file /root/autodl-tmp/structfuse/full_m2_training_data/val_embedding_distance_s42.jsonl --output-dir /root/autodl-tmp/structfuse/full_m2_unixcoder_outputs/embedding_distance_s42 --hard-negative-strategy embedding_distance --seed 42 --batch-size 16 --num-negatives 7 --max-seq-length 1024 --num-epochs 2 --learning-rate 2e-5 --eval-steps 200 --save-steps 500 --use-lora --gradient-checkpointing --wandb-project structfuse --wandb-run-name unixcoder_embedding_distance_s42 --early-stopping-patience 3\\nwandb: Tracking run with wandb version 0.26.0\\nwandb: W&B syncing is set to `offline` in this directory. Run `wandb online` or set WANDB_MODE=online to enable cloud syncing.\\nwandb: Run data is saved locally in /root/structfuse-context/wandb/offline-run-20260516_145407-62yumq1s\\n[Epoch 1] Using pre-mined negatives (embedding_distance)...\\n  Training loop start: 707 batches/epoch, total_steps_per_epoch=707\\n  step 50  loss=0.6408  lr=7.09e-06\\n  step 100  loss=0.5198  lr=1.42e-05\\n  step 150  loss=0.5119  lr=2.00e-05\\n  step 200  loss=0.5034  lr=1.99e-05\\n  [eval@200] {'val_loss': 0.4722365116112984, 'recall@1': 0.5218120805369127, 'recall@5': 0.9677852348993289, 'recall@10': 1.0}\\n  New best val_loss=0.4722, saved to /root/autodl-tmp/structfuse/full_m2_unixcoder_outputs/embedding_distance_s42/best_by_val_loss\\n  New best R@1=0.5218, saved to /root/autodl-tmp/structfuse/full_m2_unixcoder_outputs/embedding_distance_s42/best_by_recall_at_1\\n  step 250  loss=0.4970  lr=1.96e-05\\n  step 300  loss=0.4495  lr=1.92e-05\\n  step 350  loss=0.3722  lr=1.87e-05\\n  step 400  loss=0.4233  lr=1.80e-05\\n  [eval@400] {'val_loss': 0.44925363359835324, 'recall@1': 0.5426174496644295, 'recall@5': 0.97684563758389
…[truncated 3039 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_unixcoder-3strat-s42_20260516T092457",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T09:26:15.454990+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_unixcoder-3strat-s42_20260516T092457",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/",
    "description": "List artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T09:26:15.455129+00:00_

_project
analysis
bjb1_status_check.md
bm25_overlap_stratified.json
checkpoint_criterion_analysis.md
code
disk_cleanup_report_20260513.md
dream_reports
extract_eval_trajectories.py
figures
full_m2
literature
m1_progress_0513.md
m1_reextract_v2_status.md
m2_eval_summary.md
m2_full_qwen
m2_full_qwen_analysis.md
m2_full_starcoder
m2_qwen_status_check.md
m2_starcoder_status_check.md
manifest.yaml
mine_bm25_negatives.py
mvp_p1_codeql_feasibility
mvp_p2b_contrastive_training
neg_difficulty_analysis
paper_drafts
paper_figures
patch_build_m1.py
patch_train.py
plan003_eval_readiness.md
plan003_swebench_dryrun_report.md
plan003_swebench_eval_plan.md
plan005_stratification_spec.md
plan005_stratified_analysis_report.md
plan006_error_patterns.json
plan_003
plan_003_swebench_eval
plan_005
plan_005_stratified
plan_006
plan_006_scalability
plan_006_scalability_stats_29repos.json
plan_018_bm25
rename_safety_report.md
status_check_20260514.md
status_check_loop6.md
swebench_eval_readiness.md
training_status_snapshot.md
v1_v2_changelog.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_unixcoder-3strat-s42_20260516T092457",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T09:26:15.455254+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/unixcoder-3strat-s42",
  "description": "Create output directory for analysis"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_unixcoder-3strat-s42_20260516T092457",
  "tool": "Bash",
  "tool_args": {
    "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/unixcoder-3strat-s42",
    "description": "Create output directory for analysis"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T09:26:15.455368+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_unixcoder-3strat-s42_20260516T092457",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T09:26:15.455489+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/unixcoder-3strat-s42/analysis.json",
  "content": "{\n  \"random_s42\": {\n    \"best_val_loss\": 0.4513,\n    \"best_val_loss_step\": 400,\n    \"best_R@1\": 0.5534,\n    \"best_R@1_step\": 1000,\n    \"best_R@5\": 0.9772,\n    \"early_stopped_step\": 1000,\n    \"checkpoint_path\": \"/root/autodl-tmp/structfuse/full_m2_unixcoder_outputs/random_s42/best_by_recall_at_1\"\n  },\n  \"embedding_distance_s42\": {\n    \"best_val_loss\": 0.4466,\n    \"best_val_loss_step\": 600,\n    \"best_R@1\": 0.5497,\n    \"best_R@1_step\": 600,\n    \"best_R@5\": 0.9772,\n    \"early_stopped_step\": 1200,\n    \"checkpoint_path\": \"/root/autodl-tmp/structfuse/full_m2_unixcoder_outputs/embedding_distance_s42/best_by_recall_at_1\"\n  },\n  \"dataflow_aware_s42\": {\n    \"best_val_loss\": 0.4628,\n    \"best_val_loss_step\": 400,\n    \"best_R@1\": 0.5510,\n    \"best_R@1_step\": 1000,\n    \"best_R@5\": 0.9755,\n    \"early_stopped_step\": 1000,\n    \"checkpoint_path\": \"/root/autodl-tmp/structfuse/full_m2_unixcoder_outputs/dataflow_aware_s42/best_by_recall_at_1\"\n  },\n  \"summary\": \"random_s42 achieves best R@1 (0.5534) and ties best R@5 (0.9772); embedding_distance_s42 has best val_loss (0.4466) but lower R@1; dataflow_aware_s42 is middle on R@1 but worst on val_loss. Differences are marginal (<1% R@1 spread across strategies).\",\n  \"wandb_run_ids\": [\n    \"offline-run-20260516_140449-0blt4al6\",\n    \"offline-run-20260516_145407-62yumq1s\",\n    \"offline-run-20260516_161010-kfzi8sgq\"\n  ]\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_unixcoder-3strat-s42_20260516T092457",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/unixcoder-3strat-s42/analysis.json",
    "content": "{\n  \"random_s42\": {\n    \"best_val_loss\": 0.4513,\n    \"best_val_loss_step\": 400,\n    \"best_R@1\": 0.5534,\n    \"best_R@1_step\": 1000,\n    \"best_R@5\": 0.9772,\n    \"early_stopped_step\": 1000,\n    \"checkpoint_path\": \"/root/autodl-tmp/structfuse/full_m2_unixcoder_outputs/random_s42/best_by_recall_at_1\"\n  },\n  \"embedding_distance_s42\": {\n    \"best_val_loss\": 0.4466,\n    \"best_val_loss_step\": 600,\n    \"best_R@1\": 0.5497,\n    \"best_R@1_step\": 600,\n    \"best_R@5\": 0.9772,\n    \"early_stopped_step\": 1200,\n    \"checkpoint_path\": \"/root/autodl-tmp/structfuse/full_m2_unixcoder_outputs/embedding_distance_s42/best_by_recall_at_1\"\n  },\n  \"dataflow_aware_s42\": {\n    \"best_val_loss\": 0.4628,\n    \"best_val_loss_step\": 400,\n    \"best_R@1\": 0.5510,\n    \"best_R@1_step\": 1000,\n    \"best_R@5\": 0.9755,\n    \"early_stopped_step\": 1000,\n    \"checkpoint_path\": \"/root/autodl-tmp/structfuse/full_m2_unixcoder_outputs/dataflow_aware_s42/best_by_recall_at_1\"\n  },\n  \"summary\": \"random_s42 achieves best R@1 (0.5534) and ties best R@5 (0.9772); embedding_distance_s42 has best val_loss (0.4466) but lower R@1; dataflow_aware_s42 is middle on R@1 but worst on val_loss. Differences are marginal (<1% R@1 spread across strategies).\",\n  \"wandb_run_ids\": [\n    \"offline-run-20260516_140449-0blt4al6\",\n    \"offline-run-20260516_145407-62yumq1s\",\n    \"offline-run-20260516_161010-kfzi8sgq\"\n  ]\n}\n"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T09:26:15.455647+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/unixcoder-3strat-s42/analysis.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_unixcoder-3strat-s42_20260516T092457",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-16T09:26:15.455813+00:00_

分析完成。结果汇总：

| 策略 | best_val_loss (step) | best_R@1 (step) | best_R@5 | early_stop |
|------|---------------------|-----------------|----------|------------|
| random_s42 | 0.4513 (400) | **0.5534** (1000) | **0.9772** | step 1000 |
| embedding_distance_s42 | **0.4466** (600) | 0.5497 (600) | 0.9772 | step 1200 |
| dataflow_aware_s42 | 0.4628 (400) | 0.5510 (1000) | 0.9755 | step 1000 |

关键发现：3 个策略性能差异极小（R@1 跨度 < 0.4%）。random 在 R@1 上反而最好，embedding_distance 在 val_loss 上最好但 R@1 最低。dataflow_aware 居中。负采样策略对 UniXcoder 影响不显著。

结果已保存到 `artifacts/unixcoder-3strat-s42/analysis.json`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_unixcoder-3strat-s42_20260516T092457"
}
```

</details>

---
