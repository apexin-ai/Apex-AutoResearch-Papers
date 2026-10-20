# submit exp 030a tcn cheetah s0 sigma02

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_exp_030a_tcn_cheetah_s0_sigma02_20260520T092459_result.json`
- **Structured JSON:** [`b713385bec4ebf6cd443.json`](../../sessions/b7/b713385bec4ebf6cd443.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

### exp_030a_tcn_cheetah_s0_sigma02 — 已启动
- **PID**: 898483 @ bjb1-45299 cuda:0
- **tmux**: `exp_030a_tcn_cheetah_s0_sigma02`
- **状态**: prefilling dataset，nvidia-smi 确认 GPU 0 占用 264MiB
- **Registry**: RUNNING

### 其他实验快照
| 实验 | 服务器 | 当前步数 | train_return |
|------|--------|----------|-------------|
| exp_027_tcn_walker_s1 (σ=0.5 s1) | bjb1-45299 cuda:1 | **112K**/210K | ~309-389 |
| exp_027_tcn_walker_s0_sigma02 (σ=0.2 s0) | bjb1-40020 | **160K**/210K | ~535-639 |
| exp_029a_tcn_walker_s1_sigma02 (σ=0.2 s1) | bjb1-40020 | **28K**/210K | ~150-181 |

注意：用户提供的命令含 `--tcn_enabled True`，但 dreamer.py 不认这个参数（exp_027 也没用），已去掉后成功启动。TCN 通过 `--tcn_sigma` 非零值隐式启用。

---
