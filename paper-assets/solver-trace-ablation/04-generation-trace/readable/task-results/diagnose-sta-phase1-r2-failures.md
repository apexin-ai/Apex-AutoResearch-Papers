# diagnose sta phase1 r2 failures

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_sta-phase1-r2-failures_20260513T195638_result.json`
- **Structured JSON:** [`e7bede22177df2bb5c9c.json`](../../sessions/e7/e7bede22177df2bb5c9c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。总结：

**R1 (EXIT_CODE=2)**: argparse 对 4 个核心参数设了 `required=True`，`--config` 在 argparse 阶段就被拒绝，YAML 根本没被读取。此问题在 R1→R2 之间已修复。

**R2 (EXIT_CODE=1)**: 服务器上从未执行 `wandb login`，`wandb.api.api_key = [REDACTED] YAML 配置都启用了 wandb（`wandb_project: solver-trace-ablation`），`wandb.init()` 直接抛异常崩溃。

**已修复**: 在服务器上给 `train_grpo.py:211` 的 `wandb.init()` 加了 try/except，失败时自动降级为 `report_to="none"`。import + parse 验证通过。

**可以启动 R3 了。** 如果需要 wandb 追踪，先在服务器上跑 `wandb login`。

---
