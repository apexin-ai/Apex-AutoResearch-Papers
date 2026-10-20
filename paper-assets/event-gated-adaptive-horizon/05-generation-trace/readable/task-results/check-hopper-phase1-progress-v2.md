# check hopper phase1 progress v2

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_hopper-phase1-progress-v2_20260527T034538_result.json`
- **Structured JSON:** [`b2778ee21c7f9023fab6.json`](../../sessions/b2/b2778ee21c7f9023fab6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**exp_hopper_baseline** — step 32000, train_return=0.0, train_length=500, episodes=32

**exp_hopper_trained_s0** — step 32000, train_return=0.0, train_length=500, episodes=32

两个实验都停在 step 32000，train_return 均为 0.0，最近 3 条 metrics 完全相同——训练可能已停滞或挂起。

**GPU 状态：**
| GPU | 利用率 | 显存占用 |
|-----|--------|----------|
| 0 | 17% | 53860 MiB |
| 1 | 18% | 3276 MiB |

GPU 0 显存占用很高但利用率低，进一步印证训练可能卡住。

**分析脚本：** `analyze_hopper_nve.py` 存在（14264 bytes，今天 11:05 更新）。

---
