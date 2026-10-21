# monitor exp013f wandb check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_exp013f-wandb-check_20260514T094907_result.json`
- **Structured JSON:** [`5715d9e01b36ab00bab6.json`](../../sessions/57/5715d9e01b36ab00bab6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**W&B 未启用。**

日志第 1361 行显示 `trainer.logger` 配置为 `['console']`，不包含 `'wandb'`。`agent_trainer.py:408` 的逻辑是 `if "wandb" not in self.config.trainer.logger:` 则跳过 wandb 日志。

因此 pg_loss、grad_norm、ppo_kl 这些指标只输出到 console logger，但由于 console logger 可能只打印到 Ray worker 日志（不是 stdout），所以主日志文件里看不到。

如果需要这些指标，有两个选择：
1. 在配置中将 logger 改为 `['console', 'wandb']` 重启实验
2. 从 Ray worker 日志中提取（但 `/tmp/ray` 目录不存在，可能 Ray session 被清理了）

---
