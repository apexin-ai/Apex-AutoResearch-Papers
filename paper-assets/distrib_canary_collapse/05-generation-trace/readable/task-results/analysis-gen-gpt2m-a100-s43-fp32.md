# analysis gen gpt2m a100 s43 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gen_gpt2m_a100_s43_fp32_20260519T150935_result.json`
- **Structured JSON:** [`dfc00815a6b2d0f1442b.json`](../../sessions/df/dfc00815a6b2d0f1442b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结论：

**Verdict: NEGATIVE** (K≥4 = 1/8 < 4/8 threshold)

| 指标 | s42 (bf16) | s43 (fp32) |
|------|:----------:|:----------:|
| K≥4 | 6/8 | **1/8** |
| PermG_fwd | 6/8 | **8/8** |
| PermG_rev | 3/8 | 5/8 |
| Diff XCorr | 8/8 | 8/8 |
| Threshold | 8/8 | **0/8** |
| TY | 5/8 | 4/8 |
| final_ppl | 16520 | 15024 |
| entropy_drift | -86.6% | -83.6% |

K≥4 下降的根因不是 lead-lag 信号消失——PermG_fwd 反而从 6/8 升至 8/8。问题在于 threshold_onset 方法全军覆没（8/8→0/8）：token_entropy 在 Gen 0→1 暴跌 55%（3.57→1.59），collapse 太快导致 3σ threshold 无法测量 lead time。naive xcorr 的 peak lag 也因此偏向负值。如果只看 Granger-class 方法（perm+TY+diff），forward consensus ≥2/3 的 pairs = 8/8。

报告已写入 `artifacts/gen_gpt2m_a100_s43_fp32/report/gpt2m_s43_fp32_analysis.md`。

---
