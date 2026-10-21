# read exposure scores structure

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_read_exposure_scores_structure_20260516T152304_result.json`
- **Structured JSON:** [`dcb3fa7c65fd209c826a.json`](../../sessions/dc/dcb3fa7c65fd209c826a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results:

## 1. exposure_scores.json 结构

**路径**: `/root/autodl-tmp/exp003/rrf_full_n_latest/exposure_scores.json`

**结构**: `{model_name: {benchmark: {exposure_scores: [float, ...]}}}`

**Per-benchmark respondent count:**

| Benchmark | N (respondents) |
|-----------|----------------|
| mmlu | 25 |
| gsm8k | 24 |
| arc_challenge | 24 |

Qwen2.5-0.5B-Instruct 只有 mmlu（缺 gsm8k、arc_challenge）。

## 2. 完整 model 列表（exposure_scores.json 中 25 个）

**0.5B (9):** Instruct, d000_s123, d000_s42, d005_s123, d005_s42, d025_s123, d025_s42, d100_s123, d100_s42  
**1.5B (8):** d000_s123, d000_s42, d005_s123, d005_s42, d025_s123, d025_s42, d100_s123, d100_s42  
**3B (8):** d000_a32_s42, d000_s123_a32, d005_a32_s42, d005_s123, d025_s123, d025_v3_s42, d100_a32_s123, d100_a32_s42

## 3. Signals 目录覆盖情况

所有有效（非 deprecated）model dirs 都有 mmlu/gsm8k/arc_challenge 三套 signals_merged，**除了**：

| Model dir | 有的 signals | 缺的 |
|-----------|-------------|------|
| Qwen2.5-0.5B-Instruct | (空) | mmlu, gsm8k, arc |
| Qwen2.5-3B_d000_s123_a32 | arc, gsm8k | mmlu |
| Qwen2.5-3B_d025_s42 | mmlu | gsm8k, arc |

Deprecated/不在 exposure 中的 dirs：`3B_d000_v2_s42`, `3B_d005_s42`, `3B_d025_s42_DEPRECATED_alpha16`, `3B_d100_s42`（均为 alpha=16 废弃）

## 4. N 偏低的原因

N 已经很高了（24-25）。唯一缺口是 Qwen2.5-0.5B-Instruct 缺 gsm8k/arc signals（导致这两个 benchmark N=24 而非 25）。Instruct 模型可能未跑过这两个 benchmark 的信号计算。

注意：Qwen2.5-3B_d000_s123_a32 在 signals 目录中缺 mmlu merged file，但 exposure_scores.json 中已包含其 mmlu 数据——说明 exposure 计算时 mmlu signal 存在，之后文件可能被移动/删除。

---
