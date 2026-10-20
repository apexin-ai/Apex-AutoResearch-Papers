# bugfix e theta v3 seed bug

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_bugfix_e_theta_v3_seed_bug_20260520T171624_result.json`
- **Structured JSON:** [`a706ba9116c6da273334.json`](../../sessions/a7/a706ba9116c6da273334.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### Root Cause

`scierc_qwen_s123` 在 V1/V3/V4 脚本中指向 `results/exp_freeform_ablation_seed123/samples.jsonl`，但该文件的 samples 数据与 `results/exp_freeform_ablation/samples.jsonl`（seed 42）完全相同——logprobs 数组逐值一致。文件大小略有差异仅因 greedy 输出不同，但 samples（用于分析的核心数据）是 seed 42 的副本。

### 修复

三个脚本（`e_theta_v1.py`、`e_theta_v3_no_dataset.py`、`e_theta_v4_no_model.py`）的 `scierc_qwen_s123` 路径从：
- `results/exp_freeform_ablation_seed123/samples.jsonl` （重复的 seed 42 数据）

改为：
- `output/exp_018_qwen_scierc_seed123/samples.jsonl` （真正的 seed 123 数据，551 instances，ID 完全匹配）

### 修复后的 scierc_qwen 结果变化

| Config | 指标 | 修复前 | 修复后 |
|--------|------|--------|--------|
| scierc_qwen_s42 | oracle_f1 | 0.7025 | 0.7025 (不变) |
| scierc_qwen_s123 | oracle_f1 | 0.7025 (= s42!) | 0.7028 (不同了) |
| scierc_qwen_s123 | adaptive_f1 | 0.6516 (= s42!) | 0.6481 |
| scierc_qwen_s123 | fixed_f1 | 0.6533 (= s42!) | 0.6456 |

Overall 指标变化极小（adaptive_f1: 0.793164 → 0.793123），核心结论不变。

### V1/V4 影响

V1 和 V4 有完全相同的 bug，已同步修复和重跑。三个版本的结果 JSON 均已更新到本地 `artifacts/experiments/e_theta/` 和 `artifacts/e_theta/data/`。

### V2 无此 bug

V2 使用独立路径系列（`exp_001_*`），三个 SciERC seed 的 logprobs 均不同。

---
