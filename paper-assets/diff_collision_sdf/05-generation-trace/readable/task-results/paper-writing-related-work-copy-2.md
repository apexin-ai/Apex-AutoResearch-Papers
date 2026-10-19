# paper writing related work

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_related_work_20260520T233447_result.json`
- **Structured JSON:** [`5cd5b2febcff515cbfe3.json`](../../sessions/5c/5cd5b2febcff515cbfe3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Related Work 初稿已写入 `artifacts/drafts/related_work.tex`，约 770 words，4 个小节：

- **§2.1 3D-Aware VLAs** — 归纳 13 篇 3D-aware VLA 工作，重点对比 QDepth-VLA（2.5D camera-frame depth vs workspace SDF、decoder 解耦 vs 直接 feature refinement、遮挡盲区），提及 Spatial Forcing 的 implicit alignment 不产生 distance field。结尾回到"无一篇以碰撞为目标"的 gap。
- **§2.2 Collision-Safe Robot Policies** — 按 post-hoc correction（AEGIS, CoFreeVLA）和 constrained optimization（SafeVLA）归纳，简要提及 iKinQP-RL / CAPE / language-guided cost denoising（无 cite）。核心对比：安全机制独立于 VLA 表征 vs ColliForce 内化碰撞几何。
- **§2.3 SDF in Robotics** — 从表征（DeepSDF）→ 场景重建（iSDF）→ 可微碰撞检测（DiffCo）→ 运动规划（RAMP, CSSDF-Net, Neural NMPC-SDF）→ 策略学习（SAMP, Prof. Robot）。定位：SDF 从未集成到 VLA 架构。
- **§2.4 Action Refinement** — 2 句提 DFM-VLA 验证 VLA 内 iterative refinement 可行，1 句定位 ColliForce 的 SDF gradient refinement 为 collision-specific instantiation。

已通过风格检查：无 em-dash/en-dash、无 -ing 短语结尾、无 banned words、无论文堆砌式写法。

---
