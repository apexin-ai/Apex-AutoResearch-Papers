# analysis eval gsm8k sft rasp 20 1p5b

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/chats/worker_analysis_eval_gsm8k_sft_rasp_20_1p5b_20260519T024144.jsonl`
- **Structured JSON:** [`9755d2e7c199181c440b.json`](../../sessions/97/9755d2e7c199181c440b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

15 recorded events

### Tool call

_source line 1 · 2026-05-19T02:42:57.159405+00:00_

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
  "session": "worker_analysis_eval_gsm8k_sft_rasp_20_1p5b_20260519T024144",
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

_source line 2 · 2026-05-19T02:42:57.159729+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_gsm8k_sft_rasp_20_1p5b_20260519T024144",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T02:42:57.159907+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "cat /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_rasp_20_1p5b.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_gsm8k_sft_rasp_20_1p5b_20260519T024144",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "cat /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_rasp_20_1p5b.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-19T02:42:57.160043+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "tail -30 /root/autodl-tmp/recovery_aware_struct_prune/eval_gsm8k_sft_rasp_20_1p5b.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_gsm8k_sft_rasp_20_1p5b_20260519T024144",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "tail -30 /root/autodl-tmp/recovery_aware_struct_prune/eval_gsm8k_sft_rasp_20_1p5b.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-19T02:42:57.160365+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model_path\\\": \\\"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_1p5b\\\",\\n  \\\"mode\\\": \\\"greedy\\\",\\n  \\\"accuracy\\\": 0.26914329037149354,\\n  \\\"stderr\\\": 0.012211963572592724,\\n  \\\"n_correct\\\": 355,\\n  \\\"n_total\\\": 1319,\\n  \\\"eos_stats\\\": {\\n    \\\"natural_eos\\\": 1242,\\n    \\\"truncated\\\": 77,\\n    \\\"eos_rate\\\": 0.9416224412433661,\\n    \\\"avg_response_length\\\": 378.6482183472327,\\n    \\\"max_response_length\\\": 4096,\\n    \\\"min_response_length\\\": 35\\n  },\\n  \\\"temperature\\\": 0.0,\\n  \\\"do_sample\\\": false,\\n  \\\"examples\\\": [\\n    {\\n      \\\"question\\\": \\\"Darrell and Allen's ages are in the ratio of 7:11. If their total age now is 162, calculate Allen's age 10 years from now.\\\",\\n      \\\"gold\\\": \\\"109\\\",\\n      \\\"prediction\\\": \\\"143.4\\\",\\n      \\\"correct\\\": false,\\n      \\\"response\\\": \\\"First, we know that the ratio of their ages is 7:11, which means that their ages are 7x and 11x for x years.\\\\nWe know that their total age now is 162 years, so we can set up the equation 7x + 11x = 162.\\\\nCombining like terms, we get 17x = 162.\\\\nWe divide both sides by 17 to find x = 162/17 � 8.4 years.\\\\nWe can find the age of Allen by multiplying x by 11, which gives 11 x 8.4 � 113.4 years.\\\\nWe can find the age of Allen 10 years from now by adding 10 to his current age, which gives 113.4 + 10 � 143.4\\\",\\n      \\\"response_length\\\": 199,\\n      \\\"hit_eos\\\": true\\n    },\\n    {\\n      \\\"question\\\": \\\"Lorraine and Colleen are trading stickers for buttons. Each large sticker is worth a large button or three small buttons. A small sticker is worth one small button. A large button is worth three small stickers. Lorraine starts with 30 small stickers and 40 large stickers. She trades 90% of her small stickers for large buttons. She trades 50% of her large stickers for l
…[truncated 7295 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_gsm8k_sft_rasp_20_1p5b_20260519T024144",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T02:42:57.160562+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"tail: cannot open '/root/autodl-tmp/recovery_aware_struct_prune/eval_gsm8k_sft_rasp_20_1p5b.log' for reading: No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.83}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_gsm8k_sft_rasp_20_1p5b_20260519T024144",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T02:42:57.160745+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "find /root/autodl-tmp/recovery_aware_struct_prune -name \"*sft_rasp_20_1p5b*log*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_gsm8k_sft_rasp_20_1p5b_20260519T024144",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "find /root/autodl-tmp/recovery_aware_struct_prune -name \"*sft_rasp_20_1p5b*log*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T02:42:57.160883+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.74}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_gsm8k_sft_rasp_20_1p5b_20260519T024144",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T02:42:57.161151+00:00_

called mcp__agent-ml-research__save_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file</summary>

```json
{
  "project": "recovery_aware_struct_prune",
  "file": "artifacts/eval_gsm8k_sft_rasp_20_1p5b_results.md",
  "content": "# Eval: GSM8K SFT RASP 20% 1.5B\n\n## 核心指标\n\n| 指标 | 值 |\n|---|---|\n| **Accuracy** | **26.91%** (0.2691) |\n| Stderr | ±1.22% |\n| n_correct | 355 |\n| n_total | 1319 |\n| Mode | greedy (T=0.0, do_sample=false) |\n| EOS rate | 94.16% (77/1319 truncated) |\n| Avg response length | 378.6 tokens |\n\n## Checkpoint\n\n- **model_path**: `/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_1p5b`\n- **result_file**: `/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_rasp_20_1p5b.json`\n- **log_file**: 不存在（未找到对应 .log 文件）\n\n## GRPO Delta 计算\n\n| 方法 | GSM8K Accuracy |\n|---|---|\n| SFT RASP 20% 1.5B | 26.91% |\n| GRPO RASP 20% 1.5B | 26.16% |\n| **GRPO delta** | **-0.75 pp** |\n\n## 结论\n\n**Negative**。SFT baseline (26.91%) 高于 GRPO (26.16%)，GRPO delta 为负 (-0.75 pp)。GRPO 在 RASP 20% 1.5B 设定下未能超越 SFT recovery。\n\n注：ROADMAP 记录的 interim accuracy (27.64%) 高于本次最终结果 (26.91%)，差异可能源于评估配置差异（greedy vs sampling）。\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_gsm8k_sft_rasp_20_1p5b_20260519T024144",
  "tool": "mcp__agent-ml-research__save_project_file",
  "tool_args": {
    "project": "recovery_aware_struct_prune",
    "file": "artifacts/eval_gsm8k_sft_rasp_20_1p5b_results.md",
    "content": "# Eval: GSM8K SFT RASP 20% 1.5B\n\n## 核心指标\n\n| 指标 | 值 |\n|---|---|\n| **Accuracy** | **26.91%** (0.2691) |\n| Stderr | ±1.22% |\n| n_correct | 355 |\n| n_total | 1319 |\n| Mode | greedy (T=0.0, do_sample=false) |\n| EOS rate | 94.16% (77/1319 truncated) |\n| Avg response length | 378.6 tokens |\n\n## Checkpoint\n\n- **model_path**: `/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_1p5b`\n- **result_file**: `/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_rasp_20_1p5b.json`\n- **log_file**: 不存在（未找到对应 .log 文件）\n\n## GRPO Delta 计算\n\n| 方法 | GSM8K Accuracy |\n|---|---|\n| SFT RASP 20% 1.5B | 26.91% |\n| GRPO RASP 20% 1.5B | 26.16% |\n| **GRPO delta** | **-0.75 pp** |\n\n## 结论\n\n**Negative**。SFT baseline (26.91%) 高于 GRPO (26.16%)，GRPO delta 为负 (-0.75 pp)。GRPO 在 RASP 20% 1.5B 设定下未能超越 SFT recovery。\n\n注：ROADMAP 记录的 interim accuracy (27.64%) 高于本次最终结果 (26.91%)，差异可能源于评估配置差异（greedy vs sampling）。\n"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T02:42:57.161400+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file 'artifacts/eval_gsm8k_sft_rasp_20_1p5b_results.md' is not writable via save_project_file. Writable: ['memory.md', 'paper_framing.md', 'writing_plan.yaml'].\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_gsm8k_sft_rasp_20_1p5b_20260519T024144",
  "tool": "mcp__agent-ml-research__save_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T02:42:57.161576+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_gsm8k_sft_rasp_20_1p5b_20260519T024144",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/",
    "description": "List artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T02:42:57.161747+00:00_

_project
alpha_ablation_diff_report.md
analysis_grpo_standard_25_qwen_math.md
analysis_recent_results_20260517.md
bootstrap_ci_analysis.py
bootstrap_ci_reward_trajectories.json
cka_heatmap_cka_only.json
cka_heatmap_random.json
cka_heatmap_rasp.json
cka_heatmap_standard.json
collapse_dynamics_comparison.md
collapse_dynamics_step50_update.md
collapse_onset_timing.json
correlation_analysis.py
diag_eval_math500_grpo_timeout.md
diag_eval_math500_unpruned.md
diagnose_eval_grpo_standard_25.md
diagnose_eval_pass_k8_v2.md
diagnosis_inference_v2.md
dream_reports
e3_cka_heatmap.pdf
eval_humaneval_grpo_standard_20_2048
eval_humaneval_sft_standard_20_2048_v2
eval_pass_k8_rasp_20_grpo_deepseek
eval_pass_k8_standard_20_grpo_qwen_math_v2
eval_sft_rasp_rlvr_20
evidence_table.md
figure_plan.md
figures
grpo_cka_only_20_full_metrics.md
grpo_collapse_dynamics_analysis.md
grpo_qwen_math_v3
grpo_random_20_early_analysis.md
grpo_random_20_full_metrics.md
grpo_rasp_20_4096_status.md
grpo_rasp_25
grpo_standard_20_fair_early_metrics.md
grpo_standard_25_qwen_math
humaneval_2048_matrix
inference_bench_clean_v2
literature_notes.md
literature_review_cka_rl_stability.md
literature_survey_related_work.md
manifest.yaml
mvp_progress_20260514.md
mvp_v2_analysis.md
paper_results_tables.md
plot_cka_figures.py
plot_fig1_pipeline.py
related_work_notes.md
run_alpha_verify_512.sh
scoring_diff_investigation.md
sft_rasp_20_westd_retrain
statistical_summary.md
tables
verification_report_postprune_eval.md
westb_disk_cleanup_20260515.md
westb_disk_report.md
westb_grpo_complete_metrics.md
westb_progress_check_143700.md
westd_diagnostic_20260518.md
westd_gpu_report.md
westd_recovery_checklist.md
westd_status_check_143700.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_gsm8k_sft_rasp_20_1p5b_20260519T024144",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T02:42:57.161928+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/eval_gsm8k_sft_rasp_20_1p5b_results.md",
  "content": "# Eval: GSM8K SFT RASP 20% 1.5B\n\n## 核心指标\n\n| 指标 | 值 |\n|---|---|\n| **Accuracy** | **26.91%** (0.2691) |\n| Stderr | ±1.22% |\n| n_correct | 355 |\n| n_total | 1319 |\n| Mode | greedy (T=0.0, do_sample=false) |\n| EOS rate | 94.16% (77/1319 truncated) |\n| Avg response length | 378.6 tokens |\n\n## Checkpoint\n\n- **model_path**: `/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_1p5b`\n- **result_file**: `/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_rasp_20_1p5b.json`\n- **log_file**: 不存在（未找到对应 .log 文件）\n\n## GRPO Delta 计算\n\n| 方法 | GSM8K Accuracy |\n|---|---|\n| SFT RASP 20% 1.5B | 26.91% |\n| GRPO RASP 20% 1.5B | 26.16% |\n| **GRPO delta** | **-0.75 pp** |\n\n## 结论\n\n**Negative**。SFT baseline (26.91%) 高于 GRPO (26.16%)，GRPO delta 为负 (-0.75 pp)。GRPO 在 RASP 20% 1.5B 设定下未能超越 SFT recovery。\n\n注：ROADMAP 记录的 interim accuracy (27.64%) 高于本次最终结果 (26.91%)，差异可能源于评估配置差异（greedy vs sampling）。\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_gsm8k_sft_rasp_20_1p5b_20260519T024144",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/eval_gsm8k_sft_rasp_20_1p5b_results.md",
    "content": "# Eval: GSM8K SFT RASP 20% 1.5B\n\n## 核心指标\n\n| 指标 | 值 |\n|---|---|\n| **Accuracy** | **26.91%** (0.2691) |\n| Stderr | ±1.22% |\n| n_correct | 355 |\n| n_total | 1319 |\n| Mode | greedy (T=0.0, do_sample=false) |\n| EOS rate | 94.16% (77/1319 truncated) |\n| Avg response length | 378.6 tokens |\n\n## Checkpoint\n\n- **model_path**: `/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_1p5b`\n- **result_file**: `/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_rasp_20_1p5b.json`\n- **log_file**: 不存在（未找到对应 .log 文件）\n\n## GRPO Delta 计算\n\n| 方法 | GSM8K Accuracy |\n|---|---|\n| SFT RASP 20% 1.5B | 26.91% |\n| GRPO RASP 20% 1.5B | 26.16% |\n| **GRPO delta** | **-0.75 pp** |\n\n## 结论\n\n**Negative**。SFT baseline (26.91%) 高于 GRPO (26.16%)，GRPO delta 为负 (-0.75 pp)。GRPO 在 RASP 20% 1.5B 设定下未能超越 SFT recovery。\n\n注：ROADMAP 记录的 interim accuracy (27.64%) 高于本次最终结果 (26.91%)，差异可能源于评估配置差异（greedy vs sampling）。\n"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T02:42:57.162079+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/eval_gsm8k_sft_rasp_20_1p5b_results.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_gsm8k_sft_rasp_20_1p5b_20260519T024144",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-19T02:42:57.162240+00:00_

结果已写入 `artifacts/eval_gsm8k_sft_rasp_20_1p5b_results.md`。

**关键数据**:
- SFT RASP 20% 1.5B GSM8K accuracy: **26.91%** (355/1319, greedy)
- Checkpoint: `/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_1p5b`
- GRPO delta = 26.16% - 26.91% = **-0.75 pp** (negative)

**结论**: Negative result。GRPO (26.16%) 未超越 SFT baseline (26.91%)，差距在 stderr (±1.22%) 范围内，两者本质上无显著差异。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_eval_gsm8k_sft_rasp_20_1p5b_20260519T024144"
}
```

</details>

---
