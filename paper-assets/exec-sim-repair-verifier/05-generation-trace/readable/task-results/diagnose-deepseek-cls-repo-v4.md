# diagnose deepseek cls repo v4

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_deepseek-cls-repo-v4_20260517T160306_result.json`
- **Structured JSON:** [`a18544acbb0d83422233.json`](../../sessions/a1/a18544acbb0d83422233.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果：deepseek-cls-repo-v4 训练 **失败**

| 项目 | 值 |
|------|-----|
| 启动时间 | 2026-05-17 02:41 CST |
| 死亡时间 | ~2026-05-18 00:02 CST (运行 ~21.3h) |
| 训练进度 | 4422/6633 steps 已保存 checkpoint，epoch 3 训练完成后 eval 中途被 kill |
| train_loss | 3.33 → 0.0065 (正常下降) |
| eval_loss | **NaN** (epoch 1 和 epoch 2 都是 NaN) |
| best/ 目录 | 不存在 (best_metric=inf) |
| 死因 | 进程在 epoch 3 eval 49% 时被静默 kill，无 error/traceback/exit file，GPU 内存残留 (zombie PID 659888, 17334 MiB on GPU-0) |

**关键问题**：eval_loss 全程 NaN 说明 eval 计算逻辑有 bug（训练本身正常），可能是 CLS task 的 eval metric 在 repo-level 数据上存在兼容性问题。checkpoint-4422 的模型权重可能是可用的，但需要修复 eval 代码后才能验证。

**已执行**：
- Registry 更新为 DONE/failed
- Cron 已删除

**未启动 eval**（训练未成功完成，且无 best checkpoint）。

---
