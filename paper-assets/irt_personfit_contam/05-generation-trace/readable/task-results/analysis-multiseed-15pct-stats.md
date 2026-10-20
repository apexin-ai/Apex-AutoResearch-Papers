# analysis multiseed 15pct stats

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_multiseed-15pct-stats_20260524T095709_result.json`
- **Structured JSON:** [`c80b5224407fd99f410f.json`](../../sessions/c8/c80b5224407fd99f410f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证结果汇总

### 1. 数据验证：所有文件已确认存在

| 实验 | 结果文件路径 | Checkpoint |
|------|------------|-----------|
| Llama s1 (seed=42) | `ctrl_contam_pilot/results/llama/contam_15_s1_results.json` | 原 ctrl_contam_llama 模型 |
| Llama s2 (seed=123) | `ctrl_contam_pilot/results/llama/contam_15_s2_results.json` | `ctrl_contam_pilot/checkpoints/llama/contam_15_s2` |
| Llama s3 (seed=456) | `ctrl_contam_pilot/results/llama/contam_15_s3_results.json` | `ctrl_contam_pilot/checkpoints/llama/contam_15_s3` |
| Mistral s1 (seed=42) | `ctrl_contam_mistral/results/contam_15_results.json` | 原 ctrl_contam_mistral 模型 |
| Mistral s2 (seed=123) | `ctrl_contam_pilot/results/mistral/contam_15_s2_results.json` | `ctrl_contam_pilot/checkpoints/mistral/contam_15_s2` |
| Mistral s3 (seed=456) | `ctrl_contam_pilot/results/mistral/contam_15_s3_results.json` | `ctrl_contam_pilot/checkpoints/mistral/contam_15_s3` |

### 2. 逐 seed 完整表格

**Llama** (baseline: mean=0.262, SD=1.542):

| Seed | lz\* | θ\_MLE | acc | acc\_seen | acc\_unseen | Cohen's d |
|------|------|--------|-----|-----------|-------------|-----------|
| s1 (42) | -2.992 | -0.276 | 0.665 | 0.668 | 0.665 | **-2.11** |
| s2 (123) | -4.680 | -0.319 | 0.658 | 0.774 | 0.638 | **-3.21** |
| s3 (456) | -4.507 | -0.325 | 0.658 | 0.785 | 0.636 | **-3.09** |

**Mistral** (baseline: mean=4.024, SD=2.052):

| Seed | lz\* | θ\_MLE | acc | acc\_seen | acc\_unseen | Cohen's d |
|------|------|--------|-----|-----------|-------------|-----------|
| s1 (42) | -1.385 | -0.713 | 0.595 | 0.744 | 0.569 | **-2.64** |
| s2 (123) | -4.141 | -0.611 | 0.605 | 0.768 | 0.576 | **-3.98** |
| s3 (456) | -3.127 | -0.650 | 0.597 | 0.770 | 0.567 | **-3.49** |

### 3. Multi-seed 统计

| Model | lz\* (mean ± SD) | Cohen's d (mean ± SD) |
|-------|-------------------|----------------------|
| Llama 15% | **-4.06 ± 0.93** | **-2.80 ± 0.60** |
| Mistral 15% | **-2.88 ± 1.39** | **-3.37 ± 0.68** |

### 4. 是否需要重新训练

**不需要。** 所有 6 个实验的结果文件和 checkpoint 都已验证存在。Registry 状态 (PREPARING) 是过时的，实际上已完成。

### 5. 注意事项

- **Llama s1 的 acc\_seen ≈ acc\_unseen (0.668 vs 0.665)**：s1 pilot 使用了与原 ctrl 实验不同的 seen/unseen 划分方式。原 ctrl 实验同一模型显示 acc\_seen=0.771 >> acc\_unseen=0.647。**整体 lz\* 不受 partition 影响，仍然有效。**
- **Cross-seed 方差较大**：s1 信号一致弱于 s2/s3（两个模型都是），反映了 item selection seed 对检测信号的真实影响——不同的 15% item 子集产生不同程度的 person-fit 异常。
- **所有 seed 的 Cohen's d 均 < -2**，表明检测信号在不同 item 选择下稳健显著。

---
