# analysis a025 s44 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_a025_s44_fp32_20260519T135814_result.json`
- **Structured JSON:** [`2f4005c1e7c722ea366b.json`](../../sessions/2f/2f4005c1e7c722ea366b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### s44 关键指标

| 指标 | Gen 0 | Gen 9 | Drift |
|------|-------|-------|-------|
| distinct_1 | 0.0974 | 0.0600 | **-38.35%** |
| distinct_2 | 0.513 | 0.239 | -53.44% |
| distinct_3 | 0.814 | 0.363 | -55.35% |
| token_entropy | 3.234 | 3.101 | -4.11% |
| ece | 0.0108 | 0.0182 | +68.01% |
| perplexity | 26.95 | 22.57 | -16.27% |
| mauve | 0.032 | 0.019 | -40.63% |
| eff_rank | 46.61 | 46.21 | -0.87% |

**Detection**: PermG=0/8, K≥4=0/8, MMCT=0.0, TY=1/8

### 3-Seed 对比 (α=0.25)

| | s42 | s43 | s44 |
|--|-----|-----|-----|
| PermG fwd | 0/8 | 0/8 | **0/8** |
| K≥4 | 0/8 | 0/8 | **0/8** |
| MMCT | 0.0 | 0.0 | **0.0** |
| d1 drift | -39.15% | -38.95% | **-38.35%** |
| TY Granger | 3/8 | 6/8 | 1/8 |

**Conclusion**: α=0.25 blind zone 上界 3-seed 验证通过。PermG=0/8 在三个 seed 完全一致，d1 drift 跨 seed 标准差仅 0.33pp。TY Granger 持续 seed 不稳定 (1→3→6/8)，再次确认 C003。多样性塌缩真实存在 (d1≈-38.8%) 但 canary 信号不足以被 Granger 检测。

---
