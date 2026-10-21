# ops verify ced fix remote

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-ced-fix-remote_20260514T193500_result.json`
- **Structured JSON:** [`fdeb8a1ed863e5c6075f.json`](../../sessions/fd/fdeb8a1ed863e5c6075f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**VERIFIED: `--ced_recall_penalty` flag exists on remote.**

完整逻辑链路确认：
- **L406**: `argparse` 定义 `--ced_recall_penalty`（`store_true`, 默认 `False`）
- **L475**: 传递给 `CEDRewardWrapper` 的 `recall_penalty` 参数
- **L157/L165**: 构造函数接收并存储为 `self.recall_penalty`
- **L283-285**: 实际逻辑——当 `recall_penalty=True` 且有 gold_map 时，`mean_ced *= recall`，即用 recall 乘以 CED 得分来惩罚 under-prediction

---
