# eval grpo mia retry

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_grpo-mia-retry_20260523T011928_result.json`
- **Structured JSON:** [`d397711ab59dffd9b556.json`](../../sessions/d3/d397711ab59dffd9b556.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个 GRPO checkpoint 全部完成。汇总结果（取 Min-K% 最佳 k=10% 的 AUC-ROC）：

```
MIA AUC-ROC 结果 (Min-K% k=10%):
Stage              | AUC-ROC  | d(seen-unseen)
───────────────────┼──────────┼───────────────
Base               | 0.4929   | -0.0533
SFT (15%)          | 0.6111   | +0.5864
GRPO step 500      | 0.4930   | -0.0526
GRPO step 1000     | 0.4928   | -0.0534
GRPO step 1500     | 0.4930   | -0.0527
```

**完整方法对比 (Loss baseline):**
```
Stage              | Loss AUC | Min-K%(10%) | Min-K%++(10%)
───────────────────┼──────────┼─────────────┼──────────────
Base               | 0.4858   | 0.4929      | 0.4879
SFT (15%)          | 0.5916   | 0.6111      | 0.5689
GRPO step 500      | 0.4859   | 0.4930      | 0.4878
GRPO step 1000     | 0.4858   | 0.4928      | 0.4878
GRPO step 1500     | 0.4858   | 0.4930      | 0.4878
```

关键发现：
- **GRPO 所有 checkpoint (500/1000/1500) 的 MIA AUC-ROC 均 ≈ 0.49**，与 Base 模型几乎一致，接近随机猜测 (0.5)
- **SFT 后 MIA 信号显著** (AUC 0.61)，但 **GRPO 完全消除了 MIA 可检测性**
- 三个 GRPO step 之间几乎无差异 — GRPO 从 step 500 起就已抹平了 SFT 带来的 memorization 信号

---
