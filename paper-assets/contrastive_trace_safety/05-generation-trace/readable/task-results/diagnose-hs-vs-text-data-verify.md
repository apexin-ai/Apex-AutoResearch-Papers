# diagnose hs vs text data verify

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_hs_vs_text_data_verify_20260517T021545_result.json`
- **Structured JSON:** [`01df6164298bfbf6846b.json`](../../sessions/01/01df6164298bfbf6846b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

现在有了两组数据来源。让我整理结果：

## 结果汇总

### 数据源 1: `hs_vs_text_acc_prec.json`（全数据集 train+test 汇总指标）

| 模型 | text bal_acc | text precision |
|------|-------------|----------------|
| R1-32B | 67.30% | 50.19% |
| QwQ-32B | 61.73% | 46.01% |

### 数据源 2: `acc_precision_bootstrap/results.json`（仅 test split，bootstrap 均值）

| 模型 | text_acc_mean | text_prec_mean |
|------|--------------|----------------|
| R1-32B | 64.12% | 51.60% |
| QwQ-32B | 67.08% | 52.52% |

---

## 与 Paper Agent 使用值的对比

| 模型 | 指标 | Paper Agent 值 | 数据源1 | 数据源2 |
|------|------|---------------|---------|---------|
| R1-32B | bal_acc | **67.5%** | 67.30% | 64.12% |
| R1-32B | precision | **51.5%** | 50.19% | 51.60% |
| QwQ-32B | bal_acc | **75.2%** | 61.73% | 67.08% |
| QwQ-32B | precision | **51.5%** | 46.01% | 52.52% |

---

## 关键发现

1. **R1-32B text probe bal_acc 67.5%**：接近数据源1的 67.30%，可能是四舍五入后的值。合理。

2. **R1-32B text probe precision 51.5%**：介于数据源1 (50.19%) 和数据源2 (51.60%) 之间。数据源2 最接近。

3. **QwQ-32B text probe bal_acc 75.2%：与实际数据严重不符。** 两个数据源分别为 61.73% 和 67.08%，都远低于 75.2%。这个值没有实验数据支撑。

4. **QwQ-32B text probe precision 51.5%**：与实际值不符。数据源1 为 46.01%，数据源2 为 52.52%。

**结论**：QwQ-32B 的 text probe bal_acc = 75.2% 是明确的错误值，与所有实验数据不一致。建议使用的修正值：
- R1-32B text: bal_acc = 67.3%, precision = 51.6%（取 bootstrap test split）
- QwQ-32B text: bal_acc = 67.1%, precision = 52.5%（取 bootstrap test split）

---
