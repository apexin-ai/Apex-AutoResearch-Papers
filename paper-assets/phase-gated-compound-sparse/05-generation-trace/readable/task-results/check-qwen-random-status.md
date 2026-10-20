# check qwen random status

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_qwen-random-status_20260514T080325_result.json`
- **Structured JSON:** [`226b6dc15fbaa1b8e642.json`](../../sessions/22/226b6dc15fbaa1b8e642.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### 3 个 Qwen random 实验 — 全部正常运行中

Registry 已经是 RUNNING 状态，无需更新。

| 实验 | GPU | PID | 进度 | GPU Util | 显存 |
|------|-----|-----|------|----------|------|
| bf16_qw_rand_s015 | cuda:0 | 95904 | **22/50** (44%) | 76% | 25.6GB |
| bf16_qw_rand_s020 | cuda:2 | 96299 | **14/50** (28%) | 75% | 23.1GB |
| bf16_qw_rand_s025 | cuda:3 | 96442 | **14/50** (28%) | 74% | 23.1GB |

预估剩余时间：
- s015：~22 个 problem 已完成，约 20 分钟处理了 ~10 个 → 剩余 28 个约需 **~56 分钟**
- s020/s025：进度类似，剩余 36 个约需 **~70-80 分钟**

### bf16_qw_rand_s030
仍为 QUEUED，未提交（无空闲 GPU）。需等某个实验完成后才能跑。

### c4_entropy — 运行中

GPU 1 (PID 93190) 占 22.3GB 显存，当前 GPU util 0%（可能在 I/O 间隙）。

结果 JSON 显示 **20/30 problems 已完成**（67%）。运行约 36 分钟，剩余 10 个 problem 预计 **~18 分钟**完成。

已有中间结果显示 importance vs random masking 效应方向符合预期：
- **Importance pruning**: entropy_delta 一致为负（-0.033 ~ -0.046），表示 entropy 下降
- **Random pruning**: entropy_delta 一致为正（+0.13 ~ +0.28），entropy 上升，且随 sparsity 增大而增大

---
