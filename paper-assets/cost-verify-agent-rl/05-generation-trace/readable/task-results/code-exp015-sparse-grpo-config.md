# code exp015 sparse grpo config

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp015-sparse-grpo-config_20260514T124934_result.json`
- **Structured JSON:** [`74be8118285ab75f769c.json`](../../sessions/74/74be8118285ab75f769c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

---

## 产出清单

| # | 项目 | 状态 |
|---|------|------|
| 1 | 配置 yaml | `/root/cost-verify-agent-rl/RAGEN/config/_alfworld_exp015_sparse_stable.yaml` |
| 2 | 启动脚本 | `/root/cost-verify-agent-rl/scripts/run_exp015.sh` (chmod +x) |
| 3 | dry-run 验证 | Hydra `--cfg job` 解析通过 |
| 4 | Checkpoint 路径 | **`exp008_grpo/global_step_5` 已被清理**，改为 `resume_mode: "disable"` 从 SFT 模型启动 |
| 5 | Ray 清理 | 完成 |
| 6 | 磁盘 | `/root/autodl-tmp/` 219GB 可用 |

## 配置汇总（Hydra 解析确认）

| 参数 | exp012b 值 | exp015 值 | 验证 |
|------|-----------|-----------|------|
| `actor.optim.lr` | 1e-6 | **1e-7** | `1.0e-07` |
| `actor.kl_loss_coef` | 0.01 | **0.1** | `0.1` |
| `actor.grad_clip` | 1.0 (默认) | **1.0** (显式) | `1.0` |
| `format_penalty` | 0 | 0 | `0` |
| `valid_action_bonus` | 无 (AlfworldSG) | 无 (AlfworldSG) | 标签确认 `AlfworldSG` |
| `env_groups` (train) | 8 | **4** | - |
| `resume_mode` | resume_path | **disable** | `disable` |

## 需注意

**Checkpoint 变更**：exp012b 从 `exp008_grpo/global_step_5`（已有 5 步 GRPO 训练的模型）恢复，但该 checkpoint 已被清理。exp015 改为从 SFT 模型 (`qwen3_sft_final`) 全新开始 GRPO。这意味着 exp015 的起点比 exp012b 更早——模型还没有经过任何 GRPO 训练。如果需要与 exp012b 完全对齐起点，需要先跑 5 步标准 GRPO 生成 checkpoint。

---
