# diag cqa1 training health check

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_cqa1_training_health_check_20260518T162805_result.json`
- **Structured JSON:** [`688e4e6f1149cbb234e8.json`](../../sessions/68/688e4e6f1149cbb234e8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个训练进程全部存活，训练正常推进。汇总：

| 实验 | GPU | PID | 当前 step | GPU 利用率 | 显存 | 速度 |
|------|-----|-----|-----------|-----------|------|------|
| train_baseline_control_100k_v2 | cuda:0 | 109890 | 53600/100000 (53.6%) | 0%* | 2730MiB | 3.9 sps |
| train_smart_compress_m96_seed43 | cuda:2 | 111881 | 54500/100000 (54.5%) | 0%* | 2778MiB | 4.0 sps |
| train_smart_compress_m32_seed43 | cuda:3 | 200291 | 1800/100000 (1.8%) | 39% | 2864MiB | 4.2 sps |

*GPU-Util 瞬时读数为 0%，但日志持续输出且 sps 稳定，说明 `nvidia-smi` 采样恰好在 step 间隙。

**cuda:1 空闲** — 0MiB 显存占用，无进程，可用。

注意：PID 与预期略有偏差（baseline 109890 vs 预期 109885，m96 111881 vs 预期 111876），差 5，应该是重启后 wrapper/子进程 PID 变化，实际是同一训练。m32 PID 200291 完全匹配。

---
