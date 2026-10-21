# analysis genuine isr fix v3

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_genuine-isr-fix-v3_20260514T153807_result.json`
- **Structured JSON:** [`9a503b9318bf7acb9c9a.json`](../../sessions/9a/9a503b9318bf7acb9c9a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

r4 更新完成。关键变更：

**r3 → r4 差异:**
- 全面切换到 **strict normalization**（与 h7_corrected_results.txt 一致）
- Random s42: H1=56/79 (70.9%), Genuine=23 (29.1%), Genuine ISR=**0.243** (std=0.169)
- Random s44: H1 从 74 修正为 **71**/89 (79.8%), Genuine 从 15 修正为 **18** (20.2%), Genuine ISR=**0.166** (std=0.335)
- Apple-to-apple ratio: ISR s42 genuine (0.601) / Random s42 genuine (0.243) = **2.5×**（r3 报 2.4×，因 loose normalization 得 21 genuine ISR=0.252）
- 删除了 author re-classification 脚注，strict 为权威分类
- 2 borderline samples 已识别（folio_499、folio_394 结论带括号）

---
