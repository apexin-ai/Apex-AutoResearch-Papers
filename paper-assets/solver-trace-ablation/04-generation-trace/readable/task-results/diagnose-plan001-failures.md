# diagnose plan001 failures

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_plan001-failures_20260513T230853_result.json`
- **Structured JSON:** [`8e8c216190149c6d6ad0.json`](../../sessions/8e/8e8c216190149c6d6ad0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**plan001-exec-only-s42-r2 (PID 84901) 在 cuda:0 上正常运行，无需启动新训练。**

当前状态：
- **进度**：207/500 steps（41.4%），正在持续推进
- **最新 step 时间**：2026-05-13T23:09:43 UTC（几秒前还在写日志）
- **训练指标正常**：prove_rate 从 step 1 的 0.125 提升到 step 207 的 0.875，reward_mean 也在上升，loss 在下降
- **GPU 利用率 90%**，说明训练密集运行中

**结论**：
1. cuda:0 **不空闲**，PID 84901 (plan001-exec-only-s42-r2) 正在正常训练
2. cuda:1 也被 plan005 (PID 85795) 占用
3. **不应启动 r4**——r2 已经在跑且进展良好，预计还需约 293 steps 完成
4. 按当前速度（约 5 秒/step），预计还需 ~24 分钟完成

---
