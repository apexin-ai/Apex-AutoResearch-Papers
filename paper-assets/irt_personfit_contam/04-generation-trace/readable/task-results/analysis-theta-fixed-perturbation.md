# analysis theta fixed perturbation

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_theta-fixed-perturbation_20260521T185843_result.json`
- **Structured JSON:** [`7604d4e3311638ec6864.json`](../../sessions/76/7604d4e3311638ec6864.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果：

| σ_rel | d_fixed_15 mean | d_fixed_15 SD | %bias_15 | d_fixed_50 mean | d_fixed_50 SD | %bias_50 |
|-------|-----------------|---------------|----------|-----------------|---------------|----------|
| 0%    | +4.77           | —             | —        | +14.52          | —             | —        |
| 5%    | +5.07           | 0.236         | 6.33%    | +14.76          | 0.443         | 1.62%    |
| 10%   | +4.95           | 0.430         | 3.74%    | +14.45          | 0.850         | 0.46%    |

验收：
1. **原始值验证** ✓ — d_fixed(15%)=+4.7695≈4.77, d_fixed(50%)=+14.5214≈14.52
2. **2水平×100 trials** ✓ — 5%和10%各100 trials
3. **表格+JSON输出** ✓ — 服务器 `/root/autodl-tmp/theta_fixed_perturbation_results.json`，已注册 artifact

θ-fixed Cohen's d 在参数扰动下非常稳健：即使10% noise，bias 不超过6.3%，SD也很小（d_fixed_50的CV仅~6%）。

---
