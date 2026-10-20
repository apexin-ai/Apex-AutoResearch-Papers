# analysis compile accuracy summary

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_compile-accuracy-summary_20260516T002533_result.json`
- **Structured JSON:** [`e55b626f81614a17afc4.json`](../../sessions/e5/e55b626f81614a17afc4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。汇总要点：

**QW n=100 权威值**（直接可用于 Section 4.2）：
dense=0.40, s015=0.36, s020=0.35, s025=0.33, s030=0.19。b2_fix 确认原值可靠（差异 ≤1 correct），batch1 token mismatch 影响可忽略。

**DS 8k_v2**：3/5 点完成（dense=0.74, s020=0.30, s025=0.08），s015 和 s030 仍 RUNNING。已完成的点截断率 58-76%，必须标注为 lower bound。

**关键发现**：QW 呈渐进退化（s025→s030 断崖 −14pp），DS 被截断严重混淆无法直接解读。两个模型 dose-response pattern 本质不同——QW 反映真实能力退化，DS 反映 token budget 限制。

---
