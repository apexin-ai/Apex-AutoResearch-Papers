# analyze perlayer kl k16 s42

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_perlayer_kl_k16_s42_20260523T034257_result.json`
- **Structured JSON:** [`f7df536dd4c20dd760f2.json`](../../sessions/f7/f7df536dd4c20dd760f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结果：训练失败。**

- **原因**：`train_perlayer_kl_k4.py` 不支持 `--loss_type` 参数，脚本在 argparse 阶段直接报错退出，未执行任何训练。
- **Checkpoint**：无（目录不存在）。
- **Registry**：已更新为 `conclusion=failed`。

重跑时需要去掉 `--loss_type kl_normalized` 参数，或者给脚本添加该参数支持。

---
