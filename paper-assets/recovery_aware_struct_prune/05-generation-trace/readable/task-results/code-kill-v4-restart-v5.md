# code kill v4 restart v5

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_kill-v4-restart-v5_20260515T093216_result.json`
- **Structured JSON:** [`5d216e9f634e7d1be7bd.json`](../../sessions/5d/5d216e9f634e7d1be7bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

v5 已启动，PID 498474，tmux session `grpo_stage2_rasp_20_v5`。等 ~12 分钟后检查前 3 步速度。

## 当前状态汇总

| 项目 | 状态 |
|------|------|
| **v4 kill** | ✅ 已 force kill (339111) |
| **v5 启动** | ✅ PID 498474, cuda:0, tmux=grpo_stage2_rasp_20_v5 |
| **SFT retrain** | 🔄 运行中 PID 239076, cuda:1, step 1176/1870 (63%), ~4.3s/it, 预计还需 ~50 min |
| **D023 CPU re-eval** | ⚠️ 两个都卡在 `Evaluating: 0%` — CPU 推理极慢，20 样本可能需要很长时间 |
| **磁盘** | 根分区 8.6G/30G (29%), 数据盘 176G/250G (71%) — OK |
| **GPU** | cuda:0 = 0 MiB (v5 刚启动待加载), cuda:1 = 51581 MiB (SFT retrain) |

v5 修改: `max_completion_length` 从 2048→512，其他参数完全一致。预期每步从 ~29min 降到 ~7-10min。

等 12 分钟后回来检查 v5 前几步时间。

---
