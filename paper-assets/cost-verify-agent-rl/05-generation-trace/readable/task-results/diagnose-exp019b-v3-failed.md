# diagnose exp019b v3 failed

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp019b_v3_failed_20260514T205709_result.json`
- **Structured JSON:** [`7447969548be0b1f421b.json`](../../sessions/74/7447969548be0b1f421b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

**错误类型**：Pre-flight check 拦截（GPU 被占用）

**根因**：脚本 `run_exp019b.sh` 的 pre-flight 检查检测到 GPU 0 已有 49567 MiB 显存被占用，主动 abort 并退出（EXIT_CODE=1）。

占用 GPU 0 的进程：
- **PID 379367** — `python scripts/sft_train_v2.py`（正是 exp019b 自身的训练进程）
- 启动时间 04:54:43，已运行 3 分 21 秒
- 进度 15/320 steps (5%)，正在正常训练

**结论**：exp019b 实际上**已经在运行中**。日志文件包含两次输出——第一次是成功启动的训练（正在跑），后面追加了一次重复启动的 pre-flight 失败。EXIT_CODE=1 来自第二次启动尝试，不是第一次。

**修复建议**：无需修复。训练正在正常进行。如果需要跟踪进度：
```bash
tail -f ~/runs/cost-verify-agent-rl/exp019b_expert_sft_v3.log
```

---
