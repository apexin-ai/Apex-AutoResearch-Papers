# exp multi seed probing

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_multi-seed-probing_20260524T170240_result.json`
- **Structured JSON:** [`0a009f28e55b6ebdb821.json`](../../sessions/0a/0a009f28e55b6ebdb821.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

确认无 ZH activations。以下是完整结果汇总：

---

**Multi-Seed Probing Results (3 seeds × 3 models, stratified resplit per seed)**

### Llama-3.1-8B (EN→EN, 32 layers)

| Seed | Peak Layer | Balanced Acc | F1 |
|------|-----------|-------------|-----|
| 42 | 15 | 92.75% | 92.91% |
| 123 | 12 | 92.75% | 92.91% |
| 456 | 15 | 92.50% | 92.57% |

**Mean: 92.67% ± 0.12%** | Peak layers: [15, 12, 15]

### Gemma-2-9B (EN→EN, 42 layers)

| Seed | Peak Layer | Balanced Acc | F1 |
|------|-----------|-------------|-----|
| 42 | 20 | 88.01% | 87.91% |
| 123 | 12 | 89.77% | 89.74% |
| 456 | 21 | 86.55% | 86.31% |

**Mean: 88.11% ± 1.32%** | Peak layers: [20, 12, 21]

### Qwen3-8B (EN→EN, 36 layers)

| Seed | Peak Layer | Balanced Acc | F1 |
|------|-----------|-------------|-----|
| 42 | 17 | 69.85% | 70.85% |
| 123 | 18 | 74.05% | 72.80% |
| 456 | 24 | 70.23% | 70.23% |

**Mean: 71.38% ± 1.90%** | Peak layers: [17, 18, 24]

### Asymmetry

无 `zh_activations.pt`，三个模型均无法计算跨语言 asymmetry。如需此分析，需先用 `collect_activations.py` 收集 ZH activations。

### Robustness 评估

- **Llama**: 非常稳定（std=0.12%），peak layer 略有变动（12 vs 15）但 accuracy 基本一致
- **Gemma**: 中等稳定（std=1.32%），peak layer 分散（12, 20, 21），accuracy 波动稍大
- **Qwen**: 中等稳定（std=1.90%），peak layer 最不一致（17, 18, 24），但 accuracy 显著高于 chance（所有 p_binomial=0.0）

结果文件：
- `data/llama31/probe_results_multiseed.json`
- `data/gemma2_v2/probe_results_multiseed.json`
- `data/qwen3/probe_results_multiseed.json`

---
