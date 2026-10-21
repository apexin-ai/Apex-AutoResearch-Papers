# code exp16b eval

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp16b-eval_20260520T001556_result.json`
- **Structured JSON:** [`f70580666c76b2a0d17e.json`](../../sessions/f7/f70580666c76b2a0d17e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报如下：

---

## Part A - exp16b eval (Llama-only MLM, seed42)

| Test Set | F1 | P | R | n |
|---|---|---|---|---|
| llama_only_test | **0.8441** | 0.8441 | 0.8441 | 77 |
| mixed_test | 0.7212 | 0.8054 | 0.7368 | 76 |
| dd_ood | 0.3327 | 0.4694 | 0.4836 | 118 |
| aa_ood | **0.8152** | 0.8062 | 0.8336 | 118 |
| toxicchat | 0.1626 | 0.2765 | 0.1152 | 242 |

DD OOD 和 ToxicChat 上表现很差。AA OOD 上出乎意料地好。

---

## Part B - exp17

**Checkpoint 完成度: 9/9** (vanilla×3 + mlm×3 + 9class×3)

eval_exp17.py 有两个 bug 已修复：
1. MLM `gru_subpath` 从 `treatment/best.pt` → `baseline/best.pt`
2. `load_encoder` 添加 `.float()` 避免 fp16 类型错误

**完整结果表:**

| Variant | DD F1 (mean±std) | AA F1 | TC F1 | IID F1 |
|---|---|---|---|---|
| vanilla | 0.326±0.000 | 0.508±0.085 | 0.367±0.018 | 0.987±0.005 |
| mlm | 0.338±0.010 | 0.351±0.018 | 0.303±0.014 | 0.982±0.011 |
| **9class** | **0.889±0.041** | **0.913±0.041** | 0.364±0.040 | **1.000±0.000** |

9class 在 DD/AA OOD 上碾压 vanilla 和 mlm（F1 0.89/0.91 vs 0.33/0.35）。所有 variant 在 ToxicChat 上都差（~0.3-0.37）。IID 都接近 1.0。

---

## Part C - exp17 泄漏检查

```
expanded_1000/train: 700 samples
plan_002_splits/test: 76 samples
overlap: 54 samples (71% of test set!)
```

**严重泄漏**。plan_002_splits/test.jsonl 中 54/76 条样本出现在 expanded_1000/train.jsonl 中。exp17 的 IID F1≈1.0 很可能被高估——测试集绝大多数样本在训练时已见过。exp17 的 OOD 结果不受此影响（OOD 数据独立于训练集），但 IID 数字不可信。

---
