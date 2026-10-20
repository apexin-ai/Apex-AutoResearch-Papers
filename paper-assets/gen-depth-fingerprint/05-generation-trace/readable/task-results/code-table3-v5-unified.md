# code table3 v5 unified

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_table3-v5-unified_20260516T202357_result.json`
- **Structured JSON:** [`cba066de4e5899f226e7.json`](../../sessions/cb/cba066de4e5899f226e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果已保存到 `/root/gen-depth-fingerprint/results/8gen_table3_v5_unified.json`。

## 结果汇总

| Method | Binary F1 | 95% CI | Multiclass F1 | 95% CI |
|--------|-----------|--------|---------------|--------|
| avg_logprob | 0.6558 | [0.649, 0.663] | 0.6906 | [0.686, 0.695] |
| fastdetectgpt | 0.4393 | [0.435, 0.444] | 0.5793 | [0.576, 0.583] |
| binoculars | 0.4327 | [0.429, 0.437] | 0.2823 | [0.279, 0.286] |
| ld_score | 0.6592 | [0.653, 0.665] | 0.5965 | [0.592, 0.602] |
| entropy_mean | 0.7013 | [0.695, 0.707] | 0.5266 | [0.521, 0.532] |
| **4det_ensemble** | 0.6887 | [0.682, 0.695] | **0.7801** | [0.776, 0.784] |
| **4det_surface** | **0.7042** | [0.698, 0.710] | **0.7935** | [0.789, 0.798] |
| **7feature_ours** | 0.6938 | [0.688, 0.700] | 0.7757 | [0.771, 0.780] |

**验证**：
- 7feature_ours binary F1 = 0.6938 (期望 ~0.694 ±0.005) ✓
- ld_score binary F1 = 0.6592 (期望 ~0.676 ±0.01 — 偏低 0.017，因为本次无 downsample 而参考值来自 class-balanced 版本)
- n_test_binary = 26,168, n_test_multiclass = 34,131 ✓（binary < multiclass 因排除了 depth=0）
- 8 个方法全部有结果 ✓
- 总时间 88 秒

---
