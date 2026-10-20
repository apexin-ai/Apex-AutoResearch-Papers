# diagnose sweep isr b02 s42

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_sweep-isr-b02-s42_20260516T045433_result.json`
- **Structured JSON:** [`aec75093a69f37f0a0b9.json`](../../sessions/ae/aec75093a69f37f0a0b9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：训练实际已成功完成，EXIT_CODE=129 是误报。**

关键事实：
- 训练跑完了 500/500 步，日志最后打印了 "Done."，final model 已保存
- EXIT_CODE=129 (SIGHUP) 来自 tmux session 在训练进程正常退出后的清理过程，监控系统捕获的是 shell 的退出码而非 Python 进程的
- 完整模型权重在 `/root/autodl-tmp/outputs/sweep_isr_b02_s42_v2/`（含 checkpoint-500 子目录）
- GPU 1 已释放，GPU 0 正在跑 sweep-isr-b02-s43
- 磁盘 85% (39G free)，output_dir 有两份权重共 ~30GB，可删 checkpoint-500 回收 ~15GB

**下一步**：更新 registry 为 success，直接进入 eval 阶段。

---
