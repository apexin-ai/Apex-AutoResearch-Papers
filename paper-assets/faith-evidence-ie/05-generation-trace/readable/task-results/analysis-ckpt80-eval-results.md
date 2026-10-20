# analysis ckpt80 eval results

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_ckpt80_eval_results_20260515T005922_result.json`
- **Structured JSON:** [`66d291a0f846f7f0e58e.json`](../../sessions/66/66d291a0f846f7f0e58e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**ckpt-80 eval 结果** (negative):

| 指标 | 值 |
|------|-----|
| rel_f1 | **0.0116** |
| precision | 0.0109 |
| recall | 0.0124 |
| evi_f1 | 0.8280 |
| edcr | 0.9908 |
| format_ok_rate | 0.9990 |
| pred_count | 13,828 (gold: 12,151) |
| inference_time | 6,099s |

**GRPO lr5e6 完整轨迹**:

| checkpoint | rel_f1 | evi_f1 |
|-----------|--------|--------|
| ckpt-20 | 0.0077 | — |
| ckpt-40 | 0.0071 | — |
| ckpt-60 | 0.0093 | — |
| ckpt-80 | 0.0116 | 0.828 |
| SFT baseline | **0.406** | **0.798** |

rel_f1 在 0.007–0.012 区间平坦，无恢复信号。evi_f1 虽高（0.828 > SFT 的 0.798），但 relation 分类彻底崩溃——pred_count=13,828 几乎全是噪声预测，tp 仅 151。

Registry 已更新：`mvp2_eval_lr5e6_r1_ckpt80` → DONE/negative。

---
