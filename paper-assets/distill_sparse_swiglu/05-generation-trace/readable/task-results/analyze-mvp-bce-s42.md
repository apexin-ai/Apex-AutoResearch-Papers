# analyze mvp bce s42

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_mvp_bce_s42_20260515T122609_result.json`
- **Structured JSON:** [`14c02d42fd03257985c9.json`](../../sessions/14/14c02d42fd03257985c9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## mvp_bce_s42 实验结果

**训练成功完成**，1000/1000 steps，耗时 ~25.5 分钟。

| 指标 | 值 |
|------|-----|
| 最终 Total Loss | 0.6430 |
| 最终 BCE Loss | 0.6379 |
| 最终 Reg Loss | 0.0051 |
| 最终 Sparsity | 0.551（目标 0.5） |
| Checkpoint | `/root/distill_sparse_swiglu/checkpoints/mvp_bce_s42/predictor_bce.pt` (145 MB) |

Loss 从 0.6711 → 0.6430（降幅 4.2%），step 400 后 plateau。Sparsity 从 0.582 收敛到 0.551，略高于 0.5 目标。

**Eval 未执行。** `src/evaluate.py` 已就绪，支持 TEAL 全局分配 + WikiText-2/C4 perplexity 评测：
```bash
python src/evaluate.py \
  --checkpoint /root/distill_sparse_swiglu/checkpoints/mvp_bce_s42/predictor_bce.pt \
  --sparsity_target 0.5 --gpu 0
```

报告已注册为 artifact `art_20260515_1938be`。

---
