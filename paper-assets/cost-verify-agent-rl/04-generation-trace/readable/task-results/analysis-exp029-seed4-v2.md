# analysis exp029 seed4 v2

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp029_seed4_v2_20260521T161208_result.json`
- **Structured JSON:** [`f21c8c45359ccd9c49d0.json`](../../sessions/f2/f21c8c45359ccd9c49d0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。

## 结果摘要
- global_step: 15（目标 15 步，训练完整完成）
- 最终 val/success_rate: 43.75%（指标名 `val-env/AlfworldSG/pass@1`）
- 最终 train/success_rate: ~28.1%（由 `critic/score/mean=2.8125` / 10 推算）
- 最终 train/response_length_mean: 11936.9（无 explosion，max=16383）
- peak val/success_rate: **43.75% (at step 15)**
- conclusion: **success**
- 原因: 单调上升的 val 成功率（9.4%→21.9%→40.6%→43.75%），无 collapse，无 response_length explosion，且远超已有 seed 表现（Seed 1 ~25-28%, Seed 3 ~21%）

## Checkpoint
- 路径: `/root/autodl-tmp/checkpoints/exp029-seed4/global_step_15/actor/`
- 最终 step: 15
- FSDP 2-rank 完整保存（model + optim + extra_state + huggingface tokenizer），共 ~20GB

## 训练曲线关键点

| step | val success | val response_len | train response_len | critic/score/mean | val reward_mean@32 |
|------|------------|------------------|--------------------|--------------------|-------------------|
| 0    | 9.375%     | 6807.5           | —                  | —                  | 0.9375            |
| 5    | 21.875%    | 6862.2           | 12329.6            | 2.5                | 2.1875            |
| 10   | 40.625%    | 4693.7           | 10810.9            | 3.828              | 4.0625            |
| 15   | 43.75%     | 4459.1           | 11936.9            | 2.8125             | 4.375             |

趋势：val 成功率持续上升，val response_length 从 6807→4459 显著缩短（模型学会更高效行动），train response_length 稳定在 ~11k-12k 范围，无 explosion。

## 日志片段
```
(WorkerDict pid=305501) INFO:2026-05-22 00:08:31,791:[Rank 0] Saved optim to /root/autodl-tmp/checkpoints/exp029-seed4/global_step_15/actor/optim_world_size_2_rank_0.pt
(WorkerDict pid=305501) INFO:2026-05-22 00:08:31,795:[Rank 0] Saved extra_state to /root/autodl-tmp/checkpoints/exp029-seed4/global_step_15/actor/extra_state_world_size_2_rank_0.pt
(TaskRunner pid=305302) Final validation metrics: {'val-env/AlfworldSG/success': np.float64(0.4375),
  'val-env/AlfworldSG/pass@1': np.float64(0.4375),
  'val-env/AlfworldSG/action_is_effective': np.float64(0.95625),
  'val-env/AlfworldSG/action_is_valid': np.float64(0.6810),
  'val-env/response_length': np.float64(4459.0625),
  'val-core/unknown/reward/mean@32': np.float64(4.375),
  'val-core/unknown/reward/best@32/mean': np.float64(10.0)}
EXIT_CODE=0
```

---
