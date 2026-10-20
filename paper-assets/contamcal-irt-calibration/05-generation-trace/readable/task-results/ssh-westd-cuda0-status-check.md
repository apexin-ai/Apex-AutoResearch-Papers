# ssh westd cuda0 status check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westd-cuda0-status-check_20260519T074025_result.json`
- **Structured JSON:** [`21a500c002040fb122bc.json`](../../sessions/21/21a500c002040fb122bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**OLMo-2 7B d050 训练已完成。**

| 指标 | 值 |
|---|---|
| PID 111715 | 已退出 |
| `.done` | 存在 (15:31 写入) |
| 总步数 | 3642/3642 (100%) |
| 运行时间 | 2h 05m 19s (7519s) |
| 最终 train_loss | 0.9733 |
| 最终 mean_token_accuracy | 0.7418 |
| 最终 entropy | 1.122 |
| 吞吐 | 7.75 samples/s, 0.484 steps/s |
| Adapter 路径 | `/root/autodl-tmp/exp001/checkpoints/OLMo-2-7B_d050_s42/lora_adapter` |

cuda:0 当前空闲 (0 MiB, 0% util)。cuda:1/2/3 有其他进程在跑。

---
