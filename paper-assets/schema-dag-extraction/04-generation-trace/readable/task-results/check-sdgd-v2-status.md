# check sdgd v2 status

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_sdgd_v2_status_20260515T153409_result.json`
- **Structured JSON:** [`1323a5b05c10aca50788.json`](../../sessions/13/1323a5b05c10aca50788.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## SDGD v2 实验状态: **RUNNING**

**PID 278037** — 已运行 38 分钟，当前正在执行第 4 个 mode (`per_type`)，推理进度 ~100%，即将完成。

### GPU
| GPU利用率 | 显存使用 | 总显存 |
|-----------|---------|--------|
| 15% | 94,221 MiB | 97,887 MiB |

### 已完成的 3 个 mode 结果

| Mode | F1 | Precision | Recall | Batches | Latency |
|------|-----|-----------|--------|---------|---------|
| **single_pass** | **0.4451** | 0.5631 | 0.3679 | 1 (66 types) | 79s |
| **random_batch** | 0.3007 | 0.3307 | 0.2758 | 8 | 494s |
| **sdgd_zero** | 0.2407 | 0.3244 | 0.1913 | 4 | 261s |

**待完成**: `per_type` mode（日志显示正在处理最后一批 prompts，预计几分钟内完成）。

关键观察：single_pass baseline 目前 F1 最高（0.445），sdgd_zero 分解反而最低（0.241）。`per_type` 结果出来后可做完整对比。

---
