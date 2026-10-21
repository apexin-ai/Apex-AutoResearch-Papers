# diagnose factorial h2 crash v3

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_factorial_h2_crash_v3_20260518T101859_result.json`
- **Structured JSON:** [`8cf515e8057223261ee3.json`](../../sessions/8c/8cf515e8057223261ee3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 1. 根因：不是真正的崩溃，训练实际已完成全部 15/15 步

EXIT_CODE=1 由 **W&B atexit cleanup 中的 `BrokenPipeError`** 导致，发生在所有训练和 checkpoint 保存完成之后。具体位置：`wandb/sdk/lib/service/service_connection.py:teardown_atexit`。这是 wandb 已知问题，进程退出时 service connection 断开。

**没有 OOM、没有 NaN、没有 CUDA 错误、磁盘未满。**

### 2. Checkpoint 状态：完整，全部可用

| Checkpoint | 路径 |
|---|---|
| global_step_5 | `/root/autodl-tmp/checkpoints/factorial-h2-episode-adv/global_step_5/` |
| global_step_10 | `/root/autodl-tmp/checkpoints/factorial-h2-episode-adv/global_step_10/` |
| global_step_15 | `/root/autodl-tmp/checkpoints/factorial-h2-episode-adv/global_step_15/` (final) |

所有 rank (0,1) 的 model、optim、extra_state 均已保存。

### 3. KL 趋势（训练确实完成，但有质量问题）

| Step | kl_loss | ppo_kl | val success |
|------|---------|--------|-------------|
| 1 | 0.238 | 0.040 | — |
| 5 | 0.735 | 0.031 | 5.97% |
| 10 | 1.029 | 0.057 | — |
| 15 | 2.845 | 0.088 | **0.75%** |

kl_loss 从 0.24 增长到 2.85，ppo_kl 保持在 0.025-0.096 范围内（不算爆炸）。但 **validation success 从 5.97% 崩塌到 0.75%**，模型在训练后期严重退化（overfit to train distribution，丧失泛化能力）。

### 4. 结论与建议

- **无需修复崩溃**：EXIT_CODE=1 是 wandb cleanup 的假阳性，训练已正常完成。可在启动脚本尾部加 `; exit 0` 或 `wandb.finish()` 显式关闭。
- **真正的问题是训练质量**：模型在 15 步后完全退化。`kl_loss_coef=0.01` 过低，未能阻止 policy 偏移。
- **global_step_5 是最佳 checkpoint**（val success 5.97%），global_step_15 反而最差。
- **不需要从 checkpoint 恢复继续训练**，因为更多训练只会进一步退化。应调整超参后重启。

---
