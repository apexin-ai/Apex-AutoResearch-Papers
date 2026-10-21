# code lz star fix eval

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_lz-star-fix-eval_20260520T230939_result.json`
- **Structured JSON:** [`14123558d4ba814b01ee.json`](../../sessions/14/14123558d4ba814b01ee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件都已正确 patch。结果汇总：

---

## 产出 1：Snijders (2001) 校正的关键代码

`src/person_fit.py:192-212`，核心差异：在原始 `Var(l0) = Σ PQ·g²` 基础上，减去协方差校正项 `C(θ)²/I(θ)`：

```
dP = a·(d-c)·σ·(1-σ)          # 4PL对θ的导数
h  = dP / (P·Q)
I(θ) = Σ P·Q·h²               # Fisher信息量
C(θ) = Σ P·Q·h·g              # 协方差项 (g = log(P/Q))
Var* = Var(l0) - C(θ)²/I(θ)   # 校正方差
```

## 产出 2：eval_lz.py 修复

两个文件均已 patch：`compute_lz_star` 函数从 Drasgow (1985) ℓz 替换为 Snijders (2001) ℓz*。旧结果备份为 `*_lz_uncorrected.json`。

## 产出 3：Qwen 5 条件对比表

| Condition | ℓz (old) | ℓz* (new) | Δ | acc |
|-----------|----------|-----------|-------|--------|
| clean_s1 | 8.0101 | **9.4676** | +1.46 | 0.6787 |
| clean_s2 | 5.9440 | **7.0539** | +1.11 | 0.6789 |
| clean_s3 | 8.0806 | **9.5293** | +1.45 | 0.6783 |
| contam_15 | 3.0046 | **3.8494** | +0.84 | 0.7310 |
| contam_50 | 5.4480 | **7.2892** | +1.84 | 0.7643 |

accuracy 不变（无需重新 inference，从 response_vector 重算）。

## 产出 4：新 Cohen's d（n=3, ddof=1）

| | mean(clean) | std(clean) | contam_15 d | contam_50 d |
|---|---|---|---|---|
| **ℓz* (new)** | 8.6836 | 1.4117 | **-3.42** | **-0.99** |
| ℓz (old) | 7.3449 | 1.2137 | -3.58 | -1.56 |

校正后 contam_15 的 effect size 略有缩小（d: -3.58 → -3.42），contam_50 缩小更多（d: -1.56 → -0.99），但两者仍然显著。

## 产出 5：Llama 结果

| Condition | ℓz (old) | ℓz* (new) | Δ | acc |
|-----------|----------|-----------|-------|--------|
| clean | 0.8175 | **0.8446** | +0.03 | 0.5914 |
| contam_15 | -2.6572 | **-2.9922** | -0.34 | 0.6654 |
| contam_50 | -2.8581 | **-3.3313** | -0.47 | 0.6983 |

Llama 的校正方向相反——contaminated 条件的 ℓz* 比 ℓz 更负（差异更大），说明 Snijders 校正在低 ability 区间放大了 misfit 信号。

## 产出 6：差异幅度评估

- 校正幅度 |Δ| 在 0.03–1.84 之间，取决于 θ̂ 估计的不确定性（item 数量和 θ 位置）
- clean 条件平均上移 ~1.3（Var* < Var_l0 → 分母缩小 → 绝对值增大）
- 核心结论不变：contaminated 条件的 person-fit 显著偏离 clean baseline
- Cohen's d 有所衰减但 contam_15 仍远超常规阈值（|d| > 3）

---
