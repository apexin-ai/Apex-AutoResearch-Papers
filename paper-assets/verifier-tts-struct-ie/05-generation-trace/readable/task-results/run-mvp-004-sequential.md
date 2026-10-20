# run mvp 004 sequential

**verifier tts struct ie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_mvp-004-sequential_20260511T194930_result.json`
- **Structured JSON:** [`6f29540d7667bb50ed97.json`](../../sessions/6f/6f29540d7667bb50ed97.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果报告：

---

## Sequential Self-Refinement NER 结果

### F1 per Round

| Round (K) | Compute | F1 (mean±std) | P | R | ΔF1 vs K=1 |
|-----------|---------|---------------|---|---|------------|
| 1 (greedy) | 1x | **42.21** | 43.7 | 40.8 | baseline |
| 2 | 2x | 42.33±0.38 | 42.7±1.7 | 42.0±1.0 | +0.12 |
| 3 | 3x | 41.98±0.51 | 41.9±2.5 | 42.2±1.6 | -0.23 |
| 4 | 4x | 41.98±0.51 | 41.7±2.9 | 42.4±2.1 | -0.23 |

### Sequential vs Parallel (matched compute)

| Compute | Sequential | Parallel freq_merge | Parallel oracle |
|---------|-----------|--------------------|--------------------|
| 1x | 42.21 (K=1) | 42.05 (N=1) | 42.05 |
| 2x | 42.33 (K=2) | ~42.3 (N=2) | ~44.0 |
| 4x | 41.98 (K=4) | 42.71 (N=4,k=2) | 45.92 |

### Pass/Fail

**sequential@K>=3 > greedy >= 1.0pt? NO**

Best sequential (K=3): 41.98 vs Greedy (K=1): 42.21, Delta: **-0.23**

### MVP FAIL — training-free TTS 不适用于 IE

### 关键发现

1. **Refinement 不改善 F1，反而退化**：Round 2 有微小提升 (+0.12)，Round 3/4 反而下降。3 个 seed 中有 2 个出现退化。
2. **Precision 下降，Recall 微升**：refinement 每轮 precision 降 ~2pt，recall 仅升 ~1.5pt，净效果为负。模型在 refinement 中添加了更多错误 entity，recall 的提升不足以弥补。
3. **Entity 类型分析**：Metric 类 F1 降 -4.9pt 最严重；Task 类 +2.1pt 是唯一明显提升。
4. **Sequential vs Parallel**：在 4x compute 下，sequential (41.98) 不如 parallel freq_merge (42.71)。parallel 至少有聚合筛选机制，sequential 完全依赖模型自我修正能力，Qwen3-8B 不具备这一能力。

---
