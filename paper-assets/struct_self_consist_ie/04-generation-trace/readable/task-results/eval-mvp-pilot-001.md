# eval mvp pilot 001

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_mvp_pilot_001_20260514T074023_result.json`
- **Structured JSON:** [`40fa84d3b2c57c314113.json`](../../sessions/40/40fa84d3b2c57c314113.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果总结：

## mvp_pilot_001 结果

| 指标 | NER | RE |
|------|-----|-----|
| Greedy F1 | 61.1% | 35.5% |
| Oracle F1 | 78.0% | 57.2% |
| Headroom | +16.9pp | +21.7pp |
| Gold-empty filtered | 22 | 154 |
| All-samples-F1=0 filtered | 19 | 77 |
| Fleiss κ (mean) | 0.2449 | 0.0681 |
| Soft Jaccard (mean) | 0.5041 | 0.3635 |
| Full ρ(SJ,F1) | +0.3616 (n=529) | +0.2535 (n=397) |
| Full ρ(κ,F1) | +0.3515 (n=529) | +0.2885 (n=397) |
| Cond ρ(SJ,F1) | +0.3688 (n=510) | +0.3515 (n=320) |
| Cond ρ(κ,F1) | +0.3569 (n=510) | +0.3107 (n=320) |
| SJ > κ (full) | YES (+0.01) | NO (-0.03) |
| SJ > κ (cond) | YES (+0.01) | YES (+0.04) |
| Sample F1=0 | 20.4% | 58.3% |

**Verdict: FAIL** — RE full ρ_sj=0.2535 < 0.40 threshold, and SJ does not beat κ on the full set.

关键发现：
- **Parse failures**: 164/4408 stochastic, 29/551 greedy — 输出被 max_tokens=512 截断（greedy fail 的 raw output 都是有效 JSON 的前缀）
- **RE 的 conditional set 上 SJ 确实优于 κ**（+0.3515 vs +0.3107），但 full set 上不成立，因为大量 gold-empty（154）和 all-zero（77）instance 稀释了信号
- **Headroom 很大**（NER +16.9pp, RE +21.7pp），oracle best-of-8 有显著提升空间

---
