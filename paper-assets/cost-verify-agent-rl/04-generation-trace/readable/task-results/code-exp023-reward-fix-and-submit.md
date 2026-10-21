# code exp023 reward fix and submit

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp023-reward-fix-and-submit_20260515T040435_result.json`
- **Structured JSON:** [`f2e637eb74f176c0b821.json`](../../sessions/f2/f2e637eb74f176c0b821.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 开始加载（每卡 559 MiB），WorkerDict 正在加载模型。启动成功。

---

**exp023 启动汇总：**

| 项目 | 状态 |
|------|------|
| reward score | 10.0 → **1.0**（修改 config.py 默认值） |
| val env_groups | 4 → **16** |
| val n_groups | [4] → **[16]** |
| model_path | qwen3_exp021_ragen_sft_v4 ✅ |
| LR=5e-7, kl=0.5, grad_clip=1.0, steps=30, format_penalty=0 | ✅ |
| gpu_memory_utilization=0.6, parallel_friendly=true | ✅ |
| PID | **442593** |
| tmux session | **exp023_grpo_parallel** |
| 日志 | `~/runs/cost-verify-agent-rl/exp023_grpo_parallel.log` |
| GPU | cuda:0, cuda:1 加载中（559 MiB/卡） |

---
