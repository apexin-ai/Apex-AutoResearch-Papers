# verify fig count curves final

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_fig_count_curves_final_20260515T232154_result.json`
- **Structured JSON:** [`2f8aa351c7e8dc799f9d.json`](../../sessions/2f/2f8aa351c7e8dc799f9d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已获取，逐点对照完成。

## 数据对照表

### Panel (a) Few-NERD NER Qwen3 Recall
| count | 脚本值 | 正文值 | 一致? |
|-------|--------|--------|-------|
| 1     | 0.720  | 0.720  | ✓     |
| 2     | 0.698  | 0.698  | ✓     |
| 6     | 0.620  | 0.620  | ✓     |
| 12    | 0.539  | 0.539  | ✓     |
| 22    | 0.527  | 0.527  | ✓     |
| 44    | 0.551  | 0.551  | ✓     |
| 64    | 0.418  | 0.418  | ✓     |

**7/7 一致**

### Panel (b) FewRel 80-rel RE Qwen3 Accuracy
| count | 脚本值 | 正文值 | 一致? |
|-------|--------|--------|-------|
| 1     | 0.8573 | 0.8573 | ✓     |
| 4     | 0.8667 | 0.8667 | ✓     |
| 8     | 0.8021 | 0.8021 | ✓     |
| 16    | 0.6958 | 0.6958 | ✓     |
| 32    | 0.6578 | 0.6578 | ✓     |
| 40    | 0.588  | 0.5880 | ✓ (等值) |
| 64    | 0.5424 | 0.5424 | ✓     |
| 80    | 0.5042 | 0.5042 | ✓     |

**8/8 一致**（count=40 脚本写 `0.588`，正文写 `0.5880`，数值相同）

## 图表目录
| 文件 | 存在? | 大小 | 最后修改 |
|------|-------|------|----------|
| fig_count_curves.pdf | ✓ | 18,497 B | May 16 07:19 |
| fig_bcs_scaling.pdf  | ✓ | 30,052 B | May 16 07:21 |
| fig_error_taxonomy.pdf | ✓ | 28,048 B | May 16 05:43 |
| fig_count_curves.py  | 存在（源码副本） | 2,427 B | May 16 06:59 |
| fig_error_taxonomy.py | 存在（源码副本） | 3,076 B | May 16 05:42 |

三个主要 PDF 图表均存在，`fig_bcs_scaling.pdf` 确认存在（Paper Agent 正确）。

## AWQ 清理
`run_exp012_llama_awq.sh` 和 `auto_start_exp012_awq.sh` 均已删除（`No such file or directory`）。

**结论：无需修复，全部数据一致，图表齐全，AWQ 脚本已清理。**

---
