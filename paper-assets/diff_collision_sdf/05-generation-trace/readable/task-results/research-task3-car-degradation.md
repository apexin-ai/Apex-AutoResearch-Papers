# research task3 car degradation

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_task3_car_degradation_20260524T042951_result.json`
- **Structured JSON:** [`621c61225fe528aa6f08.json`](../../sessions/62/621c61225fe528aa6f08.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已获取关键数据。A1 l005 Task 3 中，失败 episode 的碰撞集中在 moka_pot (7/9)，而成功 episode 碰撞分散在 red_coffee_mug/wine_bottle。

现在汇总分析。

## Task 3 (bbq_sauce) CAR 恶化调查

### 1. Per-Episode 碰撞对比

| 指标 | Baseline (pi0.5) | A1 l005 | A1 l01 |
|------|----------|---------|--------|
| TSR | 76% | 60% | 52% |
| CAR | 34% | 26% | 28% |
| 碰撞 episodes | 33/50 | 37/50 | 36/50 |
| collision-free | 17/50 | 13/50 | 14/50 |
| success+collision | 21 | 28 | 23 |
| success+no_collision | 17 | 2 | 3 |
| fail+collision | 12 | 9 | 13 |
| fail+no_collision | 0 | 11 | 11 |

**关键发现**: Baseline 所有 17 个 collision-free episodes 都是成功的。A1 l005 的 13 个 collision-free 中只有 2 个成功，11 个失败。**SDF 造成"避障成功但任务失败"的 tradeoff。**

### 2. 碰撞对象分布变化

| 障碍物 | Baseline | A1 l005 | Δ |
|--------|---------|---------|---|
| moka_pot (0.40, -0.20) | 12 | 12 | 0 |
| wine_bottle (0.20, 0.20) | 10 | 11 | +1 |
| red_coffee_mug (-0.20, 0.20) | **5** | **10** | **+5** |
| yellow_book (-0.20, -0.20) | 6 | 4 | -2 |
| **总计** | **33** | **37** | **+4** |

**碰撞转移明确存在**: red_coffee_mug 碰撞翻倍 (5→10)。SDF 推离右侧障碍 (wine_bottle/moka_pot) 时，轨迹偏左，撞上左侧的 red_coffee_mug。

A1 l005 失败 episode 碰撞分布: moka_pot=7/9 (78%)，说明 moka_pot 的早期碰撞 (mean step=73) 最具破坏性。

### 3. 与 Task 0 的关键对比

Task 0 (orange_juice) 和 Task 3 (bbq_sauce) 有 **完全相同的障碍物布局和目标位置** (target 都在 (0.05, -0.10)，basket 在 (0.0, 0.26))。但结果截然相反：

| | Task 0 Baseline→A1 | Task 3 Baseline→A1 |
|---|---|---|
| 碰撞数 | 47→19 (**-28**) | 33→37 (**+4**) |
| CAR | 6%→62% (**+56pp**) | 34%→26% (**-8pp**) |
| TSR | 64%→18% (-46pp) | 76%→60% (-16pp) |
| max_displacement | 0.2436→0.0692 (-71%) | 0.1536→0.1298 (-15%) |

**Task 0 baseline 碰撞率 94%** → 有巨大改善空间，SDF 梯度引导效果显著。
**Task 3 baseline 碰撞率 66%** → 已处于"中等安全"状态，SDF 扰动导致碰撞转移而非减少。

### 4. 障碍物配置分析

bbq_sauce → basket 的路径 (从 (0.05, -0.10) 到 (0.0, 0.26)) 必须穿过一个 **双侧障碍走廊**：
- 左侧: red_coffee_mug (-0.20, 0.20)
- 右侧: wine_bottle (0.20, 0.20)
- 走廊宽度: 仅 ~0.40m

碰撞时序分析：
- Baseline: moka_pot mean_step=54 (approach 阶段), wine_bottle/red_mug mean_step=94-99 (transport 阶段)
- A1 l005: moka_pot mean_step=73 (+19), wine_bottle mean_step=107, red_mug mean_step=99

### 5. 假设

**假设**: **中等安全 baseline 下的碰撞转移效应 (Collision Transfer in Bilateral Obstacle Corridors)**

**机制**:
1. **Ceiling effect**: Task 3 baseline 碰撞率仅 66%（vs Task 0 的 94%），baseline 轨迹已在障碍物之间找到了一条"脆弱但可行"的路径。SDF 梯度场对这条路径的扰动不是净正的。
2. **Bilateral squeeze**: basket 两侧的 wine_bottle 和 red_coffee_mug 形成对称夹击。SDF 推离一侧时必然推向另一侧，导致碰撞转移（red_coffee_mug +5 episodes），总碰撞数不降反升。
3. **Safety-success tradeoff 错配**: SDF 使 11 个 episode 成功避障但任务失败（baseline 中这个数字是 0），说明避障轨迹偏离了 bbq_sauce 的有效抓取区间。

**论文建议**:
> SDF 的避障效果与 baseline 碰撞率正相关。对于 baseline 碰撞率已经较低的任务（如 Task 3, 66%），SDF 梯度在双侧障碍走廊中会产生"碰撞转移"效应——推离一侧障碍的同时被推向对侧障碍。这一现象表明基于单点 SDF 梯度的避障策略在多障碍约束环境中存在局限性，需要考虑全局路径规划或多点 SDF 信息融合。

可以在 Discussion/Limitations 中讨论为：*"We observe that SDF-based guidance is most effective when baseline collision rates are high, where the gradient signal provides a clear improvement direction. In scenarios with bilateral obstacle corridors where the baseline trajectory already navigates a narrow safe passage, the point-wise SDF gradient can cause collision transfer rather than avoidance."*

---
