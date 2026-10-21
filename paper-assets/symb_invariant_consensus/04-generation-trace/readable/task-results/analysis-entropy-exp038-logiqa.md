# analysis entropy exp038 logiqa

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_entropy-exp038-logiqa_20260518T211000_result.json`
- **Structured JSON:** [`4f80bb11728bb036eab0.json`](../../sessions/4f/4f80bb11728bb036eab0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已注册。核心结果：

| Entropy Bin | n (%) | SC Acc | SICA Acc | Delta (pp) | Override n | Override Prec |
|---|---|---|---|---|---|---|
| Low [0, 0.5) | 150 (75.0%) | 84.0% | 84.0% | +0.0 | 0 | N/A |
| Med [0.5, 1.0) | 34 (17.0%) | 67.6% | 64.7% | -2.9 | 1 | 0/1 |
| High [1.0, +inf) | 16 (8.0%) | 50.0% | 50.0% | +0.0 | 2 | 1/2 |

**关键发现**：

1. **Low entropy = 无差异**：与 FOLIO 一致，SC 高度一致时 SICA 无增益。
2. **High entropy 无收益**：与 FOLIO 不同（FOLIO 上 Mistral +9.6pp, Qwen +4.8pp），LogiQA 上高 entropy 区间 SICA delta = 0。仅 2 次 override，1 好 1 坏互相抵消。
3. **Override 极少**：全部 200 题仅 3 次 override (1.5%)，说明 LogiQA 上 constraint extraction 产生的区分性信号太弱。
4. **Unanimous rate 63%**，平均 majority fraction 0.913，dedup ratio 0.781。
5. **整体 -0.5pp**：中 entropy 区间 1 次坏 override 导致净负收益。

结论：SICA 在 LogiQA 上的 constraint signal 不足以有效纠正 SC，与 FOLIO 上的正向收益形成对比。

---
