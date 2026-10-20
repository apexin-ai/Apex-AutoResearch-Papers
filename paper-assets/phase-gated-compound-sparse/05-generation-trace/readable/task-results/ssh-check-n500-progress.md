# ssh check n500 progress

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-n500-progress_20260514T222745_result.json`
- **Structured JSON:** [`ecc49c4be284f0095ce6.json`](../../sessions/ec/ecc49c4be284f0095ce6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 进程状态

| GPU | Session | 当前 condition | 状态 | 进度 |
|-----|---------|---------------|------|------|
| GPU0 | tmux `c2_n500_gpu1` | `ds_imp_s020` | alive, 已跑 4h | 接近完成 |
| GPU1 | tmux `c2_n500_gpu0` | `ds_rand_s025` | alive, 刚启动 1min | 刚开始 |
| GPU2 | screen `c2_qw_gpu2` | `qw_imp_s025` | alive, 已跑 4min | 2/500 |
| GPU3 | screen `c2_qw_gpu3` | `qw_rand_s020` | alive, 已跑 3h20m | 483/500 |

## 已完成 conditions (6/16)

| Condition | 完成时间 |
|-----------|---------|
| `ds_rand_s015` | 02:05 |
| `ds_imp_s015` | 02:31 |
| `ds_rand_s020` | 06:30 (**刚完成**) |
| `qw_imp_s015` | 03:02 |
| `qw_imp_s020` | 06:27 |
| `qw_rand_s015` | 03:11 |

## GPU 使用率

| GPU | 型号 | 利用率 | 显存 |
|-----|------|--------|------|
| 0 | RTX PRO 6000 Blackwell | 77% | 33.4/97.9 GB |
| 1 | RTX PRO 6000 Blackwell | 77% | 18.6/97.9 GB |
| 2 | RTX PRO 6000 Blackwell | 96% | 22.5/97.9 GB |
| 3 | RTX PRO 6000 Blackwell | 77% | 34.7/97.9 GB |

## ETA 估算

单 condition 耗时：DeepSeek ~4.5h，Qwen ~3.5h。

| GPU | 剩余队列 | 预计完成 |
|-----|---------|---------|
| GPU0 (ds_imp) | s020(~30min) → s025 → s030 | ~16:00 |
| GPU1 (ds_rand) | s025(刚开始) → s030 | ~15:30 |
| GPU2 (qw_imp) | s025(刚开始) → s030 | ~13:30 |
| GPU3 (qw_rand) | s020(~10min) → s025 → s030 | ~13:40 |

**瓶颈在 GPU0 (DeepSeek importance)，全部实验预计 ~16:00 CST 完成。**

## Sentinel 状态

`/tmp/agent-ml-exit/` 存在，包含 39 个 sentinel 文件（均为此前批次实验），无本轮 n=500 实验的 exit sentinel。

---
