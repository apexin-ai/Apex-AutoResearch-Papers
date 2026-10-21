# research safevla deep read

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_safevla_deep_read_20260520T023304_result.json`
- **Structured JSON:** [`8dd0002ce11fb2e6dcba.json`](../../sessions/8d/8dd0002ce11fb2e6dcba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。关键发现总结：

**SafeVLA 不是 SafeLIBERO 上的竞品**。SafeVLA 用的是 AI2THOR 移动操作任务（Safety-CHORES），base model 是 SPOC，与 LIBERO tabletop manipulation 完全不同领域。

**VLSA/AEGIS 才是 SafeLIBERO 上最直接竞品**（arXiv:2512.11891）：
- CBF+QP training-free 安全层，接在 pi0.5/OpenVLA 输出后
- SafeLIBERO 总体：CAR 77.85%, TSR 68.13%（pi0.5 baseline: CAR 18.69%, TSR 50.88%）
- 我们 MVP 任务对标：Spatial-Bowl LII (AEGIS CAR 86%), Object-Pudding LI (AEGIS CAR 32%)
- 主要弱点：依赖外部感知（GroundingDINO/VLM），仅限平移，安全修正导致分布偏移

**Lan-o3dp** 与我们 A3 最相似（推理时 cost-guided denoising），但用点云欧式距离而非 SDF 梯度。

**ColliForce 可声称优势**：
1. SDF 连续可微 > 点云距离（更精确的梯度方向）
2. 训练时+推理时双重安全网（A1+A3 互补）
3. 不依赖外部 VLM/GroundingDINO 做障碍检测
4. Flow matching 原生集成（vs DDPM denoising）

Sources:
- [SafeVLA (arXiv)](https://arxiv.org/abs/2503.03480)
- [SafeVLA GitHub](https://github.com/PKU-Alignment/SafeVLA)
- [VLSA/AEGIS (arXiv)](https://arxiv.org/abs/2512.11891)
- [SafeLIBERO Benchmark](https://vlsa-aegis.github.io/benchmark.html)
- [Lan-o3dp (arXiv)](https://arxiv.org/abs/2407.00451)

---
