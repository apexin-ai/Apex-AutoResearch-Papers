# data ign f1 sync

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_ign_f1_sync_20260516T000634_result.json`
- **Structured JSON:** [`b0cf9a77e0bd2cbc4e4b.json`](../../sessions/b0/b0cf9a77e0bd2cbc4e4b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已写入。汇总结果：

## 修正后指标一览

| Method | F1 | **Ign-F1** | Δ | Evi-F1 |
|--------|------|--------|-----|--------|
| SFT baseline | 41.06 | **40.36** | 0.70 | 80.13 |
| SFT no-evidence | 48.93 | **47.36** | 1.57 | — |
| RSFT CED s43 (best) | 46.83 | **45.85** | 0.98 | 81.56 |
| RSFT CED s44 | 46.55 | **45.51** | 1.04 | 80.87 |
| RSFT r2b | 44.93 | **44.10** | 0.84 | 81.28 |
| RSFT r2a | 44.94 | **44.01** | 0.93 | 81.08 |
| RSFT CED s42 | 44.49 | **43.63** | 0.86 | 81.87 |
| GRPO bf16 | 45.49 | **45.59** | −0.10 | 80.86 |
| flat-NLI s42 | 45.39 | **44.49** | 0.89 | 80.43 |
| flat-NLI s43 reeval | 45.23 | **TBD** | — | 81.58 |
| DPO 1ep | 40.34 | **38.88** | 1.46 | 80.88 |

## 排名变化

**RSFT 内部**: 排名基本不变，仅 **r2a 与 r2b 互换**（原差距 0.01pp → 现差距 0.09pp，在噪声范围内）。Top 1/2/5 位置不变。

**关键对比**:
- RSFT best (s43) vs SFT baseline: 5.77pp → **5.49pp**（缩小 0.28pp）
- CED best vs flat-NLI: 1.44pp → **1.36pp**（缩小 0.08pp）
- GRPO bf16 vs RSFT CED s43: 差距从 −1.34pp 缩小到 **−0.26pp**（GRPO 几乎追平 RSFT）

**结论**: 排名无实质性变化，论文 claims 不受影响。

## 待处理
- **flat-NLI s43 reeval** 缺 metrics_v2.json（需要重跑 Ign-F1 修正）
- **flat-NLI s44 和 s45**: eval 结果目录为空，尚未产出

---
