# analysis c4 a025 s42 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_c4_a025_s42_fp32_20260519T221710_result.json`
- **Structured JSON:** [`b9e2f2898bbf65159186.json`](../../sessions/b9/b9e2f2898bbf65159186.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结果：

**c4_a025_s42_fp32 — PermG=0/8, K≥3=8/8, K≥4=3/8**

| 指标 | 结果 |
|------|------|
| permg_fwd_fdr | **0/8** |
| permg_rev_fdr | **0/8** |
| consensus_K3_3sigma | **8/8** |
| consensus_K4_3sigma | **3/8** |
| threshold_onset | 8/8 |
| naive_xcorr | 8/8 |
| diff_xcorr | 8/8 |
| ty_granger | 3/8 |

**Drift:** token_entropy -53.01%, mauve -52.08%, perplexity +3617%, distinct_1 -4.10%

**与 parent α=0.50 对比：** PermG 从 8/8 骤降到 0/8，相关/阈值方法仍为 8/8。PermG 的 raw p-values 在 0.03–0.09 范围，部分 nominally significant 但全部无法通过 BH FDR 校正。

**Onset 结论：** C4 PermG onset ∈ (0.25, 0.50]，与 WikiText onset ∈ (0.40, 0.50] 重叠。PermG 在 α=0.25 未检测到 → 不能证明 C4 onset 严格低于 WikiText。需要 C4 α=0.30/0.35/0.40 的实验才能分离两个域的 onset。

报告已注册：`artifacts/c4_a025_s42_fp32/report/c4_a025_s42_fp32_analysis.md`
Registry 已更新为 DONE(success)。

---
