# code probe fix v3 and both probes

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_probe_fix_v3_and_both_probes_20260521T201354_result.json`
- **Structured JSON:** [`f8adffcdeb362bdc43d7.json`](../../sessions/f8/f8adffcdeb362bdc43d7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总如下：

---

## 1. 代码修改验证

3 处全部已使用 balanced_accuracy，验证通过：

| 验证项 | 状态 |
|--------|------|
| run_direction 中 best layer 选择用 `bal_acc > best_bal_acc` | ✓ |
| main() 中 `key=lambda r: r["balanced_accuracy"]` | ✓ |
| permutation test 用 `bal_acc >= observed_bal_acc` | ✓ |
| 语法检查 SYNTAX OK | ✓ |

## 2. Llama-3.1 探针结果 (32 layers)

| 方向 | accuracy | balanced_acc | f1 | peak_layer | binomial_p | permutation_p |
|------|----------|-------------|------|------------|------------|---------------|
| EN→EN | 0.7757 | 0.7757 | 0.7814 | 28 | 0.0 | 0.0 |
| ZH→ZH | 0.7206 | 0.7206 | 0.7121 | 13 | 0.0 | 0.0 |
| EN→ZH | 0.5956 | 0.5956 | 0.5635 | 5 | 0.000966 | 0.001 |
| ZH→EN | 0.7132 | 0.7132 | 0.7516 | 15 | 0.0 | 0.0 |

## 3. Qwen-3 探针结果 (36 layers)

| 方向 | accuracy | balanced_acc | f1 | peak_layer | binomial_p | permutation_p |
|------|----------|-------------|------|------------|------------|---------------|
| EN→EN | 0.7500 | 0.7500 | 0.7500 | 24 | 0.0 | 0.0 |
| ZH→ZH | 0.7262 | 0.7262 | 0.7356 | 14 | 0.0 | 0.0 |
| EN→ZH | 0.6726 | 0.6726 | 0.6893 | 23 | 5e-06 | 0.0 |
| ZH→EN | 0.7321 | 0.7321 | 0.7097 | 18 | 0.0 | 0.0 |

数据是类别平衡的，所以 accuracy == balanced_accuracy。所有方向的 permutation_p 都显著 (p ≤ 0.001)。Qwen 的跨语言迁移 (EN→ZH: 0.6726) 明显优于 Llama (EN→ZH: 0.5956)。

---
