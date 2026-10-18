# code multi seed error bars

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_multi_seed_error_bars_20260514T073300_result.json`
- **Structured JSON:** [`0a0d48fdfbf9213840d2.json`](../../sessions/0a/0a0d48fdfbf9213840d2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已启动，状态：

- **PID**: 199404, **GPU**: cuda:0 (RTX PRO 6000 Blackwell, 98GB)
- **Baseline PPL**: 9.8106（已完成），正在跑 uniform 4-bit eval
- **预计总耗时**: ~4-5 小时（每 seed 约 336 次 calibration PPL 评估 + 1 次 WikiText-2 test eval）
- **Registry**: `multi_seed_error_bars` → RUNNING
- **监控**: 每 8 分钟自动检查日志和进程状态

脚本流程：
1. Baseline + uniform 4-bit eval（seed 无关，只做一次）
2. Seed 0/1/2 各自：生成 calibration subset → 28×4×3=336 次 profiling → constrained MCKP → eval PPL
3. 每个 seed 完成后保存 checkpoint，最终汇总 mean±std 和 allocation agreement

---
