# data prep paper figure data

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 61
- **Recorded user turns:** 0
- **Tool calls:** 30
- **Original source:** `logs/chats/worker_data-prep_paper-figure-data_20260515T132727.jsonl`
- **Structured JSON:** [`ab0c50ed0b3a5af83ff5.json`](../../sessions/ab/ab0c50ed0b3a5af83ff5.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

61 recorded events

### Tool call

_source line 1 · 2026-05-15T13:30:17.812915+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T13:30:17.813508+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T13:30:17.813876+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "limit": "0",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "limit": "0",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-15T13:30:17.814117+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "file": "memory.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "file": "memory.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-15T13:30:17.815625+00:00_

Error: result (214,604 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/5cbbb9df-024d-468c-b967-a31c715565cd/tool-results/mcp-agent-ml-research-read_registry-1778851665713.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/5cbbb9df-024d-468c-b967-a31c715565cd/tool-results/mcp-agent-ml-research-read_registry-1778851665713.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T13:30:17.816099+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/memory.md\", \"content\": \"# Memory — exec-sim-repair-verifier\\n\\n## 硬教训：标 FAILED 前必须确认进程已退出 (2026-05-15)\\n- **事故**：v1 ckpt-3000 test eval (PID 345441) 被误标 DONE/failed，但进程实际在跑。随后 v2 提交到同 GPU 导致 OOM。\\n- **规则**：标 FAILED/DONE(failed) 前必须 `ps -p PID` 确认进程已退出。标 RUNNING 的实验所在 GPU 不得提交新任务。\\n- **适用范围**：所有 registry 状态变更操作\\n\\n## 硬教训：eval 不要用 --max_samples (2026-05-15)\\n- **事故**：seed123 ckpt-6200/6400 test eval 用了 `--max_samples 8192`，只评了 8192/9784 样本，与主表 n=9784 不可比。被 Reviewer 抓出后需 kill+重跑。\\n- **规则**：test eval 禁止 --max_samples 参数，必须评完整 test set (n=9784)。val eval 同理 (n=9335)。\\n- **例外**：debug/dry-run 时可以用，但结果不入正式表。\\n\\n## 硬教训：s42 resume 从 ckpt-600 开始 (2026-05-15)\\n- s42 resume 的 checkpoint 目录 `/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/` 从 ckpt-600 开始（200步间隔），不含 ckpt-200/400。\\n- 原始训练 ckpt-200/400 在 `/root/autodl-tmp/checkpoints_repo_cls_8b_conda/`，但那是 s42 原始训练目录不是 resume 目录。\\n- **提交 s42 val eval 前检查 checkpoint 是否存在于 resume 目录**。\\n\\n## D088 Checkpoint 选择 — Val Sweep 完成 (2026-05-15)\\n- **主指标回到 val-selected checkpoint**（ML 社区规范）\\n- **8B s42 Val-best = ckpt-1000 (88.23%, F1m=82.72%)** ← 8/8 checkpoint 全完成\\n- 完整 val curve: 200(63.5%) → 400(81.0%) → 800(84.5%) → **1000(88.2%)** → 1200(87.8%) → 1400(86.0%) → 1600(86.8%)\\n- **Test curve 完整**: 200(70.07%) → 400(84.79%) → 600(79.05%) → 800(83.53%) → 1000(83.52%) → 1200(83.84%) → **1400(85.47%)** → 1600(84.99%)\\n- Test-best = ckpt-1400 (85.47%), Val-best = ckpt-1000 (88.23%, test=83.52%)\\n\\n## seed123 8B Test Curve 完成 (2026-05-15)\\n- ckpt-200: 72.55% (≈majority baseline 72.96%, 模型尚未学到)\\n- ckpt-3000: **85.60%** ← test-best (val-best checkpoint)\\n- ckpt-6200: 84.70%\\n- ckpt-6400: 85.08%\\n- ckpt-6600: 84.90%\\n- ckpt-6633: 84.89%\\n- **Val curve**: 3000(88.69%) → 6200(87.52%) → 6400(87.48%) → 6600(87.23%) → 6633(87.10%)\\n- save_total_limit=5 导致中段 checkpoint 被删，只剩 200, 6
…[truncated 3470 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T13:30:17.816613+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T13:30:17.816955+00:00_

artifacts/mvp-a-oracle-sim/data/mvp_a_results_summary.txt
artifacts/mvp-a-oracle-sim/chart/mvp_a_curves_ref.txt
artifacts/mvp-a-oracle-sim/data/mvp_a_results_ref.txt
artifacts/mvp-b-data-prep/data/mvp-b-training-data-manifest.txt
artifacts/mvp-b-data-prep/data/mvp_b_data_ref.txt
artifacts/mvp-a-oracle-sim/data/mvp_a_sensitivity_pointer.txt
artifacts/mvp-a-oracle-sim/data/mvp_a_real_f2p_pointer.txt
artifacts/_project/data/swebench_test_dist_pointer.txt
artifacts/mvp-a-oracle-sim/chart/mvp_a_sensitivity_ref.txt
artifacts/mvp-a-oracle-sim/data/mvp_a_total_results.json
artifacts/mvp-a-oracle-sim/chart/mvp_a_total_curves.pdf
artifacts/mvp-a-oracle-sim/chart/mvp_a_total_curves_ref.txt
artifacts/p2p-regression-rate/report/p2p_regression_analysis.md
artifacts/dream_reports/dream_20260511T214810/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260511T214810/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260511T214810/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260511T214810/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260511T214810/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260511T214810/best/experiment_data.json
artifacts/dream_reports/dream_20260511T214810/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260511T214810/median/experiment_data.json
artifacts/dream_reports/dream_20260511T214810/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260511T214810/worst/experiment_data.json
artifacts/dream_reports/dream_20260511T214810/best/review_report.md
artifacts/dream_reports/dream_20260511T214810/median/review_report.md
artifacts/dream_reports/dream_20260511T214810/worst/review_report.md
artifacts/dream_reports/dream_20260511T214810/meta.yaml
artifacts/dream_reports/dream_20260511T223609/meta.yaml
artifacts/dream_reports/dream_20260511T225536/logs/orchestrator.log
artifacts/dream_reports/dream_20260511T225536/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260
…[truncated 4423 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T13:30:17.817367+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/5cbbb9df-024d-468c-b967-a31c715565cd/tool-results/mcp-agent-ml-research-read_registry-1778851665713.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result if isinstance(result, list) else result.get('experiments', result.get('data', []))\n# Find relaxed matching, TOST, mutation type related experiments\nfor exp in exps:\n    eid = exp.get('exp_id', '')\n    conclusion = str(exp.get('conclusion', ''))\n    metrics = str(exp.get('metrics', ''))\n    tags = str(exp.get('tags', ''))\n    combined = (eid + conclusion + metrics + tags).lower()\n    if any(k in combined for k in ['relaxed', 'tost', 'mutation', 'per_type', 'per-type', 'breakdown']):\n        print(f'=== {eid} ===')\n        print(f'  status: {exp.get(\\\"status\\\")}')\n        print(f'  conclusion: {conclusion[:500]}')\n        print(f'  metrics: {metrics[:500]}')\n        print(f'  tags: {tags}')\n        print()\n\" 2>&1 | head -200",
  "description": "Search registry for relaxed/TOST/mutation experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/5cbbb9df-024d-468c-b967-a31c715565cd/tool-results/mcp-agent-ml-research-read_registry-1778851665713.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result if isinstance(result, list) else result.get('experiments', result.get('data', []))\n# Find relaxed matching, TOST, mutation type related experiments\nfor exp in exps:\n    eid = exp.get('exp_id', '')\n    conclusion = str(exp.get('conclusion', ''))\n    metrics = str(exp.get('metrics', ''))\n    tags = str(exp.get('tags', ''))\n    combined = (eid + conclusion + metrics + tags).lower()\n    if any(k in combined for k in ['relaxed', 'tost', 'mutation', 'per_type', 'per-type', 'breakdown']):\n        print(f'=== {eid} ===')\n        print(f'  status: {exp.get(\\\"status\\\")}')\n        print(f'  conclusion: {conclusion[:500]}')\n        print(f'  metrics: {metrics[:500]}')\n        print(f'  tags: {tags}')\n        print()\n\" 2>&1 | head -200",
    "description": "Search registry for relaxed/TOST/mutation experiments"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T13:30:17.817579+00:00_

Traceback (most recent call last):
  File "&lt;string>", line 8, in &lt;module>
    eid = exp.get('exp_id', '')
          ^^^^^^^
AttributeError: 'str' object has no attribute 'get'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T13:30:17.817761+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "artifacts/**/*relaxed*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "Glob",
  "tool_args": {
    "pattern": "artifacts/**/*relaxed*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T13:30:17.817972+00:00_

artifacts/_project/data/relaxed_matching_analysis.txt

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T13:30:17.818112+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "artifacts/**/*tost*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "Glob",
  "tool_args": {
    "pattern": "artifacts/**/*tost*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T13:30:17.818233+00:00_

artifacts/_project/report/tost_multi_margin_results.txt

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T13:30:17.818362+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "artifacts/**/*mutation*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "Glob",
  "tool_args": {
    "pattern": "artifacts/**/*mutation*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T13:30:17.818483+00:00_

artifacts/_project/report/mutation_type_analysis_w3w8_c1.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T13:30:17.818719+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "artifacts/**/*eval*.json",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "Glob",
  "tool_args": {
    "pattern": "artifacts/**/*eval*.json",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T13:30:17.818940+00:00_

artifacts/block-corr-empirical/data/eval_block_correlation_v2.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T13:30:17.819108+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/_project/data/relaxed_matching_analysis.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/_project/data/relaxed_matching_analysis.txt"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T13:30:17.819254+00:00_

1	See /home/sonny/exec-sim-repair-verifier/relaxed_matching_analysis.json on westd server.
2	
3	SUMMARY TABLE:
4	Method          | Parse%  | Acc(parsed) | Overall  | Upper Bound
5	strict          | 46.3%   | 42.88%      | 58.04%   | 59.04%
6	normalized      | 69.6%   | 54.16%      | 59.61%   | 59.87%
7	enhanced        | 77.2%   | 60.79%      | 62.34%   | 63.57%
8	Majority base   | 100%    | 72.96%      | 72.96%   | -
9	CLS 4B          | 100%    | 83.63%      | 83.63%   | -
10	CLS 8B          | 100%    | 83.52%      | 83.52%   | -
11	
12	CONCLUSION: Even with aggressive relaxed matching, CWM (62.34%) is 21.3pp below CLS (83.63%) and still below majority baseline (72.96%). Strict matching is NOT the cause.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T13:30:17.819378+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/_project/report/tost_multi_margin_results.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/_project/report/tost_multi_margin_results.txt"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T13:30:17.819513+00:00_

1	TOST Multi-Margin Equivalence Test Results
2	===========================================
3	Date: 2026-05-15
4	Method: Clustered bootstrap (by problem_id), 10,000 resamples
5	Data: 4 CLS-CWM pairs (2 CLS seeds x 2 CWM seeds), 7,560 total obs, 114 clusters
6	
7	Per-pair accuracy differences (CLS - CWM):
8	  Pair 1: cls_s42 vs cwm_s123  → +0.21pp (87.51% vs 87.30%)
9	  Pair 2: cls_s42 vs cwm_s789  → +0.85pp (87.51% vs 86.67%)
10	  Pair 3: cls_s0  vs cwm_s123  → +0.48pp (87.78% vs 87.30%)
11	  Pair 4: cls_s0  vs cwm_s789  → +1.11pp (87.78% vs 86.67%)
12	
13	Pooled mean diff: +0.661pp
14	95% CI: [-0.479, +1.792]pp
15	Bootstrap SE: 0.577pp
16	
17	TOST Results:
18	  Margin    90% CI                p-value    Equivalent?
19	  ±1pp      [-0.275, +1.620]     0.2854     NO
20	  ±2pp      [-0.275, +1.620]     0.0104     YES
21	  ±3pp      [-0.275, +1.620]     0.0000     YES
22	
23	Minimum equivalence margin: 1.620pp
24	
25	Conclusions:
26	- At ±2pp: EQUIVALENT (p=0.010), confirming the C2 claim
27	- At ±1pp: NOT equivalent (p=0.285), 90% CI upper bound 1.62pp exceeds 1pp
28	- At ±3pp: trivially equivalent (p≈0)
29	- The smallest margin that still yields equivalence is ±1.62pp

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T13:30:17.819655+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/_project/report/mutation_type_analysis_w3w8_c1.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/_project/report/mutation_type_analysis_w3w8_c1.md"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T13:30:17.819878+00:00_

1	# Mutation Type Per-Type Accuracy & Seed Variance Root Cause
2	## W3/W8 + C1 Response Analysis — 2026-05-15
3	
4	---
5	
6	## 1. Eval Set Composition
7	
8	The CLS model is evaluated on `swebench_full/swebench_{split}.jsonl`:
9	- **Test set**: 9,784 instances (100% SWE-bench verified data)
10	- **Val set**: 9,335 instances (100% SWE-bench verified data)
11	
12	Each instance has a `mutation_type`:
13	- `gold` — original gold patch (always label=pass)
14	- `mutation_operator_swap` — operator substitution in patch
15	- `mutation_boundary_removal` — boundary condition removed
16	- `mutation_return_value` — return value changed
17	- `mutation_off_by_one` — off-by-one error injected
18	
19	---
20	
21	## 2. Val → Test Mutation Type Distribution Shift
22	
23	| Mutation Type             |  Val %  | Test %  | Shift (pp) |
24	|---------------------------|---------|---------|------------|
25	| gold                      |  45.2%  |  47.4%  |    +2.1    |
26	| mutation_operator_swap    |  19.1%  |  34.3%  |   **+15.2**|
27	| mutation_boundary_removal |  15.0%  |  10.7%  |    -4.3    |
28	| mutation_return_value     |  10.7%  |   5.7%  |    -5.0    |
29	| mutation_off_by_one       |  10.0%  |   1.9%  |    -8.1    |
30	
31	**Key shift**: operator_swap nearly doubles from 19.1% → 34.3%, while off_by_one collapses from 10.0% → 1.9%.
32	
33	---
34	
35	## 3. Label Distribution by Mutation Type
36	
37	| Mutation Type             | Test N  | Pass %  | Val N   | Val Pass % |
38	|---------------------------|---------|---------|---------|------------|
39	| gold                      |  4,633  | 100.0%  |  4,223  |   100.0%   |
40	| mutation_operator_swap    |  3,357  |  50.4%  |  1,783  |    55.7%   |
41	| mutation_boundary_removal |  1,049  |  41.7%  |  1,401  |    59.2%   |
42	| mutation_return_value     |    562  |  43.8%  |    999  |    26.1%   |
43	| mutation_off_by_one       |    183  |  70.5%  |    929  |    83.5%   |
44	
45	**Majority baselines differ**: off_by_one majority=83.5% (va
…[truncated 12252 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T13:30:17.820076+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/5cbbb9df-024d-468c-b967-a31c715565cd/tool-results/mcp-agent-ml-research-read_registry-1778851665713.txt | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\n# Inspect structure\nresult_str = raw['result']\nresult = json.loads(result_str)\nif isinstance(result, dict):\n    print('Keys:', list(result.keys())[:10])\n    for k, v in result.items():\n        if isinstance(v, list):\n            print(f'{k}: list of {len(v)}, first type: {type(v[0]) if v else None}')\n            if v and isinstance(v[0], dict):\n                print(f'  first keys: {list(v[0].keys())[:10]}')\n        elif isinstance(v, dict):\n            print(f'{k}: dict with keys {list(v.keys())[:10]}')\n        else:\n            print(f'{k}: {type(v).__name__} = {str(v)[:100]}')\nelif isinstance(result, list):\n    print(f'List of {len(result)} items, first type: {type(result[0]) if result else None}')\n\" 2>&1",
  "description": "Inspect registry JSON structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/5cbbb9df-024d-468c-b967-a31c715565cd/tool-results/mcp-agent-ml-research-read_registry-1778851665713.txt | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\n# Inspect structure\nresult_str = raw['result']\nresult = json.loads(result_str)\nif isinstance(result, dict):\n    print('Keys:', list(result.keys())[:10])\n    for k, v in result.items():\n        if isinstance(v, list):\n            print(f'{k}: list of {len(v)}, first type: {type(v[0]) if v else None}')\n            if v and isinstance(v[0], dict):\n                print(f'  first keys: {list(v[0].keys())[:10]}')\n        elif isinstance(v, dict):\n            print(f'{k}: dict with keys {list(v.keys())[:10]}')\n        else:\n            print(f'{k}: {type(v).__name__} = {str(v)[:100]}')\nelif isinstance(result, list):\n    print(f'List of {len(result)} items, first type: {type(result[0]) if result else None}')\n\" 2>&1",
    "description": "Inspect registry JSON structure"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T13:30:17.820220+00:00_

Keys: ['success', 'data', 'error', 'metadata']
success: bool = True
data: dict with keys ['experiments', 'count', 'total', 'baseline']
error: NoneType = None
metadata: dict with keys ['elapsed_seconds']

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T13:30:17.820379+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/5cbbb9df-024d-468c-b967-a31c715565cd/tool-results/mcp-agent-ml-research-read_registry-1778851665713.txt | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\nresult = json.loads(raw['result'])\nexps = result['data']['experiments']\nfor exp in exps:\n    eid = exp.get('exp_id', '')\n    conclusion = str(exp.get('conclusion', ''))\n    metrics = json.dumps(exp.get('metrics', {})) if exp.get('metrics') else ''\n    tags = str(exp.get('tags', ''))\n    combined = (eid + conclusion + metrics + tags).lower()\n    if any(k in combined for k in ['relaxed', 'tost', 'equivalen']):\n        print(f'=== {eid} ===')\n        print(f'  status: {exp.get(\\\"status\\\")}')\n        print(f'  conclusion: {conclusion[:600]}')\n        print(f'  metrics: {metrics[:600]}')\n        print()\n\" 2>&1 | head -150",
  "description": "Search registry for relaxed/TOST experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/5cbbb9df-024d-468c-b967-a31c715565cd/tool-results/mcp-agent-ml-research-read_registry-1778851665713.txt | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\nresult = json.loads(raw['result'])\nexps = result['data']['experiments']\nfor exp in exps:\n    eid = exp.get('exp_id', '')\n    conclusion = str(exp.get('conclusion', ''))\n    metrics = json.dumps(exp.get('metrics', {})) if exp.get('metrics') else ''\n    tags = str(exp.get('tags', ''))\n    combined = (eid + conclusion + metrics + tags).lower()\n    if any(k in combined for k in ['relaxed', 'tost', 'equivalen']):\n        print(f'=== {eid} ===')\n        print(f'  status: {exp.get(\\\"status\\\")}')\n        print(f'  conclusion: {conclusion[:600]}')\n        print(f'  metrics: {metrics[:600]}')\n        print()\n\" 2>&1 | head -150",
    "description": "Search registry for relaxed/TOST experiments"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T13:30:17.820684+00:00_

Traceback (most recent call last):
  File "&lt;string>", line 7, in &lt;module>
    eid = exp.get('exp_id', '')
          ^^^^^^^
AttributeError: 'str' object has no attribute 'get'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T13:30:17.820841+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/5cbbb9df-024d-468c-b967-a31c715565cd/tool-results/mcp-agent-ml-research-read_registry-1778851665713.txt | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\nresult = json.loads(raw['result'])\nexps = result['data']['experiments']\n# Find all experiments with their exp_id and status for overview\nfor exp in exps:\n    eid = exp.get('exp_id', '')\n    status = exp.get('status', '')\n    metrics = exp.get('metrics', {})\n    if metrics and isinstance(metrics, dict):\n        acc = metrics.get('accuracy') or metrics.get('test_accuracy') or metrics.get('val_accuracy')\n        f1 = metrics.get('f1_macro') or metrics.get('f1')\n        if acc:\n            print(f'{eid:50s} {status:8s} acc={acc} f1={f1}')\n\" 2>&1 | head -80",
  "description": "List all experiments with accuracy metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/5cbbb9df-024d-468c-b967-a31c715565cd/tool-results/mcp-agent-ml-research-read_registry-1778851665713.txt | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\nresult = json.loads(raw['result'])\nexps = result['data']['experiments']\n# Find all experiments with their exp_id and status for overview\nfor exp in exps:\n    eid = exp.get('exp_id', '')\n    status = exp.get('status', '')\n    metrics = exp.get('metrics', {})\n    if metrics and isinstance(metrics, dict):\n        acc = metrics.get('accuracy') or metrics.get('test_accuracy') or metrics.get('val_accuracy')\n        f1 = metrics.get('f1_macro') or metrics.get('f1')\n        if acc:\n            print(f'{eid:50s} {status:8s} acc={acc} f1={f1}')\n\" 2>&1 | head -80",
    "description": "List all experiments with accuracy metrics"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T13:30:17.820983+00:00_

Traceback (most recent call last):
  File "&lt;string>", line 8, in &lt;module>
    eid = exp.get('exp_id', '')
          ^^^^^^^
AttributeError: 'str' object has no attribute 'get'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-15T13:30:17.821107+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/5cbbb9df-024d-468c-b967-a31c715565cd/tool-results/mcp-agent-ml-research-read_registry-1778851665713.txt | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\nresult = json.loads(raw['result'])\nexps = result['data']['experiments']\nprint(f'Type: {type(exps)}, len: {len(exps)}')\nprint(f'First item type: {type(exps[0])}')\nprint(f'First item (first 500 chars): {str(exps[0])[:500]}')\n\" 2>&1",
  "description": "Inspect experiments list structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/5cbbb9df-024d-468c-b967-a31c715565cd/tool-results/mcp-agent-ml-research-read_registry-1778851665713.txt | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\nresult = json.loads(raw['result'])\nexps = result['data']['experiments']\nprint(f'Type: {type(exps)}, len: {len(exps)}')\nprint(f'First item type: {type(exps[0])}')\nprint(f'First item (first 500 chars): {str(exps[0])[:500]}')\n\" 2>&1",
    "description": "Inspect experiments list structure"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-15T13:30:17.821229+00:00_

Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 7, in &lt;module>
    print(f'First item type: {type(exps[0])}')
                                   ~~~~^^^
KeyError: 0
Type: &lt;class 'dict'>, len: 125

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-15T13:30:17.821353+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/5cbbb9df-024d-468c-b967-a31c715565cd/tool-results/mcp-agent-ml-research-read_registry-1778851665713.txt | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\nresult = json.loads(raw['result'])\nexps = result['data']['experiments']\n# It's a dict keyed by exp_id\nkeys = list(exps.keys())\nprint(f'Total experiments: {len(keys)}')\nprint(f'First 5 keys: {keys[:5]}')\n# Print first experiment structure\nfirst_key = keys[0]\nfirst_exp = exps[first_key]\nprint(f'First exp type: {type(first_exp)}')\nprint(f'First exp (500 chars): {str(first_exp)[:500]}')\n\" 2>&1",
  "description": "Inspect dict-based experiments structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/5cbbb9df-024d-468c-b967-a31c715565cd/tool-results/mcp-agent-ml-research-read_registry-1778851665713.txt | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\nresult = json.loads(raw['result'])\nexps = result['data']['experiments']\n# It's a dict keyed by exp_id\nkeys = list(exps.keys())\nprint(f'Total experiments: {len(keys)}')\nprint(f'First 5 keys: {keys[:5]}')\n# Print first experiment structure\nfirst_key = keys[0]\nfirst_exp = exps[first_key]\nprint(f'First exp type: {type(first_exp)}')\nprint(f'First exp (500 chars): {str(first_exp)[:500]}')\n\" 2>&1",
    "description": "Inspect dict-based experiments structure"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-15T13:30:17.821478+00:00_

Total experiments: 125
First 5 keys: ['cwm-rank32-ablation-v2', 'cwm-rank32-ablation', 'cwm-4b-rank32-ablation', 'cls4b-v5-ckpt4000-test5120-eval', 'cwm8b-ckpt400-test-eval']
First exp type: &lt;class 'dict'>
First exp (500 chars): {'status': 'RUNNING', 'retry_count': 0, 'created_at': '2026-05-15T12:50:32.964Z', 'updated_at': '2026-05-15T12:54:32.192Z', 'spec': {'command': 'CUDA_VISIBLE_DEVICES=0 python3 train_cwm_baseline.py --data_dir data/ --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-4B --output_dir checkpoints_cwm_rank32/ --batch_size 2 --grad_accumulation 16 --no_wandb --seed 42 --lora_rank 32', 'server': 'seetacloud-westd-4x5090', 'data_path': '/home/sonny/exec-sim-repair-verifier/data/cwm_train.jsonl', 'data_c

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-15T13:30:17.821609+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/5cbbb9df-024d-468c-b967-a31c715565cd/tool-results/mcp-agent-ml-research-read_registry-1778851665713.txt | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\nresult = json.loads(raw['result'])\nexps = result['data']['experiments']\n\n# Search for relaxed, TOST, equivalence, mutation\nfor eid, exp in exps.items():\n    conclusion = str(exp.get('conclusion', ''))\n    metrics = json.dumps(exp.get('metrics', {})) if exp.get('metrics') else ''\n    tags = str(exp.get('tags', ''))\n    combined = (eid + conclusion + metrics + tags).lower()\n    if any(k in combined for k in ['relaxed', 'tost', 'equivalen', 'mutation', 'cwm']):\n        print(f'=== {eid} ===')\n        print(f'  status: {exp.get(\\\"status\\\")}')\n        if exp.get('metrics'):\n            print(f'  metrics: {json.dumps(exp[\\\"metrics\\\"])[:500]}')\n        if exp.get('conclusion'):\n            print(f'  conclusion: {str(exp[\\\"conclusion\\\"])[:300]}')\n        print()\n\" 2>&1 | head -200",
  "description": "Search experiments for relaxed/TOST/CWM data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/5cbbb9df-024d-468c-b967-a31c715565cd/tool-results/mcp-agent-ml-research-read_registry-1778851665713.txt | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\nresult = json.loads(raw['result'])\nexps = result['data']['experiments']\n\n# Search for relaxed, TOST, equivalence, mutation\nfor eid, exp in exps.items():\n    conclusion = str(exp.get('conclusion', ''))\n    metrics = json.dumps(exp.get('metrics', {})) if exp.get('metrics') else ''\n    tags = str(exp.get('tags', ''))\n    combined = (eid + conclusion + metrics + tags).lower()\n    if any(k in combined for k in ['relaxed', 'tost', 'equivalen', 'mutation', 'cwm']):\n        print(f'=== {eid} ===')\n        print(f'  status: {exp.get(\\\"status\\\")}')\n        if exp.get('metrics'):\n            print(f'  metrics: {json.dumps(exp[\\\"metrics\\\"])[:500]}')\n        if exp.get('conclusion'):\n            print(f'  conclusion: {str(exp[\\\"conclusion\\\"])[:300]}')\n        print()\n\" 2>&1 | head -200",
    "description": "Search experiments for relaxed/TOST/CWM data"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-15T13:30:17.821819+00:00_

=== cwm-rank32-ablation-v2 ===
  status: RUNNING

=== cwm-rank32-ablation ===
  status: DONE
  conclusion: killed

=== cwm-4b-rank32-ablation ===
  status: DONE
  conclusion: killed

=== cwm8b-ckpt400-test-eval ===
  status: RUNNING

=== repo-level-cwm-8b-conda-v4 ===
  status: RUNNING

=== repo-level-cwm-seed123-conda ===
  status: DONE
  metrics: {"eval_test_accuracy": 59.09, "eval_test_f1_macro": 43.43, "eval_test_f1_fail": 13.67, "eval_test_f1_pass": 73.19, "eval_test_unparseable": 6574, "eval_test_total": 9784, "eval_test_unparseable_rate": 67.2, "eval_checkpoint": "checkpoint-500"}
  conclusion: killed

=== repo-level-cwm-v12 ===
  status: DONE
  metrics: {"eval_test_accuracy": 58.04, "eval_test_f1_macro": 51.67, "eval_test_f1_fail": 34.12, "eval_test_f1_pass": 69.22, "eval_test_unparseable": 5255, "eval_test_total": 9784, "eval_test_unparseable_rate": 53.7, "eval_checkpoint": "checkpoint-500"}
  conclusion: killed

=== repo-level-cwm-8b-conda-v2 ===
  status: DONE
  conclusion: failed

=== repo-level-cwm-8b-conda-v3 ===
  status: DONE
  conclusion: failed

=== repo-level-cwm-8b-conda ===
  status: DONE
  conclusion: failed

=== repo-level-cwm-v11 ===
  status: DONE
  metrics: {"eval_checkpoint": "checkpoint-600", "eval_samples": 500, "eval_type": "subset500_tok1024", "accuracy": 66.6, "fail_f1": 27.7, "pass_f1": 78.3, "f1_macro": 52.99, "fail_precision": 33.3, "fail_recall": 23.7, "pass_precision": 74.5, "pass_recall": 82.5, "unparseable": 376, "unparseable_pct": 75.2, "majority_baseline": 73, "gap_vs_baseline": -6.4, "gen_length_mean": 3398.1, "gen_length_median": 3307.5, "gen_length_max": 7582, "confusion": {"TP": 301, "TN": 32, "FP": 103, "FN": 64}}
  conclusion: killed

=== repo-level-cwm-seed123 ===
  status: DONE
  conclusion: killed

=== repo-level-cwm-v10 ===
  status: DONE
  metrics: {"accuracy": 0.6991, "f1_macro": 0.4671, "f1_pass": 0.8187, "f1_fail": 0.1154, "precision_pass": 0.7304, "recall_pass": 0.9314, "precision_fail": 0.2815, "recall_fail": 
…[truncated 4562 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-15T13:30:17.822011+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/5cbbb9df-024d-468c-b967-a31c715565cd/tool-results/mcp-agent-ml-research-read_registry-1778851665713.txt | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\nresult = json.loads(raw['result'])\nexps = result['data']['experiments']\n\n# Find CLS experiments + seq_length ablation\nfor eid, exp in exps.items():\n    conclusion = str(exp.get('conclusion', ''))\n    metrics = json.dumps(exp.get('metrics', {})) if exp.get('metrics') else ''\n    combined = (eid + conclusion + metrics).lower()\n    if any(k in combined for k in ['cls', 'seq_length', 'seq2048', 'relaxed_match']):\n        if exp.get('metrics'):\n            print(f'=== {eid} ===')\n            print(f'  status: {exp.get(\\\"status\\\")}')\n            print(f'  metrics: {json.dumps(exp[\\\"metrics\\\"])[:400]}')\n            if exp.get('conclusion'):\n                print(f'  conclusion: {str(exp[\\\"conclusion\\\"])[:200]}')\n            print()\n\" 2>&1 | head -200",
  "description": "Search for CLS and seq_length experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/5cbbb9df-024d-468c-b967-a31c715565cd/tool-results/mcp-agent-ml-research-read_registry-1778851665713.txt | python3 -c \"\nimport json, sys\nraw = json.load(sys.stdin)\nresult = json.loads(raw['result'])\nexps = result['data']['experiments']\n\n# Find CLS experiments + seq_length ablation\nfor eid, exp in exps.items():\n    conclusion = str(exp.get('conclusion', ''))\n    metrics = json.dumps(exp.get('metrics', {})) if exp.get('metrics') else ''\n    combined = (eid + conclusion + metrics).lower()\n    if any(k in combined for k in ['cls', 'seq_length', 'seq2048', 'relaxed_match']):\n        if exp.get('metrics'):\n            print(f'=== {eid} ===')\n            print(f'  status: {exp.get(\\\"status\\\")}')\n            print(f'  metrics: {json.dumps(exp[\\\"metrics\\\"])[:400]}')\n            if exp.get('conclusion'):\n                print(f'  conclusion: {str(exp[\\\"conclusion\\\"])[:200]}')\n            print()\n\" 2>&1 | head -200",
    "description": "Search for CLS and seq_length experiments"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-15T13:30:17.822265+00:00_

=== cls8b-seed123-ckpt200-test-eval ===
  status: DONE
  metrics: {"accuracy": 72.55, "f1_macro": 70.18, "pass_f1": 78.58, "fail_f1": 61.78, "pass_precision": 91.21, "pass_recall": 69.02, "fail_precision": 49.54, "fail_recall": 82.05, "n_samples": 9784, "n_pass": 7138, "n_fail": 2646, "majority_baseline": 72.96, "unparseable": 0, "confusion_matrix": {"tn": 2171, "fp": 475, "fn": 2211, "tp": 4927}}
  conclusion: success

=== cls8b-s42-ckpt1000-test-seq2048-ablation ===
  status: DONE
  metrics: {"accuracy": 82.83, "f1_macro": 76.88, "fail_precision": 72.2, "fail_recall": 59.3, "fail_f1": 65.2, "pass_precision": 85.9, "pass_recall": 91.5, "pass_f1": 88.6, "unparseable": 136}
  conclusion: success

=== cls8b-seed123-ckpt6633-test-eval ===
  status: DONE
  metrics: {"accuracy": 84.89, "f1_macro": 77.56, "f1_fail": 64.7, "f1_pass": 90.4, "precision_fail": 87.8, "recall_fail": 51.2, "precision_pass": 84.3, "recall_pass": 97.4, "majority_baseline": 73, "gap_vs_majority_pp": 11.9, "total_samples": 9784, "unparseable_count": 0}
  conclusion: success

=== cls8b-seed123-ckpt6600-test-eval ===
  status: DONE
  metrics: {"accuracy": 84.9, "f1_macro": 77.58, "pass_f1": 90.4, "fail_f1": 64.8, "pass_precision": 84.3, "pass_recall": 97.4, "fail_precision": 87.8, "fail_recall": 51.3, "n_samples": 9784, "n_pass": 7138, "n_fail": 2646, "majority_baseline": 73, "unparseable": 0, "confusion_matrix": {"fail_as_fail": 1357, "fail_as_pass": 1289, "pass_as_fail": 188, "pass_as_pass": 6950}}
  conclusion: success

=== cls8b-s42-ckpt200-test8192-eval ===
  status: DONE
  metrics: {"accuracy": 70.07, "f1_macro": 68.18, "pass_f1": 75.9, "fail_f1": 60.4, "pass_precision": 91.8, "pass_recall": 64.7, "fail_precision": 47, "fail_recall": 84.5, "n_samples": 9784, "n_pass": 7138, "n_fail": 2646, "majority_baseline": 73, "unparseable": 0, "confusion_matrix": {"fail_as_fail": 2235, "fail_as_pass": 411, "pass_as_fail": 2517, "pass_as_pass": 4621}}
  conclusion: success

=== cls4b-v5-ckpt600-test5120-eval
…[truncated 11811 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-15T13:30:17.822706+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "artifacts/**/*cwm*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "Glob",
  "tool_args": {
    "pattern": "artifacts/**/*cwm*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-15T13:30:17.822911+00:00_

artifacts/cwm8b_seed123_analysis.txt
artifacts/_project/report/analysis_cls_vs_cwm_4b_5paired.json
artifacts/_project/data/cwm_seed42_predictions_ref.txt
artifacts/_project/data/cls_cwm_error_overlap.md
artifacts/_project/data/4b_8b_cls_cwm_paired_bootstrap_corrected.json
artifacts/4b_8b_cls_cwm_paired_bootstrap_corrected.json
artifacts/cwm_v6_health_check.md
artifacts/cwm_v6_diagnosis.md
artifacts/diag_cwm_v10.md
artifacts/diagnosis_cwm_v12_cls_8b.md
artifacts/cwm_error_mode_analysis.md
artifacts/_project/report/cwm_cls_convergence.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-15T13:30:17.823058+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "artifacts/**/*bootstrap*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "Glob",
  "tool_args": {
    "pattern": "artifacts/**/*bootstrap*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-15T13:30:17.823184+00:00_

artifacts/_project/intermediate/analysis_5paired_bootstrap.py
artifacts/analysis_5paired_bootstrap.py
artifacts/_project/data/8b_scaling_bootstrap_results.json
artifacts/_project/data/4b_8b_cls_cwm_paired_bootstrap_corrected.json
artifacts/4b_8b_cls_cwm_paired_bootstrap_corrected.json
artifacts/_project/intermediate/paired_bootstrap_repo_info.txt

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-15T13:30:17.823307+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/_project/data/4b_8b_cls_cwm_paired_bootstrap_corrected.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/_project/data/4b_8b_cls_cwm_paired_bootstrap_corrected.json"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-15T13:30:17.823451+00:00_

1	{
2	  "4B_cls_vs_cwm_5seeds": {
3	    "paired_diffs": [0.32, 2.32, 0.90, 2.33, 0.37],
4	    "mean_gap_pp": 1.25,
5	    "std": 1.01,
6	    "paired_t": 2.77,
7	    "p_value_one_sided": 0.0253,
8	    "bootstrap_95ci": [0.46, 2.04],
9	    "cohens_d": 1.24,
10	    "tost_p_2pp": 0.0855,
11	    "note": "CLS significantly better, not equivalent"
12	  },
13	  "8B_cls_vs_cwm_3seeds": {
14	    "mean_gap_pp": 2.26,
15	    "paired_t": 8.60,
16	    "p_value_one_sided": 0.0066,
17	    "bootstrap_95ci": [1.80, 2.71],
18	    "cohens_d": 4.97
19	  },
20	  "scaling_trend": {
21	    "gap_increase_pp": 1.01,
22	    "p_8b_gt_4b": 0.988
23	  }
24	}
25	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-15T13:30:17.823597+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/relaxed_matching_results.csv",
  "content": "exp_id,model,checkpoint,match_type,parse_rate,accuracy_parsed,accuracy_overall,f1_macro,upper_bound\ncwm-4b-v12-strict,CWM 4B,checkpoint-500,strict,46.3,42.88,58.04,51.67,59.04\ncwm-4b-v12-normalized,CWM 4B,checkpoint-500,normalized,69.6,54.16,59.61,,59.87\ncwm-4b-v12-enhanced,CWM 4B,checkpoint-500,enhanced,77.2,60.79,62.34,,63.57\ncwm-4b-seed123-strict,CWM 4B seed123,checkpoint-500,strict,32.8,,59.09,43.43,\ncls-8b-s42-ckpt1000,CLS 8B,ckpt-1000,strict,100.0,83.52,83.52,77.50,\ncls-8b-seed123-ckpt3000,CLS 8B seed123,ckpt-3000,strict,100.0,85.60,85.60,78.38,\ncls-4b-s42-ckpt4600,CLS 4B,ckpt-4600,strict,100.0,83.63,83.63,75.63,\ncls-4b-seed123-ckpt800,CLS 4B seed123,ckpt-800,strict,100.0,75.33,75.33,67.03,\nmajority-baseline,Majority,,strict,100.0,72.96,72.96,,\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/relaxed_matching_results.csv",
    "content": "exp_id,model,checkpoint,match_type,parse_rate,accuracy_parsed,accuracy_overall,f1_macro,upper_bound\ncwm-4b-v12-strict,CWM 4B,checkpoint-500,strict,46.3,42.88,58.04,51.67,59.04\ncwm-4b-v12-normalized,CWM 4B,checkpoint-500,normalized,69.6,54.16,59.61,,59.87\ncwm-4b-v12-enhanced,CWM 4B,checkpoint-500,enhanced,77.2,60.79,62.34,,63.57\ncwm-4b-seed123-strict,CWM 4B seed123,checkpoint-500,strict,32.8,,59.09,43.43,\ncls-8b-s42-ckpt1000,CLS 8B,ckpt-1000,strict,100.0,83.52,83.52,77.50,\ncls-8b-seed123-ckpt3000,CLS 8B seed123,ckpt-3000,strict,100.0,85.60,85.60,78.38,\ncls-4b-s42-ckpt4600,CLS 4B,ckpt-4600,strict,100.0,83.63,83.63,75.63,\ncls-4b-seed123-ckpt800,CLS 4B seed123,ckpt-800,strict,100.0,75.33,75.33,67.03,\nmajority-baseline,Majority,,strict,100.0,72.96,72.96,,\n"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-15T13:30:17.823732+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/relaxed_matching_results.csv

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-15T13:30:17.823875+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/tost_multi_margin.csv",
  "content": "margin_pp,ci90_lower,ci90_upper,pooled_mean_diff_pp,bootstrap_se,p_value,reject_null,n_pairs,n_clusters,n_obs\n1.0,-0.275,1.620,0.661,0.577,0.2854,NO,4,114,7560\n2.0,-0.275,1.620,0.661,0.577,0.0104,YES,4,114,7560\n3.0,-0.275,1.620,0.661,0.577,0.0000,YES,4,114,7560\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/tost_multi_margin.csv",
    "content": "margin_pp,ci90_lower,ci90_upper,pooled_mean_diff_pp,bootstrap_se,p_value,reject_null,n_pairs,n_clusters,n_obs\n1.0,-0.275,1.620,0.661,0.577,0.2854,NO,4,114,7560\n2.0,-0.275,1.620,0.661,0.577,0.0104,YES,4,114,7560\n3.0,-0.275,1.620,0.661,0.577,0.0000,YES,4,114,7560\n"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-15T13:30:17.824167+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/tost_multi_margin.csv

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-15T13:30:17.824375+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/mutation_type_accuracy.csv",
  "content": "mutation_type,cls_8b_s42_ckpt800,cls_8b_s42_ckpt1400,cls_8b_s123_ckpt3000,cls_8b_s123_ckpt6400,cwm_4b_s42,cwm_4b_seed123,val_pct,test_pct,test_n\ngold,94.09,98.36,99.57,98.42,,,45.2,47.4,4633\nmutation_operator_swap,82.72,82.16,82.60,83.23,,,19.1,34.3,3357\nmutation_boundary_removal,41.47,47.28,44.90,41.75,,,15.0,10.7,1049\nmutation_return_value,83.99,69.04,66.37,69.04,,,10.7,5.7,562\nmutation_off_by_one,71.04,89.07,79.23,78.69,,,10.0,1.9,183\nOVERALL,83.53,85.47,85.60,85.08,58.04,59.09,100.0,100.0,9784\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/mutation_type_accuracy.csv",
    "content": "mutation_type,cls_8b_s42_ckpt800,cls_8b_s42_ckpt1400,cls_8b_s123_ckpt3000,cls_8b_s123_ckpt6400,cwm_4b_s42,cwm_4b_seed123,val_pct,test_pct,test_n\ngold,94.09,98.36,99.57,98.42,,,45.2,47.4,4633\nmutation_operator_swap,82.72,82.16,82.60,83.23,,,19.1,34.3,3357\nmutation_boundary_removal,41.47,47.28,44.90,41.75,,,15.0,10.7,1049\nmutation_return_value,83.99,69.04,66.37,69.04,,,10.7,5.7,562\nmutation_off_by_one,71.04,89.07,79.23,78.69,,,10.0,1.9,183\nOVERALL,83.53,85.47,85.60,85.08,58.04,59.09,100.0,100.0,9784\n"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-15T13:30:17.824513+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/mutation_type_accuracy.csv

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-15T13:30:17.824852+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/multi_seed_test_curves.json",
  "content": "{\n  \"cls_8b_s42\": [\n    {\"checkpoint\": \"ckpt-200\", \"step\": 200, \"test_acc\": 70.07, \"f1_macro\": 68.18},\n    {\"checkpoint\": \"ckpt-400\", \"step\": 400, \"test_acc\": 84.79, \"f1_macro\": 81.18},\n    {\"checkpoint\": \"ckpt-600\", \"step\": 600, \"test_acc\": 79.05, \"f1_macro\": 75.12},\n    {\"checkpoint\": \"ckpt-800\", \"step\": 800, \"test_acc\": 83.53, \"f1_macro\": 78.97},\n    {\"checkpoint\": \"ckpt-1000\", \"step\": 1000, \"test_acc\": 83.52, \"f1_macro\": 77.50},\n    {\"checkpoint\": \"ckpt-1200\", \"step\": 1200, \"test_acc\": 83.84, \"f1_macro\": 77.47},\n    {\"checkpoint\": \"ckpt-1400\", \"step\": 1400, \"test_acc\": 85.47, \"f1_macro\": 78.90},\n    {\"checkpoint\": \"ckpt-1600\", \"step\": 1600, \"test_acc\": 84.99, \"f1_macro\": 78.94}\n  ],\n  \"cls_8b_s42_val\": [\n    {\"checkpoint\": \"ckpt-200\", \"step\": 200, \"val_acc\": 63.52, \"f1_macro\": 61.17},\n    {\"checkpoint\": \"ckpt-400\", \"step\": 400, \"val_acc\": 80.96},\n    {\"checkpoint\": \"ckpt-800\", \"step\": 800, \"val_acc\": 84.50, \"f1_macro\": 79.20},\n    {\"checkpoint\": \"ckpt-1000\", \"step\": 1000, \"val_acc\": 88.23, \"f1_macro\": 82.72},\n    {\"checkpoint\": \"ckpt-1200\", \"step\": 1200, \"val_acc\": 87.76, \"f1_macro\": 81.25},\n    {\"checkpoint\": \"ckpt-1400\", \"step\": 1400, \"val_acc\": 85.97, \"f1_macro\": 77.15},\n    {\"checkpoint\": \"ckpt-1600\", \"step\": 1600, \"val_acc\": 86.75, \"f1_macro\": 78.94}\n  ],\n  \"cls_8b_seed123\": [\n    {\"checkpoint\": \"ckpt-200\", \"step\": 200, \"test_acc\": 72.55, \"f1_macro\": 70.18},\n    {\"checkpoint\": \"ckpt-3000\", \"step\": 3000, \"test_acc\": 85.60, \"f1_macro\": 78.38},\n    {\"checkpoint\": \"ckpt-6200\", \"step\": 6200, \"test_acc\": 84.70, \"f1_macro\": 77.01},\n    {\"checkpoint\": \"ckpt-6400\", \"step\": 6400, \"test_acc\": 85.08, \"f1_macro\": 77.91},\n    {\"checkpoint\": \"ckpt-6600\", \"step\": 6600, \"test_acc\": 84.90, \"f1_macro\": 77.58},\n    {\"checkpoint\": \"ckpt-6633\", \"step\": 6633, \"test_acc\": 84.89, \"f1_macro\": 77.56}\n  ],\n  \"cls_8b_seed123_val\": [\n    {\"checkpoint\": \"ckpt-3000\", \"step\": 3000, \"val_acc\": 88.69, \"f1_macro\": 81.73},\n    {\"checkpoint\": \"ckpt-6200\", \"step\": 6200, \"val_acc\": 87.52, \"f1_macro\": 79.26},\n    {\"checkpoint\": \"ckpt-6400\", \"step\": 6400, \"val_acc\": 87.48, \"f1_macro\": 79.66},\n    {\"checkpoint\": \"ckpt-6600\", \"step\": 6600, \"val_acc\": 87.23, \"f1_macro\": 79.02},\n    {\"checkpoint\": \"ckpt-6633\", \"step\": 6633, \"val_acc\": 87.10, \"f1_macro\": 78.79}\n  ],\n  \"cls_4b_s42\": [\n    {\"checkpoint\": \"ckpt-4400\", \"step\": 4400, \"test_acc\": 83.24, \"f1_macro\": 74.44},\n    {\"checkpoint\": \"ckpt-4600\", \"step\": 4600, \"test_acc\": 83.63, \"f1_macro\": 75.63}\n  ],\n  \"cls_4b_s42_val\": [\n    {\"checkpoint\": \"ckpt-600\", \"step\": 600, \"val_acc\": 82.82, \"f1_macro\": 79.81},\n    {\"checkpoint\": \"ckpt-4000\", \"step\": 4000, \"val_acc\": 89.84, \"f1_macro\": 84.25},\n    {\"checkpoint\": \"ckpt-4200\", \"step\": 4200, \"val_acc\": 89.06, \"f1_macro\": 83.07},\n    {\"checkpoint\": \"ckpt-4400\", \"step\": 4400, \"val_acc\": 89.96, \"f1_macro\": 84.94},\n    {\"checkpoint\": \"ckpt-4600\", \"step\": 4600, \"val_acc\": 90.07, \"f1_macro\": 85.04}\n  ],\n  \"cls_4b_seed123\": [\n    {\"checkpoint\": \"ckpt-800\", \"step\": 800, \"test_acc\": 75.33, \"f1_macro\": 67.03}\n  ],\n  \"cwm_4b_s42\": [\n    {\"checkpoint\": \"final\", \"test_acc\": 58.04, \"f1_macro\": 51.67, \"unparseable_rate\": 53.7}\n  ],\n  \"cwm_4b_seed123\": [\n    {\"checkpoint\": \"final\", \"test_acc\": 59.09, \"f1_macro\": 43.43, \"unparseable_rate\": 67.2}\n  ],\n  \"cls_8b_s42_seq2048_ablation\": [\n    {\"checkpoint\": \"ckpt-1000\", \"step\": 1000, \"test_acc\": 82.83, \"f1_macro\": 76.88, \"note\": \"seq_length=2048 ablation\"}\n  ],\n  \"majority_baseline\": {\n    \"val\": 75.88,\n    \"test\": 72.96\n  }\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/multi_seed_test_curves.json",
    "content": "{\n  \"cls_8b_s42\": [\n    {\"checkpoint\": \"ckpt-200\", \"step\": 200, \"test_acc\": 70.07, \"f1_macro\": 68.18},\n    {\"checkpoint\": \"ckpt-400\", \"step\": 400, \"test_acc\": 84.79, \"f1_macro\": 81.18},\n    {\"checkpoint\": \"ckpt-600\", \"step\": 600, \"test_acc\": 79.05, \"f1_macro\": 75.12},\n    {\"checkpoint\": \"ckpt-800\", \"step\": 800, \"test_acc\": 83.53, \"f1_macro\": 78.97},\n    {\"checkpoint\": \"ckpt-1000\", \"step\": 1000, \"test_acc\": 83.52, \"f1_macro\": 77.50},\n    {\"checkpoint\": \"ckpt-1200\", \"step\": 1200, \"test_acc\": 83.84, \"f1_macro\": 77.47},\n    {\"checkpoint\": \"ckpt-1400\", \"step\": 1400, \"test_acc\": 85.47, \"f1_macro\": 78.90},\n    {\"checkpoint\": \"ckpt-1600\", \"step\": 1600, \"test_acc\": 84.99, \"f1_macro\": 78.94}\n  ],\n  \"cls_8b_s42_val\": [\n    {\"checkpoint\": \"ckpt-200\", \"step\": 200, \"val_acc\": 63.52, \"f1_macro\": 61.17},\n    {\"checkpoint\": \"ckpt-400\", \"step\": 400, \"val_acc\": 80.96},\n    {\"checkpoint\": \"ckpt-800\", \"step\": 800, \"val_acc\": 84.50, \"f1_macro\": 79.20},\n    {\"checkpoint\": \"ckpt-1000\", \"step\": 1000, \"val_acc\": 88.23, \"f1_macro\": 82.72},\n    {\"checkpoint\": \"ckpt-1200\", \"step\": 1200, \"val_acc\": 87.76, \"f1_macro\": 81.25},\n    {\"checkpoint\": \"ckpt-1400\", \"step\": 1400, \"val_acc\": 85.97, \"f1_macro\": 77.15},\n    {\"checkpoint\": \"ckpt-1600\", \"step\": 1600, \"val_acc\": 86.75, \"f1_macro\": 78.94}\n  ],\n  \"cls_8b_seed123\": [\n    {\"checkpoint\": \"ckpt-200\", \"step\": 200, \"test_acc\": 72.55, \"f1_macro\": 70.18},\n    {\"checkpoint\": \"ckpt-3000\", \"step\": 3000, \"test_acc\": 85.60, \"f1_macro\": 78.38},\n    {\"checkpoint\": \"ckpt-6200\", \"step\": 6200, \"test_acc\": 84.70, \"f1_macro\": 77.01},\n    {\"checkpoint\": \"ckpt-6400\", \"step\": 6400, \"test_acc\": 85.08, \"f1_macro\": 77.91},\n    {\"checkpoint\": \"ckpt-6600\", \"step\": 6600, \"test_acc\": 84.90, \"f1_macro\": 77.58},\n    {\"checkpoint\": \"ckpt-6633\", \"step\": 6633, \"test_acc\": 84.89, \"f1_macro\": 77.56}\n  ],\n  \"cls_8b_seed123_val\": [\n    {\"checkpoint\": \"ckpt-3000\", \"step\": 3000, \"val_acc\": 88.69, \"f1_macro\": 81.73},\n    {\"checkpoint\": \"ckpt-6200\", \"step\": 6200, \"val_acc\": 87.52, \"f1_macro\": 79.26},\n    {\"checkpoint\": \"ckpt-6400\", \"step\": 6400, \"val_acc\": 87.48, \"f1_macro\": 79.66},\n    {\"checkpoint\": \"ckpt-6600\", \"step\": 6600, \"val_acc\": 87.23, \"f1_macro\": 79.02},\n    {\"checkpoint\": \"ckpt-6633\", \"step\": 6633, \"val_acc\": 87.10, \"f1_macro\": 78.79}\n  ],\n  \"cls_4b_s42\": [\n    {\"checkpoint\": \"ckpt-4400\", \"step\": 4400, \"test_acc\": 83.24, \"f1_macro\": 74.44},\n    {\"checkpoint\": \"ckpt-4600\", \"step\": 4600, \"test_acc\": 83.63, \"f1_macro\": 75.63}\n  ],\n  \"cls_4b_s42_val\": [\n    {\"checkpoint\": \"ckpt-600\", \"step\": 600, \"val_acc\": 82.82, \"f1_macro\": 79.81},\n    {\"checkpoint\": \"ckpt-4000\", \"step\": 4000, \"val_acc\": 89.84, \"f1_macro\": 84.25},\n    {\"checkpoint\": \"ckpt-4200\", \"step\": 4200, \"val_acc\": 89.06, \"f1_macro\": 83.07},\n    {\"checkpoint\": \"ckpt-4400\", \"step\": 4400, \"val_acc\": 89.96, \"f1_macro\": 84.94},\n    {\"checkpoint\": \"ckpt-4600\", \"step\": 4600, \"val_acc\": 90.07, \"f1_macro\": 85.04}\n  ],\n  \"cls_4b_seed123\": [\n    {\"checkpoint\": \"ckpt-800\", \"step\": 800, \"test_acc\": 75.33, \"f1_macro\": 67.03}\n  ],\n  \"cwm_4b_s42\": [\n    {\"checkpoint\": \"final\", \"test_acc\": 58.04, \"f1_macro\": 51.67, \"unparseable_rate\": 53.7}\n  ],\n  \"cwm_4b_seed123\": [\n    {\"checkpoint\": \"final\", \"test_acc\": 59.09, \"f1_macro\": 43.43, \"unparseable_rate\": 67.2}\n  ],\n  \"cls_8b_s42_seq2048_ablation\": [\n    {\"checkpoint\": \"ckpt-1000\", \"step\": 1000, \"test_acc\": 82.83, \"f1_macro\": 76.88, \"note\": \"seq_length=2048 ablation\"}\n  ],\n  \"majority_baseline\": {\n    \"val\": 75.88,\n    \"test\": 72.96\n  }\n}\n"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-15T13:30:17.825048+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/multi_seed_test_curves.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-15T13:30:17.825189+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "relaxed_matching_results",
  "type": "data",
  "description": "CLS vs CWM accuracy comparison under strict/normalized/enhanced matching, with parse rates and upper bounds",
  "project": "exec-sim-repair-verifier",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/relaxed_matching_results.csv",
  "tags": "['paper-data', 'relaxed-matching', 'cls-vs-cwm']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "relaxed_matching_results",
    "type": "data",
    "description": "CLS vs CWM accuracy comparison under strict/normalized/enhanced matching, with parse rates and upper bounds",
    "project": "exec-sim-repair-verifier",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/relaxed_matching_results.csv",
    "tags": "['paper-data', 'relaxed-matching', 'cls-vs-cwm']"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-15T13:30:17.825549+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_1557c9\", \"name\": \"relaxed_matching_results\", \"type\": \"data\", \"description\": \"CLS vs CWM accuracy comparison under strict/normalized/enhanced matching, with parse rates and upper bounds\", \"path\": \"projects/exec-sim-repair-verifier/artifacts/_project/data/relaxed_matching_results.csv\", \"url\": null, \"project\": \"exec-sim-repair-verifier\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T13:29:59.450350+00:00\", \"tags\": [\"paper-data\", \"relaxed-matching\", \"cls-vs-cwm\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-15T13:30:17.825708+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "tost_multi_margin",
  "type": "data",
  "description": "TOST equivalence test results at margins ±1/2/3pp, clustered bootstrap with 10000 resamples, 4 CLS-CWM pairs",
  "project": "exec-sim-repair-verifier",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/tost_multi_margin.csv",
  "tags": "['paper-data', 'tost', 'equivalence-test', 'statistical']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "tost_multi_margin",
    "type": "data",
    "description": "TOST equivalence test results at margins ±1/2/3pp, clustered bootstrap with 10000 resamples, 4 CLS-CWM pairs",
    "project": "exec-sim-repair-verifier",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/tost_multi_margin.csv",
    "tags": "['paper-data', 'tost', 'equivalence-test', 'statistical']"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-15T13:30:17.825887+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_9242c9\", \"name\": \"tost_multi_margin\", \"type\": \"data\", \"description\": \"TOST equivalence test results at margins ±1/2/3pp, clustered bootstrap with 10000 resamples, 4 CLS-CWM pairs\", \"path\": \"projects/exec-sim-repair-verifier/artifacts/_project/data/tost_multi_margin.csv\", \"url\": null, \"project\": \"exec-sim-repair-verifier\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T13:30:02.260265+00:00\", \"tags\": [\"paper-data\", \"tost\", \"equivalence-test\", \"statistical\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-15T13:30:17.826066+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "mutation_type_accuracy",
  "type": "data",
  "description": "Per-mutation-type accuracy for CLS 8B (s42/s123 multiple checkpoints) and CWM 4B, with val/test distribution percentages",
  "project": "exec-sim-repair-verifier",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/mutation_type_accuracy.csv",
  "tags": "['paper-data', 'mutation-type', 'per-type-accuracy', 'distribution-shift']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "mutation_type_accuracy",
    "type": "data",
    "description": "Per-mutation-type accuracy for CLS 8B (s42/s123 multiple checkpoints) and CWM 4B, with val/test distribution percentages",
    "project": "exec-sim-repair-verifier",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/mutation_type_accuracy.csv",
    "tags": "['paper-data', 'mutation-type', 'per-type-accuracy', 'distribution-shift']"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-15T13:30:17.826241+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_e363ac\", \"name\": \"mutation_type_accuracy\", \"type\": \"data\", \"description\": \"Per-mutation-type accuracy for CLS 8B (s42/s123 multiple checkpoints) and CWM 4B, with val/test distribution percentages\", \"path\": \"projects/exec-sim-repair-verifier/artifacts/_project/data/mutation_type_accuracy.csv\", \"url\": null, \"project\": \"exec-sim-repair-verifier\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T13:30:05.098605+00:00\", \"tags\": [\"paper-data\", \"mutation-type\", \"per-type-accuracy\", \"distribution-shift\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-15T13:30:17.826818+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "multi_seed_test_curves",
  "type": "data",
  "description": "Multi-seed test/val curves for CLS 8B/4B (s42, seed123), CWM 4B baselines, seq2048 ablation, and majority baseline",
  "project": "exec-sim-repair-verifier",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/multi_seed_test_curves.json",
  "tags": "['paper-data', 'training-curves', 'multi-seed', 'test-accuracy']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "multi_seed_test_curves",
    "type": "data",
    "description": "Multi-seed test/val curves for CLS 8B/4B (s42, seed123), CWM 4B baselines, seq2048 ablation, and majority baseline",
    "project": "exec-sim-repair-verifier",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/multi_seed_test_curves.json",
    "tags": "['paper-data', 'training-curves', 'multi-seed', 'test-accuracy']"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-15T13:30:17.827093+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_693d9b\", \"name\": \"multi_seed_test_curves\", \"type\": \"data\", \"description\": \"Multi-seed test/val curves for CLS 8B/4B (s42, seed123), CWM 4B baselines, seq2048 ablation, and majority baseline\", \"path\": \"projects/exec-sim-repair-verifier/artifacts/_project/data/multi_seed_test_curves.json\", \"url\": null, \"project\": \"exec-sim-repair-verifier\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T13:30:07.496604+00:00\", \"tags\": [\"paper-data\", \"training-curves\", \"multi-seed\", \"test-accuracy\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_data-prep_paper-figure-data_20260515T132727",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 61 · 2026-05-15T13:30:17.827278+00:00_

4 个文件已生成并注册：

| 文件 | artifact ID | 内容 |
|------|-------------|------|
| `relaxed_matching_results.csv` | art_20260515_1557c9 | CLS vs CWM strict/normalized/enhanced matching 对比，含 parse rate 和 upper bound |
| `tost_multi_margin.csv` | art_20260515_9242c9 | TOST ±1/2/3pp 三档 margin，p=0.0104@±2pp 确认等价 |
| `mutation_type_accuracy.csv` | art_20260515_e363ac | 5 种 mutation type × 4 个 checkpoint 的 accuracy，含 val/test 分布比例 |
| `multi_seed_test_curves.json` | art_20260515_693d9b | 8B/4B × s42/seed123 完整 test/val curves + CWM baseline + seq2048 ablation + majority baseline |

数据来源：registry 的 125 个实验 metrics、memory.md 锁定数字、artifacts/ 已有分析报告（relaxed_matching_analysis.txt、tost_multi_margin_results.txt、mutation_type_analysis_w3w8_c1.md）交叉验证。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_data-prep_paper-figure-data_20260515T132727"
}
```

</details>

---
