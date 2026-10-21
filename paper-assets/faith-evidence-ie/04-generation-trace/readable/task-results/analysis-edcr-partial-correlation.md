# analysis edcr partial correlation

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_edcr-partial-correlation_20260523T012127_result.json`
- **Structured JSON:** [`5beed0ee7d026415e387.json`](../../sessions/5b/5beed0ee7d026415e387.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已出。整理如下：

---

## Cross-method partial correlation

| Method | ign_f1 | EDCR | evi_f1_tp |
|--------|--------|------|-----------|
| SFT 4B s42 | 0.3974 | 0.6982 | 0.7986 |
| DPO-CED 1ep 4B | 0.4034 | 0.7139 | 0.8088 |
| RSFT CED 4B s42 | 0.4423 | 0.6569 | 0.8174 |
| GRPO 4B | 0.4446 | 0.6489 | 0.8053 |
| RSFT flat-NLI 4B s42 | 0.4448 | 0.6458 | 0.8039 |
| RSFT CED 4B s43 | 0.4512 | 0.6542 | 0.8063 |
| RSFT CED 4B s44 | 0.4511 | 0.6350 | 0.8050 |
| RSFT flat-NLI 4B s43 | 0.4523 | 0.6505 | 0.8158 |
| SFT 1.7B s42 | 0.4786 | 0.6704 | 0.8316 |
| SFT 8B s42 | 0.5051 | 0.6510 | 0.8188 |
| RSFT CED 1.7B s42 | 0.5122 | 0.6224 | 0.8243 |
| SFT Llama-8B s42 | 0.5384 | 0.6280 | 0.8151 |
| RSFT CED 8B s42 | 0.5376 | 0.6231 | 0.8136 |
| RSFT CED 8B s43 | 0.5471 | 0.6094 | 0.8180 |
| RSFT CED Llama s44 | 0.5587 | 0.5829 | 0.8328 |
| RSFT CED Llama s43 | 0.5662 | 0.5783 | 0.8287 |
| RSFT CED Llama s42 | 0.5714 | 0.5799 | 0.8238 |

**All 17 data points:**
- Spearman ρ (n=17): **-0.8554**, p=0.000012
- Partial ρ controlling evi_f1_tp (n=17): **-0.8541**, p=0.000025
- Partial ρ controlling evi_f1_tp (n=16, no GRPO): **-0.8681**, p=0.000027

**7 unique methods subset (one per method category):**
- Spearman ρ (n=7): **-0.9643**, p=0.000454
- Partial ρ controlling evi_f1_tp (n=7): **-0.9617**, p=0.002176

关键发现：控制 evi_f1_tp 后 partial ρ 几乎不变（-0.8554 → -0.8541），说明 EDCR 与 ign_f1 的负相关**不是由 TP 的机械性传导造成的**。evi_f1_tp 在各方法间变化极小（0.80-0.83 的窄区间），不是混淆因素。

## Per-relation permutation test

- Observed Spearman ρ (n=76 relations with TP>0): **-0.9381**
- Permutation p-value (10000 perms): **p < 0.0001**（0 次 permutation 达到观测值）
- 95th percentile of |null ρ|: 0.2252, max |null ρ|: 0.5142
- With all 93 relations (including TP=0): ρ=-0.9660

## Similar-TP different-EDCR pairs

找到 **48 对**满足 |TP_diff_rel| < 5% 且 |EDCR_diff| > 0.05 的方法对。最显著的例子：

| Method A | Method B | evi_f1_tp_A | evi_f1_tp_B | EDCR_A | EDCR_B | EDCR_diff |
|----------|----------|-------------|-------------|--------|--------|-----------|
| DPO-CED 1ep 4B | RSFT CED Llama s43 | 0.8088 | 0.8287 | 0.7139 | 0.5783 | 0.1356 |
| DPO-CED 1ep 4B | RSFT CED Llama s42 | 0.8088 | 0.8238 | 0.7139 | 0.5799 | 0.1340 |
| SFT 4B s42 | RSFT CED Llama s43 | 0.7986 | 0.8287 | 0.6982 | 0.5783 | 0.1199 |
| DPO-CED 1ep 4B | RSFT CED 8B s43 | 0.8088 | 0.8180 | 0.7139 | 0.6094 | 0.1045 |
| SFT 1.7B s42 | RSFT CED Llama s43 | 0.8316 | 0.8287 | 0.6704 | 0.5783 | 0.0921 |

DPO-CED 1ep 与 RSFT CED Llama 的 evi_f1_tp 差异仅 2.4%，但 EDCR 差异达 0.136，证明 EDCR 捕获了 TP 之外的独立证据质量信息。

**注**: DPO 3ep 无有效 eval 数据（ckpt400 目录为空）。

---
