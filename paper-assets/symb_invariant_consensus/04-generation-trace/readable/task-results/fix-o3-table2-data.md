# fix o3 table2 data

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_o3-table2-data_20260523T124144_result.json`
- **Structured JSON:** [`c7a793b1926d6b2e469c.json`](../../sessions/c7/c7a793b1926d6b2e469c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成。最终报告：

---

**o3 原始数据来源：**
- `/root/symb_invariant_consensus/results/exp_d135_frontier_scb/o3/results.json`
- `/root/symb_invariant_consensus/results/exp_d135_frontier_scb/o3/cross_model/o3_full_metrics.json`

**根本原因：**
o3 有 8 个问题（folio_1, 2, 5, 41, 87, 109, 110, 171）所有 12 条 trace 均返回空字符串（API failure），导致 `n_valid=196`。实验代码以 196 为分母计算 SC=162/196=82.65%，而非 204。

**当前值在 n=196 上是内部一致的：**
- SC = 162/196 = 82.65% ✓
- n_err = 196-162 = 34 ✓
- BR = 1.66（mean_br=1.6565，在 34 个错误实例上计算，其中 28 个 BR=∞，6 个有限）✓
- Δ = 0.00（SICA=SC）✓

**修改：**
- `analysis.tex` L31: o3 → o3$^\dagger$
- `analysis.tex` L17 caption: 添加 `$^\dagger$8 API-failure questions excluded ($n = 196$).`

**其他行整数一致性：** 全部通过（Mistral 114/204, Qwen 155/204, R1-Distill 152/204, gpt-4o 157/204, gpt-4.1 169/204, gpt-5.5 172/204, Gemini 83/95）。

**BR 范围引用（$1.66$--$4.97\times$）：** abstract、analysis L11/59/60 均引用 o3 的 BR=1.66 作为下界，值不变，无需修改。

**建议（非必须）：** 如果投稿前有时间，可以重新跑 o3 的 8 个失败问题以获得完整 n=204 数据，消除脚注。

---
