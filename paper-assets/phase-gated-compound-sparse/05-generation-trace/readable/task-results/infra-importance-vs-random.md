# infra importance vs random

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_importance-vs-random_20260513T222105_result.json`
- **Structured JSON:** [`7e1a4fce884b1470687f.json`](../../sessions/7e/7e1a4fce884b1470687f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果汇总：

## Importance vs Random Masking PPL 退化对比

| Sparsity | Method | Head-only | KV-only | Compound (Head+KV) |
|----------|--------|-----------|---------|---------------------|
| **10%** | importance | **1.07x** | **1.46x** | **1.54x** |
| 10% | random | 0.97x | 2.20x | 2.23x |
| **20%** | importance | **1.22x** | **2.28x** | **2.71x** |
| 20% | random | 1.31x | 6.48x | 7.31x |
| **30%** | importance | **1.47x** | **5.09x** | **4.65x** |
| 30% | random | 4.02x | 13.80x | **26.20x** |

### 关键发现

1. **Importance-based 显著优于 random**，尤其在高 sparsity 下差距急剧扩大：
   - 30% compound: importance 4.65x vs random **26.20x**（差 5.6 倍）
   - 20% compound: importance 2.71x vs random 7.31x（差 2.7 倍）

2. **KV eviction 是退化主因**，不是 head masking：
   - 30% importance: head 仅 1.47x，KV 达 5.09x
   - Random KV eviction 在 30% 已达 13.80x，是灾难性的

3. **Head masking 本身退化可控**：importance-based 在 30% 仅 1.47x，说明确实有大量冗余 head 可以安全剪掉。Random 在 30% 也才 4.02x，远低于 compound 的 26.20x。

4. **M1v2 的 24-33x 退化主要来自 random KV eviction + compound 叠加效应**，而非 head pruning 本身。Importance-based 选择可以将 30% compound 退化从 26x 降到 4.6x。

---
