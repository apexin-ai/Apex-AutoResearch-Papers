# submit ced scoring topk3

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_ced_scoring_topk3_20260515T120100_result.json`
- **Structured JSON:** [`6e5c9a96a0e00f222aa9.json`](../../sessions/6e/6e5c9a96a0e00f222aa9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成：

- **mvp2_rsft_ced_scoring_topk3** 已提交到 `rtx5090-4x` cuda:3，tmux session `mvp2_rsft_ced_scoring_topk3`
- 输入：`/root/autodl-tmp/rsft_generations/generations.jsonl`（21952 records）
- 输出：`/root/autodl-tmp/rsft_filtered_topk3/`
- 参数：`--selection_strategy top_k --top_k 3 --f1_threshold 0.1 --tau 0.5`
- Registry 已更新为 RUNNING

mvp2_rsft_diagnosis 状态更新失败：当前为 PREPARING，不允许直接转 DONE。需要先转到合法中间状态。

---
