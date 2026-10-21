# analysis alpha sweep a050 s42 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_alpha_sweep_a050_s42_fp32_20260519T100331_result.json`
- **Structured JSON:** [`ea5baa8d30801c2cb3ce.json`](../../sessions/ea/ea5baa8d30801c2cb3ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE。

## 汇总：α=0.50 fp32 三种子对比

| Metric | s42 | s43 | s44 |
|---|---|---|---|
| token_entropy_gen0 | 3.2342 | 3.2342 | 3.2342 |
| token_entropy_gen10 | 2.7075 | 2.7227 | 2.7252 |
| token_entropy_drift | -16.3% | -15.8% | -15.7% |
| distinct_1_gen0 | 0.0916 | 0.0929 | 0.0929 |
| distinct_1_gen10 | 0.0649 | 0.0660 | 0.0669 |
| distinct_1_drift | -29.2% | -29.0% | -28.0% |
| perplexity_gen0 | 26.95 | 26.95 | 26.95 |
| perplexity_gen10 | 31.46 | 31.58 | 31.10 |
| perplexity_drift | +16.8% | +17.2% | +15.4% |
| ece_gen0 | 0.0108 | 0.0108 | 0.0108 |
| ece_gen10 | 0.0868 | 0.0842 | 0.0890 |
| ece_drift | +703.4% | +679.6% | +724.1% |
| **perm_granger_fwd** | **6/8** | **6/8** | **6/8** |
| perm_granger_rev | 0/8 | 0/8 | 0/8 |
| ty_granger_fwd | 4/8 | 5/8 | — |
| **consensus_k4** | **6/8** | **6/8** | **6/8** |
| mmct_wpair_fwd | 6/8 | 6/8 | 6/8 |

**结论**：3-seed 完全一致。PermG fwd=6/8、consensus_k4=6/8、MMCT=6/8 跨种子稳定复现，rev=0/8 确认方向性。α=0.50 boundary regime 的 canary lead-lag 信号在 fp32 下稳健成立。

**注意事项**：
- TY Granger 跨种子不稳定（4/8 vs 5/8），符合 C003 约束（α≤0.50 下 TY 不可靠）
- D093 padding_side fix 未应用（3443 次 right-padding 警告），三个种子条件一致
- Wall clock: 4.58 GPU-hours，EXIT_CODE=0

---
