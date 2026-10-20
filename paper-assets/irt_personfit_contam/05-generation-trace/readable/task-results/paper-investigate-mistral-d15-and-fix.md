# paper investigate mistral d15 and fix

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_investigate-mistral-d15-and-fix_20260524T065337_result.json`
- **Structured JSON:** [`a6977281839f586ef43e.json`](../../sessions/a6/a6977281839f586ef43e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 产出总结

### 1. 调查报告：contam_15_results.json 来源

**结论：用新值 lz\*=-1.3849，更新 d=-2.64**

- `contam_15_results.json` 是 May 21 统一重算的一部分（所有 clean 和 contam 文件均在 May 21-22 窗口内修改）
- `bca_bootstrap.py`（May 24 创建）的 10 个 clean seed lz\* 与 May 21 重算完全一致，但 contam_15 lz\*=-2.1468 是旧值（重算前）
- `theta_fixed_n10_recompute.json` 已经使用了 May 21 重算数据（`lz_star_free: -1.3849`），确认 fixed-θ d=2.69 正确

### 2. ARC-C 50% CI 修复

bca_bootstrap percentile CI = [3.630, 15.150] → 四舍五入 [3.6, 15.2]，与论文一致。**无需修改。**

### 3. 所有改动

| 位置 | 旧值 | 新值 |
|------|------|------|
| Table 1 (results.tex:30) | d=-3.01 CI=[-8.2,-1.8] | d=-2.64 CI=[-7.3,-1.5] |
| Table 2 (results.tex:91) | d_free=3.01, ratio=0.9× | d_free=2.64, ratio=1.0× |
| Table 3 (results.tex:151) | d=3.01 CI=[1.8,8.2] | d=2.64 CI=[1.5,7.3] |
| 正文 (results.tex:10) | Mistral \|d\|=3.01/3.50 | Mistral \|d\|=2.64/3.50 |
| gen_fig_heatmap.py | 3.01, CI [1.8,8.2] | 2.64, CI [1.5,7.3] |
| gen_fig_theta_scatter.py | (3.01, 1.75, 8.18) | (2.64, 1.49, 7.29) |

### 4. PDF 页数：**16 页**

### 5. 匿名 repo push：**成功** (`2421ca8..601aca3 main → main`)

---
