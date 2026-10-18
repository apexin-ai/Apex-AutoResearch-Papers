# analysis eval pi05 l2norm k0925 object seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_pi05_l2norm_k0925_object_seed42_20260522T000608_result.json`
- **Structured JSON:** [`f072bc85acd42b936b5d.json`](../../sessions/f0/f072bc85acd42b936b5d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇总：

## eval_pi05_l2norm_k0925_object_seed42 结果

| 指标 | 值 |
|------|-----|
| **Overall SR** | **99.2%** (496/500) |
| Total episodes | 500 (10 tasks × 50 eps) |
| 耗时 | 57.1 min |
| 异常 | 无（EXIT_CODE=0，无 error/warning） |

**Per-task SR:**

| Task | SR |
|------|-----|
| T0 alphabet soup | 98% |
| T1 cream cheese | 98% |
| T2 salad dressing | 96% |
| T3 bbq sauce | 100% |
| T4 ketchup | 100% |
| T5 tomato sauce | 100% |
| T6 butter | 100% |
| T7 milk | 100% |
| T8 chocolate pudding | 100% |
| T9 orange juice | 100% |

## Hypothesis 验证

对比矩阵（LIBERO-Object, k=0.925）：

| Method | SR |
|--------|-----|
| **L2norm k=0.925** | **99.2%** |
| L2norm k=0.9 | 98.2% |
| Random k=0.925 | 27.6% |

**Conclusion: success.** L2norm k=0.925 = 99.2%（甚至高于 k=0.9 的 98.2%，符合 monotonic degradation 模式），而 random k=0.925 = 27.6% 崩溃。Cliff 是 random-specific，L2norm 在 0.9→0.925 区间保持平稳，random 在同一区间已经崩了。

---
