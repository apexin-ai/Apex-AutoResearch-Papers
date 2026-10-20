# analysis tau 095 seed42

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_tau_095_seed42_20260515T182338_result.json`
- **Structured JSON:** [`bd80f7f9ea25c2790a46.json`](../../sessions/bd/bd80f7f9ea25c2790a46.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

## tau_095_seed42 结果

| 指标 | 值 |
|------|-----|
| **eval_ppl** | **17.723** (+0.070 vs baseline) |
| eval_loss | 2.8749 |
| train_loss | 10.198 |
| b* mean | 3.078 (baseline: 1.399) |
| b* median | 1.520 (baseline: 0.871) |
| b* ≥2 占比 | 40.3% (baseline: 16.1%) |
| **conclusion** | **negative** |

## τ sweep 全景

| τ | PPL | Δ vs baseline | b* mean | 结论 |
|---|-----|---------------|---------|------|
| 0.5 | 17.688 | +0.035 | 0.392 | success |
| 0.6 | 17.681 | +0.028 | 0.590 | success |
| 0.7 | 17.679 | +0.027 | 0.894 | success |
| **0.8** | **17.653** | **baseline** | **1.399** | **baseline** |
| 0.9 | 17.712 | +0.059 | 2.360 | negative |
| 0.95 | 17.723 | +0.070 | 3.078 | negative |

τ=0.95 确认了 τ 的上界边界。τ 在 [0.5, 0.8] 范围内鲁棒（max Δ=0.035），超过 0.8 后单调退化。Claim 3 应调整 framing 为 "τ robust in [0.5, 0.8]"。

---
