# analysis test eval llama rsft s42 no evi v2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_test_eval_llama_rsft_s42_no_evi_v2_20260523T130450_result.json`
- **Structured JSON:** [`3f06784bf378b896927e.json`](../../sessions/3f/3f06784bf378b896927e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

**Ign-F1 = 0.3380**（batch_size=16），比原 s42 no-evi（batch_size=1, 0.3334）高 **+0.46pp**。

**Evidence tax（s42 修正后）**：0.3380 - 0.3554 = **-1.74pp**（原 -2.20pp 被 batch_size 差异放大了）

**Multi-seed 修正**：
- 均值：-1.69pp → **-1.46pp**
- 跨 seed 方差减半（spread 1.03pp → 0.57pp）
- 两个 seed 一致显示 evidence 有帮助，s42 受益更大

Registry 已更新为 DONE/success，报告已注册。

---
