# paper prewrite sections

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_prewrite-sections_20260522T125352_result.json`
- **Structured JSON:** [`45895ab4d9af4ca25c69.json`](../../sessions/45/45895ab4d9af4ca25c69.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个章节已写入：

- **Related Work** (`related_work.tex`, coverage 18/20) — 3 个文献流：VLA Safety（VLSA/AEGIS, SafeVLA, CoFreeVLA, OSCBF, OGM-CBF）、3D Spatial Representations（BEVFormer, OccNet, Occ3D, OccVLA, DepthVLA, AugVLA-3D, SpatialForcing, SpatialVLA, PointVLA, ST-VLA, MiDaS, Depth Anything）、Auxiliary Task Learning（Caruana 1997, Ruder 2017, Wang et al. 2023, LoRA）。Gap 定位在三个领域交叉处。
- **Method** (`method.tex`, coverage 13/14) — Problem Formulation（总 loss 公式）、BEV Occupancy Head（完整架构参数：Linear→2×ConvTranspose2d→Conv2d, 1.2M params, FocalLoss α=0.25 γ=2.0, 指数衰减 λ=0.01·exp(-t/50000)）、Depth Head（SmoothL1, ReLU）、Ablation Design（5 条件 + 表格说明每个 pairwise comparison 隔离的因子）。
- **Experiment Setup** (`experiment_setup.tex`, coverage 16/17) — SafeLIBERO Level I 10 tasks、TSR/CAR 定义（threshold=0.001）、训练配置（LoRA r=32, batch 8, lr 5e-4, 50005 steps, 3-4 seeds, 50 rollouts/task）、硬件（4×RTX PRO 6000 98GB, ~12.9h/run）。

所有 27 篇引用均通过 WebSearch 验证真实存在，每个 `\cite{}` 旁附有完整引用信息注释。无 em-dash，无 AI 风格用词，无 -ing 分词短语结尾。

---
