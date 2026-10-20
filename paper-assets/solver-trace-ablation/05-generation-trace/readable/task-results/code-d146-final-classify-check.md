# code d146 final classify check

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d146-final-classify-check_20260520T033010_result.json`
- **Structured JSON:** [`5b31c0ff83ac04b3c3bc.json`](../../sessions/5b/5b31c0ff83ac04b3c3bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 7 个 classify.json 已完成。汇总：

| Model | proved | TS (h7) | CE (h1) | PG (h8) | CI | genuine | genuine_rate |
|---|---|---|---|---|---|---|---|
| **base** (d146_pf_base) | 16 | 0 | 0 | 0 | 0 | **16** | **100%** |
| **exec_s42** | 99 | **99** (100%) | 0 | 0 | 0 | **0** | **0%** |
| **exec_s43** | 63 | 0 | **31** (49.2%) | 0 | 0 | **32** | **50.8%** |
| **exec_s44** | 72 | 0 | **71** (98.6%) | 0 | 0 | **1** | **1.4%** |
| **isr_s42** | 46 | 0 | 0 | 0 | 0 | **46** | **100%** |
| **isr_s43** | 56 | 0 | **39** (69.6%) | 0 | 0 | **17** | **30.4%** |
| **isr_s44** | 66 | 0 | 0 | 0 | 0 | **66** | **100%** |

关键发现：
- **exec_s42** 完全 collapse 到 TS hacking（99/99 全是 h7a），genuine=0
- **exec_s44** 几乎全是 CE hacking（71/72），genuine 仅 1
- **exec_s43** 混合：约一半 CE + 一半 genuine
- **ISR 训练整体好很多**：s42 和 s44 的 genuine_rate=100%，s43 有 69.6% CE 但仍有 17 genuine
- **base** 模型 proved 很低（16）但全是 genuine
- 没有 H8/CI hacking 出现在任何 run 中

---
