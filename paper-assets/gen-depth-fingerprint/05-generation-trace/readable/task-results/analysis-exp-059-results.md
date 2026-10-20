# analysis exp 059 results

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_059_results_20260520T073622_result.json`
- **Structured JSON:** [`37a28983de6c7f0946d2.json`](../../sessions/37/37a28983de6c7f0946d2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

日志无 error，实验正常完成。结果如下：

## exp_059 TOST Bootstrap 结果

**配置**: n_bootstrap=1000, seed=42, margin(d)=0.2, α=0.05

| Feature | median_p | rejection_rate | p_ci_95 | median_d | d_ci_95 |
|---------|----------|---------------|---------|----------|---------|
| **entropy_max** | 0.0 | **100%** ✓ | [0.0, 0.0] | 0.062 | [0.037, 0.088] |
| **entropy_min** | 0.0 | **100%** ✓ | [0.0, 0.0] | −0.016 | [−0.042, 0.011] |
| **tail_decay** | 0.0 | **100%** ✓ | [0.0, 0.0] | 0.088 | [0.065, 0.111] |
| entropy_std | 1.0 | **0%** ✗ | [1.0, 1.0] | 0.458 | [0.435, 0.479] |

## 分析

**三个 stationary feature（entropy_max, entropy_min, tail_decay）在全部 1000 次 bootstrap 中 100% reject**，p 值的 95% CI 均为 [0.0, 0.0]，effect size d 全部远小于 margin 0.2。TOST equivalence 结论完全 robust，不受采样波动影响。

**entropy_std 如预期不通过**：median_d = 0.458 远超 margin 0.2，0% rejection rate，确认 depth 间差异实质性存在，不等价。

**总体结论**：TOST equivalence 在 bootstrap 下完全稳健。三个 stationary feature 的等价性是 robust finding，entropy_std 的非等价性同样稳定。这为论文中 "depth-stationary features" 的 claim 提供了强统计支撑。

---
