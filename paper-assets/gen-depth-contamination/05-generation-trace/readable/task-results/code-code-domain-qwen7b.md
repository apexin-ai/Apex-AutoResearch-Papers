# code code domain qwen7b

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_code_domain_qwen7b_20260524T094847_result.json`
- **Structured JSON:** [`145b0d5db2b0fea6da7d.json`](../../sessions/14/145b0d5db2b0fea6da7d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已完成，数据和结果完整。汇报如下：

## Qwen2.5-7B Code (Python) 实验结果

**数据**: 5500 docs × 6 depths (depth 0-5)，共 33K 条，已生成完毕。

**K\* = 2**（与预期一致，同家族 Qwen-1.5B Code 也是 K\*=2）

### Pairwise AUC (adjacent depths, 5-fold CV)

| Pair | AUC | 判定 |
|------|-----|------|
| 0 vs 1 | 0.9051 ± 0.0043 | 可区分 |
| 1 vs 2 | 0.7276 ± 0.0055 | 可区分 |
| 2 vs 3 | 0.5368 ± 0.0145 | ~随机 |
| 3 vs 4 | 0.5090 ± 0.0055 | 随机 |
| 4 vs 5 | 0.5139 ± 0.0128 | 随机 |

### Pairwise JSD

| Pair | JSD |
|------|-----|
| 0v1 | 0.0613 |
| 1v2 | 0.0423 |
| 2v3 | 0.0041 |
| 3v4 | 0.0032 |
| 4v5 | 0.0034 |

JSD 在 depth 2→3 出现数量级下降（0.042 → 0.004），与 AUC 判定一致。

### Ordinal Classification (6-class)
- MAE = 1.2651
- Accuracy = 34.2%

### Top Features
freq_entropy, surp_d2_mean, surp_d1_mean 排前三，与其他 Code 实验一致。

**结论**: Qwen2.5-7B Code 的 K\*=2，符合 Code domain 的整体模式（Qwen-1.5B=2, LLaMA-8B=2, Mistral-7B=2）。7B 规模并未比 1.5B 显示更深的可区分性，支持 "saturation depth 由 domain 决定而非 model size" 的论点。

---
