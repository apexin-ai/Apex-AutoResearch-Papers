# diag c4 kl30 s42 failure

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_c4_kl30_s42_failure_20260523T010532_result.json`
- **Structured JSON:** [`0a5009f208d3900bb1f5.json`](../../sessions/0a/0a5009f208d3900bb1f5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**结论**：训练正常跑到 step 520/1000（loss 收敛、sparsity 达标、step 500 checkpoint 已保存），然后因一个未捕获的 Python 异常退出 (EXIT_CODE=1)。**traceback 丢失**——nohup 启动时没加 `2>&1`，stderr 未写入日志。最可能的崩溃原因是 wandb 异常（该次运行没有生成 wandb 目录，说明 wandb 状态有问题）。

**修复**：
1. 重新启动时加 `2>&1` 捕获 stderr
2. `export WANDB_MODE=offline` 
3. 可从 step 500 checkpoint 恢复，不用重跑

报告已写入 `artifacts/diag_c4_kl30_s42.md`。

---
