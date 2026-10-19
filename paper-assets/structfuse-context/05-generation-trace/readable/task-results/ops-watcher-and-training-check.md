# ops watcher and training check

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_watcher_and_training_check_20260516T030543_result.json`
- **Structured JSON:** [`09abd3075046c9aa9532.json`](../../sessions/09/09abd3075046c9aa9532.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息已收集。

## Watcher Status
- **PID 966920: ALIVE**
- CMD: `bash /root/structfuse/watch_and_chain_qwen_s42.sh`
- Uptime: 1 天 11 小时 32 分
- 脚本路径: `/root/structfuse/watch_and_chain_qwen_s42.sh`
- 另有 StarCoder 版: `/root/structfuse/watch_and_chain_starcoder_s42.sh`

## Qwen (cuda:0) — dataflow_aware_s44
- **PID 134514** (parent wrapper PID 337267), 运行 12 分钟
- **Step: 50 / 1408** (epoch 1)
- Loss: 0.6256, lr: 3.56e-06 (warmup 阶段)
- 尚无 eval 指标（刚启动）
- GPU util: **99%**, 显存: 49452 / 97887 MiB
- **ETA (epoch 1):** ~50 steps/12 min → ~4.2 steps/min → 剩余 1358 steps → **约 5.4 小时**

## StarCoder (cuda:1) — embedding_distance_s43
- **PID 129747** (parent PID 519796), 运行 1 小时 00 分
- **Step: 200 / 1405** (epoch 1)
- Loss 趋势: 0.798 → 0.979 → 0.733 → **0.566** (下降中)
- lr: 1.42e-05 (warmup 阶段)
- 尚无 eval 指标
- GPU util: **100%**, 显存: 53458 / 97887 MiB
- **ETA (epoch 1):** ~200 steps/60 min → ~3.3 steps/min → 剩余 1205 steps → **约 6.1 小时**

## GPU Summary
```
GPU 0: util 99%, mem 49461 / 97887 MiB  ← Qwen (PID 134514)
GPU 1: util 100%, mem 53467 / 97887 MiB ← StarCoder (PID 129747)
```

两块 GPU 满载运行，所有进程正常。Watcher 存活等待 Qwen 主链完成后触发 supplement chain。

---
