# ops cqa1 parallel eval

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1-parallel-eval_20260518T213530_result.json`
- **Structured JSON:** [`83405f00d61fe2d75a2a.json`](../../sessions/83/83405f00d61fe2d75a2a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已清理。cuda:0 原有 eval 进程（PID 153750）未受影响，继续运行。

**结论：**

- **cqa1-21977 只有 1 张 RTX 4090 D**，不是 4 张。无法并行到多卡。
- cuda:0 (PID 153750) 正在串行跑 `run_aligned_eval_7B.sh`，当前进度：d000_s42 的 GSM8K（~12%）
- 已完成：d000_s42 的 mmlu
- **14B 基础模型不存在**
- 3 个错误启动的 CPU 进程已全部 kill，未产生有效输出（cuda1 的 d000_s123 mmlu eval 在 CPU 上刚开始，已清除）

**剩余 adapter 列表**（按脚本顺序还需跑 9 个 adapter × 2 mode = 18 个 eval）：d000_s123, d005_s42, d005_s123, d025_s42, d025_s123, d050_s42, d050_s123, d100_s42, d100_s123

按当前速度（每个 adapter 约 30min original + 30min paraphrase），预计还需 ~9h 才能全部完成。要加速的话需要换到有多卡的机器。

---
