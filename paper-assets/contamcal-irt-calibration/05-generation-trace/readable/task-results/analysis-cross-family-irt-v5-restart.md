# analysis cross family irt v5 restart

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cross_family_irt_v5_restart_20260517T043657_result.json`
- **Structured JSON:** [`e4e2dc62c747f7e245a0.json`](../../sessions/e4/e4e2dc62c747f7e245a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**v5 已于今天 12:31 成功完成，无需重跑。**

三个 benchmark 全部有结果：

| Benchmark | N | γ | 95% CI | excl0 | PPP | calMAE | ΔMAE |
|-----------|---|---|--------|-------|-----|--------|------|
| MMLU | 18 | 0.3465 | [-0.627, 1.320] | NO | 0.624 | 0.0082 | 0.0296 |
| GSM8K | 28 | -0.1306 | [-0.521, 0.273] | NO | 0.842 | 0.0080 | 0.1712 |
| ARC | 20 | 0.0074 | [-0.575, 0.565] | NO | 0.435 | 0.0151 | 0.0547 |

诊断全部通过（divergent=0, Rhat OK, ESS OK）。日志末尾显示 "Done."。

完成标准核对：
1. ARC results JSON ✓ (`arc_challenge/irt_results.json`)
2. GSM8K results JSON ✓ (`gsm8k/irt_results.json`)
3. MMLU results JSON ✓ (`mmlu/irt_results.json`)
4. COMPLETE 标记文件 — 不存在，但 `pooled_rrf_irt_results.json` 包含完整汇总结果，log 以 "Done." 结尾

唯一缺失是 COMPLETE 标记文件。需要我补创建一个吗？

---
