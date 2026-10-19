# verify cell4 equivalence

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_cell4_equivalence_20260518T013441_result.json`
- **Structured JSON:** [`f35f25ebcfe777631e88.json`](../../sessions/f3/f35f25ebcfe777631e88.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论

**Cell 4 被 Cell 3 (exp029) 自动覆盖。假设成立。**

### 分析

**1. Full context 模式下每个 episode 产生几个 window？**

**1 个。** 整个 episode 是单个 batch sample（一条 prompt+response）。

**2. 代码路径确认：**

Step-level advantage 的计算逻辑（line 272）被严格门控：

```python
if context_window_mode == "step_independent" and adv_estimator == AdvantageEstimator.GRPO:
    # 只有 step_independent 模式进入这里
    # 这里才会区分 advantage_mode == "episode_level" vs step-level
```

当 `context_window_mode == "full"` 时，这整个 block 被跳过。代码走标准 GRPO 路径（`compute_grpo_outcome_advantage`），对每个 sample 的所有 token 赋予相同的 advantage 值（基于 episode reward 的 group normalization）。

**3. Step-level vs episode-level 在单 window 下是否数值等价？**

**是的，结构上等价。** 原因：
- `compute_step_discounted_returns`：在只有 1 个 step（整个 episode 作为单 sample）时，R_0 = r_0，只有一个值
- `compute_episode_returns`：所有 step 共享从 step 0 计算的 return，也是同一个值
- 标准 GRPO outcome advantage：每个 sample 的所有 token 得到同一个 advantage

三者在单 sample 情况下数值相同。

**4. exp029 配置确认：**
- `context_window_mode: "full"`
- 未设置 `advantage_mode`（无意义，因为不进入 step_independent 分支）
- 走标准 GRPO outcome advantage = episode-level advantage

### 结论

在 full context 模式下，不存在"step-level advantage"这个有意义的区分——整个 episode 是一个不可分割的 sample，只有一个 reward signal，所有 token 共享同一个 advantage 值。Cell 4 在当前代码中无法独立实现，且概念上与 Cell 3 等价。

2×2 矩阵实际是 3-cell：
| | step-level adv | episode-level adv |
|---|---|---|
| step_independent | Cell 1: 0% | Cell 2: 15.63% |
| full context | Cell 3 = Cell 4: **28.1%** | ← 同一实验 |

---
