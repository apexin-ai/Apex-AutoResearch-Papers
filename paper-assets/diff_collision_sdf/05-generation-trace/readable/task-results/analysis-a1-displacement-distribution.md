# analysis a1 displacement distribution

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_a1_displacement_distribution_20260522T155750_result.json`
- **Structured JSON:** [`ded0afaaa46ad0a0f41a.json`](../../sessions/de/ded0afaaa46ad0a0f41a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论

### A1 Displacement 分布

| 指标 | A1 (SDF) | LoRA Baseline | A3 (force-refine) |
|------|----------|---------------|---------------------|
| Total episodes | 12 | 200 | 200 |
| TSR | **0%** | **0%** | **0%** |
| CAR | 91.7% | 90.0% | 74.5% |
| **Collapse (disp < 1e-4)** | **91.7% (11/12)** | **89.0% (178/200)** | **73.0% (146/200)** |
| Normal episodes | 1 | 22 | 54 |

### M022 式离散浮点噪声 — 确认存在

A1 的 11 个 collapse episodes 只有 **3 个离散值**（典型浮点噪声 pattern）：
- `1.80e-10`: 4 次
- `6.62e-10`: 3 次
- `3.72e-07`: 4 次

和 A3 M022 的 pattern 完全一致。

### 关键发现：LoRA Baseline 同样 89% collapse

**Action collapse 不是 SDF 训练导致的。** LoRA baseline 在没有任何 SDF signal 的情况下也有 89% 的 collapse 比例和相同的离散噪声 pattern。三个模型 TSR 全为 0%，说明 object 任务本身就没有被任何模型学会。

不过 ee_displacement 显示机器人手臂确实在动（A1 mean=0.527），只是不接触任何障碍物——这不是经典的"机器人冻住"式 collapse，而是"机器人在动但不做任务、不碰东西"。

### 结论

**CAR=90% 是假安全**，但不是 SDF 训练造成的。根因是 object 任务本身没被学会（TSR=0%），机器人随意运动但恰好不碰障碍物，导致 CAR 虚高。LoRA baseline 和 A1 的 collapse 比例几乎相同（89% vs 92%），SDF training 对 obstacle displacement 分布没有显著影响。A1 的 eval 样本量也很小（只有 12 episodes vs baseline 的 200），统计意义有限。

---
