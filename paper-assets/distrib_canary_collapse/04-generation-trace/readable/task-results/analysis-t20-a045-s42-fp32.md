# analysis t20 a045 s42 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_t20_a045_s42_fp32_20260520T201645_result.json`
- **Structured JSON:** [`1ee0508e623badb63432.json`](../../sessions/1e/1ee0508e623badb63432.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果汇总：

## T=20 α=0.45 验证结果

| 指标 | 预测 | 观测 |
|------|------|------|
| **PermG FDR fwd** | **0/8** | **5/8** |
| PermG FDR rev | 0 | 0 |
| Diff XCorr FDR fwd | — | 7/8 |
| Threshold onset fwd | — | 4/8 |
| TY Granger fwd | — | 2/8 |
| Robust pairs (K≥3) | — | 3/8 |

**Verdict: FAIL** — 点预测错误（0→5），但观测率 0.625 落在 bootstrap 95% CI [0.015, 0.828] 内。

**核心发现：Blind zone 是统计功效问题，不是 fundamental limit。** T=10 下 α=0.45 PermG=0/8，T=20 下恢复到 5/8——phase boundary α_c 随 T 左移。方向性强烈（5 fwd, 0 rev），确认因果方向为 canary→downstream。

**Near-miss:** token_entropy→distinct_1 的 p_fdr=0.052（差 0.002 就显著），无 FDR 校正时 6/8 pairs 显著。Mauve pairs 一致不显著（p>0.35）。

产出已注册（`art_20260520_2cc923`），实验状态已更新为 DONE(success)。

---
