# analysis alpha sweep a035 s42 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_alpha_sweep_a035_s42_fp32_20260519T190358_result.json`
- **Structured JSON:** [`b0e9daaf8849ecefdd23.json`](../../sessions/b0/b0e9daaf8849ecefdd23.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。

## 摘要：alpha_sweep_a035_s42_fp32

**Conclusion: success** — Pythia-410M, WikiText-103, α=0.35, seed=42, fp32, 10 gen 正常完成。

### MMCT 指标

| 方法 | 结果 |
|------|------|
| PermG fwd | **0/8** |
| PermG rev | **0/8** |
| K≥3 | 6/8 |
| K≥4 | **2/8** (token_entropy→d1, ece→d1) |
| threshold_onset | 8/8 |
| naive_xcorr fwd | 8/8 |
| diff_xcorr fwd | 4/8 |
| TY Granger | 4/8 (⚠️ C003: 低α下不可靠) |

### Drift
- token_entropy: -18.53%, ece: +651.26%, distinct_1: -36.38%, distinct_3: -50.04%, mauve: -17.78%

### Onset boundary 含义

**PermG=0/8 符合预期——α=0.35 仍在 blind zone。** Permutation Granger（最严格的因果检验）在双向均无显著对，与 α=0.30 行为一致。虽然 threshold_onset 8/8 和 K≥3 6/8 显示弱方法能检测到 lead-lag 模式，但这些弱信号不构成 causal evidence。onset boundary 下界确认 ≥ 0.35，需结合 a040_s42_fp32 结果判定 onset 是否在 [0.35, 0.40] 区间。

---
