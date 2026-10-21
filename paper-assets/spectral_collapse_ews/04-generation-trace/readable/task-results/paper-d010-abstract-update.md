# paper d010 abstract update

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_d010_abstract_update_20260517T072922_result.json`
- **Structured JSON:** [`f1485d881d6aba7f26f9.json`](../../sessions/f1/f1485d881d6aba7f26f9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

无破折号、无 -ing 短语问题。

---

### 修改总结

**Line 4 (before):**
> We provide, to our knowledge, the first spectral-level characterization of how effective rank evolves across recursive generations, derive an online early warning signal (EWS) from its normalized decline rate, and propose, to our knowledge, the first closed-loop adaptive controller that redistributes a fixed real-data budget temporally based on spectral health feedback.

**Lines 4-5 (after):**
> We provide, to our knowledge, the first spectral-level characterization of how effective rank evolves across recursive generations, and propose a closed-loop adaptive controller that redistributes a fixed real-data budget temporally based on spectral health feedback.
> Concretely, we define spectral log-volume (SLV), the log-determinant of the representation covariance, as a continuous collapse indicator and derive an online early warning signal (EWS) from its normalized decline rate.

**Line 5 (before):**
> Our controller applies reactive boosts when collapse pressure exceeds a calibrated threshold, while guaranteeing that total real-data consumption equals that of a uniform baseline.

**Line 6 (after):**
> Our controller applies reactive boosts when the SLV decline rate exceeds a calibrated threshold, while total real-data consumption equals that of a uniform baseline.

**关键变更：**
- Controller 信号从隐含的 effective rank decline rate 改为明确的 SLV (spectral log-volume) decline rate
- 新增 Line 5 显式定义 SLV 及其与 EWS 的关系
- Effective rank 保留为 collapse 特征化指标（Line 2, 4），不再作为 controller 信号
- 删除重复的 "to our knowledge, the first"（EWS 和 controller 合并为一处声明）
- "collapse pressure" 改为更精确的 "SLV decline rate"
- "guaranteeing that" 简化为 "while"

---
