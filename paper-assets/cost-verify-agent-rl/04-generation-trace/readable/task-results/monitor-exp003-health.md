# monitor exp003 health

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_exp003_health_20260513T223739_result.json`
- **Structured JSON:** [`09abaab727512d4e5335.json`](../../sessions/09/09abaab727512d4e5335.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

配置确认无误。汇报：

---

## exp003 健康检查结果

| 项目 | 状态 |
|------|------|
| **进程** | **存活** — PID 157857 (train.py) + ray workers (161095/161296/161097) 全部运行中 |
| **GPU 利用率** | **0%**（两卡均是），但 GPU 显存已分配 41GB/卡。这是 agent-env 交互的正常表现——大部分时间在 ALFWorld 环境步骤（CPU-bound），GPU 推理占比极低 |
| **当前步数** | **仍在 step 0 的训练 rollout 收集阶段**。`val_before_train` 的 validation 已在 05:52 完成（耗时 ~739s），之后进入训练循环。Training Progress: 0/100。日志从 05:52 起无新输出，但 ray 内部日志持续更新至 06:38 |
| **Step 0 指标（validation）** | `invalid_action=95%`, `success=0%`, `action_is_valid=0.125%`, `action_is_effective=5%`, `pass@1=0%`, `response_length=1922.75` |
| **Step 1+ 指标** | **尚不可用** — 训练还没完成第一个 step |
| **报错** | 无致命错误，仅有 FutureWarning（FSDP deprecated API）和 gym 版本警告 |

**分析**：128 trajectories (16×8) × 最多 50 turns，每轮包含 model inference + ALFWorld 环境交互。Validation 的 16 trajectories 用了 ~12 分钟，训练的 128 条预计需要 ~60-90 分钟。进程正常运行中，等待 step 0 rollout 完成。

## Plan B 配置

`_alfworld_exp004_instruct.yaml` 已就绪：
- model_path → `/root/cost-verify-agent-rl/models/Qwen3-1.7B-Instruct`
- experiment_name → `exp004-alfworld-selfguide-instruct`
- checkpoint → `/root/autodl-tmp/checkpoints/exp_004/`
- 其他参数与 exp003 完全相同

**启动前需要**：
1. 下载 Qwen3-1.7B-Instruct 到 `/root/cost-verify-agent-rl/models/Qwen3-1.7B-Instruct`
2. 等 exp003 完成或终止以释放 GPU

---
