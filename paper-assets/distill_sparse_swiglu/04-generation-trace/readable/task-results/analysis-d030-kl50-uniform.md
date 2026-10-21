# analysis d030 kl50 uniform

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d030_kl50_uniform_20260516T050416_result.json`
- **Structured JSON:** [`00301160ee557497f780.json`](../../sessions/00/00301160ee557497f780.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据到手。Per-layer sparsity 确认全部 32 层均为 0.500，model-level 0.500。

## d030_kl50_uniform 结果

### 核心指标

| Metric | WikiText-2 PPL | ARC-c (acc_norm) | WinoGrande (acc) | MMLU (acc) | GSM8K (exact_match) |
|--------|:-:|:-:|:-:|:-:|:-:|
| **KL 50% Uniform** | **11.96** | **0.3276** | **0.6290** | **0.2777** | **0.0212** |

Per-layer sparsity: 全部 32 层 = 0.500, model-level = 0.500 ✓

### 全方法对比

| Method | ARC-c | WG | MMLU | GSM8K |
|--------|:-----:|:--:|:----:|:-----:|
| Dense | 0.5819 | 0.7814 | 0.6532 | 0.5004 |
| KL 30% Uniform | 0.4078 | 0.6859 | **0.4061** | 0.0735 |
| **KL 50% Uniform** | **0.3276** | **0.6290** | **0.2777** | **0.0212** |
| KL 50% Global top-k | 0.3771 | 0.6156 | 0.2591 | 0.0121 |
| TEAL 50% | 0.2910 | 0.5556 | 0.2856 | 0.0190 |

### 50% Uniform vs Baselines (delta)

| vs. | ARC-c | WG | MMLU | GSM8K |
|-----|:-----:|:--:|:----:|:-----:|
| vs Dense | -0.2543 | -0.1524 | -0.3755 | -0.4792 |
| vs KL 50% Global | -0.0495 | +0.0134 | +0.0186 | +0.0091 |
| vs TEAL 50% | +0.0366 | +0.0734 | -0.0079 | +0.0022 |
| vs KL 30% Uniform | -0.0802 | -0.0569 | -0.1284 | -0.0523 |

### 结论

**50% uniform 未能修复 MMLU。** MMLU = 27.77%，接近随机水平（25%），与 KL 50% global top-k 的 25.91% 几乎无差异（仅 +1.86pp）。对比之下，30% uniform 曾将 MMLU 从 28.74% 拉到 40.61%（+12pp）。**Uniform allocation 的 MMLU 修复效应在 50% sparsity 下完全消失。**

**GSM8K 仍然接近 0**（2.12%），与 50% global（1.21%）和 TEAL 50%（1.90%）同级别。

**50% 是断崖点（Narrative B）：** 在 50% sparsity 下，uniform allocation 无法提供 30% 时观察到的知识保留优势。ARC-c 和 WG 相比 50% global 也基本持平（WG 略好 +1.3pp），uniform 的分配优势已不显著。唯一亮点是相比 TEAL 50%，WG 还有 +7.3pp 的优势，说明 KL predictor 本身在 50% 下仍优于 TEAL，但 uniform vs global 的差距在此 sparsity 下基本消失。

---
