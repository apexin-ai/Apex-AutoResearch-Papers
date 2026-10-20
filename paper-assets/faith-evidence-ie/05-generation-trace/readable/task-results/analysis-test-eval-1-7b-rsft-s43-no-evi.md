# analysis test eval 1 7b rsft s43 no evi

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_test_eval_1_7b_rsft_s43_no_evi_20260523T083247_result.json`
- **Structured JSON:** [`07157d1c97fe6e7f243d.json`](../../sessions/07/07157d1c97fe6e7f243d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE。汇总：

**Metrics**

| 指标 | 值 |
|------|-----|
| ign_f1 | 0.2410 |
| precision | 0.4282 |
| recall | 0.1677 |
| f1 | 0.2410 |
| format_ok_rate | 97.6% |
| n_documents | 500 |
| n_truncated | 472 |
| inference_time | 2348.7s |

**Evidence Tax**

- s43: no_evi(0.2410) - with_evi(0.2870) = **-4.59pp**
- s42: no_evi(0.2390) - with_evi(0.2933) = **-5.43pp**

方向一致（均为负，no_evi 劣于 with_evi），s43 tax 幅度比 s42 小 0.84pp。Evidence 对 RE 性能有正面贡献，跨 seed 稳定。

---
