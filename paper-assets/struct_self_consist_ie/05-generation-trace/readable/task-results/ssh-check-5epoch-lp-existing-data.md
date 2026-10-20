# ssh check 5epoch lp existing data

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_5epoch_lp_existing_data_20260522T113056_result.json`
- **Structured JSON:** [`2a16f248532fee385bc6.json`](../../sessions/2a/2a16f248532fee385bc6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。

---

```
5-epoch FewNERD LP selection 数据:
- 状态: 部分存在

已有数据:
  1. Pilot (exp_028_fewnerd_5epoch, n=5000, seed42):
     - LP selection F1: 0.7835
     - LP selection Δ (vs greedy): +0.624 pp
     - Greedy F1 (macro): 0.7773
     - 对比 3-epoch (exp021): LP Δ 从 +1.37 pp → +0.624 pp（确认"halving"叙事）
     - 来源: output/exp_028_fewnerd_5epoch/analysis_results.json

  2. 3-seed 全量 run (n=37648, seeds 42/123/456):
     - Greedy F1: ~0.7978 (3-seed 均值)
     - MV results: 已有 (recompute_mv_results.txt)
     - logprob_baseline rho/auroc: 已有 (report.json)
     - LP selection F1: ❌ 未计算
     - samples.jsonl 含 logprobs: ✅ (cumulative_logprob + mean_logprob per sample)

不存在的数据:
  - 3-seed 全量 run 的 LP selection F1 和 Δ 未计算
  - fewnerd_5epoch_lp_seed42 目录已创建但为空（似乎开始了 recompute 但未执行）

能否 recompute:
  - ✅ 可以，CPU only
  - 3 个 samples.jsonl (~680MB each) 均含 per-sample logprobs
  - 只需读取每个 instance 的 samples，选 max mean_logprob 的 sample，计算 F1 vs gold

对比 3-epoch LP Δ 参考值:
  - 3-epoch FewNERD LP Δ (3-seed 均值): +1.39 pp
  - 5-epoch pilot LP Δ: +0.624 pp (约减半，支持论文叙事)
```

---
