# research latency profiling design

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_latency_profiling_design_20260516T025445_result.json`
- **Structured JSON:** [`257952d2c8c652927ab8.json`](../../sessions/25/257952d2c8c652927ab8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

方案文档已保存至 `artifacts/_project/report/latency_profiling_design.md`。

核心设计要点：

1. **三层计时**：Level 1 per-sample wall-clock（已有）→ Level 2 LogitsProcessor 内部 breakdown（wrap `__call__`）→ Level 3 model forward 用差值法
2. **侵入最小**：新建独立脚本 `run_latency_profile.py`，wrap 现有 processors，不修改正式实验代码
3. **关键洞察**：TypeConstraintProcessor 每 token 做 `decode + regex`，其开销随序列长度 O(n) 增长，这是最值得量化的点
4. **实验规模**：最小矩阵 ~14h 单 GPU，双 RTX PRO 6000 并行约 7h 可完成

---
