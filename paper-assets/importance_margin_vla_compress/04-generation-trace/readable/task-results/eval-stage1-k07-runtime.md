# eval stage1 k07 runtime

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_stage1_k07_runtime_20260517T063123_result.json`
- **Structured JSON:** [`70ef06b7eb5ca5f1eeaf.json`](../../sessions/70/70ef06b7eb5ca5f1eeaf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 总结

Eval 已启动：

| 项目 | 值 |
|------|------|
| PID | 3092 |
| GPU | 1 (westd-27271) |
| Log | `logs/eval_stage1only_k07.log` |
| Output | `eval_results/eval_stage1only_k07_object.json` |
| Checkpoint | `libero_imm_twostage_fullft/stage1_done/checkpoint.pt` (k=0.5 训练的 ACIS) |
| Config | `libero_imm_twostage_fullft_k07.yaml` (k_ratio=0.7) |
| 预计耗时 | ~40 分钟 |

逻辑：同一个 ACIS scorer（k=0.5 训练），推理时保留 70% tokens（而非 50%）。由于 pruning 更少，性能预期 ≥ 44.8%。不需要重新训练。

---
