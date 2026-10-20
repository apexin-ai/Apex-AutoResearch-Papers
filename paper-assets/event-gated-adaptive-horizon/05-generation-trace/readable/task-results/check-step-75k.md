# check step 75k

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_step-75k_20260513T085906_result.json`
- **Structured JSON:** [`fc45ee11ac20e058c53c.json`](../../sessions/fc/fc45ee11ac20e058c53c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 1. 当前状态
- **exp_003**: step 96K (env step 192K), PID 27009 运行中 (1h55m)
- **baseline**: step 192K, PID 9409 运行中 (6h56m)
- Phase 3 已在 step 75K 启动，当前处于 Phase 3 运行阶段

### 2. Gate 指标演化

| Step | gate_scale | dt_mean | dt_std | entropy | entropy_ratio | dt_1_frac |
|------|-----------|---------|--------|---------|---------------|-----------|
| 5K-52K | 0.00 | 1.00 | 0.00 | 0.00 | 0.00 | 1.00 |
| 56K | 0.06 | 4.51 | 2.25 | 2.078 | 0.999 | 0.118 |
| 66K | 0.11 | 4.09 | 1.65 | 1.892 | 0.910 | 0.055 |
| 76K | 0.21 | 3.32 | 1.52 | 1.783 | 0.857 | 0.125 |
| 86K | 0.31 | 2.46 | 1.32 | 1.566 | 0.753 | 0.262 |
| 96K | 0.41 | 2.38 | 1.30 | 1.536 | 0.738 | 0.281 |

**Gate 行为分析**：
- dt_mean 从 Phase 2 初始的 4.51（接近均匀分布的 4.5）已显著下降到 2.38，说明 gate 正在学习偏好**短 dt**
- entropy 从接近最大值 2.08 下降到 1.54，gate 分布在收敛但仍保持多样性（entropy_ratio=0.74）
- dt_1_frac 从 0.055（66K 最低点）回升到 0.28，gate 越来越倾向选择 dt=1（每步决策）
- **趋势令人担忧**：gate 正在坍缩向 dt=1,2，可能退化回固定步长

### 3. Return 对比

| Step | exp_003 | baseline | ratio |
|------|---------|----------|-------|
| 5K | 31.0 | 31.8 | 0.97 |
| 15K | 153.9 | 206.6 | 0.74 |
| 25K | 254.2 | 395.3 | 0.64 |
| 35K | 290.8 | 388.5 | 0.75 |
| 45K | 443.0 | 513.8 | 0.86 |
| 56K | 416.4 | ~625 | ~0.67 |
| 66K | 210.7 | ~616 | ~0.34 |
| 76K | 387.3 | ~596 | 0.65 |
| 86K | 299.2 | ~714 | 0.42 |
| 96K | 317.8 | ~871 | 0.37 |

Return 在 Phase 2 激活后出现大幅振荡（66K 跌到 210），至 96K 仍未恢复，与 baseline 差距持续扩大。

### 4. MVP 评估 (3/4 PASS)

| Criterion | Status | Detail |
|-----------|--------|--------|
| C1: Return >= 80% baseline | **FAIL** | ratio=0.37 (需 >=0.80) |
| C2: Gate entropy > 0.3 nats | PASS | 1.54 nats |
| C3: H_eff > 1.2x H_nominal | PASS | 2.38x |
| C4: dt temporal structure | PASS | std=1.30, autocorr=0.64 |

Gate 学习指标（C2-C4）全部通过，但 **return 严重落后于 baseline**（仅 37%）。gate_scale 线性递增到 0.41 时对 policy 冲击过大，return 无法恢复。

图表已保存到 `eval_plots/`。

---
