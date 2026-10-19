# code prep exp020 grpo

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep-exp020-grpo_20260514T220755_result.json`
- **Structured JSON:** [`f2b13e23799f9d52f734.json`](../../sessions/f2/f2b13e23799f9d52f734.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。汇总：

## exp020 准备报告

**配置文件** `_alfworld_exp018_sft_grpo.yaml` 关键参数：
| 参数 | 值 |
|------|-----|
| lr | 5e-7 |
| kl_loss_coef | 0.1 |
| kl_loss_type | kl |
| total_steps | 30 |
| clip_ratio | 0.2 ~ 0.28 |
| adv_estimator | grpo |
| response_length | 1024 |
| train group_size | 16 |
| val env_groups | 16→4 (脚本覆盖) |
| save_freq | 5 |
| val_before_train | True |

**启动脚本**: `/root/cost-verify-agent-rl/scripts/run_exp020.sh` ✓ 已创建并 chmod +x

**脚本相对原始任务增加了**：磁盘空间检查（<50GB 则中止）和 GPU 状态打印，满足 C002 pre-flight checklist。

**Checkpoint**: `/root/autodl-tmp/checkpoints/exp019b_expert_sft_v3/final/model.safetensors` — 3.2GB ✓ 存在

**命令行覆盖项**（相对配置文件的变更）：
- `model_path` → exp019b checkpoint（配置文件默认指向 exp017）
- `experiment_name` → exp020-alfworld-sft-grpo
- 输出目录 → `/root/autodl-tmp/checkpoints/exp020/`
- val env_groups 16→4, n_groups [16]→[4]（减少验证开销）

**注意事项**：配置文件的 `trainer.resume_mode: disable`，不会从已有 checkpoint 恢复训练状态，仅加载模型权重作为初始化。

---
