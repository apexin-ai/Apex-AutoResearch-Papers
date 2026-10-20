# ops t25 a045 s43 analysis and 14b t15a045

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_t25-a045-s43-analysis-and-14b-t15a045_20260522T102656_result.json`
- **Structured JSON:** [`3ec20c641e03a51c81e8.json`](../../sessions/3e/3ec20c641e03a51c81e8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两件事都完成：

**任务 1 — t25_a045_s43 D102 分析**
- PermG fwd = **6/8**, rev = 0/8
- Robust pairs (≥3/5 methods) = **6/8**
- 与 s42 完全一致 → **seed-robust 确认**
- 强 pairs: ece→distinct_1 (5/5), token_entropy→distinct_3 (4/5)，其余 distinct pairs 3/5
- 弱 pairs: mauve 相关 (1/5, 2/5)
- Registry → DONE (success), 10.16 GPU-hours

**任务 2 — scale_14b_t15_a045_s42_fp32 (最后一个 1.4B)**
- westd-17855:cuda:5, PID 667187
- 模型已加载 (10284 MiB), 正在训练 gen_0
- HF_HOME + HF_HUB_CACHE + TRANSFORMERS_OFFLINE 三件套已设置
- Registry → RUNNING
- 这是 6/6 1.4B 实验的最后一个

---
