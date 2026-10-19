# diagnose exp020b final check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp020b-final-check_20260515T005722_result.json`
- **Structured JSON:** [`fd9051f871afc3afe945.json`](../../sessions/fd/fd9051f871afc3afe945.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp020b GRPO 训练状态报告

### 状态：**挂起（hung）** — 未正常完成

- 进程 PID 389242 仍存在，状态 sleeping
- 日志最后写入：08:56（约 6 小时前），停在 step 22/30 的 rollout 阶段
- GPU 利用率 0%，显存仍占用 40GB × 2
- 无 error/traceback/OOM
- 最后保存的 checkpoint：**step 20**

### 关键 Metrics 趋势

| Step | train success | val success | entropy | grad_norm | pass@16 |
|------|-------------|-------------|---------|-----------|---------|
| 0 | — | **0%** | — | — | — |
| 1 | 18.75% | — | 0.107 | 2.78 | 75% |
| 10 | 18.75% | — | 0.085 | 2.52 | 50% |
| 20 | 12.5% | **0%** | 0.045 | 5.58 | 100% |
| 22 | **4.69%** | — | **0.042** | 2.95 | 25% |

### 结论：**Negative — 实验失败**

1. **Val success 始终 0%**：从初始到 step 20 无任何改善
2. **Train success 持续下降**：18.75% → 4.69%，模型在退化
3. **Entropy 坍缩严重**：0.107 → 0.042（降了 61%），策略多样性丧失
4. **训练挂起**：step 22 完成后在 step 23 rollout 阶段卡死约 6 小时，疑似环境交互死锁

GRPO from SFT checkpoint 方案未能改善 agent 性能。进程和 Ray 残留需要清理，是否现在执行？

---
