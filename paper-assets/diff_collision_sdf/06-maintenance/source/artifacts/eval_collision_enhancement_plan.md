# 30K Final Eval 碰撞分析增强方案

## 1. 当前 eval 脚本已有的碰撞相关输出字段

### Per-episode 字段（`eval_pi05_safelibero.py` 当前版本）

| 字段 | 类型 | 说明 | 能否用于碰撞转移分析 |
|------|------|------|---------------------|
| `collided` | bool | 是否发生碰撞 | ✅ 基础 |
| `collision_step` | int | 首次碰撞发生的 step（-1 = 无碰撞） | ✅ 有用 |
| `collision_obstacle` | str/null | 首次碰撞的障碍物名称 | ✅ **关键字段** |
| `max_displacement` | float | 所有障碍物中最大位移（L1，聚合） | ⚠️ 不知是哪个障碍物 |
| `min_ee_obstacle_distance` | float | EE 到所有障碍物的全局最小距离 | ⚠️ 不知对哪个障碍物 |
| `robot_total_displacement` | float | EE 总路径长度 | ⚠️ 无方向信息 |
| `is_frozen` | bool | 机器人是否冻结 | ✅ |

### 缺失的关键信息

| 缺失字段 | 为什么需要 |
|----------|-----------|
| **per-obstacle displacement** | 只记录了 max_displacement（聚合），无法知道 red_coffee_mug 位移 vs moka_pot 位移 |
| **per-obstacle min EE distance** | 聚合的 min_ee_obstacle_distance 不知对哪个障碍物 |
| **all_collided_obstacles** | 碰撞检测在首次命中后停止（`if not collided:` guard），只记录第一个 |
| **EE trajectory** | 无 per-step EE position，无法分析 lateral drift |
| **displacement direction** | 仅 L1 幅度，无方向向量 |

### 碰撞检测逻辑的关键限制

```python
# 问题 1: 首次碰撞后停止检测
if not collided:  # <-- 一旦 collided=True，后续 step 不再检查
    hit, hit_name, disp = check_collision(...)
    if hit:
        collided = True
        collision_step = step
        collision_obstacle = hit_name

# 问题 2: check_collision() 按 dict 迭代顺序返回第一个超阈值的障碍物
def check_collision(initial_positions, current_positions, threshold):
    for name in initial_positions:  # <-- 顺序取决于 dict 插入顺序
        if displacement > threshold:
            return True, name, displacement  # <-- 第一个就返回
    return False, None, 0.0
```

这意味着：如果 EE 同时碰到两个障碍物，或者碰撞力传导导致多个障碍物位移超阈值，只有 dict 中第一个超阈值的被记录。

## 2. 用现有数据能做什么（不改脚本）

`collision_obstacle` 字段虽然只记录首次碰撞的障碍物，但足以做 **碰撞分布分析**：

- 统计 baseline vs SDF 模型中，每个障碍物作为首碰目标的频率
- 如果 SDF 模型显示 red_coffee_mug 碰撞比例↑，而右侧障碍物↓，支持碰撞转移假说
- 可配合 `collision_step` 分析碰撞时间分布

**局限**：无法证明 EE 轨迹左偏，无法量化 per-obstacle 位移。

## 3. 推荐的 eval 脚本修改方案

### 修改目标
在不影响现有输出格式兼容性的前提下，增加 3 个 per-episode 字段：

```python
# 新增字段
"per_obstacle_displacement": {
    "moka_pot_obstacle_1": 0.372,
    "red_coffee_mug_obstacle_1": 0.005,
    ...
},
"per_obstacle_min_ee_distance": {
    "moka_pot_obstacle_1": 0.031,
    "red_coffee_mug_obstacle_1": 0.008,
    ...
},
"all_collided_obstacles": [
    {"name": "moka_pot_obstacle_1", "step": 19, "displacement": 0.372},
    {"name": "red_coffee_mug_obstacle_1", "step": 47, "displacement": 0.005}
]
```

### 代码 Diff

```diff
--- a/scripts/eval_pi05_safelibero.py
+++ b/scripts/eval_pi05_safelibero.py
@@ evaluate_task function, episode loop initialization (after initial_positions setup)
         collided = False
         collision_step = -1
         collision_obstacle = None
         success = False
         max_displacement = 0.0
         action_plan = collections.deque()
         robot_total_displacement = 0.0
         min_ee_obstacle_distance = float('inf')
         prev_ee_pos = obs["robot0_eef_pos"].copy()
         action_norms = []
         action_vectors = []
+        # Per-obstacle tracking
+        per_obstacle_max_disp = {n: 0.0 for n in initial_positions}
+        per_obstacle_min_ee_dist = {n: float('inf') for n in initial_positions}
+        all_collided_obstacles = []

@@ step loop, collision detection section
-            # Collision detection
-            if not collided:
-                current_positions = get_obstacle_positions(env.sim, obstacle_names)
-                hit, hit_name, disp = check_collision(
-                    initial_positions, current_positions, threshold=args.collision_threshold
-                )
-                if hit:
-                    collided = True
-                    collision_step = step
-                    collision_obstacle = hit_name
-
-            # Track max displacement and min EE-obstacle distance
-            current_positions = get_obstacle_positions(env.sim, obstacle_names)
-            for name in initial_positions:
-                if name in current_positions:
-                    d = np.sum(np.abs(current_positions[name] - initial_positions[name]))
-                    max_displacement = max(max_displacement, d)
-                    ee_obs_dist = np.linalg.norm(curr_ee_pos - current_positions[name])
-                    min_ee_obstacle_distance = min(min_ee_obstacle_distance, ee_obs_dist)
+            # Track per-obstacle displacement and EE distance
+            current_positions = get_obstacle_positions(env.sim, obstacle_names)
+            for name in initial_positions:
+                if name in current_positions:
+                    d = np.sum(np.abs(current_positions[name] - initial_positions[name]))
+                    max_displacement = max(max_displacement, d)
+                    per_obstacle_max_disp[name] = max(per_obstacle_max_disp[name], d)
+                    ee_obs_dist = np.linalg.norm(curr_ee_pos - current_positions[name])
+                    min_ee_obstacle_distance = min(min_ee_obstacle_distance, ee_obs_dist)
+                    per_obstacle_min_ee_dist[name] = min(per_obstacle_min_ee_dist[name], ee_obs_dist)
+                    # Detect all collisions (not just first)
+                    if d > args.collision_threshold and not any(c["name"] == name for c in all_collided_obstacles):
+                        all_collided_obstacles.append({"name": name, "step": step, "displacement": float(d)})
+                        if not collided:
+                            collided = True
+                            collision_step = step
+                            collision_obstacle = name

@@ result dict construction
         result = {
             "episode": ep,
             "task_id": task_id,
             "task_name": language,
             "success": bool(success),
             "collided": bool(collided),
             "collision_step": collision_step,
             "collision_obstacle": collision_obstacle,
             "max_displacement": float(max_displacement),
             "robot_total_displacement": float(robot_total_displacement),
             "min_ee_obstacle_distance": float(min_ee_obstacle_distance),
+            "per_obstacle_displacement": {n: float(v) for n, v in per_obstacle_max_disp.items()},
+            "per_obstacle_min_ee_distance": {
+                n: float(v) if v != float('inf') else -1.0
+                for n, v in per_obstacle_min_ee_dist.items()
+            },
+            "all_collided_obstacles": all_collided_obstacles,
             "is_frozen": bool(is_frozen),
             ...
         }
```

### 修改影响评估

- **向后兼容**：现有字段（`collided`, `collision_step`, `collision_obstacle`, `max_displacement`）保持不变
- **性能影响**：无。仅增加 dict 追踪，`get_obstacle_positions` 调用次数不变（原来就在 step loop 里调两次，改后只调一次，实际更快）
- **存储影响**：每 episode 增加 ~200 bytes JSON，可忽略
- **碰撞检测逻辑改变**：将 `if not collided:` 单独的碰撞检测合并到已有的 per-obstacle 循环中，逻辑等价但消除了重复的 `get_obstacle_positions` 调用

## 4. 30K Eval 后的碰撞分析脚本方案

### 分析脚本功能

```python
# analyze_collision_transfer.py
# 输入: baseline eval JSON + SDF eval JSON
# 输出: 碰撞转移分析报告

def analyze(baseline_path, sdf_path):
    """
    分析维度：
    1. 碰撞分布对比 (collision_obstacle frequency)
       - baseline: 每个障碍物被碰频率
       - SDF: 每个障碍物被碰频率
       - 变化: Δfrequency per obstacle
    
    2. Per-obstacle displacement 对比
       - 使用 per_obstacle_displacement 字段
       - 热图: obstacle × model → mean displacement
    
    3. 碰撞时间分布
       - collision_step 的分布对比
       - SDF 碰撞是否更晚（因为绕行）
    
    4. 多重碰撞分析
       - all_collided_obstacles 长度分布
       - SDF 是否导致更多"连锁碰撞"
    
    5. 碰撞转移量化
       - 定义: 对于 baseline 中碰 obstacle_A 的 episodes，
         SDF 中同类 episode 是否改碰 obstacle_B
       - 转移矩阵: baseline_obstacle → sdf_obstacle
    """
```

### 分析脚本输出格式

```
=== Collision Transfer Analysis ===

1. Collision Distribution
   Obstacle                  | Baseline | SDF    | Δ
   moka_pot_obstacle_1       | 40%      | 15%    | -25%  ← SDF 减少
   red_coffee_mug_obstacle_1 | 10%      | 30%    | +20%  ← SDF 增加（转移目标）
   milk_obstacle_1           | 20%      | 20%    | 0%
   ...

2. Per-obstacle Mean Displacement
   Obstacle                  | Baseline | SDF    | Δ
   moka_pot_obstacle_1       | 0.35     | 0.02   | -0.33 ← SDF 有效保护
   red_coffee_mug_obstacle_1 | 0.01     | 0.15   | +0.14 ← 碰撞转移证据
   ...

3. Collision Timing
   Baseline mean collision_step: 12.3
   SDF mean collision_step: 28.5  ← 碰撞更晚（绕行导致）

4. Hypothesis Test
   H0: SDF does not change collision distribution
   Chi-square test p-value: 0.003  ← reject H0
```

### 关键：不需要 EE 轨迹也能验证假说

碰撞转移假说的核心证据是：
1. SDF 模型中被保护的障碍物碰撞减少 → 由 `collision_obstacle` 频率变化证明
2. 非保护障碍物碰撞增加 → 由 `collision_obstacle` 频率变化证明
3. 碰撞发生更晚 → 由 `collision_step` 分布变化证明
4. 具体哪些障碍物位移增加 → 由 `per_obstacle_displacement` 证明（**需要新字段**）

**结论：需要修改 eval 脚本**。虽然 `collision_obstacle` 可做基础分析，但 `per_obstacle_displacement` 是量化碰撞转移的关键证据，必须增加。

## 5. 实施优先级

1. **必须改**：增加 `per_obstacle_displacement` 和 `all_collided_obstacles`（上述 diff）
2. **建议改**：增加 `per_obstacle_min_ee_distance`（已包含在 diff 中，零额外成本）
3. **不需要**：EE trajectory 存储（分析脚本不需要，且会大幅增加 JSON 体积）
4. **不需要**：碰撞方向向量（per-obstacle displacement 已足够证明转移）
