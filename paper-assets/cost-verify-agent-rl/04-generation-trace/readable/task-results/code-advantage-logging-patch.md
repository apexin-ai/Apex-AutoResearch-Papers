# code advantage logging patch

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_advantage_logging_patch_20260517T062349_result.json`
- **Structured JSON:** [`b0277c149c3099431bcd.json`](../../sessions/b0/b0277c149c3099431bcd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**修改的文件：**

1. `/root/cost-verify-agent-rl/RAGEN/ragen/trainer/agent_trainer.py` — line 343-367（插入 26 行 logging 代码）
2. `/root/cost-verify-agent-rl/scripts/auto_next_hsweep.sh` — line 45-52（添加环境变量设置 + 传递到 tmux）

**实际可用变量：**
- `episode_ids` — numpy array `(batch_size,)`，来自 `data.non_tensor_batch["episode_ids"]`
- `window_position` — 从 `episode_ids` 动态推算（同 episode_id 内按出现顺序编号）
- `step_returns` — tensor `(batch_size,)`，discounted return per step
- `advantages` — tensor `(batch_size, response_length)`，取 `.mean()` 得到 per-sample scalar
- `uid` — 来自 `data.non_tensor_batch["uid"]`，task/prompt group identifier

**记录字段：** `episode_id`, `window_position`, `step_return`, `advantage`, `uid`

**验证结果：** 语法检查 pass。h=2 seed 1 不受影响（`LOG_PER_SAMPLE_ADV` 未设置）。h=2 seed 2 启动时 `auto_next_hsweep.sh` 会自动 export 环境变量并输出到 `/root/runs/cost-verify-agent-rl/hsweep_h2_seed2/advantage_log.jsonl`。

---
