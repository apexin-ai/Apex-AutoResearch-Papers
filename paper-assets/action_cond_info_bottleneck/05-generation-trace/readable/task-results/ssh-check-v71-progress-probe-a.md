# ssh check v71 progress probe a

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-v71-progress-probe-a_20260517T072759_result.json`
- **Structured JSON:** [`ac63f90a914c4062c70d.json`](../../sessions/ac/ac63f90a914c4062c70d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Probe A 完成。

## Probe A 结果 (seed1, step 5000)

### Probe A: Fixed Image, Swap Instruction
固定同一张图像，替换不同 language instruction，检查 scorer 输出是否变化：

| Pair | Cosine Similarity | L2 Distance |
|------|-------------------|-------------|
| inst 0 vs 1 | **0.890** | 4.56 |
| inst 0 vs 2 | **0.876** | 4.65 |
| inst 1 vs 2 | **0.973** | 1.92 |

### Probe B: Natural Cross-task Observations
不同任务的自然观测下 importance map 对比：

| Pair | Cosine Similarity | L2 Distance |
|------|-------------------|-------------|
| task 0 vs 1 | **0.687** | 4.08 |
| task 0 vs 2 | **0.771** | 3.36 |
| task 1 vs 2 | **0.815** | 3.24 |

### 判定
- **Probe A**: cos ∈ [0.876, 0.973] — **FAIL**（3 个 pair 全部 > 0.8 阈值）。scorer 确实是 language-condition-dependent（不同 instruction 产生不同权重），但 cosine similarity 偏高，尤其 inst 1 vs 2（两个相似的 "pick up black bowl" 指令）接近 0.97。
- **Probe B**: cos ∈ [0.687, 0.815] — 跨任务 importance map 有差异，但仍有一对 > 0.8。

按任务定义的 PASS 标准（所有 cosine < 0.8），**Probe A 未通过**。inst 1 vs 2 高相似度可以理解（指令语义非常接近），但 inst 0 vs 1/2 也在 0.87-0.89，说明 scorer 在 step 5000 阶段对 language conditioning 的响应程度有限——可能因为 β 仍为 0（warmup 阶段），IB 约束尚未生效。

---
