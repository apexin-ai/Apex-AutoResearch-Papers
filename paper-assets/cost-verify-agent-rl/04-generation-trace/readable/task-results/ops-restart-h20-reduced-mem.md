# ops restart h20 reduced mem

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_restart-h20-reduced-mem_20260518T190913_result.json`
- **Structured JSON:** [`e54f32dd1cb89af0cf8c.json`](../../sessions/e5/e54f32dd1cb89af0cf8c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练稳定运行中：

**汇报**

| 项目 | 状态 |
|------|------|
| **Config 修改** | `optimizer_offload: True → False`；`RAY_OBJECT_STORE_MEMORY=16GB`（环境变量） |
| **PID** | 77613（tmux: `hsweep_h20_seed1`） |
| **W&B Run** | `qi8g4f86` — https://wandb.ai/xiaoyucorynne-/cost-verify-agent-rl/runs/qi8g4f86 |
| **Log** | `~/runs/cost-verify-agent-rl/hsweep_h20_seed1.log` |
| **CPU 内存** | 118GB used / 1TB total（稳定，无增长趋势） |
| **GPU 内存** | 每卡 4.7GB / 98GB（vLLM 已加载，rollout 进行中） |
| **OOM** | 无。当前容器实际内存 ~1TB，远超之前的 220GB 限制 |
| **当前状态** | Step 0/15 rollout 中（h=20 multi-turn 较慢，属正常） |

---
