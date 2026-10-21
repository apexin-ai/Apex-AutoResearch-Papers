# ssh exp1 diagnose and launch exp2

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp1-diagnose-and-launch-exp2_20260514T230254_result.json`
- **Structured JSON:** [`552e50ec81ea35ebdc19.json`](../../sessions/55/552e50ec81ea35ebdc19.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Exp 2 正在运行，第一个 batch `count_6_low_bcs` 已开始处理。

---

## 汇报

### 1. Exp 1 最终状态：**成功完成**

94/94 batches 全部完成，耗时 12475.5s (~3.5h)。注意：代码中 `min(66, len(active_types))` = 64，实际最高档是 count_64 而非 count_66。

### 2. Exp 1 结果摘要

| Count | n | Exact F1 mean | median | min | max | Relaxed F1 mean | median | min | max |
|-------|---|--------------|--------|------|------|----------------|--------|------|------|
| 1 (solo) | 64 | 0.0111 | 0.0000 | 0.0000 | 0.1379 | 0.1168 | 0.1049 | 0.0000 | 0.3714 |
| 2 | 5 | 0.0092 | 0.0110 | 0.0000 | 0.0158 | 0.0668 | 0.0564 | 0.0407 | 0.0942 |
| 6 | 5 | 0.0031 | 0.0031 | 0.0000 | 0.0049 | 0.1030 | 0.0949 | 0.0868 | 0.1293 |
| 12 | 5 | 0.0081 | 0.0071 | 0.0033 | 0.0180 | 0.1455 | 0.1224 | 0.1153 | 0.2311 |
| 22 | 5 | 0.0127 | 0.0136 | 0.0055 | 0.0193 | 0.1851 | 0.1693 | 0.1581 | 0.2181 |
| 44 | 5 | 0.0177 | 0.0178 | 0.0156 | 0.0194 | 0.2467 | 0.2497 | 0.2305 | 0.2609 |
| 64 | 5 | 0.0132 | 0.0134 | 0.0126 | 0.0134 | 0.2453 | 0.2451 | 0.2441 | 0.2470 |

**关键趋势**：Relaxed F1 随 count 增加呈上升趋势 (0.067 → 0.247)，在 count=44 处饱和（count_64 与 count_44 几乎持平）。Exact F1 始终极低 (<0.02)，说明精确匹配困难但类型识别（relaxed）有明显的 count 效应。

### 3. Exp 2 启动状态

- **PID**: 197321
- **配置**: count_6 (1 low_bcs + 1 high_bcs + 25 random = 27 batches) + count_12 (同配置 = 27 batches) = **54 batches**
- **状态**: 模型已加载，第一个 batch `count_6_low_bcs` 正在运行
- 预估运行时间：~54 × 2min ≈ 1.5-2h

---
