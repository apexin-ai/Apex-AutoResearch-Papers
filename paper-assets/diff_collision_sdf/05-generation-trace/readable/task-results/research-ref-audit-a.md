# research ref audit A

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_ref-audit-A_20260529T064507_result.json`
- **Structured JSON:** [`53b8b685f5eb9760b921.json`](../../sessions/53/53b8b685f5eb9760b921.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。结果已写入 `artifacts/ref_audit_worker_A.md`。

**结果：10/11 ✅，1/11 ⚠️，0 ❌**

- 全部 11 条引用真实存在，元数据（标题、作者、年份、venue、arXiv ID）均正确
- **唯一问题：** `cofreeevla2026` 在 introduction.tex 第 10 行被描述为 "collision-free demonstrations"，但 CoFreeVLA 的核心方法是碰撞风险估计+动作门控，非无碰撞示教数据。related_work.tex 的描述（"collision risk gating"）是正确的
- 特别关注项全部通过：SafeVLA 确认 NeurIPS 2025 Spotlight，SafeDiffuser 确认 ICLR 2025，CoFreeVLA (2601.21712) 和 VLSA (2512.11891) 的 arXiv ID 均存在

---
