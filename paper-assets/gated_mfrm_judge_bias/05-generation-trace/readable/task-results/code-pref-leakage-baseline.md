# code pref leakage baseline

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_pref_leakage_baseline_20260522T010225_result.json`
- **Structured JSON:** [`72e1b5d7fbd10f7dccc7.json`](../../sessions/72/72e1b5d7fbd10f7dccc7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 6 个测试通过。

## 结果汇总

**PLS 公式:**
```
WR(i, j) = 模型 i 在 judge j 下的胜率
AVG(i, j) = [WR(i,i) + WR(i,j)] / 2
PLS(i, j) = {[WR(i,i) - WR(i,j)] / [WR(i,i) + WR(i,j)] + [WR(j,j) - WR(j,i)] / [WR(j,j) + WR(j,i)]} / 2
```

PLS > 0 表示 judge 对其关联模型存在系统性偏好泄露，值越大泄露越严重。

**测试结果:**
| 场景 | 结果 |
|------|------|
| No leakage (judges agree) | PLS = 0.000 |
| Strong leakage (80% self-preference) | PLS ≈ 0.37-0.40 |
| Asymmetric leakage (one judge biased) | PLS = 0.457 |
| Paper example (Mistral-GPT4o vs Gemini) | PLS = 0.211 (paper: 0.184) |
| Random tensor (no bias) | PLS max = 0.000 |
| Injected tensor leakage | Correctly detected per-judge preference |

**产出文件:**
- `/root/gated_mfrm_judge_bias/baselines/pref_leakage.py` — 完整实现，提供 `compute_pls()` 和 `fit_pref_leakage()` 双接口
- `/root/gated_mfrm_judge_bias/baselines/test_pref_leakage.py` — 6 个测试用例

---
