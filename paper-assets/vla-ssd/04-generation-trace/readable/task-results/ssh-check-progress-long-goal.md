# ssh check progress long goal

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_progress_long_goal_20260521T194056_result.json`
- **Structured JSON:** [`428883c811df76b5b216.json`](../../sessions/42/428883c811df76b5b216.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 进度汇报

### 总体状态
| 实验 | GPU | Trained (5 phases) | Untrained (5 phases) | 总进度 |
|------|-----|-------------------|---------------------|--------|
| tracvla_long_v1 | cuda:0, 50%, 9.3GB | **完成** (181.5 min) | Phase 1: Task 1/10 (~10%) | **6/10** |
| tracvla_goal_v1 | cuda:1, 50%, 9.4GB | **完成** (180.4 min) | Phase 1: Task 3/10 (~38%) | **6/10** |

**预计剩余时间**: ~170-180 min（untrained pipeline 与 trained 耗时相当）

---

### Trained 结果提取

#### 1. R² Probing（关键层）

| 层 | long image_mean | long last_preaction | goal image_mean | goal last_preaction |
|----|----------------|--------------------|-----------------|--------------------|
| L0 | 0.795 | 0.616 | 0.803 | 0.612 |
| L7 | 0.812 | 0.805 | 0.828 | 0.779 |
| L11 | 0.816 | **0.817** | 0.824 | 0.786 |
| L16 | **0.826** | 0.808 | 0.827 | 0.788 |
| L18 | 0.825 | 0.809 | **0.836** | **0.802** |
| L23 | 0.821 | 0.762 | 0.842 | 0.750 |
| L27 | 0.816 | 0.651 | 0.816 | 0.653 |
| L30 | 0.799 | 0.434 | 0.812 | 0.307 |
| L31 | 0.790 | 0.619 | 0.805 | 0.574 |

两者模式一致：image_mean 全程稳定（~0.80-0.84），last_preaction 呈 inverted-U（中层 peak，L27-L30 骤降）。goal 在 L30 的 last_preaction 降得更厉害（0.307 vs 0.434）。

#### 2. L1 Attention Profile

| 实验 | instruction_dominant | mixed | image_dominant |
|------|---------------------|-------|---------------|
| long | **30**/32 | 2/32 (h13, h22) | 0 |
| goal | **27**/32 | 5/32 (h2, h6, h13, h22, h24) | 0 |

#### 3. Cross-instruction Classification（chance=0.1）

| 实验 | image_mean (all layers) | last_preaction L0 | last_preaction L1+ |
|------|------------------------|-------------------|--------------------|
| long | **1.0** (全层) | 0.983 | **1.0** |
| goal | 0.996→1.0 (L10+) | 0.915 | **1.0** |

两者几乎完美分类——表示层编码了 task 身份信息。

#### 4. Counterfactual Sensitivity（Cohen's d 排序）

| 排名 | long condition | long d | goal condition | goal d |
|------|---------------|--------|----------------|--------|
| 1 | empty | **1.473** | empty | **1.524** |
| 2 | wrong | 1.418 | wrong | 1.405 |
| 3 | shuffled | 1.391 | shuffled | 1.336 |
| 4 | paraphrased | 1.161 | paraphrased | 1.213 |

两者敏感性排序完全一致：empty > wrong > shuffled > paraphrased。所有条件 d > 1.0，paraphrased 最低但仍有显著效应。

---

**注意**：按 C001 约束，不对 trained vs untrained 下结论——untrained 数据仍在采集中。预计 ~3 小时后两个实验全部完成。

---
