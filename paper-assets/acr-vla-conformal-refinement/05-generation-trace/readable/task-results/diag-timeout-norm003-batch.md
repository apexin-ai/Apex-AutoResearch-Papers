# diag timeout norm003 batch

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_timeout-norm003-batch_20260518T212231_result.json`
- **Structured JSON:** [`f10eb5a0b1acfa181691.json`](../../sessions/f1/f10eb5a0b1acfa181691.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完成。以下是诊断结论。

---

## 诊断结论

### 根因：timeout_hours=6 太短

所有 4 个失败实验都是**正常运行中被 timeout 杀死**，不是卡死。

### 关键证据

| 实验 | 被杀时进度 | EXIT_CODE |
|------|-----------|-----------|
| obs_only seed44 (bjb1-32546) | task 5, rollout 2/10 = **42/100** | 124 (SIGTERM) |
| obs_only seed45 (bjb1-32546) | task 5, rollout 5/10 = **45/100** | 124 |
| obs_only seed43 (bjb1-18228) | task 5, rollout 6/10 = **46/100** | 129 (SIGHUP) |
| perdof seed43 (bjb2-28827) | task 4, rollout 5/10 = **35/100** | 124 |

**额外发现：perdof-norm003-seed45 (bjb1-32546) 也超时了**（Birth 23:16 → Modified 05:16 = 正好 6h，task 5 rollout 2/10 = 42/100）。

### 基准对比

seed42 obs_only ε=0.03 成功完成：
- Birth: May 16 00:47 → Modified: May 16 13:34 = **约 12 小时 47 分钟**
- 6h 内只能完成 ~45% rollouts，符合被杀时的进度

### 所需时间

ε=0.03 实验需要 **~13 小时**。建议 `timeout_hours` 设为 **15 小时**（留余量）。

### 无部分结果

所有失败实验的 JSON 结果文件均不存在。结果只在全部完成后一次性写入，中途被杀 = 全部白费。

### 当前在运行的 ε=0.03 实验（不会超时）

| 服务器 | 实验 | 启动时间 | 已运行 | timeout |
|--------|------|---------|--------|---------|
| bjb2-28827 | obs_only seed44-bjb2 | 05:07 | ~18min | 无/长 |
| bjb1-18228 | obs_only seed49 | 05:07 | ~18min | 无/长 |
| bjb1-18228 | obs_only seed47 | 04:46 | ~39min | 无/长 |
| bjb1-18228 | obs_only seed46 | 04:46 | ~39min | 无/长 |
| bjb1-18228 | perdof seed44 | 21:31 | ~7h53m | 86400s (24h) ✓ |

这些实验的 timeout 要么是 86400s（24h），要么是直接 `bash -c` 启动无 timeout，都不会被过早杀死。

### 建议

1. 重新提交失败的 5 个实验，`timeout_hours` 设为 **15**
2. 考虑给 evaluate.py 添加**增量保存**（每完成一个 task 就写一次 JSON），避免长时间运行被杀后完全丢失结果

---
