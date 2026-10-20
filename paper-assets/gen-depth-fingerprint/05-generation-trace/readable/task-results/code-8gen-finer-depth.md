# code 8gen finer depth

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_8gen-finer-depth_20260516T145933_result.json`
- **Structured JSON:** [`0c9eb95319681cc90e93.json`](../../sessions/0c/0c9eb95319681cc90e93.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果保存到 `results/8gen_finer_depth.json`。

**结果摘要：**

| 指标 | 5-class | 3-class |
|------|---------|---------|
| LOGO avg F1 | **0.4878** | **0.7698** |
| 95% CI | [0.4825, 0.4912] | [0.7636, 0.7715] |
| Delta | **-0.2820** | — |

**Per-class F1 (5-class)：**
| Class | F1 |
|-------|-----|
| gen-0 | 0.9173 |
| gen-1 | 0.5931 |
| gen-2 | **0.2395** |
| gen-3 | **0.2337** |
| gen-4 | 0.4506 |

**验证通过：**
- 5-class F1 (0.49) 显著低于 3-class (0.77)，符合预期
- gen-2 和 gen-3 的 per-class F1 最低（~0.24），确认了 6-gen 实验中观察到的 gen-2/gen-3 难以区分的现象
- 混淆矩阵显示 gen-2 和 gen-3 互相混淆严重，且都大量被误分为 gen-4
- gen-0 几乎完美分类 (0.98 recall)，gen-1 次之 (0.70 recall)

---
