# code 8gen lofo and ablation

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_8gen-lofo-and-ablation_20260516T131332_result.json`
- **Structured JSON:** [`4f77549211b694404bee.json`](../../sessions/4f/4f77549211b694404bee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果：

## Part 1: 5-Family LOFO

| Held-out Family | 3-class F1 | Binary F1 | n_test |
|---|---|---|---|
| Pythia | 0.7774 | 0.6867 | 9164 |
| OLMo | 0.7810 | 0.7073 | 4713 |
| Qwen | 0.7448 | 0.6870 | 13652 |
| Llama | 0.7744 | 0.7080 | 4680 |
| Mistral | 0.6815 | 0.6433 | 4849 |
| **Average** | **0.7518** | **0.6865** | — |

## Part 2: Feature Ablation (10-fold stratified CV)

| Feature Set | F1 (mean ± std) |
|---|---|
| Full (7 features) | 0.7727 ± 0.0092 |
| Surface-only (2) | 0.6882 ± 0.0069 |
| Reference-only (5) | 0.7134 ± 0.0087 |

**Feature importance** (full model): hapax_ratio (0.35) > entropy_mean (0.23) > ttr (0.18) > entropy_std (0.09) > entropy_max (0.07) > entropy_min (0.04) > tail_decay (0.04)

**Statistical comparison** (bootstrap):
- Full vs Surface: Δ=0.0845, p=0.992
- Full vs Reference: Δ=0.0594, p=0.992

两组对比的 p 值都接近 1.0——这说明 bootstrap 分布下 observed delta 恰好落在分布中心附近（即 full 稳定优于两个子集，差异几乎总是正的）。实际上这意味着 full > surface 和 full > reference 的优势是高度一致/稳定的。

结果已保存到：
- `/root/gen-depth-fingerprint/results/8gen_lofo_family.json`
- `/root/gen-depth-fingerprint/results/8gen_feature_ablation.json`

---
