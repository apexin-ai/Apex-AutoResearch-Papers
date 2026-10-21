# diagnose 8b rsft s42 ground truth

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_8b-rsft-s42-ground-truth_20260522T214202_result.json`
- **Structured JSON:** [`0b8d363ad5a7588ed381.json`](../../sessions/0b/0b8d363ad5a7588ed381.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据全部拿到。两个 s42 eval 的差异已清楚。

## 诊断报告

### 两个 s42 eval 的差异

| | d102_8b_k1_s42 | plan_006_qwen3_8b_rsft_eval |
|---|---|---|
| **ign_f1** | **0.5376** | **0.5433** |
| model_path | `rsft_output_qwen3_8b_k1` | `rsft_output_qwen3_8b/checkpoint-3393` |
| n_predictions | 16,314 | 16,831 |
| n_truncated | 242 | 267 |
| max_new_tokens | 1024 | 1024 |
| split | dev | dev |
| seed | 42 | 42 |

**根因：模型不同。** plan_006 用的是早期 RSFT 模型的 checkpoint-3393，d102 系列用的是 k1 rejection sampling RSFT 模型。不是同一个模型的两次 eval，而是两个不同模型的 eval。

### 3-seed 同协议结果（d102 系列，k1 RSFT）

| Seed | Model | ign_f1 |
|------|-------|--------|
| s42 | rsft_output_qwen3_8b_k1 | 0.5376 |
| s43 | rsft_output_qwen3_8b_k1_s43 | 0.5471 |
| s44 | rsft_output_qwen3_8b_k1_s44 | 0.5451 |

三个 seed 的 eval 配置完全一致（同 base_model、同 sft_adapter、同 max_new_tokens=1024、同 split=dev、同 seed=42），仅训练 seed 不同。

### 正确的 Mean ± Std

```
vals = [0.5376, 0.5471, 0.5451]
Mean = 0.5433
Std  = 0.0050 (0.50pp)
```

**论文应报告：54.33 ± 0.50**

### Registry 问题

Registry 中 plan_006_qwen3_8b_rsft_eval 的 ign_f1=0.5433 是那个**旧模型**（非 k1）的真实结果，不是 d102 s42 的结果。Registry 如果把这个值当作 s42 的 ign_f1 来算 3-seed 均值，就混入了不同模型的数据——尽管巧合地 0.5433 恰好接近 3-seed 均值。

正确的 s42 ign_f1 是 **0.5376**（来自 d102_8b_k1_s42/metrics.json）。

### 其他关键指标（d102 三 seed 均值）

| 指标 | s42 | s43 | s44 | Mean |
|------|-----|-----|-----|------|
| ign_f1 | 53.76 | 54.71 | 54.51 | 54.33 |
| evi_f1 (TP-only) | 81.36 | 81.80 | 81.45 | 81.54 |
| evi_f1_joint | 44.01 | 45.44 | 44.72 | 44.72 |
| edcr | 62.31 | 60.94 | 62.33 | 61.86 |
| n_truncated | 242 | 231 | 230 | 234 |

---
