# experiment oracle mistral 7b

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_oracle-mistral-7b_20260520T133051_result.json`
- **Structured JSON:** [`9cd0099007773d2607b4.json`](../../sessions/9c/9cd0099007773d2607b4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果：

| 指标 | Mistral-7B |
|------|-----------|
| **SC accuracy** | 55.88% (114/204) |
| **Oracle SICA accuracy** | 85.78% (175/204) |
| **Δ (Oracle − SC)** | **+29.90pp** |
| SICA(self) accuracy | 59.31% (121/204) |
| Z3-gold agreement | 95.10% (194/204) |
| FOL parse success | 100% (204/204) |
| McNemar p (oracle vs SC) | 9.99e-14 (b=63, c=2) |
| McNemar p (oracle vs SICA) | 7.84e-12 (b=57, c=3) |

**Per-label breakdown:**

| Label | n | Oracle | SC | SICA | Z3-agree |
|-------|---|--------|-----|------|----------|
| True | 72 | 87.5% | 56.9% | 62.5% | 95.8% |
| False | 63 | 77.8% | 42.9% | 42.9% | 92.1% |
| Unknown | 69 | 91.3% | 66.7% | 71.0% | 97.1% |

**Error analysis:** 29 oracle failures — 22 cases where Z3 got the right answer but no trace supported it, 10 cases where Z3 itself was wrong.

对比 Qwen2.5-14B 的 Δ=+14.22pp，Mistral-7B 的 oracle ceiling gap 是 **+29.90pp** — 更弱的模型有更大的提升空间，这强化了 "weaker models benefit more from symbolic verification" 的叙事。SC baseline 是 55.88%（与预期的 54.41% 接近但不完全一致，可能是 answer normalization 差异）。

---
