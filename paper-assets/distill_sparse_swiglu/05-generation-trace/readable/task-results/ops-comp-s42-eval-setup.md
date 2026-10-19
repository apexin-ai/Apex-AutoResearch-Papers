# ops comp s42 eval setup

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_comp-s42-eval-setup_20260518T085448_result.json`
- **Structured JSON:** [`590bc930a3e5bcb9a7fe.json`](../../sessions/59/590bc930a3e5bcb9a7fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**kl_comp_30pct_s42 训练结果**（已标记 DONE）：
- Final loss: 0.6992 (从 2.36 下降), 1000 steps
- Compensation params: 67.2M (0.837% of 8B)
- Checkpoint: `checkpoints/kl_comp_30pct_s42/predictor_with_comp.pt` (273MB, predictor + comp_network 合并)

**Checkpoint 搬运**：
- 41718 → 34887 通过临时 SSH key + scp 完成，临时 key 已清理

**提交的 eval 任务**：

| Exp ID | Server | GPU | Tasks | Status |
|--------|--------|-----|-------|--------|
| `kl_comp_30pct_s42_eval` | westd-34887 | cuda:1 (PID 14307) | wikitext2,arc,winogrande,mmlu,gsm8k | RUNNING |
| `kl_comp_30pct_s42_ppl` | westd-41718 | cuda:0 (PID 61490) | wikitext2,c4 | RUNNING |

两个 eval 日志都确认 "Compensation network loaded from checkpoint"，合并 checkpoint 工作正常。

---
