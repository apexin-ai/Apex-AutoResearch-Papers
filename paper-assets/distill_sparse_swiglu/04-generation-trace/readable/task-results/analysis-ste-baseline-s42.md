# analysis ste baseline s42

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_ste_baseline_s42_20260515T195504_result.json`
- **Structured JSON:** [`05439fe0469e524ce82d.json`](../../sessions/05/05439fe0469e524ce82d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验 `ste_baseline_s42` 分析报告

### 1. 训练状态

| 项目 | 值 |
|------|-----|
| 训练完成 | **是** — 跑满 1000/1000 步，EXIT_CODE=0 |
| 完成标记 | 无 "Training complete" 字样，但 checkpoint 已保存 |
| Relaxation | STE (Straight-Through Estimator) |
| Loss type | KL normalized |
| Trainable params | 75,960,320 / 8,030,261,248 (0.946%) |
| Checkpoint | `/root/distill_sparse_swiglu/checkpoints/ste_baseline_s42/predictor_kl_normalized.pt` — **145M** |
| Errors | **无**（仅有 HF token warning，无关紧要） |

### 2. 最终训练指标 (Step 1000)

| 指标 | 值 |
|------|-----|
| loss | 0.3262 |
| kl_raw | 0.3262 |
| kl_normalized | 0.3262 |
| constraint_loss | 0.0 |
| sparsity | **0.484** |
| lambda | 1000.00 |
| tau | 0.000 |
| lr | 0.0 (cosine schedule 结束) |

### 3. Eval 指标

**日志中没有 evaluation 段。** grep ppl/perplexity/eval 全部无匹配。训练脚本在 step 1000 后直接保存 checkpoint + wandb summary，没有运行 PPL evaluation。

**需要单独执行 eval 脚本才能获得 `predictor_hard_mask_ppl` 等指标。**

### 4. Lambda (Lagrangian) 统计

配置：`lambda=1.0, target=0.5, margin=0.02, growth=2.0x, decay=0.5x, cap=1000`

**三阶段行为：**

| 阶段 | Steps | Lambda 范围 | 行为 |
|------|-------|-------------|------|
| 探索期 | 1-80 | 0.01 → 81.92 | 指数增长，sparsity 初始偏高(0.539)后下冲到 0.449 |
| 震荡期 | 80-130 | 81.92 → 1000 | 剧烈震荡，快速撞到 cap=1000 |
| 饱和期 | 130-1000 | **1000**（偶降 500/250） | **lambda 长期钉死在 cap** |

Lambda 在 step ~130 后基本恒定在 1000（cap 值）。偶尔 sparsity 短暂超过 0.52 时回落到 500/250，但马上回到 1000。**这是 multiplicative update + low cap 的典型饱和现象——lambda 失去了调节能力。**

### 5. Sparsity 训练曲线

| Step | Sparsity | 备注 |
|------|----------|------|
| 1 | 0.539 | 初始偏高 |
| 50 | 0.508 | |
| 80 | 0.449 | 下冲 |
| 100 | 0.514 | |
| 200 | 0.480 | |
| 300 | ~0.504 | |
| 400 | 0.480 | |
| 500 | 0.477 | |
| 600 | ~0.496 | |
| 700 | 0.480 | |
| 800 | 0.484 | |
| 900 | 0.492 | |
| 1000 | **0.484** | |

最终 sparsity 0.484，略低于目标 0.50 但在 margin(±0.02) 边界内（0.48-0.52）。后半程稳定在 0.480-0.496 区间。

### 6. 结论判定

**暂无法判定。** 缺少 `predictor_hard_mask_ppl`，无法与 Gumbel-sigmoid baseline (~9.19) 对比。

### 7. 值得注意的现象

1. **Lambda 饱和问题**：cap=1000 太低，lambda 在 step 130 后就钉死了。这意味着 Lagrangian 约束基本退化为固定权重，丧失了自适应能力。对比 Gumbel 实验的 lambda 行为可以判断这是 STE 特有的还是通用问题。

2. **tau=0.000 全程**：STE 不使用 temperature annealing（符合预期），但注意 Gumbel-sigmoid 依赖 tau 做 soft→hard 过渡，这是两种方法的本质区别。

3. **kl_raw ≡ kl_normalized 全程**：后半段两者完全相等（constraint=0），说明 sparsity 一直在合规范围内，normalization penalty 没有起作用。

### 下一步

需要对 checkpoint 跑 eval 获取 PPL 指标，才能完成 plan_002 的 conclusion。

---
