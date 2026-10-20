# submit exp002 3B signals cuda3 v2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_exp002_3B_signals_cuda3_v2_20260515T183405_result.json`
- **Structured JSON:** [`4593f2d2966b2da4d389.json`](../../sessions/45/4593f2d2966b2da4d389.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 注册完成。任务总结：

**exp_002_signals_3B_v3 已在 cuda:3 启动** (PID 611720)

**OOM 修复**：`s4_selfcritique.py` 第 120-125 行，根据数据集大小动态调整 batch_size：
- \>5000 items (mmlu 14k) → bs=2
- \>2000 items → bs=8
- 其他 (gsm8k/arc ~1.2k) → bs=32

**执行状态**：
- 跳过 3 个已完成：d000/gsm8k, d000/arc, d005/arc
- 运行 9 个：d000/mmlu, d005/{mmlu,gsm8k}, d025/{mmlu,gsm8k,arc}, d100/{mmlu,gsm8k,arc}
- 首个任务 d000/mmlu 已开始（正在加载模型，576 MiB on GPU 3）
- 日志：`/root/autodl-tmp/exp002/logs/3B_signals_v3.log`
- 预估 6-10 小时（mmlu batch 缩小后单任务更慢）

---
