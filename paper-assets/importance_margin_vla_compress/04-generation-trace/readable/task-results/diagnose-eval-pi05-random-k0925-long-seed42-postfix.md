# diagnose eval pi05 random k0925 long seed42 postfix

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_pi05_random_k0925_long_seed42_postfix_20260525T182215_result.json`
- **Structured JSON:** [`7a4561258f4ad292ae0f.json`](../../sessions/7a/7a4561258f4ad292ae0f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

**实验成功完成。**

**关键指标：**
- Overall SR: **38.6%** (193/500)
- 运行时间: 257.9 min
- 配置: random pruning, k=0.925, 236/256 tokens kept

**Cliff zone 分析：**

| keep ratio | SR |
|---|---|
| 0.95 | 61.2% |
| **0.925** | **38.6%** |
| 0.90 | 32.0% |

k=0.95→0.925 下降了 22.6 个百分点（61.2→38.6），而 k=0.925→0.9 只下降 6.6 个百分点（38.6→32）。这说明 cliff 的主要跌落发生在 k=0.95 到 k=0.925 区间，衰退模式是**突变式**而非渐进式——仅多剪 2.5% tokens（从保留 243→236），性能就断崖式下跌。

---
