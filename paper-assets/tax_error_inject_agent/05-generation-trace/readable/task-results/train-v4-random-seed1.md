# train v4 random seed1

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_v4-random-seed1_20260515T152040_result.json`
- **Structured JSON:** [`025cc27bfcfca472f379.json`](../../sessions/02/025cc27bfcfca472f379.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已正常启动并在推进。

**状态汇总：**
- 实验 `v4-random-seed1` 已在 registry 中标记为 RUNNING
- tmux session: `v4-random-seed1`，PID: 163009
- GPU: cuda:0，速度 ~1.93s/it
- 总步数: 3387，预计耗时 ~110min
- checkpoint 路径: `checkpoints/mini_random_sft_v4_seed1/v0-20260515-232340/`
- 日志: `~/runs/tax_error_inject_agent/v4-random-seed1.log`

注意：由于 `submit_training_job` MCP 工具在当前 session 不可用，用 ssh_execute + tmux 手动启动，**没有自动 cron 监控回调**。训练完成后需要手动检查或设置轮询。

---
