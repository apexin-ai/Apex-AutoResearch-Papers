# experiment prep cellc v3 eval retry

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_prep-cellc-v3-eval-retry_20260520T211508_result.json`
- **Structured JSON:** [`8927b8753585aa701da6.json`](../../sessions/89/8927b8753585aa701da6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有必要信息已收集完。

---

## Cell C v3 Eval 配置总结

### 1. Eval 方式：内置 val 已足够

训练配置已包含完整 val：
- `val_before_train: True` → step 0 已执行
- `test_freq: 5` → val 在 step 0, 5, 10, 15 执行
- `val.env_groups: 32, group_size: 1` → **32 episodes/val**（满足 C003 ≥16 要求）
- 温度 0.4（`val_kwargs.temperature: 0.4`）

**不需要独立 eval 脚本。** 服务器上也没有现成的 `eval_scienceworld*.py`。

### 2. Metrics 提取方式

**W&B（首选）：**
- Project: `cost-verify-agent-rl`
- Run: `scienceworld-cell-c-episode`（ID: `ghswaew5`）
- URL: `https://wandb.ai/xiaoyucorynne-/cost-verify-agent-rl/runs/ghswaew5`

**训练日志：**
```bash
grep "Training Progress\|val-env" /root/runs/cost-verify-agent-rl/scienceworld_grpo_cell_c_v3.log
```

**Step 0（SFT baseline）val 结果已出：**
| Metric | Value |
|--------|-------|
| success | 0.0 |
| pass@1 | 0.0 |
| score | 2.71/10 |
| final_score | 5.0 |
| num_actions | 7.72 |
| action_is_valid | 0.56 |
| reward/mean@32 | 0.5 |

### 3. Checkpoint 路径

- 保存目录：`/root/autodl-tmp/checkpoints/scienceworld-cell-c/`
- save_freq: 5 → 预期 checkpoint 在 **step 5, 10, 15**
- `max_actor_ckpt_to_keep: 10`（不会被清理）
- 目录目前还不存在（step 1 刚完成，首次保存在 step 5）

### 4. 训练进度

- Step 1/15（7%），~39 min/step
- 启动时间：2026-05-21 02:24
- 预估完成：~2026-05-21 12:00-12:30（约 10h 总时长）

### 5. 潜在问题

- **SFT baseline success=0%**：SFT 模型在 ScienceWorld 上完全无法完成任务。GRPO 需要从 0% 突破。reward/mean=0.5 表明有 partial reward 信号可供学习，但从 0% success 起步风险较高。
- **无独立 eval**：如果论文需要更多 episodes（如 64 或 128）或 test split eval，需额外编写脚本。当前 32 episodes 的 val 对 paper 基本结论够用。
- **Step 5 是第一个关键观察点**：第一次 val + checkpoint 保存，可以判断是否有学习信号（success > 0%）。如果 step 5 仍为 0%，需要提前决策是否继续。

---
