# analysis run statistical tests

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/chats/worker_analysis_run_statistical_tests_20260527T194600.jsonl`
- **Structured JSON:** [`f20e4fee500458f3a2d0.json`](../../sessions/f2/f20e4fee500458f3a2d0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

11 recorded events

### Tool call

_source line 1 · 2026-05-27T19:46:42.919725+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_run_statistical_tests_20260527T194600",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-27T19:46:42.920088+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_run_statistical_tests_20260527T194600",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-27T19:46:42.920277+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34685",
  "command": "ls -la /root/occsafe_vla/analysis/statistical_tests.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_run_statistical_tests_20260527T194600",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34685",
    "command": "ls -la /root/occsafe_vla/analysis/statistical_tests.py",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-27T19:46:42.920414+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34685",
  "command": "cat /root/occsafe_vla/analysis/statistical_tests.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_run_statistical_tests_20260527T194600",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34685",
    "command": "cat /root/occsafe_vla/analysis/statistical_tests.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-27T19:46:42.920549+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 13405 May 28 03:13 /root/occsafe_vla/analysis/statistical_tests.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.07}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_run_statistical_tests_20260527T194600",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-27T19:46:42.920852+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"\\nStatistical analysis for BN x gradient flow 2x2 factorial study.\\nP0: Bootstrap + Permutation tests\\nP1: Effect sizes (Cohen's d, Hedges' g, Glass's delta)\\nP2: Per-task analysis\\n\\nALL DATA: Pure v2, 50K checkpoint, 50 rollouts only.\\n\\\"\\\"\\\"\\nimport numpy as np\\nfrom itertools import combinations\\n\\n# ============ DATA (pure v2 50K 50r) ============\\n# Cell 1: Full OCC BN (Grad ON + BN)\\n# full_occ_retrain_s0=0.746, full_occ_bn_v2_s1=0.654, mvp_occ_s3_v2=0.776\\ncell1_full_occ_bn = [0.746, 0.654, 0.776]  # n=3\\n\\n# Cell 2: Full OCC LN (Grad ON + LN)\\n# full_occ_ln_s3_v2=0.740, full_occ_ln_v2_s1c=0.792, full_occ_ln_v2_s2=0.798\\ncell2_full_occ_ln = [0.740, 0.792, 0.798]  # n=3\\n\\n# Cell 3: Detach BN (Grad OFF + BN)\\n# detach_bn_v2_s0=0.774, detach_bn_v2_s1=0.736, detach_bn_v2_s2=0.762, ablation_occ_detach_s3_v2=0.794\\ncell3_detach_bn = [0.774, 0.736, 0.762, 0.794]  # n=4\\n\\n# Cell 4: Detach LN (Grad OFF + LN)\\n# detach_ln_v2_s1=0.826\\ncell4_detach_ln = [0.826]  # n=1\\n\\n# Vanilla baseline\\n# vanilla_retrain_s0=0.768, vanilla_v2_s1=0.748, vanilla_v2_s2=0.720\\nvanilla = [0.768, 0.748, 0.720]  # n=3\\n\\n# Per-task CAR data {task: {condition: [values]}}\\n# Cell 1 (n=3): full_occ_retrain_s0, full_occ_bn_v2_s1, mvp_occ_s3_v2\\n# Cell 2 (n=3): full_occ_ln_s3_v2, full_occ_ln_v2_s1c, full_occ_ln_v2_s2\\n# Cell 3 (n=4): detach_bn_v2_s0, detach_bn_v2_s1, detach_bn_v2_s2, ablation_occ_detach_s3_v2\\n# Cell 4 (n=1): detach_ln_v2_s1\\n# Vanilla (n=3): vanilla_retrain_s0, vanilla_v2_s1, vanilla_v2_s2\\nTASKS = ['T0', 'T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9']\\n\\nper_task_data = {\\n    'T0': {\\n        'cell1': [0.98, 0.96, 0.98],\\n        'cell2': [0.98, 0.98, 0.98],\\n        'cell3': [0.98, 0.98, 0.98, 0.98],\\n        'cell4': [0.98],\\n        'vanilla': [0.98, 0.98, 0.98],\\n    },\\n    'T1': {\\n        'cell1': [1.00, 0.98, 0.94
…[truncated 6945 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_run_statistical_tests_20260527T194600",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-27T19:46:42.921107+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-34685",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/analysis && python statistical_tests.py 2>&1",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_run_statistical_tests_20260527T194600",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-34685",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/analysis && python statistical_tests.py 2>&1",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-27T19:46:42.921324+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"======================================================================\\nBN x GRADIENT FLOW 2x2 FACTORIAL STUDY — STATISTICAL ANALYSIS\\nDATA: Pure v2, 50K checkpoint, 50 rollouts\\n======================================================================\\n\\n--- Cell Means (Bootstrap 95% CI) ---\\n  Cell 1 Full OCC BN  (Grad ON  + BN): mean=0.7253 [0.6540, 0.7760] (n=3)\\n  Cell 2 Full OCC LN  (Grad ON  + LN): mean=0.7767 [0.7400, 0.7980] (n=3)\\n  Cell 3 Detach BN    (Grad OFF + BN): mean=0.7665 [0.7455, 0.7860] (n=4)\\n  Cell 4 Detach LN    (Grad OFF + LN): mean=0.8260 (n=1, no CI)\\n  Vanilla baseline: mean=0.7453 [0.7200, 0.7680] (n=3)\\n\\n--- P0: Permutation Tests ---\\n  Gradient flow main effect: Delta=-0.0274, p=0.3961 n.s.\\n    Grad ON mean=0.7510, Grad OFF mean=0.7784\\n  Norm type main effect: Delta=-0.0401, p=0.1758 n.s.\\n\\n  Pairwise comparisons:\\n    Cell1 vs Cell2 (BN vs LN, Full): Delta=-0.0513, p=0.3000 n.s.\\n    Cell1 vs Cell3 (Full vs Detach, BN): Delta=-0.0412, p=0.2857 n.s.\\n    Cell1 vs Vanilla: Delta=-0.0200, p=0.8000 n.s.\\n    Cell2 vs Vanilla: Delta=+0.0313, p=0.3000 n.s.\\n    Cell3 vs Vanilla: Delta=+0.0212, p=0.3143 n.s.\\n    All OCC vs Vanilla: Delta=+0.0181, p=0.5110 n.s.\\n\\n--- P1: Effect Sizes ---\\n  Cell1 vs Cell3 (Full vs Detach, BN):\\n    Cohen's d=-0.928 (large), Hedges' g=-0.781, Glass's Delta=-1.707\\n    Bootstrap Delta: -0.0412 [-0.1095, +0.0140]\\n  Cell1 vs Vanilla:\\n    Cohen's d=-0.416 (small), Hedges' g=-0.333, Glass's Delta=-0.830\\n    Bootstrap Delta: -0.0204 [-0.0847, +0.0367]\\n  Cell3 vs Vanilla:\\n    Cohen's d=+0.875 (large), Hedges' g=+0.737, Glass's Delta=+0.878\\n    Bootstrap Delta: +0.0210 [-0.0093, +0.0503]\\n  Cell2 vs Vanilla:\\n    Cohen's d=+1.108 (large), Hedges' g=+0.887, Glass's Delta=+1.300\\n    Bootstrap Delta: +0.0314 [-0.0053, +0.0667]\\n  Grad ON vs Grad OFF (main effect):\\n    Cohen's d=-0.602 (medium), Hedges' g=-0.550, Glas
…[truncated 3157 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_run_statistical_tests_20260527T194600",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-27T19:46:42.921511+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34685",
  "command": "ls -la /root/occsafe_vla/analysis/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_run_statistical_tests_20260527T194600",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34685",
    "command": "ls -la /root/occsafe_vla/analysis/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-27T19:46:42.921654+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 188\\ndrwxr-xr-x  4 root root  4096 May 28 02:58 .\\ndrwxr-xr-x 17 root root  4096 May 26 03:42 ..\\n-rw-r--r--  1 root root 11178 May 23 18:22 bootstrap_ci.py\\n-rw-r--r--  1 root root  1657 May 23 14:18 bootstrap_config.json\\n-rw-r--r--  1 root root  8902 May 23 14:18 bootstrap_results.json\\n-rw-r--r--  1 root root  9747 May 24 07:54 cka_analysis.py\\n-rw-r--r--  1 root root  4212 May 23 11:54 cka_compare.py\\ndrwxr-xr-x  2 root root  4096 May 23 14:17 eval_data_from_10894\\n-rw-r--r--  1 root root  8140 May 23 14:12 eval_data_manifest.json\\n-rw-r--r--  1 root root 10126 May 27 20:20 factorial_anova.py\\n-rw-r--r--  1 root root  1140 May 27 20:20 factorial_data.json\\n-rw-r--r--  1 root root  7402 May 25 14:22 grad_debug_test.py\\n-rw-r--r--  1 root root 16673 May 24 20:59 gradient_analysis.py\\n-rw-r--r--  1 root root 18777 May 25 14:13 gradient_dose_response.py\\n-rw-r--r--  1 root root 12349 May 23 18:22 plot_gradient_figure.py\\n-rw-r--r--  1 root root  5939 May 24 02:38 plot_gradient_paper.py\\ndrwxr-xr-x  5 root root  4096 May 24 02:04 results\\n-rwxr-xr-x  1 root root 11388 May 24 02:11 run_full_analysis.sh\\n-rw-r--r--  1 root root 13405 May 28 03:13 statistical_tests.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_run_statistical_tests_20260527T194600",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-27T19:46:42.921859+00:00_

脚本仅输出到 stdout，未生成新文件。`factorial_data.json` 是之前已存在的（May 27 20:20）。

数值验证结果：

```
脚本执行: 成功（return_code=0）
输出文件: 无新文件生成（仅 stdout 输出）
数值验证: 全部一致
```

逐项对比：

| 指标 | 预期值 | 脚本输出 | 匹配 |
|------|--------|----------|------|
| Cell 1 Full OCC BN mean | ~0.725 | 0.7253 | ✓ |
| Cell 1 数据 | [0.746, 0.654, 0.776] n=3 | 同上 | ✓ |
| Cell 2 Full OCC LN mean | ~0.777 | 0.7767 | ✓ |
| Cell 2 数据 | [0.740, 0.792, 0.798] n=3 | 同上 | ✓ |
| Cell 3 Detach BN mean | ~0.767 | 0.7665 | ✓ |
| Cell 3 数据 | [0.774, 0.736, 0.762, 0.794] n=4 | 同上 | ✓ |
| Cell 4 Detach LN mean | 0.826 | 0.8260 | ✓ |
| Cell 4 数据 | [0.826] n=1 | 同上 | ✓ |
| Vanilla mean | ~0.745 | 0.7453 | ✓ |
| Vanilla 数据 | [0.768, 0.748, 0.720] n=3 | 同上 | ✓ |
| Gradient flow main effect Δ | ≈-0.027 | -0.0274 | ✓ |
| Gradient flow p | ≈0.396 | 0.3961 | ✓ |
| Gradient flow Cohen's d | ≈-0.60 | -0.602 | ✓ |
| Cell 1 vs Cell 3 Cohen's d | ≈-0.93 | -0.928 | ✓ |

所有数值与预期完全一致，无差异。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_run_statistical_tests_20260527T194600"
}
```

</details>

---
