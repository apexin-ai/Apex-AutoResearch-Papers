# ops eval exc type only

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval_exc_type_only_20260522T103309_result.json`
- **Structured JSON:** [`ee6fa57abd0380c3143e.json`](../../sessions/ee/ee6fa57abd0380c3143e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 1. exc_type_only_seed42 评估

**accuracy = 100.0%** — 1190 个测试样本全部预测正确。pass F1 = 1.00, fail F1 = 1.00。majority baseline = 71.5%。

这与 cross_mbpp2he_exception_only = 100% 一样，**强烈暗示 exception type 本身就直接编码了 pass/fail 信息**（例如：pass 的样本没有 exception，fail 的样本有 exception type — 模型只需判断有无 exception 就能 100% 区分）。这不是 bug，而是说 exception type 是一个"泄漏"特征，在 ablation 分析中需要特别讨论。

### 2. Cross-dataset MBPP→HE 结果（全部完成）

| Condition | Accuracy | Pass F1 | Fail F1 |
|---|---|---|---|
| cross_he2mbpp_exception_only | 99.41% | 0.9957 | 0.9906 |
| cross_he2mbpp_no_trace | 70.56% | 0.8074 | 0.3756 |
| cross_mbpp2he_exception_only | **100.0%** | 1.00 | 1.00 |
| cross_mbpp2he_no_trace | 67.99% | 0.7363 | 0.5927 |

exception_only 条件在两个方向都接近/达到 100%，进一步确认 exception type 是决定性信号。no_trace 条件跨数据集泛化明显下降（~68-70%），说明纯代码信息跨数据集迁移有限。

### 3. Paper 文件时间戳

所有 `.tex` 文件都是今天 (May 22) 更新的：
- `experiments.tex`: 17:23
- `appendix.tex`: 17:46（最新）
- `introduction.tex`: 17:02
- `method.tex`: 17:00
- 其余文件: 16:52-17:05

---
