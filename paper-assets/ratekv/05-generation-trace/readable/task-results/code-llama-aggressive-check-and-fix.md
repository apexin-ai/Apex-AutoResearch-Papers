# code llama aggressive check and fix

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama_aggressive_check_and_fix_20260514T053240_result.json`
- **Structured JSON:** [`3511e84cecf21f72ecf4.json`](../../sessions/35/3511e84cecf21f72ecf4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验正在运行中，进展良好。当前状态：

**已完成：**
- Baseline PPL: **8.0918**
- Uniform 4-bit (ref): **8.4690** (与之前一致)
- Budget 0.1875 (5.3x) Uniform 2-bit: **2643.77** (全2-bit，崩坏)
- Budget 0.1875 (5.3x) MCKP: bit dist {4:128, 2:128}，正在评估 PPL，chunk ~150/564，running ppl ~57

**进行中：** MCKP 5.3x 的 PPL 评估（约 27% 完成），之后还有 budget=0.125 (8x) 的两个评估。

**初步观察：** MCKP 在 5.3x 下 running ppl ~57 vs uniform 2-bit 的 2643——MCKP 把一半 heads 保留在 4-bit，PPL 从 2643 降到 ~57，差距巨大。虽然 ~57 远高于 baseline 8.09，但相比 uniform 2-bit 改善了 ~46 倍。

预计还需 10-15 分钟完成剩余评估。无需干预，进程正常。

---
