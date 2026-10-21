# ops instruct numbers confirm

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_instruct-numbers-confirm_20260516T170917_result.json`
- **Structured JSON:** [`2cef72566f435061b6ee.json`](../../sessions/2c/2cef72566f435061b6ee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Instruct 实验精确数字摘要

### OLMo-2-0425-1B-Instruct
```
LOGO 3-class macro F1:  0.3379  [95% CI: 0.325 – 0.351]
Binary F1:              0.4255  [95% CI: 0.413 – 0.439]
对应 base (OLMo-2-1B):  0.7633  [95% CI: 0.752 – 0.774]  (3-class)
                         0.7944  [95% CI: 0.782 – 0.805]  (binary)
Delta (instruct−base):  −0.4254 (3-class)
Evaluation scope:       7-gen LOGO (instruct 作为 held-out generator)
训练集包含 instruct 数据: 否 (LOGO held-out)
```

### Qwen3-0.6B-Instruct
```
LOGO 3-class macro F1:  0.6674  [95% CI: 0.656 – 0.679]
Binary F1 (gen0 vs 1+): 0.9883
对应 base (Qwen3-0.6B): 0.8158  [95% CI: 0.805 – 0.827]  (3-class)
                         0.9876  (binary)
Delta (instruct−base):  −0.1484 (3-class)
Evaluation scope:       7-gen LOGO (instruct 作为 held-out generator)
训练集包含 instruct 数据: 否
```

### Qwen3-1.7B-Instruct
```
LOGO 3-class macro F1:  0.5434
Binary F1:              0.6582
对应 base (Qwen3-1.7B): 0.8023 (3-class)
                         0.8208 (binary)
Delta (instruct−base):  −0.2589 (3-class)
Evaluation scope:       7-gen LOGO (instruct 作为 held-out generator)
训练集包含 instruct 数据: 否
```

### 共同特征
- 三个 instruct 模型均为 **7-gen LOGO** 评估（6 个 base + 1 个 instruct，instruct 作为 held-out）
- instruct tuning 一致降低 depth signal，delta 范围 −0.15 ~ −0.43
- OLMo-Instruct 退化最严重（F1 仅 0.34），Qwen3-0.6B-Instruct 相对最好（0.67）
- `review_p1c_instruct.json` 是 Qwen3-1.7B-Instruct 的 Spearman 相关分析（无 LOGO F1），`p1c_instruct_logo_f1.json` 包含其 LOGO F1
- `instruct_length_confound.json` 确认三个 instruct 模型均存在 length confound（depth 与 length 的 |ρ| = 0.37–0.58），但 partial correlation 控制 length 后 entropy reversal 仍然存活

---
