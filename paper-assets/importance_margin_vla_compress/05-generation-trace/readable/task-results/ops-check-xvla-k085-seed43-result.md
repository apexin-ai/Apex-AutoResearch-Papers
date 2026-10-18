# ops check xvla k085 seed43 result

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-xvla-k085-seed43-result_20260520T220212_result.json`
- **Structured JSON:** [`046edf6114687d6ee068.json`](../../sessions/04/046edf6114687d6ee068.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## X-VLA k=0.85 seed43 结果

**overall_success_rate = 67.6%** (338/500)，Wilson CI 95%: [63.4%, 71.6%]

### Per-task 明细

| Task | Description | Success Rate |
|------|-------------|-------------|
| 0 | alphabet soup → basket | **100%** |
| 1 | cream cheese → basket | 44% |
| 2 | salad dressing → basket | **100%** |
| 3 | bbq sauce → basket | 88% |
| 4 | ketchup → basket | 28% |
| 5 | tomato sauce → basket | 90% |
| 6 | butter → basket | **0%** |
| 7 | milk → basket | 94% |
| 8 | chocolate pudding → basket | 34% |
| 9 | orange juice → basket | 98% |

### 与 k=0.8 seed43 对比

- **k=0.80 seed43 = 88.4%**
- **k=0.85 seed43 = 67.6%**

**确认同 seed 非单调效应：k=0.85 比 k=0.80 保留更多 token，反而性能暴跌 20.8 个百分点。** butter 任务从有一定成功率直接降到 0%，ketchup/cream cheese/chocolate pudding 也大幅退化。这说明 keep_ratio 与性能的关系不是简单的单调递增，pruning 存在非平凡的甜蜜点。

---
