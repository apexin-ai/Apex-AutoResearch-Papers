# eval zeroshot codellama13b

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_zeroshot_codellama13b_20260517T134955_result.json`
- **Structured JSON:** [`9572f1fedf06268aa65e.json`](../../sessions/95/9572f1fedf06268aa65e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## CodeLlama-13B-Instruct Zero-Shot 结果

### Accuracy 对比

| Model | Zero-Shot Acc | Method |
|---|---|---|
| Qwen-7B | 89.08% | generation (yes/no → pass/fail) |
| DeepSeek-6.7B | 90.59% | generation |
| **CodeLlama-13B** | **51.01%** | generation (max_new_tokens=10) |
| SFT best | 99.83% | fine-tuned |

### Per-class 指标

| | Precision | Recall | F1 |
|---|---|---|---|
| Pass | 1.0000 | 0.3502 | 0.5187 |
| Fail | 0.3585 | 0.9115 | 0.5146 |

- 95% CI: [48.24%, 53.95%]
- **低于 majority baseline (71.51%)，lift = -20.5%**
- Unknown: 30/1190 (2.5%)

### 错误模式

极度偏向 "fail"：
- **pass→fail: 553 条**（占全部 851 个 pass 样本的 65%）
- fail→pass: 0 条
- fail→unknown: 30 条

### Raw output 分布

| Output | Count |
|---|---|
| "no, this code does not pass all tests" | 773 |
| "yes, the code passes all the tests." | 106 |
| "yes, this code passes all three tests." | 100 |
| "no, the code does not pass all tests" | 89 |
| "yes, the code passes all three tests." | 58 |
| 其他（代码解释等 unknown） | ~30 |

### 前 5 条错误
全部是 label=pass, pred=fail, raw="no, this code does not pass all tests"

### 总结
CodeLlama-13B-Instruct 在 verdict prediction 上表现极差，严重倾向预测 "fail"（862/1190 = 72.4% 预测为 fail），导致 accuracy 甚至低于 majority baseline。这与 Qwen-7B (89.08%) 和 DeepSeek-6.7B (90.59%) 形成鲜明对比，说明 CodeLlama 在 zero-shot 场景下对代码正确性判断存在系统性负面偏差。

---
