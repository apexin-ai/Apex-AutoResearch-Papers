# analysis exp 014 deepseek r1 7b

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-014-deepseek-r1-7b_20260517T133544_result.json`
- **Structured JSON:** [`49d400fb8ee78cb825f1.json`](../../sessions/49/49d400fb8ee78cb825f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成，报告写入 `artifacts/exp-014/report/exp014_analysis.md`。

**核心发现：**

| 指标 | 值 |
|------|-----|
| SICA acc | 68.3% (41/60) |
| SC acc | 71.7% (43/60) |
| Gap | **-3.4pp** (SICA < SC) |
| C0 | **58.3%** (35/60 non-unanimous) |
| McNemar p | 0.4795 (不显著) |
| Contradiction rate | 3.7% |

**Hypothesis 判定：FALSIFIED。**

C0 = 58.3%，远高于预期的 < 5%。7B distill 模型并未复现 QwQ-32B 的极端确定性行为，不能作为第二个 capability trap 数据点。

关键差异：QwQ-32B (32B) C0=2.6%，diversity 几乎为零；DeepSeek-R1-7B (7B) 保留了大量 diversity，但 SICA 仍然输给 SC（0 次 rescue，2 次 flip wrong）。这进一步证实了跨所有实验的一致结论：constraint extraction 产出的是 domain facts 而非 answer-discriminative constraints，这才是根本瓶颈，与 diversity 水平无关。

---
