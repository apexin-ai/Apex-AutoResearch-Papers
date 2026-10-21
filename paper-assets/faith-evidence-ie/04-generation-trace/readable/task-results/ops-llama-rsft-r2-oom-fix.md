# ops llama rsft r2 oom fix

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_llama_rsft_r2_oom_fix_20260517T031213_result.json`
- **Structured JSON:** [`d0f009c8a3354c065826.json`](../../sessions/d0/d0f009c8a3354c065826.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**R2 已在正常训练中，无需重新提交。**

PID 405397（另一个 session 提交）已在 GPU 2 上运行，使用 `--quantize --bf16 --per_device_batch_size 2 --gradient_accumulation_steps 8`：

- 进度：20/1656 steps（~1.2%），~9s/step
- 显存：18374MiB / 32607MiB（4-bit QLoRA 模式）
- 预计完成时间：约 4 小时（~15:15 左右）
- Registry 已标记 RUNNING

我的启动是重复的——405397 在我初始 nvidia-smi 检查（11:12:34）和启动（11:14:43）之间的 1 分钟窗口内被另一个 session 抢先提交到了 GPU 2，导致我的进程因显存不足 OOM。无需进一步操作。

---
