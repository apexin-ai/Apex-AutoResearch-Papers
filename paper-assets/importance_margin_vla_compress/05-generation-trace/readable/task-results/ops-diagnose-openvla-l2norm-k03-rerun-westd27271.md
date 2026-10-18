# ops diagnose openvla l2norm k03 rerun westd27271

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_diagnose-openvla-l2norm-k03-rerun-westd27271_20260521T125426_result.json`
- **Structured JSON:** [`60d7232f15bfc99880b7.json`](../../sessions/60/60d7232f15bfc99880b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**eval_openvla_l2norm_k03_object_seed42_rerun** — 已完成，registry 已更新。

| 指标 | 值 |
|------|-----|
| **Overall SR** | **25.0%** (125/500) |
| Vision tokens | 256 → 76 (k=0.3) |
| 耗时 | ~299 min |
| Seed | 42 |

Per-task SR:

| Task | SR |
|------|-----|
| ketchup | 66% |
| alphabet soup | 42% |
| milk | 36% |
| salad dressing | 28% |
| chocolate pudding | 28% |
| orange juice | 26% |
| bbq sauce | 10% |
| butter | 8% |
| cream cheese | 6% |
| tomato sauce | 0% |

**GPU 状态**: PID 193983 已结束。GPU 1 被 PID 921279 占用 (42180 MiB)。**GPU 0 空闲。**

---
