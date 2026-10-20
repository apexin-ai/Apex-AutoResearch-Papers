# ops check v5 training progress

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-v5-training-progress_20260515T015133_result.json`
- **Structured JSON:** [`fc50dc50a97acc01dab5.json`](../../sessions/fc/fc50dc50a97acc01dab5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## v5 训练状态

**两个实验刚启动约 7 分钟（09:46 UTC+8），不是 4h40m。**

| 实验 | 进度 | 速度 | 预计总时长 | 预计完成 (UTC+8) |
|------|------|------|-----------|-----------------|
| vota_seed42_v5 | 24/444 (5%) | ~17.2s/step | ~2h08m | ~11:54 |
| full_trace_seed42_v5 | 25/444 (6%) | ~16.3s/step | ~2h01m | ~11:47 |

**GPU 使用**：
- GPU 0 (full_trace): 100% 利用率, 90.4GB / 97.9GB VRAM
- GPU 1 (vota): 99% 利用率, 41.2GB / 97.9GB VRAM

**异常**：无。无 OOM、NaN、错误。训练正常推进。

**注意事项**：
- full_trace 占用 90GB VRAM（是 vota 的 2 倍多），说明 full_trace 条件的序列显著更长
- 日志中尚未出现 eval_loss/train_loss（还没到第一个 eval step）
- 数据集规模：Train 4720, Eval 1190, 总 444 steps

如果之前确实有运行 4h40m 的 v5 实验，那些进程已经不存在了——当前跑的是全新的。需要我检查是否有旧的 v5 日志或 checkpoint 残留吗？

---
