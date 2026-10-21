# ops batch kill preparing

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_batch_kill_preparing_20260529T062725_result.json`
- **Structured JSON:** [`aede7feb533d4c5f8b87.json`](../../sessions/ae/aede7feb533d4c5f8b87.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 96 个实验 PENDING → DONE 转换成功。

**最终统计：**
- 总计 PREPARING 实验：97 个
- 成功清理：**97 个**（含先前测试的 `eval_pi05_attn_k095_long_seed47_cqa1_v3`）
- 失败：**0 个**

每个实验均完成三步清理：`conclusion=killed` → `status=PENDING` → `status=DONE`。

---
