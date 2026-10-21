# code grpo ckpt1000 eval

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_grpo-ckpt1000-eval_20260521T142617_result.json`
- **Structured JSON:** [`11790b8f0743155abfb3.json`](../../sessions/11/11790b8f0743155abfb3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Checkpoint-1500 结果已收集并备份。现在编译完整对比表。

## GRPO 训练轨迹对比（3 checkpoints + SFT baseline）

| 指标 | SFT | GRPO-500 | GRPO-1000 | GRPO-1500 |
|------|-----|----------|-----------|-----------|
| **theta_mle** | 0.228 | 0.157 | 0.155 | 0.152 |
| **lz\*** | 2.914 | 7.771 | 7.803 | 7.686 |
| **accuracy_overall** | 73.39% | 71.44% | 71.43% | 71.41% |
| **accuracy_seen** | 83.10% | 73.03% | 73.08% | 73.22% |
| **accuracy_unseen** | — | 71.16% | 71.14% | 71.10% |
| **lz\*_seen** | — | 3.410 | 3.625 | 3.539 |
| **lz\*_unseen** | — | 7.000 | 6.948 | 6.859 |
| **HT_param** | — | -0.0349 | -0.0348 | -0.0341 |
| **HT_param_seen** | — | -0.0282 | -0.0281 | -0.0272 |

### 相对变化（GRPO-1000 vs 500 / GRPO-1500 vs 500）

| 指标 | 1000 vs 500 | 1500 vs 500 |
|------|-------------|-------------|
| theta_mle | -1.3% | -3.2% |
| lz\* | +0.4% | -1.1% |
| accuracy_overall | -0.01% | -0.04% |
| accuracy_seen | +0.07% | +0.26% |
| accuracy_unseen | -0.03% | -0.08% |
| lz\*_seen | +6.3% | +3.8% |
| lz\*_unseen | -0.7% | -2.0% |
| HT_param | +0.4% | +2.3% |

### 判断

**结论高度稳定。** 所有核心指标在 step 500→1000→1500 之间变化极小：

1. **accuracy**：三个 checkpoint 的 overall accuracy 几乎一致（71.41%–71.44%），差异 < 0.05%，远低于 5% 阈值。
2. **theta_mle**：缓慢下降（0.157→0.155→0.152），趋势一致但幅度很小（-3.2% across 1000 steps）。
3. **lz\***：整体稳定在 7.7±0.1 范围内，波动 < 1.5%。
4. **seen/unseen 分离**：三个 checkpoint 一致表现为 lz\*\_seen ≈ 3.4–3.6 vs lz\*\_unseen ≈ 6.9–7.0，差距稳定存在。

**无两阶段学习效应。** GRPO 在 step 500 之前已经完成主要变化（SFT→GRPO-500 的 lz\* 从 2.9 跳到 7.8，theta 从 0.228 降到 0.157），之后 1000 步内指标基本不再变动。学习曲线呈"快速跳变后平台"模式，而非两阶段渐变。

---
