# ops check t10 a050 s44 d102

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-t10-a050-s44-d102_20260523T205305_result.json`
- **Structured JSON:** [`b5d1d8b171ddd3dd039e.json`](../../sessions/b5/b5d1d8b171ddd3dd039e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**t10_a050_s44_fp32_14b** — 已完成，registry 已更新为 DONE(success)
- distinct_3: 0.819→0.503 (↓39%), ppl: 19.8→34.4 (↑74%)
- D102 (d3): Robust pairs **0/2**，PermG 2/2，threshold_onset 0/2，TY 0/2
- 与 s42(K≥3=TBD)、s43(K≥3=1/8) 一致：α=0.50 onset boundary 下 consensus 弱

**仍在运行的 4 个实验：**

| 实验 | 服务器 | 进度 | 预估剩余 |
|---|---|---|---|
| t10_a045_s44 | 17855 | 9/11 gen | ~2h |
| t15_a045_s43 | 17855 | 15/16 gen | ~1h |
| t15_a075_s43 | 19828 | 14/16 gen | ~2h |
| t10_a075_s44 | 19828 | 11/11 gen (写 metrics 中) | <1h |

---
