# analysis 8b block correlation cuda1

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_8b-block-correlation-cuda1_20260516T020114_result.json`
- **Structured JSON:** [`2c5a79868b77f37e1714.json`](../../sessions/2c/2c5a79868b77f37e1714.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 4B vs 8B Block-Correlation 对比

| 指标 | 4B (HumanEval/MBPP) | 8B (SWE-bench) | 变化 |
|------|-----|-----|------|
| ICC | 0.1909 | **0.3146** | +65% |
| Design Effect | 3.97 | **114.41** | +28.8x |
| Avg cluster size (k₀) | 16.54 | 361.42 | — |
| Per-problem error rate std | 0.1531 | **0.2195** | +43% |
| Expected std (i.i.d.) | 0.0812 | 0.0183 | — |
| Std ratio (observed/expected) | 1.89x | **11.99x** | — |
| N samples / K problems | 1890 / 114 | 9784 / 25 | — |
| Overall accuracy | 87.51% | 84.48% | — |
| p-value | 0.0000 | 0.0000 | — |

**注意**：DEFF 巨大的主要原因是 SWE-bench 的 cluster size 远大于 HumanEval/MBPP（361 vs 16.5）。ICC 是 scale-invariant 的更公平指标——8B 的 ICC (0.31) 显著高于 4B (0.19)，说明 8B 在 SWE-bench 上的错误更聚集于特定 problem。

### cuda:1 状态

**cuda:1 正在使用**（88% GPU util, 21133/32607 MiB）——正在跑 CWM 8B eval shard2。cuda:0 和 cuda:2 空闲。

---
