# diagnose alpha3p0 checkpoint check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_alpha3p0_checkpoint_check_20260522T105413_result.json`
- **Structured JSON:** [`5080437f7fea254cdb36.json`](../../sessions/50/5080437f7fea254cdb36.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== Checkpoint 检查 ===
checkpoint-50: 不存在（无中间 checkpoint）
checkpoint-100: 存在，7,661,944,832 bytes (7.1GB)，截断（应为 ~12.3GB）
其他 checkpoint: 无

=== 磁盘状态 ===
/root/autodl-tmp: 250G 已用 250G，剩余 3.3MB，使用率 100%
⚠️ 数据盘已满，无法写入任何文件

=== GPU 状态 ===
GPU 0: RTX PRO 6000 — 空闲（0MiB, 0%）
GPU 1: RTX PRO 6000 — 占用（16547MiB, 99%）
  └ 正在跑 grpo_qwen_math_cka_only_20 的 eval_gsm8k.py（PID 179898，17:35 启动）

=== completions 文件大小 ===
grpo_rasp_alpha3p0_20/completions/: 128K（10 个 parquet，步数 10-100）
grpo_qwen_math_cka_only_20/completions/: 144K（10 个 parquet，步数 10-100）
completions 占用极小，清理价值不大。

=== 建议 ===
**Plan B（需重跑）。** 原因：
1. 只有 checkpoint-100，无中间 checkpoint（checkpoint-50 不存在）
2. checkpoint-100 的 model.safetensors 仅 7.1GB，确认截断（差 ~5.2GB）
3. **磁盘 100% 满**，必须先清理空间才能重跑

重跑前需释放至少 ~13GB 空间（12.3GB model + buffer）。GPU 0 当前空闲可用。
```

---
