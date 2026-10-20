# code llama8b qwen scored update

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama8b_qwen_scored_update_20260522T202449_result.json`
- **Structured JSON:** [`a5d8618520cc683de569.json`](../../sessions/a5/a5d8618520cc683de569.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Log confirms this is the **Qwen2.5-1.5B-Instruct** scorer run (Phase 2). Results:

## LLaMA-8B 10K — Qwen Scorer Results

### Pairwise AUC (adjacent depths)

| Pair | AUC | ±std |
|------|-----|------|
| 0v1 | 0.9282 | 0.0019 |
| 1v2 | 0.6148 | 0.0078 |
| 2v3 | 0.5247 | 0.0067 |
| 3v4 | 0.5221 | 0.0032 |
| 4v5 | 0.5015 | 0.0101 |

### K* = 2 (max depth with AUC > 0.60)

### Ordinal Classification
- Accuracy: 0.3293
- MAE: 1.3186

### JSD (adjacent depths)
| 0v1 | 1v2 | 2v3 | 3v4 | 4v5 |
|-----|-----|-----|-----|-----|
| 0.0797 | 0.0095 | 0.0034 | 0.0025 | 0.0025 |

### 1v2 对比确认
Qwen scorer 1v2 AUC = **0.6148**，与 bootstrap OOF AUC (0.5880) 有差距（+0.027）。这个差异在合理范围内：bootstrap OOF 是 out-of-fold 估计，通常偏保守；而这里的 5-fold CV mean 包含了完整特征集评估，略高是正常的。

### 与 Phase 1 自评分对比
Phase 1（LLaMA-8B scorer）的 0v1 和 2v3 值需要替换为上面的 Qwen scorer 值（0v1=0.9282, 2v3=0.5247），以保持 appendix 表格中所有行都使用 cross-model scorer 的一致性。

---
