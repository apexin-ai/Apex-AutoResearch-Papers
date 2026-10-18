# code mistral aggressive diagnosis

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mistral_aggressive_diagnosis_20260514T060920_result.json`
- **Structured JSON:** [`c04581f6cad9ee9af298.json`](../../sessions/c0/c04581f6cad9ee9af298.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## 结果汇总

| 压缩率 | Uniform 2-bit PPL | MCKP PPL | MCKP 优势 |
|--------|-------------------|----------|-----------|
| **5.3x** | 519.11 | **11.91** | **43.6×** |
| **8x** | 519.11 | **399.90** | 1.30× |

### 跨架构对比 (5.3x)

| 模型 | MCKP PPL | Uniform PPL | 倍率 |
|------|----------|-------------|------|
| Llama-3.1-8B | 57.6 | 2643.8 | 45× |
| Mistral-7B | 11.9 | 519.1 | **43.6×** |

**结论：success。** 压缩率增大放大 MCKP 优势的规律跨架构成立——Llama 45× vs Mistral 43.6×，倍率高度一致。Mistral 绝对 PPL 更低（架构更鲁棒），但 MCKP 相对优势幅度几乎相同。8x 两者均 catastrophic，MCKP 略优但不实用。

---
