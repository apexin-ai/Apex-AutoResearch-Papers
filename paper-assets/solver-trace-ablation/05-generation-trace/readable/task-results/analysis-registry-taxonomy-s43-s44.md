# analysis registry taxonomy s43 s44

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_registry-taxonomy-__-s43-s44_20260515T164655_result.json`
- **Structured JSON:** [`fba85f8598a7af623f19.json`](../../sessions/fb/fba85f8598a7af623f19.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 完成。核心结论：

**s44-1000-r2 的 3 个 "genuine" proof 全部是 H1-near，genuine_strict = 0。**

三个 proof 共享同一漏检模式：结论是析取式 (∨)，存在 `∀x` premise 实例化后精确等于/包含结论，加上 ground facts 冗余满足各析取项。ISR 全部为 0。classify_h7 漏检因为：H1 不做 ∀x 实例化文本匹配，H8 只查合取式。

### 已完成

| 项目 | 结果 |
|------|------|
| s43-1000-r2 taxonomy | H7a=90/90 (100%), genuine=0 ✓ |
| s44-1000-r2 taxonomy | H1=85, H8=15, H1∩H8=3, genuine=3 (all H1-near) |
| s44 3个genuine审查 | folio_1296/1428/1051 均为 ∀x 实例化析取式，非真实推理 |
| Registry 更新 | 两个实验 metrics + notes 已更新，含 genuine_strict=0 |
| 审计报告 | `art_20260515_79720b` 已注册 |

### 待注意
- **无 s42-1000 实验**：任务提到 s42: genuine=0/96，但 registry 和服务器均无 s42 1000步实验。s42-r2 是 500 步 (genuine=7/93)，其 7 个 genuine 尚未做 H1-near 审计。
- **两 seed 统计** (1000步): genuine_strict = 0.0% ± 0.0% (s43, s44)。Reviewer 怀疑的 1.0%±1.7% 已被修正为 0。

---
