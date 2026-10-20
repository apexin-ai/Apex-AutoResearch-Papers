# ssh server status check

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_server-status-check_20260514T221008_result.json`
- **Structured JSON:** [`41e93cb6140c9f03043b.json`](../../sessions/41/41e93cb6140c9f03043b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 服务器状态汇总

### GPU 状态

| GPU | 型号 | 显存占用 | GPU利用率 | 状态 |
|-----|------|---------|----------|------|
| cuda:0 | RTX 5090 | 19539/32607 MiB (60%) | 26% | **taxei-seed123 训练中** |
| cuda:1 | RTX 5090 | 19537/32607 MiB (60%) | 94% | **random-seed123 训练中** |
| cuda:2 | RTX 5090 | 0 MiB | 0% | 空闲 |
| cuda:3 | RTX 5090 | 0 MiB | 0% | 空闲 |

### seed=123 训练进度

| 任务 | PID | GPU | 进度 | 已运行 | 预计剩余 | Loss |
|------|-----|-----|------|--------|---------|------|
| **v4-taxei-seed123** | 92263 | cuda:0 | 614/3387 (18%) | ~19min | ~1h30m | ~0.52 |
| **v4-random-seed123** | 93477 | cuda:1 | 333/3387 (10%) | ~10min | ~1h40m | ~0.60 |

两个任务都通过 `swift sft` 启动，Qwen3-8B LoRA 微调，3 epochs，有 tmux session 监控（`/tmp/tmux-0` 存在），有 exit trap 写日志到 `~/runs/tax_error_inject_agent/`。

### Checkpoints

seed=123 的 checkpoint 目录已创建但目前只有初始版本：
- `checkpoints/mini_taxei_sft_v4_seed123/v0-20260515-055026/`
- `checkpoints/mini_random_sft_v4_seed123/v0-20260515-055925/`

save_strategy=epoch，预计每完成 1 epoch (~1129 steps) 保存一次。

### 无 orphan 进程

所有 python 进程都归属于两个 seed=123 训练任务，有 tmux 和 exit trap 监控，无孤儿进程。

---
