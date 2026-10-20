# knowledge paper framing update

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_knowledge_paper-framing-update_20260514T172304_result.json`
- **Structured JSON:** [`d0f0710443f8f3eb5653.json`](../../sessions/d0/d0f0710443f8f3eb5653.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

paper_framing.md 已更新。变更摘要：

1. **新增 Claim 状态总览表**：Claim 1 ✅、Claim 2 ✅ (D057)、Claim 3 ⏳
2. **Claim 2 标题**：`D033→D043→D051 定论` → `D033→D043→D051→D057 闭环`，加 ✅
3. **Claim 3 标题**：移除 `conditional on plan006`，改为 `exec-only D056 done; STA awaiting s43/s44`
4. **Claim 3 证据重组**：分为 Part A (D056 exec-only 闭环) 和 Part B (STA Goodhart 跨逻辑复现)，添加 D056 结论总结和 C006 ISR 语义区分警告
5. **β 剂量表**：补全 3-seed random PR/ISR 数据（之前缺 s43/s44 random 的 per-seed 标注）
6. **Goodhart Landscape 标题**：更新为 `D033→D051→D057 闭环`
7. **Structural Fixes checklist**：新增 D057/D056/SFT baseline 已完成项 + Claim 3 待办项

Claim statements 未改动，仅更新 evidence 和 status。

---
