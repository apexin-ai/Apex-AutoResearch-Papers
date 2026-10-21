# diagnose exp029 c prime resume mt50 v2

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp029_c_prime_resume_mt50_v2_20260522T024218_result.json`
- **Structured JSON:** [`2fd9fece539681a4fef6.json`](../../sessions/2f/2fd9fece539681a4fef6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成，结果如下：

---

## exp029_c_prime_resume_mt50_v2 诊断报告

### 状态：正在运行中

**PID 376153** 存活，状态 `Ss+`，启动时间 10:10:02（服务器本地时间）。进程未退出（`/tmp/agent-ml-exit/exp029_c_prime_resume_mt50.exit` 不存在）。

### 训练进度

- **当前进度**: Step 6/7 (86%)，每步约 1605s (~26.7 min)
- 从 `global_step_5` 恢复，`val_before_train=true` → 先跑了 step 5 的 validation
- Step 6 是恢复后的第一个实际训练步，正在进行中
- **预计完成时间**: ~11:00 服务器本地时间（约 10:33 + 27 min）

### Metrics（来自日志 + W&B）

W&B run `u6jn1njs`，状态 `running`，runtime ≈ 1849s。目前仅有 step 5 的 val 指标：

| 指标 | 值 |
|------|-----|
| val-env/AlfworldSG/success | 21.875% |
| val-env/AlfworldSG/pass@1 | 21.875% |
| val-env/response_length | 6891.9 |
| val-env/AlfworldSG/action_is_valid | 63.0% |
| val-env/AlfworldSG/action_is_effective | 97.6% |
| val-core/unknown/reward/mean@32 | 2.1875 |
| val-core/unknown/reward/best@32/mean | 9.99 |

**train metrics 尚未产出**（step 6 还在跑 rollout/training phase）。

### Checkpoint

- 仅有 `global_step_5`（恢复源）：`/root/autodl-tmp/checkpoints/exp029_intervention_c_prime/global_step_5/`
- 无新 checkpoint 产出（`save_freq=5`，下次保存在 step 10，但总步数只有 7）

### GPU 状态

| GPU | 型号 | 显存占用 | 利用率 |
|-----|------|---------|--------|
| 0 | RTX PRO 6000 Blackwell 96GB | 97191/97887 MiB | 0% (快照) |
| 1 | RTX PRO 6000 Blackwell 96GB | 97191/97887 MiB | 0% (快照) |

显存几乎满载，GPU 利用率 0% 是快照瞬间值（可能处于 CPU 计算阶段）。

### 关键发现

1. **Cron 误报**：cron 用了错误服务器名 `bjb1`（正确为 `bjb1-17606`），导致 SSH 连接失败被标记为 failed。训练进程本身一直正常运行。
2. **v2 复用了 v1 的配置名和日志文件**：config 名仍为 `_alfworld_c_prime_resume_mt50`，日志写到同一个 `.log`，但 config 中 `optimizer_offload: false` 确认这是 v2 修复版。
3. **W&B run 名为 `exp029-c-prime-resume-mt50`**（无 v2 后缀），entity: `xiaoyucorynne-`，project: `cost-verify-agent-rl`。
4. **注意**: `save_freq=5` 意味着 step 6 和 7 不会自动保存 checkpoint，需确认训练结束时是否有 final checkpoint 逻辑。

---
