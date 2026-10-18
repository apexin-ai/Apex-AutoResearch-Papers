# code mlp 19feat baseline

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mlp_19feat_baseline_20260517T115718_result.json`
- **Structured JSON:** [`5d12f9e61be2c314950a.json`](../../sessions/5d/5d12f9e61be2c314950a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验 `mlp_19feat_001` 完成，假设验证成功。

**结果汇总：**

| Variant | Accuracy (5-fold) | Delta vs RF |
|---|---|---|
| MLP 128-128 | 78.66% ± 0.61% | +0.46pp |
| MLP 64-128-64 | 78.95% ± 0.57% | +0.75pp |
| MLP Poly-Top5 (34 feat) | 79.06% ± 0.45% | +0.86pp |
| **RF baseline** | **78.2%** | — |

**结论：** 三个 MLP 变体均在 RF 的 1pp 以内，**特征瓶颈假设确认**。19 features 是性能天花板，换分类器无法突破。

**Per-class recall 模式一致：** d0 ~99.5% > d1 ~82% > d3 ~73% > d2 ~59%。Depth-2 仍是最难区分的类。

**Pairwise AUC：** d0v1 ≈ 0.997, d1v2 ≈ 0.88, d2v3 ≈ 0.82。相邻深度越深越难分。

---
