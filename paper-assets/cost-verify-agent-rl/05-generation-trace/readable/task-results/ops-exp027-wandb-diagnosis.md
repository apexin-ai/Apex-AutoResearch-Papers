# ops exp027 wandb diagnosis

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp027_wandb_diagnosis_20260515T172858_result.json`
- **Structured JSON:** [`419b1df41ae10831ba7b.json`](../../sessions/41/419b1df41ae10831ba7b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。Ray worker log 显示 **step 2 已经完成**，训练在继续。以下是完整报告。

---

## 诊断报告

### 1. W&B 未上报的根因：**大幅延迟，非丢失**

**Metrics 实际已上报**，W&B internal log 中 `history` 字段确认：

| 时间 | history_offset | 对应 | 状态 |
|------|---------------|------|------|
| 23:55:25 | 0 → 1 line | step 0 (初始 val) | 200 OK |
| 01:33:25 | 1 → 1 line | step 1 (train) | 200 OK |

- Step 0 的 `wandb.log()` 在 ~22:42 调用，但 history 数据到 23:55 才通过 filestream 上传 — **延迟 73 分钟**
- 原因：训练极度计算密集（step 耗时 4342s），Python GIL 竞争导致 wandb 后台线程无法及时将数据传递给 wandb-core (Go backend)
- filestream 心跳（events）每 15s 正常发送，console output 正常同步，但 history（metrics）被大幅延迟
- `wandb-summary.json` 本地不存在是 SDK 0.26.0 的正常行为（summary 由 wandb-core 在服务端管理）
- 无任何 error/warning/exception

**结论**：刷新 W&B dashboard，step 0 和 step 1 metrics 应已可见。

### 2. 热修复评估：**不推荐**

- Metrics 已在上传，只是延迟
- 训练正常进行（step 2 已完成）
- 任何修改都有中断训练的风险
- 可通过 Ray worker log 直接获取实时数据

### 3. 主日志停止更新的原因

| 日志源 | 最后修改 | 内容覆盖 |
|--------|---------|---------|
| `exp027_stable_grpo.log` (nohup) | 00:14 | 停在 step 1 rollout 警告 |
| W&B `output.log` (stdout capture) | 01:33 | step 0 + step 1 + step 2 完整 |
| Ray worker log (worker-793046.out) | 01:33 | step 0 + step 1 + step 2 完整 |

主日志 PID 789790 是 Ray driver，实际训练在 Ray worker PID 793046 中。Ray 的 stdout 转发在计算密集期间停滞，导致 nohup 日志不再更新。W&B output.log 直接捕获 worker stdout，比主日志更完整。

### 4. Cron 监控影响

- **PID 检测**：不受影响，PID 789790 存活
- **W&B 检测**：有延迟但 metrics 最终会到达，不影响存活判断
- **Log tail**：cron 指向 `exp027_stable_grpo.log`（停在 00:14），看不到 step 1/2 数据。但 cron 主要依赖 PID + W&B，log tail 不是关键路径

### 5. 建议 Workaround

1. **实时监控源**：改用 Ray worker log
   ```
   /root/autodl-tmp/tmp/ray/session_2026-05-15_22-33-13_032304_789790/logs/worker-1c0c3125f578501ad5705c524bd19adcfcd41768c1d59d6194d73f97-01000000-793046.out
   ```
2. **W&B**：立即刷新 dashboard 确认 step 0/1 metrics 可见
3. **Cron**：无需修改，PID 存活检测是核心机制，不受 log/W&B 延迟影响

### 重要警告：Step 2 Success 大幅下降

```
step 1: train/AlfworldSG/success = 35.94%
step 2: train/AlfworldSG/success = 10.16%  ← 跌落
```

Step 2 batch_size 从 5152 增到 6144，kl_loss 从 0.058 暴涨到 0.413，training 时间从 4342s 增到 5886s。需要关注 step 3 是否继续恶化。

---
