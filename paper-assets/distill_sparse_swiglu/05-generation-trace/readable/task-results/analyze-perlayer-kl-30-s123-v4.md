# analyze perlayer kl 30 s123 v4

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_perlayer_kl_30_s123_v4_20260521T190749_result.json`
- **Structured JSON:** [`7f47d9e75e02373dec53.json`](../../sessions/7f/7f47d9e75e02373dec53.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## perlayer_kl_30_s123_v4 分析结果

### 训练状态: 成功完成

- 10000/10000 steps, EXIT_CODE=0
- 训练时长: ~18586s (~5.16h)

### 关键 Metrics (final step)

| Metric | Value |
|--------|-------|
| avg_kl | 0.0114 |
| tau (annealed) | 0.100 |
| lr | 0.00e+00 (fully decayed) |

### Per-Layer Sparsity & KL (U-shape pattern)

各层 avg sparsity 在 0.294–0.312 范围，接近 target 0.30。KL 呈明显 U 形分布：

- **高 KL 层** (边缘): L0=0.0199, L1=0.0197, L2=0.0175, L3=0.0164, L31=0.0164
- **低 KL 层** (中间): L7=0.0094, L8–L13 ≈ 0.0077–0.0084
- **中等 KL 层** (中后段): L14–L22 ≈ 0.0093–0.0132

大部分层 lambda 达到 lambda_max=5000，少数层（L4, L5, L6, L7, L14, L23, L26, L29, L30, L31）lambda < 5000，说明这些层 sparsity 更容易达标。

### Checkpoints

```
checkpoints/perlayer_kl_30_s123/
├── predictor_perlayer_kl.pt              (151MB, final weights)
├── predictor_perlayer_kl_step_2000.pt    (455MB)
├── predictor_perlayer_kl_step_4000.pt    (455MB)
├── predictor_perlayer_kl_step_6000.pt    (455MB)
├── predictor_perlayer_kl_step_8000.pt    (455MB)
└── predictor_perlayer_kl_step_10000.pt   (455MB)
```

### Eval PPL: 未计算

日志显示 `Eval mode: all layers masked simultaneously (inference config)` 但没有输出 PPL 数值。需要单独跑 eval pass 才能得到 PPL，与 s456 (PPL=9.0282) 和 end-to-end baseline (PPL=8.81) 对比。

### W&B

`list_wandb_runs` 工具有内部 bug（`wandb_project` 参数问题），无法查询。

### 下一步

需要对 `predictor_perlayer_kl.pt` 跑 all-layers-simultaneous eval 以获取 PPL。是否要我执行？

---
