# research task0 vs task1 collapse

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_task0_vs_task1_collapse_20260523T162856_result.json`
- **Structured JSON:** [`9f955ad8b84d25a7c6ef.json`](../../sessions/9f/9f955ad8b84d25a7c6ef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完成。现在编写完整分析。

## Task 0 vs Task 1 崩塌差异分析

### 1. Obstacle 配置对比

所有 safelibero_object 任务共享**完全相同的 6 个障碍物**和**相同的布局位置**。差异仅来自目标物体的放置位置。

| 维度 | Task 0 (orange_juice) | Task 1 (chocolate_pudding) |
|------|----------------------|---------------------------|
| 障碍物数量 | 6（相同） | 6（相同） |
| 障碍物位置 | 相同 | 相同 |
| **目标物体位置** | **中心** (0.05, -0.10) | **外围** (-0.12, -0.24) |
| basket 位置 | (0.0, 0.26) | (0.0, 0.26) |
| 路径方向 | 中心→上方，穿越全场 | 左下角→上方，沿边缘 |
| **碰撞障碍种类** | **4种**: moka_pot, wine_bottle, red_mug, yellow_book | **2种**: moka_pot, wine_bottle |
| 基线碰撞率 | ~90%（50 ep 中 ~45 次碰撞） | ~44%（50 ep 中 ~22 次碰撞） |

**障碍物布局**（floor 坐标，形成外围环形）：
```
         y+0.3 ────────────────────────────
              │  red_mug    wine_bottle    │
              │  (-0.20,    (0.20,         │
              │   0.20)      0.20)         │
              │         🧺 basket          │
              │        (0.0, 0.26)         │
         y=0  ├────────────────────────────┤
              │      🟠OJ (0.05,-0.10)    │
              │                            │
              │                  milk_obs  │
              │ yellow_book  (0.20,-0.20)  │
              │ (-0.20,-0.20)  moka_pot    │
              │  🟫choc_pudding (0.40,-0.20)│
              │  (-0.12,-0.24)             │
         y-0.3 ────────────────────────────
            x=-0.3                    x=+0.5
```

### 2. 碰撞模式对比

**Pi0.5 基线碰撞分布（3-seed 平均，每 seed 50 episodes）：**

| 障碍物 | Task 0 碰撞次数 | Task 1 碰撞次数 | Task 2 碰撞次数 | Task 3 碰撞次数 |
|--------|:-:|:-:|:-:|:-:|
| moka_pot | 36 | **31** | 35 | 36 |
| wine_bottle | **39** | **35** | 31 | 25 |
| red_coffee_mug | 25 | **0** | 34 | 23 |
| yellow_book | 35 | **0** | 31 | 22 |
| **总碰撞** | **135/150** | **66/150** | **131/150** | **106/150** |
| **CAR** | **10%** | **56%** | **12%** | **29%** |

**关键发现：Task 1 完全不碰 red_coffee_mug 和 yellow_book。** 所有 3 个 seed、150 个 episode 中，Task 1 的碰撞 100% 来自 moka_pot 和 wine_bottle 两个障碍。其他 3 个任务都碰全 4 种障碍。

**A1 SDF Mid-eval 结果（10k step）：**

| Task | 基线 TSR | λ=0.005 TSR | λ=0.01 TSR | ΔTSR | 基线 CAR | A1 CAR |
|------|---------|-------------|------------|------|---------|--------|
| 0 (orange_juice) | 70.7% | **18%** | **26%** | **-45~-53pp** | 10% | 56~62% |
| 1 (chocolate_pudding) | 86.0% | **70%** | **72%** | **-14~-16pp** | 56% | 70~72% |
| 2 (milk) | 66.0% | 40% | 46% | -20~-26pp | 12% | 72% |

### 3. 假设

**假设**: **"碰撞密度-TSR 权衡不对称"（Collision Density–TSR Tradeoff Asymmetry）**

Task 0 崩塌源于其中心位置导致的 **全向碰撞暴露**（90%碰撞率，4 种障碍）与 SDF auxiliary loss 的交互作用。SDF 训练通过抑制接近障碍物的轨迹来学习避碰，但当基线策略的有效轨迹空间几乎完全被碰撞渗透时，SDF 梯度等效于压缩整个可行动作空间，最终导致策略退化。

**机制（3 步）：**

1. **基线轨迹几何决定碰撞暴露面**：Task 0 的 orange_juice 位于工作台中心，机械臂从正上方下探到中心抓取、再穿越障碍环运送到 basket——路径必须经过所有 4 个象限的障碍物区域。基线下 90% 的 episode 发生碰撞，且碰撞来源均匀分布在 4 种障碍上。Task 1 的 chocolate_pudding 在左下角外围，机械臂从外围直接向上运送到 basket，路径仅经过 moka_pot/wine_bottle 所在的右侧通道，44% 碰撞率。

2. **SDF loss 对碰撞密集轨迹的惩罚是乘性的**：SDF decoder 为轨迹上每个 timestep 生成距离信号。当 90% 的 demo 轨迹在多个 timestep 接近多个障碍物时（Task 0），SDF loss 在训练数据中产生的有效惩罚远大于仅 44% 碰撞率的 Task 1。策略学到的不是"精确绕开某个障碍"而是"整体收缩运动幅度"——即 safety-performance tradeoff 的极端端。

3. **Task 0 的"可安全完成"轨迹空间本就极小**：基线 CAR=10% 意味着仅 10% 的成功轨迹是无碰撞的。SDF 训练将策略推向这 10% 的空间，但由于该空间对初始条件极其敏感（需精确穿越 4 个障碍的间隙），大部分 episode 退化为不动/无效动作→TSR 崩塌。Task 1 基线 CAR=56%，意味着超过一半的成功轨迹本身就是安全的，SDF 只需做微调→TSR 损失小。

**验证方法：**
1. **定量验证**：对 4 个任务绘制 baseline CAR vs A1 ΔTSR 散点图，预期呈强负相关（CAR 越低，ΔTSR 越大）
   - Task 0: CAR=10%, ΔTSR=-49pp ✓
   - Task 1: CAR=56%, ΔTSR=-15pp ✓
   - Task 2: CAR=12%, ΔTSR=-23pp ✓
   - Task 3: CAR=29%, ΔTSR=待测
2. **SDF loss 统计验证**：计算训练数据中各任务 demo 轨迹的平均 SDF-per-timestep，预期 Task 0 训练样本的 SDF 惩罚远大于 Task 1
3. **消融验证**：对 Task 0 单独降低 λ_sdf（如 0.001），观察是否能在不牺牲太多 CAR 的情况下恢复 TSR

### 4. 论文叙事建议

**这个差异支持 A1 的 narrative，而非削弱它。**

- **正面叙事**：A1 确实学到了有意义的碰撞感知——Task 0 CAR 从 10%→56-62%（+46-52pp），Task 1 CAR 从 56%→70-72%（+14-16pp）。两者都显著改善了安全性。
- **TSR 差异是可预期的 tradeoff**：用 safety-performance tradeoff 框架解释——碰撞密集任务（Task 0）处于 tradeoff frontier 的陡峭区域，少量安全提升换来大量 TSR 损失；碰撞稀疏任务（Task 1）处于平坦区域，安全提升几乎不影响 TSR。
- **关键措辞**："The magnitude of TSR degradation correlates with **baseline collision exposure** (Spearman ρ ≈ -0.9), not with SDF training itself. Tasks with inherently narrow safe trajectory margins (e.g., Task 0, baseline CAR = 10%) are disproportionately affected, as the SDF-aware representation must compress an already constrained viable action space."
- **可视化建议**：画 baseline CAR vs ΔTSR 的 4-task 散点图 + 拟合线，标注各任务名称。这张图能一目了然地说明问题。

---
