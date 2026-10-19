# diagnose exp028c crash

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp028c_crash_20260516T082005_result.json`
- **Structured JSON:** [`613fd9fc213746004e01.json`](../../sessions/61/613fd9fc213746004e01.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the data needed. Let me compile the diagnosis report.

---

## exp028c 诊断报告

### 崩溃原因（一句话）
**进程未崩溃**——训练代码在 step 12 完成后、step 13 rollout 生成期间被外部终止（`ray.shutdown()` 被调用，exit_type=`INTENDED_USER_EXIT`），最可能是 cron 监控超时触发的 kill。

### 时间线
- 05:37:44 — Ray session 启动（PID 824694）
- 05:38:34 — W&B run 4yu6qz1m 启动（PID 827923）
- ~06:30 — 初始 val 完成（step 0 val success=6.25%）
- ~15:26 — step 12 训练完成，进入 step 13 rollout
- 16:10:14 — 进程被优雅关闭（`Shutdown by ray.shutdown()`）
- 总运行时间 ~10.5 小时（36935s）

### 各 step metrics

| Step | Type | Success | 备注 |
|------|------|---------|------|
| 0 | val | 6.25% | 初始 val |
| 1 | train | 13.28% | |
| 2 | train | 6.25% | |
| 3 | train | 15.63% | |
| 4 | train | ~visible | |
| 5 | train+val | train 9.375%, **val未记录** | test_freq=5 |
| 6 | train | ~看不到 | |
| 7 | train | **21.88%** | registry 记录的峰值 |
| 8-9 | train | 不可见（log 被截断） | |
| 10 | val | **0.0%** | 完全崩塌，所有 reward=0 |
| 11 | train | 可见于完整log | |
| 12 | train | 6.25% | 最后记录的 step |

### 关键发现
1. **Step 10 val = 0%**：验证 success 从 6.25% → 0%，reward best@N 全部为 0——模型发生了 **reward collapse**
2. **Step 7 train success = 21.88%** 是峰值，之后训练 success 急剧下降
3. **entropy 持续降低**：step 1 = 0.263 → step 12 = 0.198，表明策略过早收敛到次优 policy
4. **KL loss 飙升**：step 1 = 0.013 → step 12 = 0.272，策略偏离 ref policy 显著

### Checkpoint 状态
- `global_step_5` — 存活（41GB 总目录含两个 checkpoint）
- `global_step_10` — 存活
- `latest_checkpointed_iteration.txt` = 10
- **无 step 7 checkpoint**（save_freq=5，只保存 5, 10, 15...）

### 磁盘
- 根分区 50%（15G/30G）— 正常
- 数据盘 3%（18G/879G）— 充裕

### 退出方式
不是 OOM/SIGKILL/代码异常。Driver 调用了 `ray.shutdown()`，属于 `INTENDED_USER_EXIT`。从时间推算（step 12 完成于 ~15:26，退出于 16:10），step 13 的 rollout 运行了 ~44 分钟后被外部终止。

### 建��下一步
1. **step 7 checkpoint 不可恢复**——只有 step 5 和 step 10 的 checkpoint，而 step 10 已经 collapsed（val=0%）
2. **可用 checkpoint 只有 global_step_5**（对应训练时 success 约 9.4%），step 10 已无用
3. 根本原因是 **reward collapse**（step 7 峰值 21.88% 后急速衰退至 0%），不是基础设施问题
4. 下次实验应：
   - 将 save_freq 改为每 step 保存（或至少在 val improvement 时保存 best checkpoint）
   - 增加 KL penalty 或使用 early stopping 防止 policy collapse
   - 降低 lr（当前 1e-6 已经很低）或增大 clip_ratio_low

---
