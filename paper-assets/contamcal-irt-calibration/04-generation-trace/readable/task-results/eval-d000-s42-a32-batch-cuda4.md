# eval d000 s42 a32 batch cuda4

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_d000_s42_a32_batch_cuda4_20260516T005549_result.json`
- **Structured JSON:** [`0ede6b4b258cef5f5334.json`](../../sessions/0e/0ede6b4b258cef5f5334.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

状态汇总：

**Checkpoint 验证通过**：
- 路径：`/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter`
- `lora_alpha=32`，确认是 D076 版本
- `Qwen2.5-3B_d000_a32_s42/` 是空目录（没有文件），实际 checkpoint 在 `Qwen2.5-3B_d000_s42/` 下

**cuda:4 不空闲，无法提交**：
- PID 668217 正在运行 `compute_signals.py`，已运行 5 分 13 秒，占用 6876 MiB
- 所有 6 张 GPU 都在使用中（均有 python 进程）

按 C001/C002 约束，不能在 cuda:4 有进程时提交。两个选项：

1. **等 compute_signals 跑完再提交**——signals 任务通常多久完成？
2. **kill PID 668217 腾出 cuda:4**——需要你确认是否可以终止这个 signals 进程

怎么处理？

---
