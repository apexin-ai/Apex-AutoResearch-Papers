# launch alpha3p0 grpo eval westb0

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_launch_alpha3p0_grpo_eval_westb0_20260522T102814_result.json`
- **Structured JSON:** [`d64f6e8c57a7fd86f521.json`](../../sessions/d6/d64f6e8c57a7fd86f521.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**汇报：checkpoint 损坏，无法执行 eval**

```
Checkpoint: /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20/checkpoint-100/model.safetensors
  实际大小: 7,661,944,832 bytes (7.2G)
  期望大小: 12,323,931,248 bytes (11.5G) — 对比 sft_rasp_alpha3p0_20/checkpoint-935
  状态: 截断/损坏 — safetensors 反序列化失败
  原因: 数据盘 250G 已满 (100% used, 20K avail)，训练保存时写入被截断
```

GRPO alpha3p0 训练本身完成了 100 步（completions 文件齐全到 step 100），但保存 checkpoint 时磁盘满导致 `model.safetensors` 只写了 ~62% 就被截断。

```
=== nvidia-smi ===
GPU 0: 0 MiB, 0% (空闲 — eval 已退出报错)
GPU 1: 16547 MiB, 99% (其他任务)

=== ps 输出 ===
(无 eval_gsm8k 进程)

GPU 0 占用确认: 否（进程已因 checkpoint 损坏退出）
日志状态: 报错 — safetensors_rust.SafetensorError: incomplete metadata, file not fully covered
```

**需要你决策**：
1. 清理数据盘腾出 ~5GB 空间，重新跑 GRPO alpha3p0 训练（~1.5h）再 eval
2. 指定哪些目录可以删除腾空间（`grpo_qwen_math_cka_only_20` 占 38GB 最大）
3. 等 westd-29022 恢复后检查是否有完整副本

---
