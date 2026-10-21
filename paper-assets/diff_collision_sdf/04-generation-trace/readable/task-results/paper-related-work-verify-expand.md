# paper related work verify expand

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_related_work_verify_expand_20260525T082751_result.json`
- **Structured JSON:** [`d6db73d71c7eb7a33f1c.json`](../../sessions/d6/d6db73d71c7eb7a33f1c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成所有更新。最终结果：

---

### Part 1: 引用核实

| 论文 | 状态 |
|------|------|
| CoFreeVLA (Zhai et al., 2026) | **Verified** — arXiv 2601.21712，非 hallucinated |
| APEX (IROS 2024) | **Verified** |
| Safe Learning Survey (Zhang 2025) | **Verified** |
| C-space SDF (Li, RSS 2024) | **Verified** |
| SDF-SC ("Liu" 2024) | **Needs correction** — 一作是 Zhu 非 Liu，已修正 |
| Neural NMPC-SDF (Jacquet, IJRR 2025) | **Verified** |

### Part 2: VLA Foundations

RT-2、π0、OpenVLA 已在文献列表中，无需新增。

### Part 3: 新增 5 篇（已写入 literature_map.yaml）

**Action Collapse（2 篇）:**
- **Conditioning Matters / Cocos** (Dong et al., 2025) — diffusion policy 中的 loss collapse 机制，与 ColliForce action collapse 直接类比
- **Diffusion Policy** (Chi et al., RSS 2023) — IL 中 mode averaging 的规范表述

**Safe RL/IL（3 篇）:**
- **CPO** (Achiam et al., ICML 2017) — 训练时安全 RL 基础，标量 cost vs ColliForce 几何 SDF 信号
- **RAIL** (Jung et al., ICRA 2025) — 测试时可达性安全过滤 vs 训练时嵌入
- **TamedPUMA** (Bakker et al., L4DC 2025) — 运行时 geometric fabrics vs 训练时 SDF

---
