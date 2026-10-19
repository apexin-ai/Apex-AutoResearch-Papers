# infra sync checkpoints and resubmit

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_sync_checkpoints_and_resubmit_20260517T175039_result.json`
- **Structured JSON:** [`b3dcd65603d2af81d77e.json`](../../sessions/b3/b3dcd65603d2af81d77e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。

- **checkpoint 拷贝**: mvp_kl_norm_v2_s123 已成功拷贝到 westd-41718（~145MB）
- **KL-30% checkpoint**: kl_sparsity30_s42_v3 已存在于 westd-41718，无需拷贝
- **eval 已启动**: PID 14578，模型加载完成，正在计算 TEAL global masks，已开始 wikitext2 评估。日志无 FileNotFoundError。
- 日志路径: `/root/distill_sparse_swiglu/logs/kl50_global_s123_reeval.log`

---
