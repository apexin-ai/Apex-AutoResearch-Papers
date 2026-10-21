# eval zeroshot deepseek7b

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_zeroshot_deepseek7b_20260517T132723_result.json`
- **Structured JSON:** [`0c3391999d0df5d1a632.json`](../../sessions/0c/0c3391999d0df5d1a632.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已得到关键信息。结果汇总：

---

## DeepSeek-Coder-6.7B-Instruct Zero-Shot 结果

| 指标 | 值 |
|------|------|
| **Accuracy** | **90.59%** (95% CI: [88.99%, 92.18%]) |
| Majority Baseline | 71.51% |
| Lift over baseline | +19.08% |

### Per-class 指标

| Class | Precision | Recall | F1 |
|-------|-----------|--------|------|
| Pass | 0.9743 | 0.8919 | 0.9313 |
| Fail | 0.7762 | 0.9410 | 0.8507 |

### 对比

| Model | Method | Accuracy |
|-------|--------|----------|
| Qwen2.5-Coder-7B-Instruct | Zero-shot | 89.08% |
| **DeepSeek-Coder-6.7B-Instruct** | **Zero-shot (logit)** | **90.59%** |
| Qwen2.5-Coder-7B-Instruct | SFT | 99.83% |

### 错误分析

- **总错误数**：112/1190
- **Unknown 比例**：0（logit 方法始终产出 pass/fail）
- **pass→fail（false negative）**：92 条 — 占错误的 82%
- **fail→pass（false positive）**：20 条 — 占错误的 18%

**主要错误模式**：模型对 pass 样本过度保守，倾向判 fail。Fail recall(94.1%) 远高于 pass recall(89.2%)，说明模型对"代码有问题"的判断比较积极。

### 前 5 条错误（均为 fail→pass 类型）

| idx | label | pred | margin |
|-----|-------|------|--------|
| 29 | fail | pass | 0.5977 |
| 30 | fail | pass | 0.1406 |
| 31 | fail | pass | 0.1406 |
| 33 | fail | pass | 0.1406 |
| 35 | fail | pass | 0.1406 |

margin 很小（多为 0.14），说明这些 borderline case 模型信心不足。

### 注意

因 DeepSeek 使用 chat template 后会直接生成解释性文本而非单词回答，采用了 **logit-based classification**（比较 yes/pass vs no/fail token 的 logit 大小）而非 generation-based，这是公平的 zero-shot 方法（不需要任何 prompt engineering，只需一次 forward pass）。

---
