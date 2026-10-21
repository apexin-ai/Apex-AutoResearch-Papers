# verify gpu status

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_gpu_status_20260515T122142_result.json`
- **Structured JSON:** [`55f743910a66e905dd38.json`](../../sessions/55/55f743910a66e905dd38.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 占用状态报告

### cuda:0 — 8,879 MiB / 97,887 MiB — 66% util
| PID | 实验 | 显存 |
|-----|------|------|
| 145173 | **exp_009d_baseline_walker_s0** (dreamer.py, seed=0, steps=500k) | 4,154 MiB |
| 146371 | **exp_009d_baseline_walker_s0** (dreamer.py, seed=0, steps=500k, 同一实验的另一进程) | 4,154 MiB |
| 148933 | **exp_015b_frozen_dt_emb** (dreamer.py, seed=1, steps=105k, 跨双GPU) | 552 MiB |

### cuda:1 — 3,550 MiB / 97,887 MiB — 13% util
| PID | 实验 | 显存 |
|-----|------|------|
| 145319 | **exp_015b_frozen_dt_emb** (dreamer.py, seed=1, steps=105k, `--device cuda:0`，但实际也占 cuda:1) | 2,742 MiB |
| 148933 | **exp_015b_frozen_dt_emb** (同上进程，跨GPU) | 794 MiB |

**注意**：PID 145319 的 cmdline 显示 `--device cuda:0`，但 nvidia-smi 显示它在 cuda:1 上占用 2,742 MiB。PID 148933 的 cmdline 显示 `--device cuda:1`，但它同时占用了 cuda:0 (552 MiB) 和 cuda:1 (794 MiB)。说明 015b 可能启动了两个进程，或者存在设备分配混乱。

### Metrics 状态
| 实验 | 文件大小 | 最新 step | 最后写入时间 |
|------|---------|-----------|-------------|
| exp_009d | 4,180 bytes | **step 5,000** | 20:21 (1分钟前) |
| exp_015b | 15 bytes | **step 5,000** (仅 `{"step": 5000}`，无指标) | 20:20 (2分钟前) |

### 关键发现
1. **exp_015b metrics 异常**：文件仅 15 bytes，只写了 `{"step": 5000}` 没有任何训练指标，而 009d 同 step 有完整指标。015b 的 metrics 记录可能有 bug。
2. **015b 设备分配混乱**：两个进程 (145319 用 `--device cuda:0`，148933 用 `--device cuda:1`) 都跨 GPU 占用显存，说明可能启动了两份 015b 或代码内部有跨设备操作。
3. **009d 有两个 PID** (145173, 146371) 在 cuda:0 上，命令行完全相同——可能是主进程 + 子进程，或意外重复启动。

---
