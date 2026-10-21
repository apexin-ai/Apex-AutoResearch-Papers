# ssh submit floor 0p6 westd2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_submit_floor_0p6_westd2_20260523T110325_result.json`
- **Structured JSON:** [`2491f40a4b170cb1aa54.json`](../../sessions/24/2491f40a4b170cb1aa54.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务正常运行中。

**状态汇报**：
- **PID**: 127420（进程存活）
- **进度**: Step 1（剪枝）已完成，正在执行 **Step 2/4**（SFT warmup），模型已加载到 GPU 2
- **剪枝结果**: cka_only 模式，MLP 199/784 groups 剪除，实际稀疏度 18.99%（目标 20%），floor=0.6
- **模型保存**: `/root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_20_floor_0.6`
- **磁盘**: `/root/autodl-tmp` 剩余 60GB（91% 已用），足够完成实验
- **GPU 2**: nvidia-smi 显示 0MiB 是因为模型刚开始加载，日志确认已在加载中

---
