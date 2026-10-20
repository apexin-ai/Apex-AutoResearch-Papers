# verify adaptive fix seed42 running

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_adaptive_fix_seed42_running_20260514T174347_result.json`
- **Structured JSON:** [`5a0d87cf4bdd91a30cd2.json`](../../sessions/5a/5a0d87cf4bdd91a30cd2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**PID 125292 已不存在**，但 adaptive_fix_seed42 实际运行在 **PID 123836**（python 进程），外层 wrapper 为 PID 123831。进程存活，CPU 占用 108%。

**日志状态：**
- 参数解析通过，371499 条数据加载成功，max_steps=6103
- 配置：adaptive, tau=0.8, contamination_ratio=0.4, seed=42, lr=5e-5
- 从 checkpoint-1500 成功恢复（进度条从 step 1501 开始）
- 当前进度：**step 1547/6103 (25%)**，~2.86s/it，预计剩余 ~3.6 小时
- 无 `--overwrite_output_dir` 错误
- weighting 指标正常输出（b 值在 0.2~3.8 范围波动，alpha_eff 多数在 0.8）

训练正常运行中。

---
