# exp mistral pid cron

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_mistral_pid_cron_20260521T043553_result.json`
- **Structured JSON:** [`80349cfa5558889d0f0d.json`](../../sessions/80/80349cfa5558889d0f0d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

**1. Mistral 进程 PID**

| GPU | PID |
|-----|------|
| 0 | 79682 |
| 1 | 79683 |
| 2 | 79684 |
| 3 | 79685 |

**2. Qwen 自动启动脚本** — 已部署并在后台运行（PID 86043）。脚本每 60 秒检测 Mistral 进程，全部退出后自动在 4 个 GPU 上启动 Qwen 推理。注意：我在 Qwen 启动命令中补了 `--items` 和 `--few-shot` 参数（与 Mistral 一致），确保推理配置完整。

**3. Mistral 进度**

| Shard | 已完成行数 |
|-------|-----------|
| shard_0 | 50,000 |
| shard_1 | 48,800 |
| shard_2 | 49,400 |
| shard_3 | 52,400 |
| **总计** | **200,600** |

每个 shard CSV 有 324 个任务（325 行含表头）。进程已运行约 56 分钟，CPU 占用率 ~121%，状态正常。

---
