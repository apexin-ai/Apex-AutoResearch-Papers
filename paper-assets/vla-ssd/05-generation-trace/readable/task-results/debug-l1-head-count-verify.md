# debug l1 head count verify

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_l1_head_count_verify_20260517T215604_result.json`
- **Structured JSON:** [`05cb65458fb4accebca1.json`](../../sessions/05/05cb65458fb4accebca1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Got all the data. Here's the complete analysis:

```
=== L1 Per-Head Instruction Attention ===
Head  0: 0.8589 [dominant]
Head  1: 0.5308 [dominant]
Head  2: 0.6857 [dominant]
Head  3: 0.4749 [not]
Head  4: 0.5781 [dominant]
Head  5: 0.4976 [not]
Head  6: 0.4083 [not]
Head  7: 0.5673 [dominant]
Head  8: 0.5797 [dominant]
Head  9: 0.4300 [not]
Head 10: 0.7138 [dominant]
Head 11: 0.5671 [dominant]
Head 12: 0.5216 [dominant]
Head 13: 0.4147 [not]
Head 14: 0.7040 [dominant]
Head 15: 0.6226 [dominant]
Head 16: 0.5382 [dominant]
Head 17: 0.5290 [dominant]
Head 18: 0.5196 [dominant]
Head 19: 0.6500 [dominant]
Head 20: 0.5185 [dominant]
Head 21: 0.4537 [not]
Head 22: 0.8264 [dominant]
Head 23: 0.5683 [dominant]
Head 24: 0.3657 [not]
Head 25: 0.7706 [dominant]
Head 26: 0.5614 [dominant]
Head 27: 0.6854 [dominant]
Head 28: 0.4949 [not]
Head 29: 0.5971 [dominant]
Head 30: 0.5430 [dominant]
Head 31: 0.5552 [dominant]

Total >50%: 24/32
Head indices: [0, 1, 2, 4, 7, 8, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 22, 23, 25, 26, 27, 29, 30, 31]

=== Ablation Code Used ===
INSTRUCTION_HEADS_24 = [0, 1, 2, 4, 7, 8, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 22, 23, 25, 26, 27, 29, 30, 31]
Match with data: ✓ YES — exact match, both are the same 24 heads
```

**结论：**

| 来源 | 数量 |
|------|------|
| 原始数据 (`full_32layer_trained.json` L1 `n_instruction_dominant`) | **24** |
| Per-head 手动验证 (>50% threshold) | **24** |
| 消融脚本 (`INSTRUCTION_HEADS_24`) | **24** |

论文不一致处：
- Abstract "21-25 heads" — 这描述的是 L0 (21) 到 L1 (24) 的范围，不是 L1 单层
- Table 2 "25/32" — **错误**，应为 24/32
- 消融代码 24 个 — **正确**

Table 2 需要修正为 **24/32**。

---
