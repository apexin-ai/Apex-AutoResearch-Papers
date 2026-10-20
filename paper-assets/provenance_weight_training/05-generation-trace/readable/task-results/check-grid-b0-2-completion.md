# check grid b0 2 completion

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_grid_b0_2_completion_20260517T124128_result.json`
- **Structured JSON:** [`3d0fbf9120d53222c619.json`](../../sessions/3d/3d0fbf9120d53222c619.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论：grid_b0_2_seed42 已正常完成

| 项目 | 状态 |
|------|------|
| **是否完成** | 是，全部 6103 steps 完成 |
| **Final checkpoint** | `/root/autodl-tmp/provenance_weight_training/output/models/grid_b0_2_seed42/checkpoint-6103` |
| **Final model** | `/root/autodl-tmp/provenance_weight_training/output/models/grid_b0_2_seed42/final/` (含 model.safetensors) |
| **最终 loss** | ~1.91 - 2.86（step 6102 的多个 micro-batch），unweighted_loss ~1.51 - 2.66 |
| **PPL / eval** | 无 eval_results 文件 |
| **step_metrics** | `/root/autodl-tmp/provenance_weight_training/output/models/grid_b0_2_seed42/step_metrics.jsonl` |
| **cuda:3** | 已释放，0 MiB 显存占用，0% 利用率，空闲可用 |

训练正常结束，产出了 final model 和 checkpoint-6103。没有找到单独的训练日志文件或 eval 结果。cron 报 "no sentinel, no W&B" 可能是因为训练脚本没有写 sentinel 文件或未对接 W&B，但从 checkpoint 和 metrics 看训练确实完整跑完。

---
