# analysis gemma2 n3 bootstrap ci

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gemma2-n3-bootstrap-ci_20260521T023757_result.json`
- **Structured JSON:** [`8b45b2406d6c189e55d9.json`](../../sessions/8b/8b45b2406d6c189e55d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Gemma-2-9B n=3 BCa Bootstrap CI 结果

| Benchmark | Δ per seed (pp) | Mean Δ | 95% BCa CI | Excludes 0 | Pattern |
|-----------|-----------------|--------|------------|------------|---------|
| **MMLU** | +1.90, +3.76, +1.49 | **+2.38** | **[+1.49, +3.14]** | **✓** | Benefit |
| **ARC** | -1.97, -1.20, +2.73 | **-0.15** | **[-1.97, +1.42]** | ✗ | Inconclusive |

**Family-level:** Dir-Con = **✗** (MMLU consistently positive, ARC mixed)

### 与 n=2 对比

| | n=2 | n=3 | 变化 |
|---|---|---|---|
| **MMLU mean** | +2.62pp | +2.38pp | 均值略降 |
| **MMLU CI** | [-11.81, +17.06] (width=28.87) | [+1.49, +3.14] (width=1.65) | **CI 缩窄 17.5×，且排除 0** |
| **ARC** | +2.73pp (n=1, 无 CI) | -0.15pp [-1.97, +1.42] | s0/s42 加入后均值翻转为负 |

关键发现：
- MMLU 的 n=2→n=3 CI 收窄极为显著（28.87→1.65），第三个 seed 确认了 contamination benefit
- ARC 的 n=1 点估计 +2.73pp 完全来自 s123；加入 s0(-1.97) 和 s42(-1.20) 后均值翻转，说明 s123 是 outlier
- 两个 benchmark 方向不一致，与 Qwen-7B（两个 benchmark 均为 Benefit）形成对比

---
