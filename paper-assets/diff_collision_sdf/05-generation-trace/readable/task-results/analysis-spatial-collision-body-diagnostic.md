# analysis spatial collision body diagnostic

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_spatial_collision_body_diagnostic_20260522T185900_result.json`
- **Structured JSON:** [`6f6ab5c6c57a278df652.json`](../../sessions/6f/6f6ab5c6c57a278df652.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有关键数据已收集完毕。下面是完整诊断报告。

---

## 诊断结果

### 1. 碰撞检测范围：**不区分 EE vs arm body，检测 obstacle 位移**

**代码证据**：`scripts/eval_safelibero.py`

碰撞检测是 **obstacle displacement-based**，不是 contact-based：

```python
# line 400-423: 记录 obstacle 初始 body_xpos
def get_obstacle_positions(sim, obstacle_names):
    for name in obstacle_names:
        body_id = sim.model.body_name2id(name + "_main")
        pos = sim.data.body_xpos[body_id].copy()

# line 426-435: 检查 obstacle 是否移动
def check_collision(initial_positions, current_positions, threshold=0.001):
    for name in initial_positions:
        displacement = np.sum(np.abs(current_positions[name] - initial_positions[name]))
        if displacement > threshold:
            return True, name, displacement
```

**结论：任何 robot 部位（EE、gripper、forearm、elbow、shoulder）推动 obstacle 都会触发碰撞。代码不记录碰撞来自哪个 robot link。**

### 2. Threshold 0.001m 含义：**obstacle 位移的 L1 距离**

- `COLLISION_THRESHOLD = 0.001` (line 89)
- 计算：`np.sum(np.abs(current_pos - initial_pos))`，即 xyz 三轴绝对值之和
- 含义：obstacle 从初始位置被推动超过 1mm (L1) 就算碰撞
- **不是** penetration depth，**不是** min distance，是 obstacle 实际位移量

### 3. 碰撞 Link 统计：**日志不记录碰撞 link，但间接证据强烈指向 arm body**

日志只记录 `collision_obstacle`（被撞的 obstacle），不记录 robot 的哪个 link。

**关键间接证据**：

| 指标 | Object Suite | Spatial Suite |
|------|-------------|---------------|
| A1 CAR | 80-96% | 0-1.5% |
| LoRA baseline CAR | 46-98% | 0% |
| Fullft baseline CAR | 76-90% | 0% |
| Avg collision_step | — | **4-20 步**（大部分 <20） |

Spatial task 0 (lora baseline, 50ep) 碰撞步骤分布：
- moka_pot: avg ~25步
- **milk: avg ~9步**（最早）
- wine_bottle: avg ~25步
- red_coffee_mug: avg ~70步（最晚）
- **yellow_book: avg ~15步**

**碰撞在 step 4-20 发生，此时 EE 刚开始移动，几乎没有到达任何目标附近。这强烈暗示碰撞来自 arm body 在初始运动阶段扫过 obstacle。**

### 4. Spatial Bowl 布局：**6 个 obstacle 环绕 workspace**

从 BDDL 文件，obstacle 在 table 坐标系中的布局：

```
              x=-0.3      x=-0.1      x=0.1       x=0.3      x=0.5
y=-0.3  ┌──────────────┬─────────────┬──────────────┬──────────────┐
        │ yellow_book  │             │  milk        │  moka_pot    │
y=-0.1  ├──────────────┤             ├──────────────┤              │
        │              │  bowl(-0.05,│              │              │
y=0.1   │              │  0.20)      │              │              │
        │              │  plate(0.06,│              │              │
y=0.1   ├──────────────┤  0.20)      ├──────────────┤              │
        │  red_mug     │             │ wine_bottle  │ storage_box  │
y=0.3   └──────────────┴─────────────┴──────────────┴──────────────┘
```

- 6 个 obstacle 形成**包围圈**，距 workspace 中心 10-50cm
- moka_pot 碰撞体已 **放大 1.6 倍**（XML 注释 "已放大 1.6 倍"），主碰撞 box 尺寸 8cm×8cm×21cm
- Robot 到达 bowl 的路径**必须穿过 obstacle 密集区域**
- Spatial task 的 bowl 位置变化大（ramekin 旁、stove 上、cabinet 上），arm 需要大范围摆动

### 5. 结论：**EE-only SDF 在 spatial_bowl 上天然不足**

| 证据 | 含义 |
|------|------|
| 碰撞检测不区分 link | EE-only SDF 即使完美避开 EE 碰撞，arm body 碰撞仍然无法避免 |
| 碰撞在 step 4-20 发生 | EE 尚未到达目标，是 arm body 扫到了 obstacle |
| Object suite CAR 80-96% vs Spatial CAR 0% | 同一 obstacle set，不同 task layout → arm trajectory 不同 |
| 6 obstacle 包围 workspace | arm 大范围运动必经 obstacle 区域 |
| Obstacle 碰撞体放大 1.6 倍 | 碰撞区域比视觉大得多，arm body 更容易触碰 |

**项目 scope 影响**：EE-only SDF 方法在 spatial 场景中**结构性失效**。要解决 spatial 场景，需要 whole-arm collision avoidance（全臂碰撞检测+回避），而非仅 EE。这不是调参能解决的问题。

---
