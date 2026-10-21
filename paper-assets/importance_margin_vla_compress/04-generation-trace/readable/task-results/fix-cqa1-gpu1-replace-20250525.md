# fix cqa1 gpu1 replace 20250525

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_cqa1_gpu1_replace_20250525_20260525T232537_result.json`
- **Structured JSON:** [`a55b5994371d618d5c5c.json`](../../sessions/a5/a55b5994371d618d5c5c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU1 已释放（4MiB），模型正在加载中。加载完成后会占用显存并开始评估。

总结：
- **已 kill**: PID 865972 + 865983（均为冗余 k=0.925 实验）
- **GPU1 已释放**: 4MiB 占用，完全空闲
- **新任务已提交**: `eval_pi05_l2norm_k075_long_seed42_v3` (PID 885789, tmux session)，模型加载中
- **v2 参考**: T0=96%, T1=94%, T2=90%, T3 跑到 ep30=70% 后卡死，avg T0-T2=93.3%
- 预计 10 个 task × ~22min/task ≈ 3.5-4 小时完成

---
