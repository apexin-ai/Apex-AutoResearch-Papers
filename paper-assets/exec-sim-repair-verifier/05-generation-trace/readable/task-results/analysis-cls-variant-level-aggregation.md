# analysis cls variant level aggregation

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cls-variant-level-aggregation_20260518T183449_result.json`
- **Structured JSON:** [`574d7592f0ca69d93e13.json`](../../sessions/57/574d7592f0ca69d93e13.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总结果:

## Variant-Level Aggregation (n=48, AND rule)

| Model | Form | Seed | Per-test Acc (n=9784) | Variant Acc (n=48) |
|---|---|---|---|---|
| **DeepSeek-6.7B TRAJ s42** | TRAJ | 42 | N/A | **81.25%** |
| **DeepSeek-6.7B TRAJ s123** | TRAJ | 123 | N/A | **75.00%** |
| Qwen3-8B CLS s42 | CLS | 42 | 84.48% | 72.92% |
| Qwen3-8B CLS s123 | CLS | 123 | 85.60% | **81.25%** |
| Qwen3-4B CLS s42 | CLS | 42 | 76.92% | 68.75% |
| DeepSeek CLS s123 (8192) | CLS | 123 | 74.93% | 56.25% |
| DeepSeek CLS s123 (2048) | CLS | 123 | 82.62% | 72.92% |
| Qwen3-8B CWM s42 | CWM | 42 | 65.17% | 52.08% |
| DeepSeek CWM s123 | CWM | 123 | N/A | 47.92%* |
| DeepSeek CWM s42 | CWM | 42 | N/A | 47.92%* |

Majority baseline: 54.17% (variant-level) vs 72.96% (per-test)

*incomplete predictions

## 关键发现

1. **AND 聚合很严格**: CLS per-test 84.48% 降到 variant-level 72.92% (s42)。即使 1161 个 test 中只有 18 个 false negative (xarray gold), 整个 variant 就被判 unresolved。

2. **CLS s123 = TRAJ s42 = 81.25%**: 在 variant level 上 CLS 和 TRAJ 可以达到相同水平, 回应了 reviewer 的比较关切。

3. **CWM variant-level 接近随机**: 52.08% (Qwen3-8B), 接近 majority baseline 54.17%。

4. **错误模式**: CLS 在 variant level 的错误主要是 false negative (gold variant 被判 unresolved), 因为少量 per-test false negative 就足以翻转整个 variant。这与 TRAJ 的错误模式不同, TRAJ 直接在 variant level 做判断。

5. **缺失**: 没找到 Qwen3-4B CLS repo 83.63% (paper Table 4 报告的) 对应的 predictions 文件, `cls_v5` 只有 76.92%。

脚本和结果均已保存到服务器:
- 脚本: `/home/sonny/exec-sim-repair-verifier/aggregate_variant_level.py`
- 结果 JSON: `/home/sonny/exec-sim-repair-verifier/artifacts/variant_level_aggregation.json`

---
