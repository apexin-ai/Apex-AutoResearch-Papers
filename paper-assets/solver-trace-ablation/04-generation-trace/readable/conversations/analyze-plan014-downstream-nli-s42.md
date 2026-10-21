# analyze plan014 downstream nli s42

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 7
- **Recorded user turns:** 0
- **Tool calls:** 3
- **Original source:** `logs/chats/worker_analyze_plan014-downstream-nli-s42_20260514T042736.jsonl`
- **Structured JSON:** [`889e824ab64d952767dd.json`](../../sessions/88/889e824ab64d952767dd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

7 recorded events

### Tool call

_source line 1 · 2026-05-14T04:28:27.230829+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_plan014-downstream-nli-s42_20260514T042736",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T04:28:27.231142+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_plan014-downstream-nli-s42_20260514T042736",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T04:28:27.231316+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "tail -200 ~/runs/solver-trace-ablation/plan014-downstream-nli-s42.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_plan014-downstream-nli-s42_20260514T042736",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "tail -200 ~/runs/solver-trace-ablation/plan014-downstream-nli-s42.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-14T04:28:27.231446+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-39279",
  "command": "cat /root/autodl-tmp/outputs/plan014_downstream_nli.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_plan014-downstream-nli-s42_20260514T042736",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-39279",
    "command": "cat /root/autodl-tmp/outputs/plan014_downstream_nli.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-14T04:28:27.231645+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"The tokenizer you are loading from '/root/autodl-tmp/outputs/plan001_exec_only_s42' with an incorrect regex pattern: https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503/discussions/84#69121093e8b480e709447d5e. This will lead to incorrect tokenization. You should set the `fix_mistral_regex=True` flag when loading this tokenizer to fix this issue.\\n`torch_dtype` is deprecated! Use `dtype` instead!\\nLoaded 100 problems from data/proofwriter_fol_100.jsonl\\nLoading model from /root/autodl-tmp/outputs/plan001_exec_only_s42 ...\\n\\rLoading checkpoint shards:   0%|          | 0/4 [00:00<?, ?it/s]\\rLoading checkpoint shards:  25%|██▌       | 1/4 [00:00<00:02,  1.12it/s]\\rLoading checkpoint shards:  50%|█████     | 2/4 [00:01<00:01,  1.14it/s]\\rLoading checkpoint shards:  75%|███████▌  | 3/4 [00:02<00:00,  1.15it/s]\\rLoading checkpoint shards: 100%|██████████| 4/4 [00:02<00:00,  1.59it/s]\\rLoading checkpoint shards: 100%|█████��████| 4/4 [00:02<00:00,  1.39it/s]\\nModel loaded.\\n\\n=== Phase 1: Inference (K=8, T=0.7) ===\\n[1/100] folio_765 ... 8 generated\\n[2/100] folio_1179 ... 8 generated\\n[3/100] folio_66 ... 8 generated\\n[4/100] folio_1378 ... 8 generated\\n[5/100] folio_592 ... 8 generated\\n[6/100] folio_71 ... 8 generated\\n[7/100] folio_556 ... 8 generated\\n[8/100] folio_938 ... 8 generated\\n[9/100] folio_833 ... 8 generated\\n[10/100] folio_1312 ... 8 generated\\n[11/100] folio_1119 ... 8 generated\\n[12/100] folio_160 ... 8 generated\\n[13/100] folio_1202 ... 8 generated\\n[14/100] folio_192 ... 8 generated\\n[15/100] folio_207 ... 8 generated\\n[16/100] folio_304 ... 8 generated\\n[17/100] folio_402 ... 8 generated\\n[18/100] folio_999 ... 8 generated\\n[19/100] folio_204 ... 8 generated\\n[20/100] folio_452 ... 8 generated\\n[21/100] folio_669 ... 8 generated\\n[22/100] folio_393 ... 8 generated\\n[23/100] folio_1331 ... 8 generated\\n[24/100] folio_699 ... 8 generated\\n[25/1
…[truncated 4117 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_plan014-downstream-nli-s42_20260514T042736",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T04:28:27.232014+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"summary\\\": {\\n    \\\"n_samples\\\": 100,\\n    \\\"n_generations\\\": 800,\\n    \\\"overall_accuracy\\\": 0.3412,\\n    \\\"by_gold_label\\\": {\\n      \\\"false\\\": {\\n        \\\"correct\\\": 0,\\n        \\\"total\\\": 200,\\n        \\\"accuracy\\\": 0.0\\n      },\\n      \\\"unknown\\\": {\\n        \\\"correct\\\": 25,\\n        \\\"total\\\": 328,\\n        \\\"accuracy\\\": 0.0762\\n      },\\n      \\\"true\\\": {\\n        \\\"correct\\\": 248,\\n        \\\"total\\\": 272,\\n        \\\"accuracy\\\": 0.9118\\n      }\\n    },\\n    \\\"by_isr_bucket\\\": {\\n      \\\"high\\\": {\\n        \\\"n\\\": 12,\\n        \\\"correct\\\": 9,\\n        \\\"accuracy\\\": 0.75,\\n        \\\"mean_isr\\\": 0.9375\\n      },\\n      \\\"mid\\\": {\\n        \\\"n\\\": 69,\\n        \\\"correct\\\": 26,\\n        \\\"accuracy\\\": 0.3768,\\n        \\\"mean_isr\\\": 0.4812\\n      },\\n      \\\"low\\\": {\\n        \\\"n\\\": 651,\\n        \\\"correct\\\": 213,\\n        \\\"accuracy\\\": 0.3272,\\n        \\\"mean_isr\\\": 0.0777\\n      }\\n    },\\n    \\\"by_isr_quartile\\\": {\\n      \\\"Q1_lowest\\\": {\\n        \\\"n\\\": 183,\\n        \\\"correct\\\": 56,\\n        \\\"accuracy\\\": 0.306,\\n        \\\"isr_range\\\": [\\n          0.0,\\n          0.0\\n        ]\\n      },\\n      \\\"Q2\\\": {\\n        \\\"n\\\": 183,\\n        \\\"correct\\\": 79,\\n        \\\"accuracy\\\": 0.4317,\\n        \\\"isr_range\\\": [\\n          0.0,\\n          0.1111\\n        ]\\n      },\\n      \\\"Q3\\\": {\\n        \\\"n\\\": 183,\\n        \\\"correct\\\": 52,\\n        \\\"accuracy\\\": 0.2842,\\n        \\\"isr_range\\\": [\\n          0.1111,\\n          0.1667\\n        ]\\n      },\\n      \\\"Q4_highest\\\": {\\n        \\\"n\\\": 183,\\n        \\\"correct\\\": 61,\\n        \\\"accuracy\\\": 0.3333,\\n        \\\"isr_range\\\": [\\n          0.1667,\\n          1.0\\n        ]\\n  
…[truncated 7990 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_plan014-downstream-nli-s42_20260514T042736",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-14T04:28:27.232259+00:00_

实验成功完成（EXIT_CODE=0）。以下是完整结果：

## plan014 Downstream NLI 结果

### 配置
- Checkpoint: plan001_exec_only_s42
- 100 samples, K=8 generations, T=0.7
- Solver: prover9
- 推理耗时 408.8s，评估 13.6s

### 核心指标

| 指标 | 值 |
|------|-----|
| Overall accuracy | **34.1%** |
| Proved rate | 732/800 (91.5%) |
| Parse errors | 0 |

### 按 gold label 分解 — 严重 true bias

| Gold Label | Accuracy | 分布 |
|------------|----------|------|
| true | **91.2%** (248/272) | 34% of data |
| unknown | 7.6% (25/328) | 41% of data |
| false | **0.0%** (0/200) | 25% of data |

模型几乎总是预测 "true"（entailment），完全无法预测 "false"。

### ISR 与 NLI 准确率的关系

**ISR bucket:**

| Bucket | μ(ISR) | Accuracy | n |
|--------|--------|----------|---|
| high | 0.94 | 75.0% | 12 |
| mid | 0.48 | 37.7% | 69 |
| low | 0.08 | 32.7% | 651 |

Bucket 层面有单调趋势，但 high bucket 仅 12 个样本。

**ISR quartile（等分）:**

| Quartile | Range | Accuracy | n |
|----------|-------|----------|---|
| Q1 | [0.00, 0.00] | 30.6% | 183 |
| Q2 | [0.00, 0.11] | **43.2%** | 183 |
| Q3 | [0.11, 0.17] | 28.4% | 183 |
| Q4 | [0.17, 1.00] | 33.3% | 183 |

Quartile 层面**非单调**（Q2 最高，Q3 最低），无清晰趋势。

### Best-of-N 选择

| 策略 | Accuracy |
|------|----------|
| oracle | 44.0% |
| isr_best | 35.0% |
| prove_first | 35.0% |
| random | 34.1% |

ISR-best 仅比 random 高 +0.9 pp，与 prove_first 持平。

### 统计检验 — 全部不显著

| Test | Statistic | p-value |
|------|-----------|---------|
| Spearman ρ(ISR, correct) | **-0.049** | 0.187 |
| Mann-Whitney Q4>Q1 | U=17202 | 0.288 |
| Bootstrap BoN (ISR vs random) | diff=0.009 | 95% CI [-0.015, +0.037] |

### 结论

**ISR 作为 downstream NLI quality proxy 的结果是阴性的。** Spearman ρ 接近零且不显著，Best-of-N ISR 选择无实质提升，quartile 分析非单调。主要原因：模型存在严重的 "true" prediction bias（false accuracy = 0%），NLI 任务本身的 accuracy 天花板很低（overall 34.1%），ISR 的区分度在此基础上没有空间发挥。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analyze_plan014-downstream-nli-s42_20260514T042736"
}
```

</details>

---
