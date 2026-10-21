# code exp 001

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_001_20260513T182718_result.json`
- **Structured JSON:** [`65deacc22a1a3f9e345f.json`](../../sessions/65/65deacc22a1a3f9e345f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已成功启动并通过验证。总结：

**exp_001 Phase A 执行结果**：

| 项目 | 结论 |
|------|------|
| Self-Guide | RAGEN 未内置，通过 `AlfworldSG` 环境标签在 prompt 层面实现 always-on self-guidance |
| 微调方式 | 全量微调（lora_rank=0），匹配原始论文 + 硬件充足 |
| 训练配置 | 50 GRPO steps, 16 episodes/step, eval@10/20/30/40/50, checkpoint@10步 |
| 初始基线 | pass@1=0.0, invalid_action=95%（未训练模型预期表现） |
| 状态 | 训练循环已启动 (Training Progress: 0/50)，tmux session `exp_001` |

**修改文件**：
- `config/envs.yaml` — 追加 `AlfworldSG` 环境标签（含 self-guidance instruction）
- `config/_alfworld_exp001.yaml` — 新建实验配置

**注意**：wandb 未配置，已改为 console-only 日志。训练日志在 `~/runs/cost-verify-agent-rl/exp_001.log`。

---
