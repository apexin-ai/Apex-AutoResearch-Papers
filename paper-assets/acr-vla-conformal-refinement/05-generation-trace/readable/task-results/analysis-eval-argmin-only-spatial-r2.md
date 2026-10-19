# analysis eval argmin only spatial r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval-argmin-only-spatial-r2_20260515T063659_result.json`
- **Structured JSON:** [`14a18bea851b1ca8edad.json`](../../sessions/14/14a18bea851b1ca8edad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

日志读取完毕。结果如下：

**T9 task name:** `pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate`

**T9 success rate:** 1/10 (10%)

**合并 10-task overall:** (33 + 1) / 100 = **34% (34/100)**

**异常检查:** 无异常。EXIT_CODE=0，无 crash、NaN、GPU error。日志末尾有一个 `DeprecationWarning: builtin type swigvarlink has no __module__ attribute`，是 SWIG 绑定的无害警告，不影响结果。

**与 baselines 对比：**

| 方法 | LIBERO-Spatial 10-task |
|------|----------------------|
| VLA-only K=1 | 30% |
| VLA-mean K=10 | 31% |
| **Argmin K=10** | **34%** |

Argmin baseline 比 VLA-only (+4%) 和 VLA-mean (+3%) 略高，但提升幅度有限。K=10 采样 + scalar Euclidean argmin 选择带来的增益不显著。

---
