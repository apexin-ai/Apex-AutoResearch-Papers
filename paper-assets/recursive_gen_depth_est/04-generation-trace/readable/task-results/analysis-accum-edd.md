# analysis accum edd

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_accum_edd_20260522T021351_result.json`
- **Structured JSON:** [`0dcfee7c6722785e00ae.json`](../../sessions/0d/0dcfee7c6722785e00ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

| Cell | Type | d0v1 AUC | d1v2 AUC | d2v3 AUC | EDD_0.70 |
|------|------|----------|----------|----------|----------|
| GPT-2 XL nucleus | full-rep | 0.9941 | 0.9131 | 0.8829 | 3 |
| GPT-2 XL nucleus | accum25 | 0.9995 | 0.8168 | 0.7258 | 3 |
| OLMo temp09 | full-rep | 0.9960 | 0.9010 | 0.8214 | 3 |
| OLMo temp09 | accum25 | 1.0000 | 0.8481 | 0.7585 | 3 |
| Pythia nucleus | full-rep | 0.9975 | 0.8607 | 0.8005 | 3 |
| Pythia nucleus | accum25 | 0.9998 | 0.8090 | 0.7486 | 3 |

所有 6 个 cell 的 EDD_0.70 均为 3（所有 adjacent pair AUC 都 >= 0.70）。

Accumulation mix25 相比 full-replacement 的 AUC 下降幅度：
- **d0v1**: 几乎无变化（accum 反而略高，因为 d0 特征极易区分）
- **d1v2**: 下降 ~0.05–0.10（GPT-2 XL 降幅最大 0.096，OLMo 最小 0.053）
- **d2v3**: 下降 ~0.05–0.16（GPT-2 XL 降幅最大 0.157，OLMo 最小 0.063）

结果已保存到 `results/accumulation_edd/edd_comparison.json`。

---
