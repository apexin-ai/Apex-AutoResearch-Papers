# analysis d073 cycle detector oh urgent

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d073-cycle-detector-oh-urgent_20260516T035618_result.json`
- **Structured JSON:** [`09e509aa92333df5d417.json`](../../sessions/09/09e509aa92333df5d417.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

Cycle detector 在 OH 上 zero-shot cross-agent **彻底失败**：

| Method | SWE Silver F1 | OH All F1 | OH Conf≥2 F1 | Δ(SWE→OH) |
|--------|-------------|-----------|-------------|-----------|
| **Structural GB** | 0.995 | **0.967** | **0.992** | -2.8pp |
| Cycle 3-gram (t=0.70) | 0.721 | 0.530 | 0.592 | -19.1pp |
| Cycle 2-gram (t=0.75) | 0.661 | 0.520 | 0.535 | -14.1pp |

关键发现：
- Cycle 3-gram 在 OH 上 F1 仅 **0.530**（all）/ **0.592**（conf≥2），f1_stag 只有 0.19/0.28，几乎无法检测 stagnation
- **即使 oracle 调参**，OH 上 cycle detector 天花板也只有 **0.552**（all）/ **0.614**（conf≥2）
- Structural GB 的 cross-agent 0.967 vs cycle 的 0.530，差距 **43.7pp** — cross-agent transfer 是论文的 genuine contribution

---
