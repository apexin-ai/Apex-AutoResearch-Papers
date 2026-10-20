# run mvp 002 re

**verifier tts struct ie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_mvp-002-re_20260511T192301_result.json`
- **Structured JSON:** [`455929544cacec657874.json`](../../sessions/45/455929544cacec657874.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## RE F1 矩阵 (micro-F1 %, 3 seeds 均值±std)

| N | greedy | exact_sc | freq_merge_best(k=?) | oracle | random |
|---|--------|----------|---------------------|--------|--------|
| 1 | 6.20 | — | — | — | — |
| 4 | — | 6.35±0.15 | 6.51±0.11 (k=2) | 8.83±0.22 | 6.40±0.63 |
| 8 | — | ❌ | ❌ | ❌ | ❌ |
| 16 | — | ❌ | ❌ | ❌ | ❌ |

**N=8/16 失效原因**: vLLM `n=8/16` 请求导致连接错误（N=8: 2016/2400 connection errors, 84%；N=16: 4800/4800, 100%）。单卡 RTX 5090 32GB + Qwen3-8B + max_model_len=4096 + n=8/16 超出 vLLM 并发序列限制。

### 有效结果 (N=1, N=4)

| 策略 | P | R | F1 |
|------|---|---|----| 
| N=1 greedy | 6.4 | 6.0 | 6.20 |
| N=4 exact_sc | 6.4 | 6.3 | 6.35±0.15 |
| N=4 freq_merge_k1 (union) | 4.7 | 9.0 | 6.18±0.29 |
| N=4 freq_merge_k2 | 6.7 | 6.3 | **6.51±0.11** |
| N=4 freq_merge_k3 | 8.6 | 4.7 | 6.10±0.09 |
| N=4 freq_merge_k4 (intersect) | 11.2 | 3.3 | 5.13±0.26 |
| N=4 oracle | 9.2 | 8.5 | 8.83±0.22 |
| N=4 random | 6.7 | 6.2 | 6.40±0.63 |

### 关键指标

- **Parse 成功率**: N=1: 97.0%, N=4: 98.2%, N=8: 13.8% (connection errors), N=16: 0%
- **Oracle-greedy gap (N=4)**: +2.63pt
- **Best aggregation vs greedy**: +0.31pt (freq_merge_k2)
- **Pass: aggregation@N≥8 > greedy ≥ 1.0pt?** **NO** (N≥8 数据无效)

### 关键对比: RE vs NER

| | NER | RE |
|---|-----|-----|
| Greedy F1 | ~39% | 6.2% |
| Oracle gap (N=4) | ~6.49pt | +2.63pt |
| Best agg vs greedy | +0.66pt | +0.31pt |

RE 整体 F1 极低 (6.2%)，说明 Qwen3-8B zero-shot RE 远比 NER 更难。Oracle gap +2.63pt 表明候选中有更优解，但 exact_sc 和 freq_merge 只能利用 0.31pt。N≥8 因 vLLM `n` 参数并发限制全部失败，需要改用循环调用（每次 n=1，循环 N 次）来获取 N=8/16 结果。

---
