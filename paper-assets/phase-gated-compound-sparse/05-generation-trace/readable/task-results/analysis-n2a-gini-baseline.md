# analysis n2a gini baseline

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_n2a_gini_baseline_20260515T113851_result.json`
- **Structured JSON:** [`ad2b86047c1a2582ba23.json`](../../sessions/ad/ad2b86047c1a2582ba23.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据提取完成。以下是完整结果：

---

## Baseline Gini & 相对变化汇总

**数据源**: `c4_attention_entropy` 实验，n=30 C4 text problems/model，seed=42

### Baseline Gini（Dense，无 pruning）

| Model | mean ± std | median | min | max | 95% range |
|-------|-----------|--------|-----|-----|-----------|
| DS (DeepSeek-R1-Distill-Qwen-7B) | **0.4959 ± 0.0305** | 0.4867 | 0.4536 | 0.5840 | [0.4569, 0.5653] |
| QW (Qwen2.5-7B-Instruct) | **0.5708 ± 0.0267** | 0.5672 | 0.5285 | 0.6636 | [0.5344, 0.6490] |

> Reviewer 预估 DS ~0.52，实测 0.496，偏低约 5%。QW baseline 更高，head importance 更集中。

### Importance Masking — ΔGini & 相对变化

| Model | Sparsity | ΔGini median [95% CI] | Relative Change (median) |
|-------|----------|----------------------|--------------------------|
| DS | s015 | **-0.0290** [-0.0386, -0.0222] | **-6.0%** |
| DS | s020 | **-0.0402** [-0.0495, -0.0311] | **-8.1%** |
| DS | s025 | **-0.0646** [-0.0732, -0.0531] | **-13.5%** |
| DS | s030 | **-0.0817** [-0.0904, -0.0589] | **-17.0%** |
| QW | s015 | **-0.0108** [-0.0184, +0.0054] | **-1.9%** |
| QW | s020 | **-0.0137** [-0.0231, +0.0082] | **-2.5%** |
| QW | s025 | **-0.0101** [-0.0307, +0.0057] | **-1.8%** |
| QW | s030 | **-0.0201** [-0.0418, -0.0008] | **-3.5%** |

### Random Masking — ΔGini & 相对变化（对比用）

| Model | Sparsity | ΔGini median [95% CI] | Relative Change (median) |
|-------|----------|----------------------|--------------------------|
| DS | s015 | -0.0309 [-0.0454, -0.0143] | -6.4% |
| DS | s020 | -0.0418 [-0.0593, -0.0255] | -8.1% |
| DS | s025 | -0.0597 [-0.0915, -0.0386] | -12.4% |
| DS | s030 | -0.0707 [-0.1090, -0.0507] | -14.5% |
| QW | s015 | -0.0195 [-0.0292, -0.0052] | -3.3% |
| QW | s020 | -0.0229 [-0.0383, -0.0092] | -4.0% |
| QW | s025 | -0.0362 [-0.0584, +0.0283] | -6.6% |
| QW | s030 | -0.0460 [-0.0616, -0.0107] | -8.1% |

### Summary 中预计算的 gini_delta_mean（交叉验证）

| Model | Condition | gini_delta_mean (summary) |
|-------|-----------|--------------------------|
| DS | s015 imp | -0.0301 |
| DS | s020 imp | -0.0404 |
| DS | s025 imp | -0.0647 |
| DS | s030 imp | -0.0806 |
| QW | s015 imp | -0.0105 |
| QW | s020 imp | -0.0121 |
| QW | s025 imp | -0.0100 |
| QW | s030 imp | -0.0202 |

与 per-problem 计算结果一致。

### 关键观察

- **DS 对 pruning 更敏感**：importance masking 下 Gini 降幅达 -6% ~ -17%，而 QW 仅 -1.8% ~ -3.5%
- **QW s015/s020/s025 的 CI 跨零**，说明这些 sparsity 下 Gini 变化不显著；仅 s030 的 CI 完全为负
- DS 的 importance masking 与 random masking ΔGini 幅度接近（s015: -0.029 vs -0.031），说明被 mask 掉的 head 并非最集中的那些——pruning 的"均匀化"效应主要来自减少 head 数量本身

---
