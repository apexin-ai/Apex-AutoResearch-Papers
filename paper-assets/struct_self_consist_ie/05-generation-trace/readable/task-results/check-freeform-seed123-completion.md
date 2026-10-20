# check freeform seed123 completion

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_freeform_seed123_completion_20260515T183847_result.json`
- **Structured JSON:** [`44a07a6241f8a506eb2e.json`](../../sessions/44/44a07a6241f8a506eb2e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 已不存在（可能已被之前清除）。Registry 已更新完毕。

## 实验结果摘要：exp_freeform_seed123

**状态**：成功完成，228s，551 instances × 8 samples，parse rate 99.95%

### Selection F1（seed123 freeform vs constrained baseline）

| Subtask | Constrained (greedy→sel) | Freeform seed123 (greedy→sel) |
|---------|--------------------------|-------------------------------|
| **NER** | 0.6182 → 0.6241 (+0.006) | 0.6194 → 0.6222 (+0.003) |
| **RE**  | 0.2913 → 0.2845 (**-0.007**) | 0.2874 → 0.3050 (**+0.018**) |

**RE LP flip 在 seed123 复现**：constrained RE selection 仍然为负（-0.007），freeform 翻正（+0.018），与 seed42 一致。

### QE Signals（freeform seed123 vs seed42 对比）

| Signal | NER AUROC (s42/s123) | RE AUROC (s42/s123) |
|--------|---------------------|---------------------|
| SJ | 0.746 / 0.749 | 0.617 / 0.614 |
| FK | 0.762 / 0.766 | 0.684 / 0.679 |
| logprob | 0.698 / 0.702 | 0.702 / 0.704 |
| voting_conf | 0.796 / 0.800 | 0.655 / 0.647 |

seed123 和 seed42 的 QE 指标高度一致，差异均在 ±0.01 以内，证实结果稳定。

---
