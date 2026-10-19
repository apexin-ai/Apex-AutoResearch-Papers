# code d045 stats framework prep

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d045-stats-framework-prep_20260515T140254_result.json`
- **Structured JSON:** [`fecc90161ab360edcd24.json`](../../sessions/fe/fecc90161ab360edcd24.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本完成，所有测试通过。总结：

**已创建**: `/root/structfuse/scripts/analyze_m2_stats.py`

**功能覆盖**:
- **A)** best_by_R@1 汇总 — 从 train log 解析所有 eval checkpoint，找 best R@1
- **B)** Mean ± Std — 每个 (encoder, strategy) 的 3-seed 统计
- **C)** Pairwise delta — per-seed delta + mean delta ± std + paired t-test + Cohen's d
- **D)** Leave-one-out — 逐个去掉 seed，报告 2-seed mean 偏移
- **E)** Instance-level bootstrap CI — cluster by repo, 10k iterations, 95% CI
- **输出**: JSON + CSV + console pretty-print
- **额外**: Seed Variance vs Treatment Effect 摘要（直接标注 reviewer concern）

**当前数据状态** (8/18 runs):
| Encoder | random | embedding | dataflow |
|---------|--------|-----------|----------|
| Qwen | s42✓ s43✓ s44✓ | s43✓ s44✓ | — |
| StarCoder | s42✓ s43✓ s44✓ | — | — |

**关键初步发现**: Qwen embedding vs random delta 仅 +0.18pp，seed_std 1.19pp（ratio 6.69），验证了 reviewer 的 seed variance concern。

**M2 完成后运行**:
```bash
python scripts/analyze_m2_stats.py --output-dir /root/structfuse/results
```
Bootstrap 需要先跑 `evaluate_stratified.py` 生成 per-query JSONL 文件到 `results/stratified/per_query/per_query_{encoder}_{strategy}_s{seed}_p50.jsonl`。

---
