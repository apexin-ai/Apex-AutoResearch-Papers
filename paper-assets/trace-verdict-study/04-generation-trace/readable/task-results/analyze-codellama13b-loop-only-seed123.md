# analyze codellama13b loop only seed123

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_codellama13b_loop_only_seed123_20260520T030311_result.json`
- **Structured JSON:** [`019b6266616c39e35488.json`](../../sessions/01/019b6266616c39e35488.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 分析结果

| Metric | seed42 | seed123 | Δ |
|--------|--------|---------|---|
| **Accuracy** | 77.06% | **76.05%** | -1.01pp |
| Pass Recall | 0.72 | 0.70 | -0.02 |
| Fail Recall | 0.89 | 0.90 | +0.01 |
| Lift over majority | +5.5pp | +4.5pp | -1.0pp |

**seed123 95% CI: [73.9%, 78.6%]** — seed42 的 77.06% 落在此区间内，差异不显著。

**结论**:
- ✅ 假设验证通过：76.05% ∈ [74%, 80%]
- ✅ Tier 2 collapse 是 **seed-robust** 的——两个 seed 都呈现相同模式（强 fail-recall ~90%、弱 pass-recall ~70%、lift 仅 4-5pp）
- CodeLlama-13B 确认无法从 loop-only trace 提取足够判别信息，这是模型能力限制而非训练随机性

Registry 已更新为 DONE(success)，报告已注册。

---
