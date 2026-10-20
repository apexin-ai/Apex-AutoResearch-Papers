# ops v3 eval track and 512tok fix

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_v3_eval_track_and_512tok_fix_20260515T233603_result.json`
- **Structured JSON:** [`62cfafc7ae224fa5e31d.json`](../../sessions/62/62cfafc7ae224fa5e31d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两项更新完成。

---

### Part A: deepseek_full_trace_seed42_v3 eval 结果

Eval 已完成，结果从 `final/eval_results.json` 读取并写入 registry：

| 指标 | 值 | 95% CI |
|------|-----|--------|
| accuracy | **79.16%** | [76.8%, 81.3%] |
| majority baseline | 71.51% | — |
| lift | +7.65pp | — |
| pass_f1 | 0.854 | [0.836, 0.870] |
| fail_f1 | **0.637** | [0.592, 0.678] |
| fail_recall | 0.643 | — |
| fail_precision | 0.632 | — |

v3 label-preserving truncation 修复后 accuracy 从 v1 的 28.49%（崩溃）恢复到 79.16%。相比 DeepSeek VOTA (84.45%) 低 5.3pp，符合 "full_trace intermediate performance" 的预期。

### Part B: full_trace_512tok_seed42 reproduce 字段

已补全：
- **pid**: 197608
- **gpu**: cuda:0
- **started_at**: 2026-05-15T23:16:00Z
- **wandb_run_id**: full_trace_512tok_seed42
- **code_commit**: e404237ccc765768e267d4d6fd3c89549dcf41a4
- **完整 command**: 含 train + eval 两阶段

512tok 当前状态：epoch 1 训练中（step 148/444），预计还需 ~40min 完成 3 epoch + eval。

---
