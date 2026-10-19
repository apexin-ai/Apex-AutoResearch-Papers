# check m2 progress 20260514 v3

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_m2_progress_20260514_v3_20260514T204214_result.json`
- **Structured JSON:** [`8ca4579ed0428b2063de.json`](../../sessions/8c/8ca4579ed0428b2063de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## M2 全量训练进度

### Qwen (cuda:0, PID 337267) ✅ 正常运行
- **GPU**: 100%, 51.5/97.9 GB VRAM
- **进程**: alive, 9h18m uptime
- **当前**: run 3/10 — **random_s44**, epoch 1/2, **step 650/2816**
- **eval@500**: R@1=**0.6009**, val_loss=0.4252 (比 s43 的 0.5501 大幅提升)
- **已完成**:
  - random_s42: R@1=0.5527 (pre-done)
  - random_s43: R@1=0.5501, 耗时 6h34m
- **剩余**: random_s44 (77%) + embedding×3 + dataflow×3 = 7.77 runs
- **ETA**: ~50h ≈ **2 天** (按 6.5h/run 估算)

### StarCoder (cuda:1, PID 519791) ✅ 正常运行
- **GPU**: 100%, 53.9/97.9 GB VRAM
- **进程**: alive, 2h39m uptime (之前的脚本被 kill，已用新脚本恢复)
- **当前**: run 2/9+ — **random_s43**, epoch 1/2, **step 500/2810**
- **无 eval 结果**（eval@500 可能刚触发或即将触发）
- **已完成**: random_s42: R@1=0.4604 (pre-done)
- **剩余**: random_s43 (82%) + random_s44 + embedding×3 + dataflow×3 = 7.82 runs
- **ETA**: ~96h ≈ **4 天** (StarCoder 训练速度约为 Qwen 的一半，~195 steps/h vs ~428 steps/h)

### 关键观察
1. Qwen random_s44 的 R@1=0.6009 @step500 非常强，远超 s42 (0.5527) 和 s43 (0.5501)
2. StarCoder 比 Qwen 慢约 2x，GPU memory 占用也更高 (53.9 vs 51.5 GB)
3. 两个实验都正常推进，无异常

---
