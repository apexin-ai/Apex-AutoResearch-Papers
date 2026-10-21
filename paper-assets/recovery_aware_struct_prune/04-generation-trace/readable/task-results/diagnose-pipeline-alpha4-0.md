# diagnose pipeline alpha4 0

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_pipeline_alpha4_0_20260521T173519_result.json`
- **Structured JSON:** [`fb3a0dee689a8e160d99.json`](../../sessions/fb/fb3a0dee689a8e160d99.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**Root cause: 数据盘 `/root/autodl-tmp` 100% 满（619G/619G，仅剩 212KB）。**

Pipeline 在 Step 1/4 剪枝计算成功完成（α=4.0, 19.09% sparsity），但保存模型时 `safetensors` 序列化报 `No space left on device (os error 28)`。

关键错误：
```
safetensors_rust.SafetensorError: Error while serializing: I/O error: No space left on device (os error 28)
```
崩溃点：`src/prune.py:437` → `model.save_pretrained()`

**当前状态：**
- 进程已死（EXIT_CODE=1），GPU 0 空闲可用
- `pruned_alpha4_20` 已部分写入 9.7GB（损坏文件）
- GPU 1/3 在跑其他 eval，GPU 0/2 空闲

**修复需要：**
1. 删除损坏的 `pruned_alpha4_20`（~9.7GB）
2. 清理旧 checkpoint 腾出空间（完整 pipeline 需 ~36GB：pruned model + SFT + GRPO）
3. 重跑 pipeline

数据盘有 ~50 个 checkpoint 目录，需要你确认哪些可以删除。

---
