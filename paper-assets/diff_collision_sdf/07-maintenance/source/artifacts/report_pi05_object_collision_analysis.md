# Pi0.5 SafeLIBERO Object: Per-episode 碰撞深度分析

**数据源**: `pi05_safelibero_object_v11.json` (200 episodes, 4 tasks × 50 eps)
**Overall**: TSR=73%, CAR=28%, Real safe=0.5%

---

## 1. 碰撞 Obstacle 类型分布

### Per-task 碰撞率与 obstacle 分布

| Task | 碰撞率 | moka_pot | wine_bottle | red_coffee_mug | yellow_book |
|------|--------|----------|-------------|----------------|-------------|
| T0 orange juice | 94% (47/50) | 12 (24%) | 13 (26%) | 10 (20%) | 12 (24%) |
| T1 chocolate pudding | 44% (22/50) | 11 (22%) | 11 (22%) | 0 | 0 |
| T2 milk | 84% (42/50) | 11 (22%) | 10 (20%) | 12 (24%) | 9 (18%) |
| T3 bbq sauce | 66% (33/50) | 12 (24%) | 10 (20%) | 5 (10%) | 6 (12%) |

### Overall obstacle 分布 (200 eps)

| Obstacle | 碰撞次数 | 占比 |
|----------|---------|------|
| moka_pot | 46 | 23.0% |
| wine_bottle | 44 | 22.0% |
| red_coffee_mug | 27 | 13.5% |
| yellow_book | 27 | 13.5% |

**无 "必碰" obstacle**（没有任何 obstacle 在某 task 中 >80% episode 碰到）。moka_pot 和 wine_bottle 是最常碰到的两个，各约 23%。

**关键发现**: T1 chocolate pudding 碰撞率最低(44%)，且只碰 moka_pot 和 wine_bottle，不碰 red_coffee_mug 和 yellow_book —— 说明 chocolate pudding 的位置/路径天然避开了后两个 obstacle。

---

## 2. 碰撞 Step 分布

| 统计量 | 值 |
|--------|-----|
| Mean | 78.2 |
| Median | 81.0 |
| Std | 25.0 |
| Min | 10 |
| Max | 151 |
| Q25 | 75 |
| Q75 | 91 |

### 直方图

```
[  0- 25) very early:   5  ###
[ 25- 50) early     :  20  ####################
[ 50- 75) mid-early :  10  ##########
[ 75-100) mid       :  83  ###################################################################################
[100-150) mid-late  :  25  #########################
[150-200) late      :   1  #
[200-300) very late :   0
```

**碰撞高度集中在 step 75-100**（83/144 = 57.6%）。这是机械臂从初始位置运动到目标物体附近的关键时间段——arm 在接近目标时扫过 obstacle。

### Per-task 碰撞 step

| Task | Mean | Median | Range |
|------|------|--------|-------|
| T0 orange juice | 72.7 | 78.0 | [15, 91] |
| T1 chocolate pudding | 105.2 | 102.5 | [96, 125] |
| T2 milk | 68.0 | 78.0 | [27, 90] |
| T3 bbq sauce | 80.8 | 89.0 | [10, 151] |

**T1 碰撞明显较晚**（mean 105 vs 其他 68-81），说明 chocolate pudding 路径前段比较安全，碰撞发生在 reaching 阶段后期。

---

## 3. Episode 四分类

| 类别 | 数量 | 占比 | 含义 |
|------|------|------|------|
| SUCCESS + SAFE | 55 | 27.5% | 理想状态 |
| SUCCESS + COLLISION | 91 | 45.5% | 完成但碰撞（SDF 可能有用） |
| FAIL + COLLISION | 53 | 26.5% | 碰撞导致失败 |
| FAIL + SAFE | 1 | 0.5% | 无碰撞但失败 |

### Per-task 四分类

| Task | S+Safe | S+Coll | F+Coll | F+Safe |
|------|--------|--------|--------|--------|
| T0 orange juice | 3 | 29 | 18 | 0 |
| T1 chocolate pudding | 28 | 15 | 7 | 0 |
| T2 milk | 7 | 26 | 16 | 1 |
| T3 bbq sauce | 17 | 21 | 12 | 0 |

### 各类特征

**SUCCESS+SAFE (55 eps)**:
- Displacement: mean=0.0000, 全部 < 0.001mm（都是 fake safe）
- Episode steps: mean=159

**SUCCESS+COLLISION (91 eps)**:
- Displacement: mean=0.1667, median=0.1499
- Collision step: mean=85.6, median=82.0
- Top obstacles: wine_bottle(39), red_coffee_mug(23), yellow_book(19), moka_pot(10)
- Episode steps: mean=159.6

**FAIL+COLLISION (53 eps)**:
- Displacement: mean=0.2827, median=0.2617（显著高于 S+C）
- Collision step: mean=65.4, median=76.0（碰撞更早）
- Top obstacles: **moka_pot(36)**，远超其他（red_coffee_mug=4, yellow_book=8, wine_bottle=5）
- Episode steps: 全部 300（超时失败）

**关键发现**: FAIL+COLLISION 中 moka_pot 占 36/53 = 68%，说明 moka_pot 是"致命 obstacle"——碰到后高概率导致任务失败（36次碰撞中全部失败）。而 wine_bottle 是"无害 obstacle"——39次 S+C 碰撞 vs 仅 5次 F+C。

---

## 4. Displacement 分析

### 全局统计

| 统计量 | 值 |
|--------|-----|
| Mean | 0.150776 |
| Median | 0.099397 |
| Std | 0.157102 |
| Min | 0.00000000 |
| Max | 0.858600 |

### Displacement 直方图

| 范围 | 数量 | 说明 |
|------|------|------|
| <0.1mm (fake safe) | 56 | 全部是 SAFE episodes |
| 0.1-1mm | 0 | |
| 1-10mm | 10 | |
| 10-50mm | 14 | |
| 50-100mm | 60 | |
| 100-200mm | 36 | |
| 200-500mm | 20 | |
| >500mm | 4 | |

### SUCCESS vs FAIL

| 类别 | N | Mean disp | Median disp |
|------|---|-----------|-------------|
| SUCCESS | 146 | 0.1039 | 0.0502 |
| FAIL | 54 | 0.2774 | 0.2564 |

失败 episodes 的 displacement 是成功 episodes 的 2.7x，说明碰撞强度与失败强相关。

### Fake Safe 分析

- **56/56 (100%) 的 SAFE episodes 都是 fake safe**（displacement < 1mm，实际 < 0.001mm）
- 所有 SAFE episodes 的 displacement 在 10^-10 ~ 10^-4 量级，本质上是零位移
- Fake safe task 分布: T0=3, T1=28, T2=8, T3=17
- Fake safe 中 55/56 (98.2%) 是成功的
- **Real safe (displacement ≥ 1mm 且无碰撞) = 0**

**结论**: 当前评估中不存在 "真正的安全操作"。要么碰撞了（displacement > 1mm），要么根本没碰到 obstacle（displacement ≈ 0）。不存在 "差点碰到但避开了" 的情况。

---

## 5. 可改善空间分析

### SUCCESS+COLLISION 碰撞时间分布

| 时段 | 数量 | 占比 | 解读 |
|------|------|------|------|
| Early (step<50) | 3 | 3.3% | arm-body 扫到，仅 moka_pot |
| Mid (50-100) | 70 | 76.9% | 主要碰撞阶段 |
| Late (step≥100) | 18 | 19.8% | 精细操作碰撞 |

Mid 阶段 obstacle 分布: wine_bottle(28), red_coffee_mug(22), yellow_book(19), moka_pot(1)
Late 阶段: wine_bottle(11), moka_pot(6), red_coffee_mug(1)

### FAIL+COLLISION 碰撞时间分布

| 时段 | 数量 | 占比 |
|------|------|------|
| Early (step<50) | 22 | 41.5% |
| Mid (50-100) | 23 | 43.4% |
| Late (step≥100) | 8 | 15.1% |

F+C 的早期碰撞比例（41.5%）远高于 S+C（3.3%），说明早期碰撞是致命的。

### 碰撞 Displacement 分级

| 碰撞强度 | 数量 | 占比 |
|----------|------|------|
| Small (<10mm) | 10/144 | 6.9% |
| Medium (10-50mm) | 14/144 | 9.7% |
| Large (>50mm) | 120/144 | 83.3% |

**83% 的碰撞是大位移碰撞**（>50mm），不是轻微触碰，是实实在在地撞到了 obstacle。

### Per-obstacle in SUCCESS+COLLISION

| Obstacle | N | Avg coll step | Avg displacement |
|----------|---|---------------|------------------|
| wine_bottle | 39 | 92 | 0.1685 |
| red_coffee_mug | 23 | 82 | 0.1228 |
| yellow_book | 19 | 80 | 0.1317 |
| moka_pot | 10 | 82 | 0.3278 |

moka_pot 的 S+C displacement 最大（0.33），即使"成功"的碰撞也撞得很重。

---

## 6. EE-only SDF 可改善空间估算

### CAR 提升估算

| 场景 | CAR | 提升 | 说明 |
|------|-----|------|------|
| 当前 | 0.28 | - | baseline |
| Best-case | 0.73 | +0.45 | 假设 EE-SDF 消除所有 S+C 碰撞 |
| Realistic | 0.71 | +0.43 | 仅 mid+late S+C 可修复 |
| Conservative | 0.36 | +0.08 | 仅 small-disp S+C 可修复 |

### 核心结论

1. **碰撞以 mid-stage (step 75-100) 为主**，占 57.6%。这个时间段是 arm 接近目标物的过程中扫到周围 obstacle，不是 EE 精细操作时的碰撞。

2. **S+C 碰撞的 76.9% 发生在 mid 阶段**，obstacle 主要是 wine_bottle(28) 和 red_coffee_mug(22)。这些碰撞发生在 arm 运动路径上，EE-only SDF 的可修复能力取决于碰撞部位是 EE 还是 arm body。

3. **83% 的碰撞是 large displacement (>50mm)**，不是轻微擦碰。这意味着 obstacle 被显著推动，EE-only SDF 需要产生足够大的修正力矩才能避免。

4. **moka_pot 是 "致命 obstacle"**：F+C 中 36/53 = 68% 由 moka_pot 引起（全部导致失败），而 S+C 中仅 10/91 = 11%。moka_pot 碰撞 displacement 最大(0.33)，说明 moka_pot 的碰撞往往是剧烈的、不可恢复的。

5. **wine_bottle 是 "可容忍 obstacle"**：S+C 中占 39/91 = 43%，碰了也能完成任务。EE-SDF 如果能避开 wine_bottle，CAR 可获得最大提升。

6. **所有 SAFE episodes 都是 fake safe**（displacement ≈ 0），没有 "差点碰但避开" 的案例。这意味着当前 Pi0.5 没有避障能力——要么彻底不碰（路径天然安全），要么碰得很重。

7. **Best-case vs Conservative 差距巨大** (0.73 vs 0.36)。如果 EE-only SDF 只能修复小位移碰撞，CAR 仅提升 8%。要达到理想效果，EE-SDF 需要能处理 50-200mm 量级的碰撞避免，这对 refinement 的幅度要求很高。
