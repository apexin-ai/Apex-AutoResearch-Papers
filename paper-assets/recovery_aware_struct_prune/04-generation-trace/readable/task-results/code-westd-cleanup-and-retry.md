# code westd cleanup and retry

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_westd-cleanup-and-retry_20260515T124515_result.json`
- **Structured JSON:** [`89895d515b536c00aa12.json`](../../sessions/89/89895d515b536c00aa12.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两项操作完成：

**操作 1 — PID 32700 身份：** 不是 GraSP，是 GraSP 剪枝模型的 GSM8K 评估：
```
python3 src/eval_gsm8k.py --model_path .../pruned_graspune_20 --output_path results/eval_pruned_graspune_20_greedy.json
```
运行在 GPU 0（13079 MiB）。

**操作 2 — α=4.0 SFT 重试：** 已提交 `sft_alpha4_0_westd_retry`，运行在 westd GPU 1。
- 修改了 `sft_recovery.py` 第115行：`save_strategy="epoch"` → `"no"`，跳过中间 checkpoint 序列化
- `--save_steps` 不是脚本参数，问题根源是 SFTConfig 硬编码的 epoch checkpoint
- 最终模型仍会通过 `trainer.save_model()` 保存
- 日志：`~/runs/recovery_aware_struct_prune/sft_alpha4_0_westd_retry.log`，模型加载中

---
