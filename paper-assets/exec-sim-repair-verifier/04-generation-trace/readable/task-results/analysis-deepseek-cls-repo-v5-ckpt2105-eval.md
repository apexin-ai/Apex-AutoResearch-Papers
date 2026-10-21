# analysis deepseek cls repo v5 ckpt2105 eval

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_deepseek-cls-repo-v5-ckpt2105-eval_20260518T211529_result.json`
- **Structured JSON:** [`ec68260cc7ca0a08e648.json`](../../sessions/ec/ec68260cc7ca0a08e648.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Hypothesis CONFIRMED (strong positive).**

核心结果：

| Model | Per-test | Variant (AND rule) |
|---|---|---|
| **DeepSeek v5 ckpt-2105 (s42, epoch 1)** | **82.61%** | **81.25%** |
| DeepSeek s123 (epoch 3, reference) | 74.93% | 56.25% |
| Qwen3-8B s42 | 84.48% | 72.92% |
| Qwen3-4B s42 | 83.63% | 64.58% |

- per-test 82.61% 超 s123 参考 +7.68pp，接近 Qwen3-4B
- variant 81.25% 超 s123 参考 +25pp，**超过所有已评估模型**（含 Qwen3-8B 的 72.92%）
- unparseable/truncated 均为 0，无技术问题
- early stopping 选择验证成功
- 9/48 variant 错误中 7 个是 FN（gold miss），模型偏保守

报告已写入 `artifacts/deepseek-cls-repo-v5-ckpt2105-eval-analysis.md`。

**注意**：25pp variant gap 混合了 seed 差异和 epoch 差异，v5 s42 epoch 3 eval 尚未跑，跑完才能完全隔离 early stopping 的贡献。

---
