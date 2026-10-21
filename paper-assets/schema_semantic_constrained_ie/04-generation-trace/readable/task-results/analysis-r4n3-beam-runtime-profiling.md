# analysis r4n3 beam runtime profiling

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r4n3_beam_runtime_profiling_20260518T120631_result.json`
- **Structured JSON:** [`cd05976061ad8390d95f.json`](../../sessions/cd/cd05976061ad8390d95f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Report written to `artifacts/r4_n3_runtime_profiling.md`.

## 结果总结

### 最可靠的对比: Qwen DocRED (matched 50-doc subset, 同 GPU 近时运行)

| | Greedy | Beam k=4 | Overhead |
|---|---|---|---|
| Per-doc avg | 18.5s | 31.4s | **1.69x** |
| Per-doc median | 18.1s | 24.5s | **1.35x** |

Beam 的 tail latency 显著更高 (max 129s vs 33s)。

### Beam width scaling (Qwen SciERC, 551 docs)

| k | Avg (s) | 相对 k=2 |
|---|---|---|
| 2 | 5.39 | 1.00x |
| 4 | 5.92 | 1.10x |
| 8 | 7.06 | 1.31x |

**Sub-linear scaling**: k 翻倍只增加 10-19% latency。

### Fine-tuned beam 加速

FT beam k=4 比 ZS beam k=4 快 **1.6x** (avg 3.7s vs 5.9s)，因为 FT 模型 token 分布更集中，beam 更早收敛。

### Caveats

- SciERC greedy baseline 跑的时间比 beam 早 2-3 天，不是严格控制变量对比 (Qwen greedy 反而比 beam k=4 慢，不合理)
- Llama DocRED beam vs greedy 几乎无差异 (0.98x)，可能因 greedy tail variance 大
- **建议**: 论文引用 Qwen DocRED 的 1.69x/1.35x 作为 beam overhead；如需 clean SciERC 数据，需重跑 greedy baseline

---
