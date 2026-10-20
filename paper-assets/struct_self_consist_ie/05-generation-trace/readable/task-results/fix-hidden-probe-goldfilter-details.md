# fix hidden probe goldfilter details

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_hidden_probe_goldfilter_details_20260518T105341_result.json`
- **Structured JSON:** [`f5896ab19d528d4ac107.json`](../../sessions/f5/f5896ab19d528d4ac107.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 完成汇总

### 关键发现：评估本已正确

原始 probe 代码 (`hidden_state_probe.py`) **已经在 evaluation 阶段 gold-filter 了** — `load_instance_data()` 跳过 `gold_entities == []` 的 instance。`results.json` 显示的 `n_instances: 529` 是正确的。3 seeds [42, 123, 456] × 5-fold CV 也已完成。

本次新增：overfitting 追踪 + 综合 `results_goldfiltered.json`。

### 实验细节

| 项目 | 值 |
|---|---|
| **Hidden state 来源** | Qwen3-8B + SciERC LoRA merged (v2), last hidden layer, mean-pool over output tokens |
| **Hidden dim** | 4096 |
| **Linear probe** | Ridge (α=1.0), StandardScaler |
| **MLP 架构** | 4096→256→64→1, ReLU, Dropout=0.1 |
| **MLP 训练** | Adam (lr=1e-3, wd=1e-4), batch=256, max 100 epochs, early stopping patience=15 |
| **评估** | 5-fold CV × 3 seeds (42, 123, 456), instance-level split |

### Overfitting

- **Linear**: 严重过拟合 (train MSE=0.0004, val MSE=0.565) — 4096 features vs ~3400 training samples
- **MLP**: 适度 (train MSE=0.042, val MSE=0.078, gap=0.036), early stopping 有效 (avg best epoch=9.4)

### 最终结果表 (gold-filtered 529 instances, 3-seed mean±std)

| Method | Dim | Spearman ρ | Selection F1 | Gap Closure |
|--------|-----|-----------|-------------|-------------|
| LP (mean logprob) | 1 | 0.2207 | 0.6087 | -0.4% |
| Hidden Linear | 4096 | 0.2346±0.020 | 0.6206±0.005 | 7.0% |
| Hidden MLP | 4096 | 0.4611±0.020 | 0.6317±0.004 | 13.9% |
| Oracle | — | — | 0.7692 | 100% |

结果文件:
- 服务器: `output/hidden_state_probe/results_goldfiltered.json`
- 本地: `artifacts/hidden_state_probe/results_goldfiltered.json`

---
