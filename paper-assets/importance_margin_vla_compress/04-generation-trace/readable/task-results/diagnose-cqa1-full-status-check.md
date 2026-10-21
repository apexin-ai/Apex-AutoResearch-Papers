# diagnose cqa1 full status check

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_cqa1_full_status_check_20260519T072505_result.json`
- **Structured JSON:** [`adeb90a78dc76c441e33.json`](../../sessions/ad/adeb90a78dc76c441e33.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 张卡都在正常训练，没有空闲卡。汇总如下：

| GPU | 实验 | 状态 | Step/100K | 最新 Loss | 备注 |
|-----|------|------|-----------|-----------|------|
| 0 | m32_seed44 | **训练中** | 89700/100K (89.7%) | ~0.039 | tmux session, log: `smart_compress_m32_seed44.log` |
| 1 | m64_seed44 | **训练中** | 89550/100K (89.6%) | ~0.071 | tmux session, log: `train_smart_compress_m64_seed44.log` |
| 2 | m96_seed44 | **训练中** | 92450/100K (92.5%) | ~0.103 | tmux session, 刚存了 step 92000 checkpoint, log: `smart_compress_m96_seed44.log` |
| 3 | m32_official | **训练中** | 73950/100K (74.0%) | ~0.120 | nohup PID 742212, log: `train_smart_compress_m32_official.log` |

**结论：cqa1:1 没有空闲，M=64 seed44 在 step 89550，尚未完成。** 全部 4 张卡都在跑，GPU-Util 18%-41%，显存占用 2.8-3.2 GiB。

预计完成时间（按 sps=4.0, 每 step 50 samples 的 log 间隔约 13s）：
- GPU 0/1 (m32/m64 seed44)：剩 ~10K steps → ~33 min
- GPU 2 (m96 seed44)：剩 ~7.5K steps → ~24 min
- GPU 3 (m32 official)：剩 ~26K steps → ~87 min

---
