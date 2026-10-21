# research rsa method audit

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_rsa_method_audit_20260516T023726_result.json`
- **Structured JSON:** [`4532fb95a3943ca8590d.json`](../../sessions/45/4532fb95a3943ca8590d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入。核心发现：

**DINO RSA=0.388 与 CLIP RSA=0.5572 不可直接比较**，存在两个关键方法学差异：

1. **配对范围不同** — `rsa_analysis.py` 做跨任务全局配对（~4950 pairs，含跨任务对），`rsa_clip.py` 只做任务内配对（~45 pairs/task，再取均值）。前者混入了 task-level confound。

2. **Action 距离度量不同** — `rsa_analysis.py` 对 7-dim action 用 **cosine distance**，`rsa_clip.py` 用 **euclidean distance**。异构维度（位移/旋转/gripper）上两者行为差异很大。

此外还有中等差异：`rsa_analysis.py` 做 3-phase temporal binning 后取均值（late phase=0.2601 拉低了整体），`rsa_clip.py` 直接用全轨迹。

**0.388 来源确认**：由 `/root/vla-ssd/rsa_analysis.py` 生成，输出到 `/root/autodl-tmp/vla-ssd/results/rsa/rsa_results.json`，= mean(early=0.4909, mid=0.4132, late=0.2601)。

报告路径：`artifacts/rsa_method_audit_report.md`

---
