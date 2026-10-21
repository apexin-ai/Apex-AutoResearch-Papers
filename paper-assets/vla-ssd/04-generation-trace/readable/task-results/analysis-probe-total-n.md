# analysis probe total N

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_probe_total_N_20260517T185400_result.json`
- **Structured JSON:** [`1ab23ff27e1d4dff3345.json`](../../sessions/1a/1ab23ff27e1d4dff3345.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

| 指标 | 值 |
|---|---|
| Tasks | 10 |
| Demos/task | 50 |
| Total demos | 500 |
| **N (total obs-action pairs)** | **63,728** |
| N_train (80%) | 50,982 |
| MLP probe params | 1,050,631 (1.05M) |
| **N_train / params ratio** | **0.05** |

每个 task 都恰好 50 demos，所以 all demos 和 50 demos/task 版本相同。

N/params ratio = 0.05，即训练样本数只有参数量的 5%。这是一个严重欠定的 regime（通常希望 ratio >> 1），说明 probe 的泛化能力高度依赖正则化或特征质量，也从侧面说明如果 probe 仍然能学到有意义的表征，那底层特征的质量是很高的。

---
