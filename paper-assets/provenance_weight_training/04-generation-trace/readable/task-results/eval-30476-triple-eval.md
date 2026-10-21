# eval 30476 triple eval

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_30476-triple-eval_20260518T170650_result.json`
- **Structured JSON:** [`037728348eeeb2d2e18a.json`](../../sessions/03/037728348eeeb2d2e18a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个 eval 全部完成。

## 结果汇总

| 实验 | Loss | PPL |
|------|------|-----|
| epoch_matched_dr_seed123 (final) | 2.8713 | **17.66** |
| epoch_matched_dr_seed456 (final) | 2.8712 | **17.66** |
| detect_remove_q07_seed42 (final) | 2.8519 | **17.32** |

**detect_remove_q07**: final checkpoint PPL=17.32，比之前 checkpoint-3500 的 PPL=17.49 有所改善。

**detect_remove_q01_seed42 进度**: 仍在 GPU 3 上训练中（PID 47640，已运行 ~2.5h），当前 checkpoint 到 4000（checkpoint-3000 / 3500 / 4000 已保存）。

---
