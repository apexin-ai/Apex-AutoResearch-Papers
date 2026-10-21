# ops falcon3 westd cleanup and submit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_falcon3-westd-cleanup-and-submit_20260522T051728_result.json`
- **Structured JSON:** [`0323390bbb512a364578.json`](../../sessions/03/0323390bbb512a364578.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**磁盘清理**: 释放 ~23GB（1.8GB → 25GB 可用）
- 删除：HF datasets 缓存(6.8GB)、LLM-Research/Llama-3.1-8B base model(15GB)、eval_vllm_0shot_DO_NOT_USE(279MB)、hub 元数据/lock 文件

**训练提交**: 4 个 Falcon3-7B-Base SFT 已启动并稳定训练中
- 首次提交因 OOM 失败（7B 模型 batch_size=4 在 95GB GPU 上撑满），加 `--gradient-checkpointing` 后成功
- GPU 0-3 各占 ~71-76GB，利用率 97-99%
- d000: 3125 steps, ETA ~3h
- d005/d025/d050: 步数更多（数据量更大），ETA 类似

**Registry**: 4 个实验已更新为 RUNNING 状态，spec 含完整 provenance。

---
