# analysis paper evidence table

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_paper-evidence-table_20260514T070810_result.json`
- **Structured JSON:** [`b782ca2baf5ab4b2b09c.json`](../../sessions/b7/b782ca2baf5ab4b2b09c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出已写入并注册。

核心内容：
- **8 个有效实验**按 reward mode 分组（exec-only 3 seeds / additive ISR 2 β / convex random / additive random / convex ISR）
- **Claim 1 证据**：exec-only 3-seed 中 2/3 退化（s43 PR=14% degenerate, s44 PR=98% tautological collapse）
- **Claim 2 证据**：ISR + component count 联合诊断 — comp≈2 标记 tautological（s44, plan013），comp>5 + moderate ISR 标记 genuine（s42, plan002-b01）
- **Claim 3 证据**：β=0.3 → PR collapse（Goodhart），β=0.1 → sweet spot（PR=0.81, ISR 2.73x baseline）
- 底部标注了 D029（s43 eval 方法差异）和 D030（plan005 无 eval）
- 附带论文直接可用的 compact table

---
