# ops check t15 a045 s43 d102

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-t15-a045-s43-d102_20260523T221809_result.json`
- **Structured JSON:** [`24f54d2d93156b2b72de.json`](../../sessions/24/24f54d2d93156b2b72de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### t15_a045_s43 — DONE
- gen_0–gen_15 完整，EXIT_CODE=0
- distinct_3: 0.817 → 0.464 (−43%)，perplexity: 19.8 → 34.2 (+72%)
- D102: 2/2 robust pairs (K≥3)，方法 = diff + perm + ty（threshold_onset 未触发 — 低 α 下降解是渐进式的）
- Registry 已更新 DONE，artifact 已注册

### t10_a045_s44 — RUNNING
- PID 796624，已运行 9h46m，gen_0–gen_9 就绪（差 gen_10）

### t15_a075_s43 — RUNNING
- PID 857058，已运行 15h37m，gen_0–gen_14 就绪（差 gen_15）

两个仍在运行的实验预计 1-2h 内完成。总结已写入 `artifacts/_project/batch_check_4_20260523.md`。

---
