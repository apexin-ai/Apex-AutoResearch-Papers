# code prep exp029 seed2 config

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep-exp029-seed2-config_20260518T044832_result.json`
- **Structured JSON:** [`60f9795a2a7788621f2b.json`](../../sessions/60/60f9795a2a7788621f2b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

配置完成。汇报：

| 项目 | 值 |
|---|---|
| **配置文件** | `/root/cost-verify-agent-rl/RAGEN/config/_alfworld_exp029_episode_level_seed2.yaml` |
| **运行脚本** | `/root/cost-verify-agent-rl/RAGEN/scripts/run_exp029_episode_level_seed2.sh` |
| **seed.train** | 43（seed 1 用 10000，从 base.yaml 继承） |
| **seed.val** | 123（与 seed 1 一致） |
| **SFT checkpoint（起始模型）** | `/root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4` — 已确认存在 |
| **checkpoint 输出路径** | `/root/autodl-tmp/checkpoints/exp029-seed2/` — 独立于 seed 1 的 `exp029/` |
| **experiment_name** | `exp029-episode-level-seed2` |
| **total_training_steps** | 15 |
| **test_freq / save_freq** | 5（eval & save at step 5, 10, 15） |
| **磁盘空间** | `/root/autodl-tmp/` 114G 可用（55% used） |
| **dry-run** | 通过 |

**注意事项**：
- 训练期间 val 用 `AlfworldSG` 32 groups（与 seed 1 一致）。OOD 134-task eval (`AlfworldSG_OOD`) 需训练后用 reeval 配置单独跑（seed 1 也是这样做的，已有 `_alfworld_exp029_reeval_valid_unseen.yaml` 模板）。
- 入口点：`python train.py --config-name _alfworld_exp029_episode_level_seed2`，与 seed 1 一致。

---
