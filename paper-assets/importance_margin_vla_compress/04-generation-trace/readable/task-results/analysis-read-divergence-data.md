# analysis read divergence data

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_read_divergence_data_20260517T103629_result.json`
- **Structured JSON:** [`b986aba23f2c57f4c613.json`](../../sessions/b9/b986aba23f2c57f4c613.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已提取完毕。

---

## Action Divergence 分析报告

### 实验配置
- 3 个 tasks (pick-and-place: alphabet soup / bbq sauce / milk)
- 每 task 5 episodes, 共 15 episodes
- 每 episode 280 步
- 对比: baseline (未剪枝) vs ACIS (剪枝后)

---

### 1. Divergence 起始点

**Step 0 即刻偏离，L2 = 1.70**

这不是渐进累积，而是从第一步就完全崩溃。Baseline action L2 norm 约 1.29，而 divergence 达 1.70 (1.32x baseline magnitude)。剪枝后的模型输出的是本质上不同的 action。

### 2. 增长模式

| 段 | L2 增长率/步 |
|---|---|
| Step 0-10 | 0.0322 (快速) |
| Step 10-50 | 0.0037 (减速) |
| Step 50-100 | 0.0009 (平坦) |
| Step 100-200 | 0.0001 (几乎不变) |

**模式: 立即跳到高值 (1.70)，前 10 步快速增至 ~2.0，之后平稳在 2.0-2.3。** 总增长仅 +13.5%。不是指数增长，不是线性累积，是初始即崩溃后小幅恶化。

### 3. Per-Dimension Breakdown

| 维度 | Mean |Diff| 主要原因 |
|---|---|---|
| **rot_x** | 0.615 | baseline 恒为 ~1.0 (quaternion w?)，ACIS 输出 ~0.0 |
| **gripper** | 0.989 | baseline 恒为 ~0.0 (开)，ACIS 输出 ~-1.0 (闭) 或随机 |
| **pos_x** | 0.717 | 方向相反 |
| **rot_z** | 0.719 | 方向相反 |
| **pos_z** | 0.648 | 方向相反 |
| **pos_y** | 0.437 | 较小偏差 |
| **rot_y** | 0.734 | 较大偏差 |

**关键发现**: rot_x 和 gripper 两个维度贡献了恒定 ~1.0 的 offset。ACIS 模型似乎完全丢失了这两个维度的正确输出模式。

### 4. 跨 Task 一致性

| Task | Step 0 L2 | Step 10 | Step 50 | Mean |
|---|---|---|---|---|
| alphabet soup | 1.692 | 2.094 | 2.285 | 2.046 |
| bbq sauce | 1.780 | 2.027 | 2.112 | 2.004 |
| milk | 1.617 | 1.935 | 2.103 | 2.075 |

**三个 task 高度一致** (mean L2: 2.00-2.08)。Divergence pattern 与具体 task 无关，说明问题出在模型层面（全局结构被破坏），而非任务特定的能力退化。

### 5. 核心结论

1. **剪枝导致 catastrophic failure，不是 graceful degradation。** Step 0 L2=1.70 说明模型从第一步就输出错误动作。
2. **两个固定维度 (rot_x, gripper) 完全崩坏**——各贡献恒定 ~1.0 误差，这不是噪声而是系统性错误（模型输出默认值 ~0 而非正确值）。
3. **Position 维度方向反转**——ACIS 输出方向与 baseline 相反，不仅是幅度偏差。
4. **问题是 task-agnostic 的**——暗示剪枝破坏了 action decoder 的基础表征能力，而非某个 task-specific 的知识。

这为 importance-margin 方法提供了强动机：naive pruning 直接摧毁 action prediction，需要保护 action-critical 的参数。

---
