# analysis tsr collapse mechanism

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_tsr_collapse_mechanism_20260526T040202_result.json`
- **Structured JSON:** [`f891df6afb9992b02083.json`](../../sessions/f8/f891df6afb9992b02083.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心发现：

**TSR Collapse 机制诊断：COMPOSITE（复合机制）**

| 指标 | Pi0.5 Base | SDF λ=0.005 30K | LoRA Baseline 30K |
|------|-----------|-----------------|-------------------|
| avg TSR | 75.5% | 6.8% | 7.1% |
| Safe Failure Rate | 0.5% | 49.8% | 47.5% |
| Collision Failure Rate | 24.0% | 43.0% | 45.4% |
| Obstacle Displacement | 0.143m | 0.059m | 0.060m |
| EE Displacement | N/A | ~0.5m | N/A |
| Frozen Episodes | N/A | 0% | N/A |

**3 条关键证据链：**

1. **SDF loss 不是 TSR 崩溃的原因**：LoRA baseline（无 SDF loss）TSR 崩溃幅度完全一致（68.4% vs 68.7%）。根因是 LoRA 在 safety 数据上 fine-tuning 破坏了 pre-trained task policy。

2. **不是纯粹的 catastrophic forgetting（motor level）**：robot 没有冻结，EE displacement 均值 0.5m，0% 冻结 episode。Robot 在动，但不是目标导向的运动。

3. **有 learned collision avoidance 组件**：safe failure rate 从 0.5% 暴增到 ~50%（100 倍），obstacle displacement 减半。Robot 学会了避障但丢失了 task completion 能力。

**对审稿人的回复论点**：TSR collapse 的 root cause 是 LoRA fine-tuning 的 catastrophic forgetting of task semantics（不是 SDF loss），fine-tuned model 保留了部分 collision avoidance 能力但丧失了 goal-directed grasping/placing 行为。

**产出路径：**
- 脚本：`westd-35807:/root/colliforce-vla/scripts/analysis_tsr_collapse.py`
- 图表：`westd-35807:/root/colliforce-vla/figures/` （4 组 PDF+PNG）
- 已注册：`art_20260526_b41f73`（report）、`art_20260526_c26246`（figures index）

---
