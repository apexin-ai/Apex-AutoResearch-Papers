# code plan 010 cross domain

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_010_cross_domain_20260514T084200_result.json`
- **Structured JSON:** [`e21833709274836a79e3.json`](../../sessions/e2/e21833709274836a79e3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已成功启动，模型已加载，C4 calibration 44 样本，正在进行 Phase A2 profiling。

112 heads × 3 bit-widths = 336 profiling 步骤 × 2 conditions + eval，预计 2-4 小时完成。

实验详情：
- **脚本**: `/root/ratekv/run_cross_domain.py`
- **PID**: 204192
- **GPU**: cuda:1 (RTX PRO 6000 Blackwell, 98GB)
- **日志**: `/root/ratekv/cross_domain.log`
- **输出**: `/root/ratekv/cross_domain_results.json`
- **C4 calibration**: 44 序列 × 2048 tokens（c4_calibration.json 只有 90K tokens，不足 64 序列）
- **WT2 calibration**: 64 序列 × 2048 tokens（充足）
- 中间 checkpoint: `cross_domain_c4_profiles.json`, `cross_domain_checkpoint_a.json`, `cross_domain_wt2_profiles.json`

---
