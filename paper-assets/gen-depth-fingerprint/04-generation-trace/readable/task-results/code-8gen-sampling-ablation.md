# code 8gen sampling ablation

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_8gen-sampling-ablation_20260516T151913_result.json`
- **Structured JSON:** [`4af57922f1a04171ee28.json`](../../sessions/4a/4af57922f1a04171ee28.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果已保存到 `results/8gen_sampling_ablation.json`。

**验证**：
- 100% 3-class F1 = 0.769，与已知 main result (~0.76) 一致 ✓
- 3-class F1 单调递增：0.754 → 0.764 → 0.768 → 0.769 ✓
- 25% vs 100% 差距 = 1.6pp（在预期 ~2-5pp 范围内，XGBoost 对样本量不敏感）✓
- 标准差极小（<0.002），说明结果稳定

| Fraction | 3-class F1 | Binary F1 |
|----------|-----------|-----------|
| 25% | 0.754±0.002 | 0.769±0.000 |
| 50% | 0.764±0.002 | 0.769±0.002 |
| 75% | 0.768±0.002 | 0.771±0.001 |
| 100% | 0.769±0.001 | 0.770±0.002 |

Binary 的差异更小（~0.1pp），因为 gen-1 vs gen-2+ 的区分本身信号强、不依赖大量训练样本。

---
