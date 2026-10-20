# diagnose status report

**Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_status-report_20260516T125803_result.json`
- **Structured JSON:** [`2adbb932f3f9bfd15512.json`](../../sessions/2a/2adbb932f3f9bfd15512.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== QUICK PROBE 03 ===
Status: RUNNING (PID 497183)
Current phase: Gen 1, Step 5 (Evaluation) — scoring quality with ArmoRM

Gen 0 Metrics:
  mean_quality (ArmoRM): 0.1123
  vendi_score: 107.54
  mean_nn_distance: 0.7088
  self_bleu: 0.0059
  perplexity: 10.60
  batch_fallbacks: 2 (batch-level "Token pattern not found", fell back to per-sample scoring; no samples lost)

Gen 0 Training:
  loss: 0.4805 → 0.356 (5 checkpoints), train_loss=0.4134

Gen 1 Training (completed):
  loss: 0.296 → 0.186, train_loss=0.2399
  Model saved to: outputs/gen_1/condition_0/merged

Gen 1 Metrics: not yet available (eval in progress — ArmoRM checkpoint loading)

=== NO-CURATION BASELINE 01 ===
Status: RUNNING (PID 501406)
Current phase: Gen 0, Step 1 (Generation) — 1216/2000 prompts

No metrics yet. Still generating candidates.

=== ANALYSIS SCRIPTS ===
analyze_results.py: EXISTS (4293 bytes, 2026-05-16 20:26)
compare_conditions.py: EXISTS (5313 bytes, 2026-05-16 20:26)
```

Quick Probe 进展正常，Gen 0 完成，Gen 1 训练已结束正在做 eval scoring。Baseline 刚启动不久，Gen 0 生成阶段约 61% 进度。两个 WARN 是 ArmoRM batch 级别 token pattern 错误导致 fallback 到逐样本打分，未丢失样本。

---
