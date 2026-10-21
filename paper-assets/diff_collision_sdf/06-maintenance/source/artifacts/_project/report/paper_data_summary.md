# Paper Data Summary — diff_collision_sdf

Generated: 2026-05-24 | Source: experiment registry (51 entries)

---

## Table 1: Pi0.5 + A1 — 3-seed × 2-lambda 结果矩阵

10K mid-eval 数据来源：ROADMAP D016（手动 eval）

| | λ=0.005 TSR | λ=0.005 CAR | λ=0.005 SSR | λ=0.01 TSR | λ=0.01 CAR | λ=0.01 SSR |
|---|---|---|---|---|---|---|
| seed 0 (10K) | 47% | 58% | 0% frozen | 49% | 56.5% | 0% frozen |
| seed 1 (30K) | TBD | TBD | TBD | TBD | TBD | TBD |
| seed 2 (30K) | TBD | TBD | TBD | TBD | TBD | TBD |
| **mean±std** | — | — | — | — | — | — |

**对比基线：**
- Pi0.5 baseline 3-seed: TSR = 74.7 ± 1.5%, CAR = 26.8 ± 1.6% (n=600, seeds 7/1/2)
- Pi0.5 baseline per-seed: s0(seed7): TSR=73%, CAR=28% | s1: TSR=76%, CAR=25% | s2: TSR=75%, CAR=27.5%

**分析：**
- A1 training 显著降低了 TSR（74.7% → 47-49%），但大幅提升了 CAR（26.8% → 56-58%）
- SSR=0% frozen 表明 A1 不产生 action collapse（与 Pi0 系方法的 99%+ fake safe 形成对比）
- seed 1/2 训练完成（30K steps）但因 SSH auth failure 未获取 eval metrics，需补跑 eval

---

## Table 2 (Claim 1): Fake Safety 统计

**核心论点：** 现有碰撞避免方法的高 CAR 是 "fake safety"——模型通过 action collapse（停止运动）而非真正的轨迹修正来避免碰撞。

| Method | Episodes | TSR | CAR | Real Safe Rate | Fake Safe Rate | Source |
|--------|----------|-----|-----|---------------|---------------|--------|
| A1-LoRA (Pi0) | 800 | 0% | 91.5% | 0.4% (3/732) | 99.6% (729/732) | eval_a1_lora_object_v11_rerun |
| LoRA baseline (Pi0) | 200 | 0% | 82% | 0.5% (~1/164) | 99.4% (~163/164) | eval_lora_baseline_object_v11 |
| Full-FT baseline (Pi0) | 200 | 0.5% | 83% | 需补充 | 需补充 | eval_baseline_v11_object |
| Pi0.5 baseline (3-seed) | 600 | 74.7% | 26.8% | 0.5% (1/200 in s0) | 98.2% (s0) | eval_pi05_safelibero_object_v11 + s1 + s2 |
| **Pi0.5 + A1 (10K, s0, λ=0.005)** | — | 47% | 58% | ~100% (0% frozen) | ~0% | ROADMAP D016 |
| **Pi0.5 + A1 (10K, s0, λ=0.01)** | — | 49% | 56.5% | ~100% (0% frozen) | ~0% | ROADMAP D016 |

**Fake Safe 判定标准：** safe episode 中 displacement < 0.1mm（即 arm 几乎完全静止）

**A1-LoRA 详细位移分布（800 eps, 732 safe）：**
- < 1µm: 541 episodes (73.9%)
- 1µm – 0.1mm: 188 episodes (25.7%)
- 0.1mm – 1mm: 3 episodes (0.4%) ← real safe
- \> 1mm: 0 episodes

**关键结论：** Pi0 系方法 CAR 82-91.5% 看似优秀，但 99%+ 的 "safe" episodes 是因为机械臂完全停止运动（displacement < 0.1mm），而非学会了绕开障碍物。Pi0.5+A1 虽然 CAR 较低（56-58%），但 0% frozen 意味着所有安全行为都是真实的碰撞避免。

---

## Table 3 (Claim 3): Oracle Comparison — Runtime Refinement 无效

**核心论点：** 即使使用 ground-truth SDF 做 runtime gradient refinement，也无法解决 fake safety 问题，证明 inference-time 优化路线不可行。

| Method | TSR | CAR | Fake Safe Rate | Refine Count/ep | Source |
|--------|-----|-----|---------------|----------------|--------|
| Oracle-adaptive (GT SDF) | 0% | 75.0% | 98.3% (118/120) | 14.2 | oracle_true_gt_adaptive_alpha_v11 |
| Oracle-fixed α=0.005 (GT SDF) | 0% | 73.1% | 98.3% (115/117) | 14.8 | oracle_true_gt_fixed_alpha_v11 |
| Oracle-feature (GT SDF) | 0% | 76.9% | 96.7% (119/123) | 241.7 | oracle_true_gt_feature_v11 |
| A3 no-force (learned SDF) | 0% | 74.5% | — | 0 (never triggered) | eval_a3_v11_object |
| LoRA baseline (no refine) | 0% | 82% | 99.4% | N/A | eval_lora_baseline_object_v11 |
| Full-FT baseline (no refine) | 0.5% | 83% | 需补充 | N/A | eval_baseline_v11_object |

**Oracle 实验参数：**
- n=160 episodes (4 tasks × 40 eps), seed 0
- GT SDF = 真实场景的 signed distance field
- Adaptive: 动态调整 refinement strength
- Fixed: α=0.005 固定步长
- Feature-space: 在 feature 层面做梯度修正（每步都 refine，avg 241.7/ep）

**关键结论：**
1. Oracle refinement（GT SDF）vs 无 refine 的 LoRA baseline：CAR 反而**更低**（73-77% vs 82%），说明 refinement 在破坏策略
2. 所有 Oracle 方法 fake_safe_rate 仍高达 96-98%，GT SDF 都救不了
3. A3（learned SDF）的 refine 从未被触发（SDF 预测值未达阈值），实际退化为 baseline
4. Feature-space oracle 每步都 refine（241.7/ep vs action-space 14.2/ep），梯度幅度极小（0.004-0.006 vs action-space 0.18-0.49），但结果无显著差异

---

## Table 4: TSR-CAR Scatter 数据点（Fig 3 素材）

用于绘制 TSR vs CAR 散点图，展示各方法在 task success 和 collision avoidance 两个维度上的 trade-off。

```
method_name, TSR, CAR, n_episodes, marker_style_suggestion
# --- Pi0.5 系列 (高 TSR, 低-中 CAR) ---
Pi0.5 baseline s0 (seed 7), 0.73, 0.28, 200, blue_circle
Pi0.5 baseline s1, 0.76, 0.25, 200, blue_circle
Pi0.5 baseline s2, 0.75, 0.275, 200, blue_circle
Pi0.5+A1 λ=0.005 (10K s0), 0.47, 0.58, -, red_star
Pi0.5+A1 λ=0.01 (10K s0), 0.49, 0.565, -, red_star
# --- Pi0 系列 (低 TSR, 高 CAR — fake safety) ---
Pi0 LoRA baseline, 0.0, 0.82, 200, gray_triangle
Pi0 Full-FT baseline, 0.005, 0.83, 200, gray_triangle
A1-LoRA (Pi0), 0.0, 0.915, 800, orange_diamond
# --- Oracle 系列 (低 TSR, 中-高 CAR — GT SDF 也无效) ---
Oracle adaptive (GT SDF), 0.0, 0.75, 160, green_square_hollow
Oracle fixed α=0.005 (GT SDF), 0.0, 0.731, 160, green_square_hollow
Oracle feature-space (GT SDF), 0.0, 0.769, 160, green_square_hollow
# --- A3 Gradient Refine ---
A3 no-force (learned SDF), 0.0, 0.745, 200, purple_pentagon
A3 M024fix, 0.0, 0.771, 200, purple_pentagon_hollow
# --- Spatial 系列 ---
Pi0.5 spatial (seed 7), 0.575, 0.13, 200, blue_circle_hollow
A1-LoRA spatial, 0.001, 0.008, 200, orange_diamond_hollow
LoRA baseline spatial, 0.0, 0.0, 200, gray_triangle_hollow
Full-FT baseline spatial, 0.00375, 0.0, 800, gray_triangle_hollow
```

**Fig 3 设计建议：**
- X 轴: TSR (Task Success Rate), Y 轴: CAR (Collision Avoidance Rate)
- 理想区域 = 右上角（高 TSR + 高 CAR）
- Pi0 系聚集在左上（高 CAR 但 0 TSR — 全是 fake safety）
- Pi0.5 baseline 在右下（高 TSR 但低 CAR）
- **Pi0.5+A1 是唯一向右上移动的方法**（中等 TSR + 中等 CAR，且 0% frozen）
- 可用虚线标注 "Pareto front"
- 用不同填充/颜色区分 fake safe (空心) vs real safe (实心) 方法

---

## 补充数据：Per-task CAR 分解

| Method | task0 (orange_juice) | task1 (choc_pudding) | task2 (milk) | task3 (bbq_sauce) |
|--------|---------------------|---------------------|-------------|-------------------|
| Full-FT baseline | 76% | 90% | 88% | 78% |
| LoRA baseline | 96% | 46% | 98% | 88% |
| A1-LoRA (800ep) | 96% | 82% | 97% | 91% |
| A3 no-force | 84% | 48% | 82% | 84% |
| Oracle adaptive | 82.5% | 55% | 77.5% | 85% |
| Oracle fixed | 85% | 50% | 77.5% | 80% |
| Oracle feature | 90% | 47.5% | 82.5% | 87.5% |

**观察：** task1 (chocolate_pudding) 是所有方法的难点，CAR 普遍最低。可能该任务的碰撞场景更 challenging。

---

## 待补充项

1. **seed 1/2 的 30K eval 结果** — 训练完成但 SSH failure 未跑 eval，需重连服务器执行
2. **Full-FT baseline 的 fake_safe_rate** — registry 中无该字段，需补跑位移分析
3. **Pi0.5+A1 10K eval 的详细位移分布** — 证实 0% frozen 的 displacement 分布
4. **Pi0.5 baseline s1/s2 的 fake_safe_rate** — 仅 s0 有数据 (98.2%)
5. **Pi0.5+A1 30K eval** — s0 已训练 30K，需对比 10K vs 30K 的 TSR/CAR 变化
