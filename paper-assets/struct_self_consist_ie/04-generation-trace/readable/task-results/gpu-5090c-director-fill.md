# gpu 5090c director fill

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_5090c_director_fill_20260521T112255_result.json`
- **Structured JSON:** [`7e87e337b0a99b4f87b4.json`](../../sessions/7e/7e87e337b0a99b4f87b4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已正常启动：

| 实验 | GPU | PID | 状态 |
|------|-----|-----|------|
| `exp_fewnerd_n16_s123` | cuda:0 | 311981 | Rendering prompts ~13% (4886/37648) |
| `exp_conll_n16_s42` | cuda:2 | 312281 | Rendering done, 开始 inference (0/55248) |

CoNLL 数据量小（3453 instances），已完成 prompt rendering 进入生成阶段。FewNERD 37648 instances，prompt rendering 进行中。

关于 `fewnerd_n16_s456_v2`：该目录在 5090-c 的 output/ 下不存在，搜索 `*s456*` 也只找到 `scierc_t12_s456`。可能在其他服务器（如 5090-b）上运行的。

---
