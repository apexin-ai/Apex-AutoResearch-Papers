# analyze k2 l2 calibration results

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_k2-l2-calibration-results_20260519T204957_result.json`
- **Structured JSON:** [`46900745e73a0d4db0d7.json`](../../sessions/46/46900745e73a0d4db0d7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**实验仍在运行，尚未完成。**

状态总结：
- **tmux session**: DEAD（但 nohup 保持进程存活）
- **进程 PID 995736**: 运行中，已运行 18 分钟，CPU 369%
- **`k2_l2_calibration.json`**: 尚未生成（脚本完成后才写入）
- **进度**: 日志显示完成 ~6/50 episodes（10 tasks × 5 episodes），约 12%
- **预计剩余时间**: 每 episode ~150s，剩余 ~44 episodes → ~110 分钟（约 1.5-2 小时）

**已有的 `fmvd_calibration.json` 是之前 K=10 FMVD 基线实验的结果**（非本次 K=2 L2 实验），其中：
- `spearman_rho(FMVD, K10_variance)` = **0.0825**（对照值，与预期的 ~0.08 吻合）

**行动**：
- 不更新 registry（实验未完成）
- 不删除 cron（需要继续监控）
- 建议 ~2 小时后再检查

---
