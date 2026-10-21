# paper per task analysis

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_per-task-analysis_20260529T150201_result.json`
- **Structured JSON:** [`d9904a7acb0b8692f48b.json`](../../sessions/d9/d9904a7acb0b8692f48b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已生成并注册：`art_20260529_a01313`

核心发现：

- **Fingerprint 完全一致**：CP > Milk > OJ > BBQ 排序在 4/4 条件均值和 12/12 seed 中保持（BBQ 最后 100%，CP 最高 83%）
- **Task identity 解释 94% 的 CAR 方差**，seed/condition 仅占 6%——直接支撑 Claim 3（demonstration-driven）
- **BBQ 20pp seed 波动（λ=0.01 s0=34→s2=14）**是 n=50 下的 binomial noise（预期 95% CI 宽 ~23pp），且 LoRA-only 和 SDF 条件下方差相当
- **无任何 task 有显著 SDF 收益**：最大的 Milk delta (+4.2pp) 不到 1σ；BBQ（SDF 最应帮助的 task）仅 +1.8pp

---
