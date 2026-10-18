# check fewshot bcs status

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_fewshot_bcs_status_20260517T120917_result.json`
- **Structured JSON:** [`39337319f9021b873a64.json`](../../sessions/39/39337319f9021b873a64.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已完成，12/12 batch 全部跑完。

关键发现：**所有条件下 gap 均为负值或零**，即 low-BCS 子集表现 >= high-BCS 子集。count_8 上效果更明显（1-shot gap=-0.2083 最大），count_16 上几乎无差异（gap 接近 0）。

状态文件已写入 `artifacts/fewshot_bcs_status.md`。

---
