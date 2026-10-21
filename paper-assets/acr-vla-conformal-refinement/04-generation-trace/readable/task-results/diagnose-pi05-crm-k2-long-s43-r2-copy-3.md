# diagnose pi05 crm k2 long s43 r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_pi05-crm-k2-long-s43-r2_20260526T124742_result.json`
- **Structured JSON:** [`7687987554aff4432f5a.json`](../../sessions/76/7687987554aff4432f5a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断：pi05-crm-k2-long-s43-r2

- **失败原因：误报（false positive）。实验已成功完成。**
- **日志关键信息：** 日志文件 `pi05-crm-k2-long-s43-r2.log` 不存在于 `/root/runs/acr-vla-conformal-refinement/`，但输出文件已完整生成。
- **输出文件：** `/root/acr-vla-conformal-refinement/logs/eval_long_crm_obs_only_norm0.05_seed43_pi05_K2.json`（1800 bytes, May 26 20:22），包含完整结果：
  - 10 个 task × 20 rollouts，**overall success rate = 0.76**
  - 各 task 成功率：0.25 ~ 0.95
- **服务器状态：**
  - GPU：cuda:0/1/3 空闲，cuda:2 在跑 `pi05-adaptive-goal-s44-bjb1`（11.2GB/24.6GB, 43% util），硬件正常
  - 内存：33GB/1TB used，充足
  - 磁盘：root 38%, autodl-tmp 80%，正常
- **是否可恢复：** 不需要恢复——结果已完整
- **建议：** 将实验状态从 failed 改为 completed，录入结果（overall SR = 0.76）。cron 判定失败的原因是日志路径不匹配（期望 `pi05-crm-k2-long-s43-r2.log` 但该文件未生成）且无 sentinel/W&B 信号，进程正常退出被误判为"死亡"。

---
