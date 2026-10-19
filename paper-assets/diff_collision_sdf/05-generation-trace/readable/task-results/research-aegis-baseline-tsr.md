# research aegis baseline tsr

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_aegis_baseline_tsr_20260522T032224_result.json`
- **Structured JSON:** [`eca980fee8026f0ae8fb.json`](../../sessions/ec/eca980fee8026f0ae8fb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕，汇总如下。

---

## AEGIS (VLSA) 论文 SafeLIBERO Baseline 数据

**论文**: VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer (arXiv 2512.11891, 2024-12)

### 1. Baseline 模型和训练配置

| | OpenVLA-OFT | π0.5 |
|---|---|---|
| Base model | OpenVLA-7B + optimized fine-tuning | π0.5 (Physical Intelligence) |
| 训练数据 | **50 demos/task** (LIBERO 标准: 500 demos / 10 tasks per suite) | 同上 |
| Action space | Delta end-effector pose | - |
| 训练 steps | 50K–150K gradient steps (8×A100) | - |
| Eval episodes | **50 episodes/scenario** (共 1600 episodes = 4 suites × 4 tasks × 2 levels × 50 eps) | 同上 |

### 2. SafeLIBERO-Object TSR（重点关注）

| Task | Level | OpenVLA-OFT | π0.5 | AEGIS |
|------|-------|------------|------|-------|
| Orange juice → basket | I | **0%** | **84%** | 88% |
| Orange juice → basket | II | 78% | 72% | 74% |
| Chocolate pudding → basket | I | **0%** | **6%** | 92% |
| Chocolate pudding → basket | II | 70% | 82% | 92% |
| Milk → basket | I | **0%** | **0%** | 74% |
| Milk → basket | II | 48% | 72% | 68% |
| BBQ sauce → basket | I | **0%** | **56%** | 82% |
| BBQ sauce → basket | II | 40% | 58% | 72% |
| **Suite 平均** | | **29.5%** | **53.8%** | 80.3% |

### 3. 全 benchmark 平均 TSR

| | OpenVLA-OFT | π0.5 | AEGIS |
|---|---|---|---|
| Overall avg | **22.81%** | **50.88%** | 68.13% |

### 4. 与我们的配置差异

| | 我们 | VLSA baseline |
|---|---|---|
| Model | π0 | π0.5 / OpenVLA-OFT |
| Demos | 50 | 50/task (标准 LIBERO) |
| 当前 TSR | 0% (20 eps) | π0.5: 0%–84%, 平均 53.8% |
| Eval eps | 20 (进行中) | 50 |

### 5. 判断

- **数据量相同**：VLSA 也是 50 demos/task，和我们一样，所以 50 demos 不是问题根源。
- **Task 确实有难的**：Level I 下 OpenVLA-OFT 在 Object suite 全是 0%；π0.5 在 milk Level I 也是 0%。障碍物靠近目标物体时，vanilla VLA 确实很难。
- **但 π0.5 整体远好于 0%**：π0.5 Object suite 平均 53.8%，说明 π0.5 比 π0 强很多。我们用 π0 而非 π0.5 可能是关键差异。
- **OpenVLA-OFT Level I 全 0%**：说明没有安全约束的 VLA 在高难度场景确实趋近 0%，但 Level II（障碍物在路径上而非目标旁）时能恢复到 40%–78%。

**结论**：50 demos 数据量够，但 π0 vs π0.5 的模型能力差异可能是主要原因。建议确认我们 eval 的具体 task 和 obstacle level 配置，以及是否对标的是 Level I（最难）场景。

Sources:
- [VLSA Paper (arXiv)](https://arxiv.org/abs/2512.11891)
- [VLSA Paper HTML](https://arxiv.org/html/2512.11891v1)
- [VLSA Project Page](https://vlsa-aegis.github.io/)
- [OpenVLA-OFT Paper](https://arxiv.org/html/2502.19645v1)
- [SafeLIBERO Dataset](https://huggingface.co/datasets/THURCSCT/SafeLIBERO)

---
