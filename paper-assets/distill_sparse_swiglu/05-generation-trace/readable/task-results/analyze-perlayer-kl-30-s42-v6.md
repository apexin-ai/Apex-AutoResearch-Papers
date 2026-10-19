# analyze perlayer kl 30 s42 v6

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_perlayer_kl_30_s42_v6_20260521T190755_result.json`
- **Structured JSON:** [`4b10992ff00d05d4cd78.json`](../../sessions/4b/4b10992ff00d05d4cd78.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 分析结果

### 训练状态：成功完成

| 指标 | 值 |
|------|-----|
| Steps | 10000/10000 ✓ |
| Final avg_kl | 0.0113 |
| Final tau | 0.100 |
| 总训练时间 | ~18568s (~5.2h) |
| EXIT_CODE | 0 |

### Per-Layer Sparsity Summary

所有 32 层的平均 sparsity 都非常接近 target 0.3（范围 0.293–0.311）。各层 KL 差异明显：

- **最难层（高 KL）**：Layer 0 (0.019), Layer 1 (0.022), Layer 31 (0.015) — 首尾层
- **最易层（低 KL）**：Layer 7–12 (0.007–0.009) — 中间层
- **Lambda 分布**：20/32 层命中 lambda_max=5000，说明大部分层需要很强的 sparsity 压力

### Checkpoints

```
checkpoints/perlayer_kl_30_s42/
├── predictor_perlayer_kl.pt          (152MB, final predictor weights)
├── predictor_perlayer_kl_step_10000.pt (456MB, full checkpoint)
├── predictor_perlayer_kl_step_2000.pt
├── predictor_perlayer_kl_step_4000.pt
├── predictor_perlayer_kl_step_6000.pt
└── predictor_perlayer_kl_step_8000.pt
```

### 缺失项

- **Eval PPL 未计算**：训练脚本只打印了 "Eval mode: all layers masked simultaneously" 但没有实际跑 eval。需要单独用 `src/evaluate.py --checkpoint checkpoints/perlayer_kl_30_s42/predictor_perlayer_kl.pt --sparsity_target 0.3` 来获取 PPL。
- **W&B**：list_wandb_runs 工具有内部错误，无法查询。

### 下一步

需要运行 eval 获取 PPL 才能与 baseline 对比：
- End-to-end KL: **8.81**
- Per-layer KL s456: **9.0282** (sparsity=0.297)

要现在在 westd-41718 上跑 eval 吗？

---
