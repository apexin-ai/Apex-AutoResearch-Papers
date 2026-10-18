# code budget sweep

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_budget_sweep_20260514T010123_result.json`
- **Structured JSON:** [`1eca0e031ee622a9cd25.json`](../../sessions/1e/1eca0e031ee622a9cd25.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。

**Budget Sweep 结果总结：**

| 压缩率 | Budget | Uniform PPL | MCKP PPL | Delta | MCKP 分配 |
|--------|--------|------------|----------|-------|-----------|
| 2x | 0.500 | 10.10 (8b) | 10.66 | -0.56 | 16b:38, 4b:66, 2b:8 |
| 4x | 0.250 | 15.45 (4b) | 11.23 | **+4.21** | 8b:4, 4b:100, 2b:8 |
| 8x | 0.125 | 14758.92 (2b) | 906.78 | **+13852** | 4b:4 (L0), 2b:108 |

**核心结论**：MCKP 在 4x 和 8x 下显著优于 uniform（success 标准达成）。2x 下 MCKP 反而略差，因为宽松 budget 下 uniform 8-bit 已足够好，而 MCKP 的混合分配引入了低 bit-width heads 的额外伤害。MCKP 的优势随压缩率增大而急剧增长——这是论文的好数据点。

---
