# analysis collect qw results and ds progress

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_collect_qw_results_and_ds_progress_20260515T210339_result.json`
- **Structured JSON:** [`3df13c76ed2fb393f1fd.json`](../../sessions/3d/3df13c76ed2fb393f1fd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Summary

### 1. QW Accuracy Eval 结果

| 指标 | dense | s015 | **s020** | **s025** | s030 |
|------|-------|------|----------|----------|------|
| accuracy | 32% | 32% | **24%** | **26%** | 14% |
| null_rate | — | — | **4%** (2) | **16%** (8) | — |
| trunc_rate | — | — | **4%** (2) | **4%** (2) | — |
| wrong_rate | — | — | **72%** (36) | **58%** (29) | — |
| Δ vs dense | — | 0 | **-8pp** | **-6pp** | -18pp |

s025 null_rate 高达 16%（8/50），其中仅 2 个是 max_token 截断，其余 6 个是答案解析失败。

### 2. DS 进度

| 实验 | PID | 进度 | running acc | elapsed | 速率 | ETA |
|------|-----|------|-------------|---------|------|-----|
| acc_ds_s020 | 273846 | **29/50** | 7/29 (24%) | 14:43 | ~30s/问题 | **~10 min** |
| acc_ds_s025 | 274546 | **26/50** | 3/26 (12%) | 14:02 | ~32s/问题 | **~13 min** |

两个进程均在运行，状态正常。

### 3. 单调性检查

期望：s015 ≥ s020 ≥ s025 ≥ s030

实际：32% ≥ 24% ≥ **26%** ≥ 14%

**s020→s025 反转 (+2pp)**：s025 (26%) 反而高于 s020 (24%)。差异仅 1 题 (12 vs 13 correct)，在 n=50 下不显著（二项 CI 约 ±12pp）。但 s025 null_rate 达 16%，远高于 s020 的 4%——s025 有更多题目彻底放弃作答，反而在"愿意作答"的题目上正确率更高。整体趋势 dense→s030 仍为单调下降，中间两点的反转属采样噪声。

Registry 已更新完毕（补充了 null_rate / wrong_rate 指标）。两个 QW 实验此前已被 hook 自动完成，conclusion=negative。

---
