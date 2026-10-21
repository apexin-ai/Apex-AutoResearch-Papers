# monitor westd sft progress check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_westd-sft-progress-check_20260515T171256_result.json`
- **Structured JSON:** [`78b5c1ebff5f85671f20.json`](../../sessions/78/78b5c1ebff5f85671f20.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

| | RASP SFT (cuda:0) | Standard SFT (cuda:1) |
|---|---|---|
| **PID** | 48946 | 49645 |
| **tmux session** | `sft_rasp_westd` | `sft_std20_westd` |
| **运行时间** | 12h49m | 9h21m |
| **进度** | 658/1870 (35%) | 456/1870 (24%) |
| **epoch** | 0.696 | 0.482 |
| **当前 loss** | ~0.80-0.89 | ~0.84-0.87 |
| **token accuracy** | ~0.78-0.79 | ~0.77-0.79 |
| **速度** | 1.11 it/s | 1.05 it/s |
| **GPU 利用率** | 86%, 51.5/97.9 GB | 81%, 51.5/97.9 GB |
| **预估剩余** | ~18m14s (进度条显示) | ~22m27s (进度条显示) |
| **Checkpoints** | output_dir 为空，尚未保存 | output_dir 为空，尚未保存 |

**注意事项**:
- 两个 output_dir 目前都是空的，还没有 checkpoint 写入。可能是设置了按 epoch 或训练结束才保存。
- Loss 趋势平稳，RASP 略低于 Standard（0.80-0.89 vs 0.84-0.87），token accuracy 两者接近（~0.78）。
- 按当前速度，RASP 约 18 分钟后完成，Standard 约 22 分钟后完成。

---
