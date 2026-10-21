# audit claim wording

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_claim_wording_20260527T233938_result.json`
- **Structured JSON:** [`77f4451458173dc9ddd8.json`](../../sessions/77/77f4451458173dc9ddd8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 6 fixes verified. Summary of changes:

---

##修正清单

| # | 文件:行 | 原文 | 修改后 | 原因 |
|---|--------|------|--------|------|
| 1 | abstract.tex:5 | "demonstrations **alone** account for **all** measured avoidance gains (~28pp)" | "demonstrations account for all measured avoidance gains **at $\lambda \leq 0.01$** (~28pp)" | 去掉"alone"，限定"all"的scope到3-seed有统计支撑的λ范围 |
| 2 | abstract.tex:5 | "two-tailed permutation test)" | "two-tailed permutation test, **$n{=}2$**)" | λ=0.1结果必须标注样本量 |
| 3 | abstract.tex:6 | "**cannot** be credited" | "cannot **reliably** be credited" | λ=0.1的marginal signal不允许完全否定 |
| 4 | discussion.tex:3 | "account for **all** measured avoidance gains" | "account for **the** measured avoidance gains" | 同fix #1，去掉绝对量词 |
| 5 | discussion.tex:6 | "arises **entirely** from this distributional shift" | "arises **primarily** from this distributional shift" | λ=0.1有marginal increment，"entirely"过强 |
| 6 | claim3.tex:27 | "SDF gradients produce no lasting behavioral effect" | "**this provides preliminary evidence that** SDF gradients produce no lasting behavioral effect" | Phase 2 ablation仅n=1，不能下确定性结论 |

### λ=0.1 Provisional 状态：全部合规 ✓

所有λ=0.1相关描述均使用provisional措辞（"marginal"/"suggestive"/"inconclusive"），且现在abstract也标注了n=2。无处使用"significantly"描述λ=0.1结果。

---
