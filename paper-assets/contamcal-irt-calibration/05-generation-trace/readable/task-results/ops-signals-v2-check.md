# ops signals v2 check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_signals-v2-check_20260522T182120_result.json`
- **Structured JSON:** [`7023599edb99b2a4a8e8.json`](../../sessions/70/7023599edb99b2a4a8e8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## 结果报告

**Falcon3-7B-Base d100 s42 — 信号文件状态：**

| Signal | MMLU | ARC Challenge | GSM8K |
|--------|------|---------------|-------|
| S1 embedding | ✅ 7.8MB | ✅ 662KB | ✅ 733KB |
| S2 minkpp | ✅ 2.9MB | ✅ 250KB | ✅ 272KB |
| S4 selfcritique | ✅ 3.3MB | ✅ 290KB | ✅ 315KB |

- **S1/S2**：从 v1 保留完好（时间戳 May 22 22:28-22:52）
- **S4**：v2 全部完成（时间戳 May 23 01:55-02:12），MMLU 15 chunks 覆盖 0-14042 项
- **全部 9 个 signal × benchmark 组合已就绪**，无缺失

---
