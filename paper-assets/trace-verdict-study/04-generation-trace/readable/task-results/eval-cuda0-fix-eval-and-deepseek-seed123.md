# eval cuda0 fix eval and deepseek seed123

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_cuda0_fix_eval_and_deepseek_seed123_20260515T180305_result.json`
- **Structured JSON:** [`cef161a9b958c785e41a.json`](../../sessions/ce/cef161a9b958c785e41a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已提交。

---

## 产出汇总

### 1. Sanity Check — ✅ 全部通过

| Check | 期望 | 实际 | 状态 |
|-------|------|------|------|
| Qwen VOTA | 99.41% | 99.41% | ✅ |
| Qwen full_trace | 81.76% | 81.76% | ✅ |

### 2. DeepSeek full_trace re-eval (截断修复后)

| Metric | Value |
|--------|-------|
| **accuracy** | **10.59%** [8.91%, 12.27%] |
| pass P/R/F1 | 0.0 / 0.0 / 0.0 |
| fail P/R/F1 | 0.373 / 0.372 / 0.372 |
| n | 1190 |

截断修复后 DeepSeek full_trace 从 28.49% → 10.59%，更差。模型输出大量乱码（`{`, `assert`, `{}`, `execution` 等），0 个样本预测为 "pass"。该 checkpoint 在 full_trace 上彻底失效。

### 3. deepseek_exception_only_seed123 训练 — ✅ 已提交

- PID: 144507
- tmux session: `deepseek_exception_only_seed123`
- Log: `~/runs/trace-verdict-study/deepseek_exception_only_seed123.log`
- GPU: cuda:0
- 训练完成后自动跑 eval

---
