# analysis plan002 additive b01 s42

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan002-additive-b01-s42_20260514T063941_result.json`
- **Structured JSON:** [`c152d27dbc9a49a08271.json`](../../sessions/c1/c152d27dbc9a49a08271.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据齐全。

## plan002-additive-b01-s42 分析报告

### 训练指标
- Total steps: 500 (完成，EXIT_CODE=0)
- 训练时长: 63 min
- Windowed PR / ISR (训练日志，binary approx):

| Window | PR | ISR |
|--------|------|------|
| 1-50 | 0.1450 | 0.0658 |
| 51-100 | 0.1675 | 0.0904 |
| 101-200 | 0.3725 | 0.1808 |
| 201-300 | 0.4387 | 0.2019 |
| 301-400 | 0.5875 | 0.1890 |
| 401-500 | 0.6875 | 0.1954 |

- Overall PR: 0.4485, ISR: 0.1690
- Last100 PR: 0.6875, ISR: 0.1954, loss: 0.0150
- Last50 PR: 0.6525, ISR: 0.1985
- Max rolling-10 PR: 0.9250, ISR: 0.3180
- First rolling-10 PR>=0.8 at step 392

### Eval 指标 (eval_sta.py, full STA)
- **prove_rate: 0.81**
- **mean_isr: 0.3365** (std=0.3227)
- **proved_only_isr: 0.4154**
- median_isr: 0.20
- component_count_mean: 5.58 (median=5)
- component_count_2_ratio: 3.7% (3/81)
- ISR=1.0 ratio: 12.4% (10/81)
- ISR=0.0 ratio: 3.7% (3/81)
- **tautological_collapse: No** (component 分布健康，mean=5.58)

By type breakdown:

| Type | Count | Proved | PR | ISR |
|------|-------|--------|------|------|
| false | 25 | 22 | 0.88 | 0.3515 |
| unknown | 41 | 34 | 0.83 | 0.3684 |
| true | 34 | 25 | 0.74 | 0.2869 |

### 对比 (关键参照)

| 实验 | Reward | eval_PR | eval_ISR | Components | Tautological |
|------|--------|---------|----------|------------|-------------|
| plan001-s42 (exec-only) | r_exec | 0.93 | 0.1232 | 6.58 | No |
| plan002-b03 (additive β=0.3) | r_exec*(1+0.3*ISR) | 0.18 | 0.0257 | ? | No |
| **plan002-b01 (additive β=0.1)** | **r_exec*(1+0.1*ISR)** | **0.81** | **0.3365** | **5.58** | **No** |
| plan017 (additive random) | r_exec*(1+0.3*random) | 0.48 | 0.0453 | 9.56 | No |
| plan013-r4 (convex random) | 0.9*r_exec+0.1*random | 1.00 | 0.535 | 2 (taut) | Yes |

### 结论

**conclusion = success**

理由：
1. **PR 保持高水平**: eval_PR=0.81，虽比 exec-only baseline (0.93) 下降 12pp，但远高于 β=0.3 (0.18) 和 random (0.48)，仍在可接受范围
2. **ISR 显著提升**: eval_ISR=0.3365，是 exec-only baseline (0.1232) 的 **2.73 倍**，说明 additive ISR bonus 有效引导模型写出更精简的形式化
3. **无 tautological collapse**: component 均值 5.58，分布健康（4-8 区间占主体），ISR 提升是真实的结构改善而非退化到平凡证明
4. **β 强度梯度清晰**: β=0.3 → PR 崩塌(0.18)；β=0.1 → PR 保持(0.81) + ISR 大幅提升(0.3365)。β=0.1 是 additive 路线的最佳工作点
5. **优于 random control**: 远超 plan017 (random additive, PR=0.48/ISR=0.0453)，证明 ISR bonus 的效果不是噪声驱动

---
