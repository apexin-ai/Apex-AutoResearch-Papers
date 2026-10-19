# code scienceworld cell d grpo prep

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_scienceworld_cell_d_grpo_prep_20260525T145957_result.json`
- **Structured JSON:** [`1fb40d9bcc53e7d0a78f.json`](../../sessions/1f/1fb40d9bcc53e7d0a78f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已成功提交并运行中。总结：

**ScienceWorld Cell D Episode-Level GRPO — 已提交**

| 项目 | 值 |
|------|------|
| Registry ID | `scienceworld_cell_d_episode` |
| 服务器 | bjb1-17606 cuda:0 |
| tmux session | `scienceworld_cell_d_episode` |
| W&B run | `v69s8kz0` |
| 配置 | `_scienceworld_cell_d_grpo.yaml` |
| 关键参数 | context_window_mode=full, 5 steps, seed=42, 8×8=64 episodes/step |
| SFT checkpoint | `/root/autodl-tmp/checkpoints/scienceworld_sft_bjb1/final` (via symlink `qwen3_scienceworld_sft_bjb1`) |
| 日志 | `~/runs/cost-verify-agent-rl/scienceworld_cell_d_episode.log` |
| Cron 监控 | 每 5 分钟检查 |

**修复的问题**：
1. `model_path` 指向不存在的 `scienceworld_sft_v2` → 改为 `scienceworld_sft_bjb1`
2. 路径不含 "qwen" 触发 `enable_response_mask` assertion → 创建 symlink `qwen3_scienceworld_sft_bjb1`
3. `total_training_steps` 15→5（DDL 紧）
4. `experiment_name` 改为 `scienceworld-cell-d-episode`

GPU 已占用 48GB/97GB（80% util），无报错，初始化阶段正常。ScienceWorld 50-turn episodes + val_before_train 32 episodes 初始化需要几分钟。

---
