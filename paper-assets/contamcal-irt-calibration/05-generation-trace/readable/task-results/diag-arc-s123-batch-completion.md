# diag arc s123 batch completion

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_arc-s123-batch-completion_20260520T171507_result.json`
- **Structured JSON:** [`da4cf73efca61e4def9b.json`](../../sessions/da/da4cf73efca61e4def9b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总如下：

## eval_arc_s123_batch — 20/20 runs 全部成功

### ARC 25-shot s123 完整结果

| Family | d000 | d005 | d025 | d050 | d100 | Δ(d100) |
|--------|------|------|------|------|------|---------|
| Qwen-14B | 90.44% | 91.47% | 89.76% | 88.74% | 87.29% | **-3.15pp** |
| Phi-4 | 91.89% | 91.89% | 92.24% | 92.58% | 92.75% | **+0.86pp** |
| Qwen-7B | 87.12% | 82.42% | 85.15% | 85.07% | 84.73% | **-2.39pp** |
| OLMo-2 | 76.88% | 77.22% | 76.62% | 79.18% | 79.78% | **+2.90pp** |

### MMLU vs ARC Cross-Benchmark Direction

| Family | MMLU Δ(s123) | ARC Δ(s123) | Match |
|--------|-------------|-------------|-------|
| Qwen-14B | -12.74pp | -3.15pp | ✅ Both Collapse |
| Phi-4 | +1.83pp | +0.86pp | ✅ Both Immune |
| Qwen-7B | ≈0pp | -2.39pp | ⚠️ Partial |
| OLMo-2 | -0.55pp | +2.90pp | ❌ Opposite |

**2/4 方向完全一致，1/4 部分一致，1/4 相反。** 假说"archetypes are model-intrinsic"对 Qwen-14B 和 Phi-4 成立，但 OLMo-2 方向反转表明 contamination effect 在部分 family 上是 benchmark-specific。

Registry 已更新为 DONE/success，cron 已清理，memory.md 已写入完整数据。

---
